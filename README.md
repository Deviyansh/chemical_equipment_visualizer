# Chemical Equipment Parameter Visualizer  

---

## 1. Project Overview

The **Chemical Equipment Parameter Visualizer** is a hybrid data analysis and visualization system.

The application allows users to upload CSV datasets containing chemical equipment parameters and analyze them through:
- A **web-based dashboard**
- A **desktop-based application**

Both interfaces use a **single Django REST backend**, demonstrating reusability, modularity, and clean software architecture.


## 2. System Architecture

The system follows a **client–server architecture** with a shared backend.



CSV Dataset  
│  
▼  
Django REST API (Backend)  
│  
├── Web Dashboard (HTML + CSS + JavaScript + Chart.js)  
│  
└── Desktop Application (PyQt5 + Matplotlib)


### Key Architectural Decisions
- A **single REST API** handles all data processing  
- Frontends are **decoupled** from backend logic  
- Same analytics logic is reused across platforms  
- Easy to extend with additional clients in the future

## 3. Project Structure

chemical-equipment-visualizer/  
├── backend/  
│ ├── backend/ # Django project settings  
│ ├── equipment_api/ # Core application  
│ │ ├── views.py # API + web views  
│ │ ├── models.py # Database models  
│ │ ├── utils.py # CSV analysis logic  
│ │ ├── pdf_utils.py # PDF report generation  
│ │ ├── templates/ # HTML templates  
│ │ └── static/ # CSS and JavaScript  
│ └── manage.py  
│  
├── desktop_app/  
│ └── app.py # PyQt5 desktop application  
│  
├── sample_equipment_data.csv # Sample dataset  
├── requirements.txt # Python dependencies  
└── README.md


## 4. Data Flow (End-to-End)

1. User uploads a CSV file (Web or Desktop)  
2. File is sent to Django REST API  
3. Backend:
   - Reads CSV using Pandas
   - Computes summary statistics
   - Stores recent uploads
4. Processed data is returned as JSON  
5. Frontend:
   - Displays metrics
   - Renders charts
   - Updates tables
   
## 5. CSV File Format

The application expects CSV files with the following columns:

```csv
Equipment Name,Type,Flowrate,Pressure,Temperature
```

## 6. Technology Stack

| Layer | Technology |
|-------|------------|
| Backend | Django, Django REST Framework |
| Data Processing | Pandas |
| Web Frontend | HTML, CSS (Bootstrap), JavaScript, Chart.js |
| Desktop Frontend | PyQt5, Matplotlib |
| Authentication | Django Basic Authentication |
| PDF Generation | ReportLab |

## 7. Backend Setup & Execution

From the root of the repo:

1. Go to backend:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   - Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - macOS / Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```

## 8. Web Dashboard Usage

- Login via Django admin: [Django Admin](http://127.0.0.1:8000/admin/)  
- Open the web dashboard: [Web Dashboard](http://127.0.0.1:8000/api/)

Web Features:
- CSV upload  
- Summary metrics  
- Equipment type distribution chart  
- Tabular data visualization

## 9. Desktop Application Usage

Run the desktop app:

```bash
cd desktop_app
python app.py
```

Desktop Features:
- File dialog CSV upload  
- Dark-themed dashboard UI  
- Metric cards  
- Doughnut chart visualization  
- Uses same backend API as web app

## 10. PDF Report Generation

The system supports automatic PDF report generation containing:
- Summary statistics  
- Equipment distribution  
- Timestamped analysis

Access the report endpoint: [PDF Report](http://127.0.0.1:8000/api/report/)

## 11. Design Rationale

A single Django REST backend is shared between web and desktop clients to demonstrate separation of concerns, modularity, and scalability.  
UI design across platforms was intentionally kept consistent to provide a unified and professional user experience.

## 12. Features Summary

- CSV upload and validation  
- Statistical analysis of equipment parameters  
- RESTful API design  
- Web-based data visualization  
- Desktop-based data visualization  
- Authentication-protected endpoints  
- PDF report generation

## 13. Author

Deviyansh  
