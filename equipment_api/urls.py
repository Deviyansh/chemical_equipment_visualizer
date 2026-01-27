from django.urls import path
from .views import (
    CSVUploadView,
    LatestSummaryView,
    UploadHistoryView,
    home
)

urlpatterns = [
    path('', home, name='home'),          # 👈 Django web page
    path('upload/', CSVUploadView.as_view()),
    path('summary/', LatestSummaryView.as_view()),
    path('history/', UploadHistoryView.as_view()),
]
