# ⚡ UniEase - Quick Start Guide

Get UniEase up and running in under 2 minutes!

## 📋 Prerequisites

Before you begin, ensure you have:
- **Python 3.10+** installed.
- **MySQL Server** running (optional if using local SQLite for testing).

## 🚀 Setup Steps

### 1. Database Configuration
UniEase is configured for **MySQL** by default.
1. Create a database named `uniease_db`.
2. Update your credentials in `uniease/settings.py` (Default: `root` / `system`).

> [!TIP]
> To use **SQLite** instead, simply comment out the MySQL settings and uncomment the SQLite block in `uniease/settings.py`.

### 2. Automated Installation
Run these commands in your terminal:

```bash
# Install dependencies
pip install django pillow pymysql

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Populate realistic sample data
# Creates 100+ entries across all 23 models
python scripts/populate_sample_data.py
```

### 3. Start the Platform
```bash
python manage.py runserver
```

---

## 🔑 Access & Credentials

Open your browser to: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

### Sample Accounts (Password: `password123`)
| Role | Username | Note |
|------|----------|------|
| **Student** | `student1` | Full student dashboard access |
| **Faculty** | `faculty1` | Academic management tools |
| **Warden** | `warden` | Hostel complaint resolution |
| **Mess Head** | `messhead` | Menu and food feedback management |
| **Librarian** | `librarian` | Book and seat tracking |
| **Placement** | `placement` | Job and internship posting |

**Admin Portal**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
*Username: `admin` | Password: `admin123`*

---

## 🛠️ Troubleshooting

- **Database Errors**: Ensure MySQL is running and `uniease_db` exists.
- **Images Not Showing**: Ensure `pip install pillow` was successful.
- **Static Assets**: Run `python manage.py collectstatic` if styles are missing in production mode.

Enjoy your unified campus experience with **UniEase**! 🎓
