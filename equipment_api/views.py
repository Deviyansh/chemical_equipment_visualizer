from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from django.core.files.storage import FileSystemStorage
from .serializers import CSVUploadSerializer

from .models import UploadedDataset
from .utils import analyze_csv


class CSVUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    serializer_class = CSVUploadSerializer

    def post(self, request):
        serializer = CSVUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data["file"]

        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_path = fs.path(filename)

        summary = analyze_csv(file_path)

        UploadedDataset.objects.create(
            filename=filename,
            summary=summary
        )

        extra = UploadedDataset.objects.count() - 5
        if extra > 0:
            UploadedDataset.objects.all().order_by('uploaded_at')[:extra].delete()

        return Response(summary)

class LatestSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        latest = UploadedDataset.objects.last()
        if not latest:
            return Response({"message": "No data uploaded yet"})
        return Response(latest.summary)


class UploadHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(list(
            UploadedDataset.objects.values(
                "filename", "uploaded_at", "summary"
            ).order_by("-uploaded_at")
        ))

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json

@login_required
def home(request):
    return render(request, "dashboard.html")
