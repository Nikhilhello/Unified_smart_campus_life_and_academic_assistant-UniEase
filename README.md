### Next Gen Employability Program (Next Gen 4.0) -Edunet Foundation 
#### Course: Full Stack Web Development with AI Tools | 2025 – 2026 (Dec-Feb) 

# 🎓 UniEase - Unified Campus Life & Academic Assistant

UniEase is a comprehensive Django-based campus management system designed to streamline university operations and enhance the student experience. It provides a unified platform for students, faculty, and administrators to manage academic, hostel, library, placement, and other campus-related activities.

## 🚀 Features

### 🎓 For Students
- **📈 Dashboard** - Personalized view with announcements, notifications, and library/complaint status.
- **📚 Academics** - Download notes, view timetables, syllabus, and exam schedules.
- **❓ Doubt Forum** - Ask questions and get answers from peers and faculty (anonymous posting available).
- **📖 Library Management** - Search books, check availability, and view real-time library seat status.
- **🔍 Lost & Found** - Report lost items or found items with image uploads.
- **🏠 Hostel Complaints** - Submit and track maintenance or service complaints.
- **🍽️ Mess Menu & Ratings** - View weekly mess menu and provide food quality feedback.
- **🚌 Transport** - View bus routes and schedules with real-time delay info.
- **💼 Placements** - Browse job/internship opportunities and submit applications.
- **🎥 Learning Resources** - Access curated videos, articles, and courses.
- **🛡️ Academic Vault** - Securely store certificates and academic records.

### 👨‍🏫 For Faculty & Staff
- **📢 Announcements** - Post important updates for specific departments or audiences.
- **📁 Upload Notes** - Share study materials and academic resources with students.
- **📊 Manage Syllabus** - Track and update syllabus completion status.
- **📝 Schedule Exams** - Create and manage exam dates, halls, and seating.
- **💼 Post Placements** - Add new job and internship opportunities.
- **💡 Answer Doubts** - Directly engage with student queries in the forum.

### 🛠️ For Administrators
- **💻 Robust Admin Panel** - Full-featured Django admin with custom dashboard.
- **👤 User Management** - Handle 7 distinct user roles: Student, Faculty, Admin, Warden, Mess Head, Librarian, and Placement Officer.
- **📂 Content Management** - Manage all platform data including timetables, menus, and routes.
- **🔧 Complaint Resolution** - Track and resolve hostel issues with admin responses.

## 🛠️ Technology Stack

- **Backend**: Django 4.2 (Python 3.10+)
- **Database**: MySQL (Default) / SQLite (Development)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla) + Django Templates
- **Auth**: Django Built-in Authentication System
- **Storage**: Media files (Resumes, Notes, Certificates) handled via Django FileField/ImageField

## 📂 Project Structure

```
UniEase/
├── campus/                 # Main Django app
│   ├── models.py          # 23 Database models for all campus operations
│   ├── views.py           # Business logic and view functions
│   ├── admin.py           # Enhanced admin interface configuration
│   └── templates/         # 40+ HTML templates for a rich UI
├── media/                 # User-uploaded files (Profiles, Notes, Resumes)
├── scripts/              # Setup and data population scripts
│   └── populate_sample_data.py # Automation for rich sample data
├── static/                # Static assets (CSS, JS, Images)
├── uniease/             # Project settings & URL routing
├── manage.py             # Django management script
└── QUICKSTART.md         # Fast 2-minute setup guide
```

## 📊 Core Modules (23 Models)

UniEase is built on a highly structured database architecture:

- **Identity**: `UserProfile`, `Notification`
- **Academia**: `Note`, `Timetable`, `Syllabus`, `Exam`, `AcademicRecord`
- **Interaction**: `Announcement`, `Doubt`, `Answer`, `AnswerUpvote`
- **Operations**: `LostItem`, `HostelComplaint`, `BusRoute`, `MessMenu`, `MessRating`
- **Library**: `Book`, `BookBorrowing`, `LibrarySeat`
- **Careers**: `Placement`, `PlacementApplication`
- **Growth**: `LearningResource`, `Certificate`

## ⚙️ Installation & Setup

### 1. Clone & Install
```bash
git clone <repository-url>
cd UniEase
pip install django pillow pymysql
```

### 2. Configure Database
1. Create a MySQL database named `uniease_db`.
2. Update credentials in `uniease/settings.py` (Default: `root` / `system`).
3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Quick Setup (Highly Recommended)
Load 100+ sample entries to see the platform in action:
```bash
python scripts/populate_sample_data.py
```
*Creates admin user: `admin` / `admin123`*

### 4. Run Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/`

## 🔑 Sample Credentials (Auto-Generated)

| Role | Username | Password |
|------|----------|----------|
| **Admin** | admin | admin123 |
| **Student** | student1 | password123 |
| **Faculty** | faculty1 | password123 |
| **Warden** | warden | password123 |
| **Mess Head** | messhead | password123 |
| **Librarian** | librarian | password123 |
| **Placement** | placement | password123 |

## 🔮 Future Enhancements
- **Mobile Application** - Cross-platform mobile app (React Native / Flutter) for on-the-go access.
- **Real-time Notifications** - Implementation of WebSockets for instant alerts and updates.
- **QR-based Attendance** - Streamlined attendance tracking for classes and events.
- **Integrated Payment Gateway** - Secure payments for library fines, mess bills, and other campus fees.
- **Event Management** - Comprehensive system for organizing, promoting, and managing campus events.
- **E-Learning Platform** - Integrated video lectures and digital learning resources.
- **Hostel Finder** - Room and hostel availability tracker for areas surrounding the campus.
- **Carpooling System** - Petrol/car-sharing system for student and staff commuting.
- **Alumni Portal** - Dedicated network for alumni engagement and mentorship.
- **AI Campus Assistant** - AI-powered Information Retrieval Assistant for campus queries.

## 📄 License
Licensed under the MIT License.

---
**Version**: 1.1.0 | **Released**: Feb 2026 | **UniEase Team**
