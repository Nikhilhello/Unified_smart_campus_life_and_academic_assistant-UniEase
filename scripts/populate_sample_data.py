# -*- coding: utf-8 -*-
"""
Populate Sample Data Script
This script creates sample data for UniEase including users, announcements, notes, etc.
"""

import os
import sys

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import django
from datetime import datetime, timedelta, time
from django.utils import timezone

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uniease.settings')
django.setup()

from django.contrib.auth.models import User
from campus.models import *

def create_users():
    """Create sample users with different roles"""
    print("\n[1/10] Creating users...")
    
    users_data = [
        # Students
        {'username': 'student1', 'email': 'student1@uniease.com', 'first_name': 'Rahul', 'last_name': 'Sharma', 
         'role': 'student', 'department': 'Computer Science', 'phone': '9876543210', 'year': 3, 'semester': 5},
        {'username': 'student2', 'email': 'student2@uniease.com', 'first_name': 'Priya', 'last_name': 'Patel',
         'role': 'student', 'department': 'Computer Science', 'phone': '9876543211', 'year': 3, 'semester': 5},
        {'username': 'student3', 'email': 'student3@uniease.com', 'first_name': 'Amit', 'last_name': 'Kumar',
         'role': 'student', 'department': 'Electronics', 'phone': '9876543212', 'year': 3, 'semester': 5},
        
        # Faculty
        {'username': 'faculty1', 'email': 'faculty1@uniease.com', 'first_name': 'Dr. Suresh', 'last_name': 'Verma',
         'role': 'faculty', 'department': 'Computer Science', 'phone': '9876543220'},
        {'username': 'faculty2', 'email': 'faculty2@uniease.com', 'first_name': 'Prof. Anjali', 'last_name': 'Singh',
         'role': 'faculty', 'department': 'Electronics', 'phone': '9876543221'},
        
        # Warden
        {'username': 'warden', 'email': 'warden@uniease.com', 'first_name': 'Mr. Rajesh', 'last_name': 'Gupta',
         'role': 'warden', 'department': 'Hostel Management', 'phone': '9876543230'},
        
        # Mess Head
        {'username': 'messhead', 'email': 'messhead@uniease.com', 'first_name': 'Mrs. Lakshmi', 'last_name': 'Devi',
         'role': 'mess_head', 'department': 'Mess Management', 'phone': '9876543240'},
        
        # Librarian
        {'username': 'librarian', 'email': 'librarian@uniease.com', 'first_name': 'Mr. Arun', 'last_name': 'Nair',
         'role': 'librarian', 'department': 'Library', 'phone': '9876543250'},
        
        # Placement Officer
        {'username': 'placement', 'email': 'placement@uniease.com', 'first_name': 'Ms. Kavita', 'last_name': 'Reddy',
         'role': 'placement_officer', 'department': 'Training & Placement', 'phone': '9876543260'},
    ]
    
    created_count = 0
    for user_data in users_data:
        if not User.objects.filter(username=user_data['username']).exists():
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password='password123',  # Default password for all users
                first_name=user_data['first_name'],
                last_name=user_data['last_name']
            )
            
            UserProfile.objects.create(
                user=user,
                role=user_data['role'],
                department=user_data['department'],
                phone=user_data['phone'],
                year=user_data.get('year'),
                semester=user_data.get('semester')
            )
            created_count += 1
    
    print(f"  ✓ Created {created_count} users (password: password123)")

def create_announcements():
    """Create sample announcements"""
    print("\n[2/10] Creating announcements...")
    
    admin = User.objects.get(username='admin')
    faculty1 = User.objects.get(username='faculty1')
    
    announcements_data = [
        {'title': 'Welcome to UniEase!', 'content': 'Welcome to the new academic year. We wish you all the best for your studies.', 
         'posted_by': admin, 'target_audience': 'all', 'priority': 'high'},
        {'title': 'Mid-Semester Exams Schedule', 'content': 'Mid-semester exams will be conducted from 15th Feb to 25th Feb 2026.',
         'posted_by': faculty1, 'target_audience': 'students', 'priority': 'high'},
        {'title': 'Library Timing Update', 'content': 'Library will remain open till 10 PM from next week.',
         'posted_by': admin, 'target_audience': 'all', 'priority': 'medium'},
        {'title': 'Guest Lecture on AI', 'content': 'A guest lecture on Artificial Intelligence will be conducted on 5th Feb at 2 PM in Seminar Hall.',
         'posted_by': faculty1, 'target_audience': 'Computer Science', 'priority': 'medium'},
    ]
    
    created_count = 0
    for ann_data in announcements_data:
        if not Announcement.objects.filter(title=ann_data['title']).exists():
            Announcement.objects.create(**ann_data)
            created_count += 1
    
    print(f"  ✓ Created {created_count} announcements")

def create_timetable():
    """Create sample timetable"""
    print("\n[3/10] Creating timetable...")
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    time_slots = ['9:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-1:00', '2:00-3:00', '3:00-4:00']
    
    cs_subjects = [
        {'subject': 'Data Structures', 'faculty': 'Dr. Suresh Verma', 'room': 'CS-101'},
        {'subject': 'Database Management', 'faculty': 'Dr. Suresh Verma', 'room': 'CS-102'},
        {'subject': 'Operating Systems', 'faculty': 'Prof. Anjali Singh', 'room': 'CS-103'},
        {'subject': 'Computer Networks', 'faculty': 'Dr. Suresh Verma', 'room': 'CS-101'},
        {'subject': 'Software Engineering', 'faculty': 'Prof. Anjali Singh', 'room': 'CS-104'},
    ]
    
    created_count = 0
    for day in days:
        for i, slot in enumerate(time_slots[:5]):  # 5 classes per day
            subject_data = cs_subjects[i % len(cs_subjects)]
            if not Timetable.objects.filter(department='Computer Science', year=3, semester=5, day=day, time_slot=slot).exists():
                Timetable.objects.create(
                    department='Computer Science',
                    year=3,
                    semester=5,
                    day=day,
                    time_slot=slot,
                    **subject_data
                )
                created_count += 1
    
    print(f"  ✓ Created {created_count} timetable entries")

def create_syllabus():
    """Create sample syllabus"""
    print("\n[4/10] Creating syllabus...")
    
    topics = [
        # Data Structures
        {'subject': 'Data Structures', 'topic': 'Arrays and Linked Lists', 'completed': True},
        {'subject': 'Data Structures', 'topic': 'Stacks and Queues', 'completed': True},
        {'subject': 'Data Structures', 'topic': 'Trees and Graphs', 'completed': False},
        {'subject': 'Data Structures', 'topic': 'Hashing', 'completed': False},
        {'subject': 'Data Structures', 'topic': 'Heaps', 'completed': False},
        
        # DBMS
        {'subject': 'Database Management', 'topic': 'ER Diagrams', 'completed': True},
        {'subject': 'Database Management', 'topic': 'Relational Model', 'completed': True},
        {'subject': 'Database Management', 'topic': 'SQL Queries', 'completed': False},
        {'subject': 'Database Management', 'topic': 'Normalization', 'completed': False},
        {'subject': 'Database Management', 'topic': 'Transactions', 'completed': False},
        
        # OS
        {'subject': 'Operating Systems', 'topic': 'Process Management', 'completed': True},
        {'subject': 'Operating Systems', 'topic': 'Threads', 'completed': True},
        {'subject': 'Operating Systems', 'topic': 'CPU Scheduling', 'completed': True},
        {'subject': 'Operating Systems', 'topic': 'Deadlocks', 'completed': False},
        {'subject': 'Operating Systems', 'topic': 'Memory Management', 'completed': False},
        {'subject': 'Operating Systems', 'topic': 'File Systems', 'completed': False},
    ]
    
    created_count = 0
    for topic_data in topics:
        if not Syllabus.objects.filter(subject=topic_data['subject'], topic=topic_data['topic']).exists():
            Syllabus.objects.create(
                department='Computer Science',
                semester=5,
                **topic_data,
                completion_date=timezone.now().date() if topic_data['completed'] else None
            )
            created_count += 1
    
    print(f"  ✓ Created {created_count} syllabus topics")

def create_exams():
    """Create sample exams"""
    print("\n[5/10] Creating exams...")
    
    today = timezone.now().date()
    exams_data = [
        {'exam_name': 'Mid-Semester Exam', 'subject': 'Data Structures', 'date': today + timedelta(days=10), 
         'time': time(9, 0), 'duration': '3 hours', 'hall': 'Exam Hall A', 'seat_number': 'A-101'},
        {'exam_name': 'Mid-Semester Exam', 'subject': 'Database Management', 'date': today + timedelta(days=12),
         'time': time(9, 0), 'duration': '3 hours', 'hall': 'Exam Hall B', 'seat_number': 'B-205'},
        {'exam_name': 'Mid-Semester Exam', 'subject': 'Operating Systems', 'date': today + timedelta(days=14),
         'time': time(14, 0), 'duration': '3 hours', 'hall': 'Exam Hall A', 'seat_number': 'A-102'},
        {'exam_name': 'Practical Exam', 'subject': 'Data Structures Lab', 'date': today + timedelta(days=16),
         'time': time(10, 0), 'duration': '2 hours', 'hall': 'Lab 1', 'seat_number': 'L1-05'},
        {'exam_name': 'Practical Exam', 'subject': 'DBMS Lab', 'date': today + timedelta(days=17),
         'time': time(10, 0), 'duration': '2 hours', 'hall': 'Lab 2', 'seat_number': 'L2-15'},
    ]
    
    created_count = 0
    for exam_data in exams_data:
        if not Exam.objects.filter(exam_name=exam_data['exam_name'], subject=exam_data['subject']).exists():
            Exam.objects.create(
                department='Computer Science',
                semester=5,
                **exam_data
            )
            created_count += 1
    
    print(f"  ✓ Created {created_count} exams")

def create_library_data():
    """Create sample library books and seats"""
    print("\n[6/10] Creating library data...")
    
    books_data = [
        {'title': 'Introduction to Algorithms', 'author': 'Cormen, Leiserson, Rivest', 'isbn': '9780262033848', 
         'category': 'Computer Science', 'total_copies': 5, 'available_copies': 5},
        {'title': 'Database System Concepts', 'author': 'Silberschatz, Korth', 'isbn': '9780078022159',
         'category': 'Computer Science', 'total_copies': 3, 'available_copies': 2},
        {'title': 'Operating System Concepts', 'author': 'Silberschatz, Galvin', 'isbn': '9781118063330',
         'category': 'Computer Science', 'total_copies': 4, 'available_copies': 4},
        {'title': 'Computer Networks', 'author': 'Tanenbaum', 'isbn': '9780132126953',
         'category': 'Computer Science', 'total_copies': 3, 'available_copies': 3},
        {'title': 'Artificial Intelligence', 'author': 'Stuart Russell, Peter Norvig', 'isbn': '9780136042594',
         'category': 'Computer Science', 'total_copies': 2, 'available_copies': 2},
    ]
    
    book_count = 0
    for book_data in books_data:
        if not Book.objects.filter(isbn=book_data['isbn']).exists():
            Book.objects.create(**book_data)
            book_count += 1
    
    # Create library seats
    seat_count = 0
    for floor in range(1, 4):  # 3 floors
        for seat_num in range(1, 21):  # 20 seats per floor
            seat_number = f"F{floor}-S{seat_num:02d}"
            if not LibrarySeat.objects.filter(seat_number=seat_number).exists():
                LibrarySeat.objects.create(
                    seat_number=seat_number,
                    floor=floor,
                    is_available=True
                )
                seat_count += 1
    
    print(f"  ✓ Created {book_count} books and {seat_count} library seats")

def create_mess_menu():
    """Create sample mess menu"""
    print("\n[7/10] Creating mess menu...")
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meals = [
        {'meal_type': 'breakfast', 'items': 'Idli, Sambar, Chutney, Tea/Coffee'},
        {'meal_type': 'lunch', 'items': 'Rice, Dal, Roti, Vegetable Curry, Curd'},
        {'meal_type': 'snacks', 'items': 'Samosa, Tea/Coffee'},
        {'meal_type': 'dinner', 'items': 'Rice, Roti, Dal, Paneer Curry, Salad'},
    ]
    
    created_count = 0
    for day in days:
        for meal in meals:
            if not MessMenu.objects.filter(day=day, meal_type=meal['meal_type']).exists():
                MessMenu.objects.create(
                    day=day,
                    **meal
                )
                created_count += 1
    
    print(f"  ✓ Created {created_count} mess menu items")

def create_transport():
    """Create sample bus routes"""
    print("\n[8/10] Creating transport routes...")
    
    routes_data = [
        {'route_number': 'R1', 'route_name': 'Campus - Railway Station', 'departure_time': time(7, 0), 
         'arrival_time': time(7, 30), 'stops': 'Campus Gate, City Center, Railway Station'},
        {'route_number': 'R2', 'route_name': 'Campus - Bus Stand', 'departure_time': time(8, 0),
         'arrival_time': time(8, 45), 'stops': 'Campus Gate, Market, Bus Stand'},
        {'route_number': 'R3', 'route_name': 'Campus - Airport', 'departure_time': time(6, 0),
         'arrival_time': time(7, 0), 'stops': 'Campus Gate, Highway, Airport'},
    ]
    
    created_count = 0
    for route_data in routes_data:
        if not BusRoute.objects.filter(route_number=route_data['route_number']).exists():
            BusRoute.objects.create(**route_data)
            created_count += 1
    
    print(f"  ✓ Created {created_count} bus routes")

def create_placements():
    """Create sample placement opportunities"""
    print("\n[9/10] Creating placements...")
    
    placement_officer = User.objects.get(username='placement')
    today = timezone.now().date()
    
    placements_data = [
        {'company_name': 'Google', 'job_role': 'Software Engineer', 'package': '25 LPA', 
         'eligibility': '7.5 CGPA, No backlogs', 'application_deadline': today + timedelta(days=15),
         'description': 'Looking for talented software engineers for our Bangalore office.'},
        {'company_name': 'Microsoft', 'job_role': 'Software Developer', 'package': '22 LPA',
         'eligibility': '7.0 CGPA, No backlogs', 'application_deadline': today + timedelta(days=20),
         'description': 'Join our team to work on cutting-edge cloud technologies.'},
        {'company_name': 'Amazon', 'job_role': 'SDE Intern', 'package': '50k/month',
         'eligibility': '6.5 CGPA', 'application_deadline': today + timedelta(days=10),
         'description': 'Summer internship opportunity for final year students.'},
    ]
    
    created_count = 0
    for placement_data in placements_data:
        if not Placement.objects.filter(company_name=placement_data['company_name'], job_role=placement_data['job_role']).exists():
            Placement.objects.create(
                posted_by=placement_officer,
                **placement_data
            )
            created_count += 1
    
    print(f"  ✓ Created {created_count} placement opportunities")

def create_doubts():
    """Create sample doubts and answers"""
    print("\n[10/10] Creating doubts and answers...")
    
    student1 = User.objects.get(username='student1')
    student2 = User.objects.get(username='student2')
    faculty1 = User.objects.get(username='faculty1')
    
    doubt1 = None
    if not Doubt.objects.filter(question__contains='difference between stack and queue').exists():
        doubt1 = Doubt.objects.create(
            question='What is the difference between stack and queue?',
            subject='Data Structures',
            topic='Basic Data Structures',
            posted_by=student1,
            is_anonymous=False
        )
    
    doubt2 = None
    if not Doubt.objects.filter(question__contains='ACID properties').exists():
        doubt2 = Doubt.objects.create(
            question='Can someone explain ACID properties in DBMS?',
            subject='Database Management',
            topic='Transactions',
            posted_by=student2,
            is_anonymous=False
        )
    
    # Add answers
    answer_count = 0
    if doubt1 and not Answer.objects.filter(doubt=doubt1).exists():
        Answer.objects.create(
            doubt=doubt1,
            answer='Stack follows LIFO (Last In First Out) principle, while Queue follows FIFO (First In First Out) principle. Stack operations are push and pop, while Queue operations are enqueue and dequeue.',
            answered_by=faculty1,
            upvotes=5
        )
        answer_count += 1
    
    if doubt2 and not Answer.objects.filter(doubt=doubt2).exists():
        Answer.objects.create(
            doubt=doubt2,
            answer='ACID stands for Atomicity, Consistency, Isolation, and Durability. These are properties that guarantee database transactions are processed reliably.',
            answered_by=faculty1,
            upvotes=3
        )
        answer_count += 1
    
    doubt_count = 2 if doubt1 or doubt2 else 0
    print(f"  ✓ Created {doubt_count} doubts and {answer_count} answers")

def create_lost_and_found():
    """Create sample lost and found items"""
    print("\n[11/11] Creating lost and found items...")
    
    student1 = User.objects.get(username='student1')
    student2 = User.objects.get(username='student2')
    
    items_data = [
        {'item_name': 'Blue Water Bottle', 'description': 'Blue Milton water bottle lost near computer lab', 
         'category': 'Others', 'location': 'Computer Lab 1', 'status': 'lost', 
         'contact': '9876543210', 'posted_by': student1},
        {'item_name': 'Scientific Calculator', 'description': 'Casio fx-991ES Plus found in library',
         'category': 'Electronics', 'location': 'Library 1st Floor', 'status': 'found',
         'contact': '9876543211', 'posted_by': student2},
        {'item_name': 'ID Card', 'description': 'ID Card of 1st year student found in playground',
         'category': 'Documents', 'location': 'Playground', 'status': 'returned',
         'contact': '9876543211', 'posted_by': student2},
        {'item_name': 'Car Keys', 'description': 'Suzuki car keys with a red keychain',
         'category': 'Others', 'location': 'Parking Lot', 'status': 'lost',
         'contact': '9876543210', 'posted_by': student1},
    ]
    
    created_count = 0
    for item_data in items_data:
        # Check if item exists (simple check by name and description)
        if not LostItem.objects.filter(item_name=item_data['item_name'], description=item_data['description']).exists():
            LostItem.objects.create(**item_data)
            created_count += 1
            
    print(f"  ✓ Created {created_count} lost and found items")

def create_notes():
    """Create sample notes"""
    print("\n[12/15] Creating sample notes...")
    
    student1 = User.objects.get(username='student1')
    faculty1 = User.objects.get(username='faculty1')
    
    # We need a dummy file for notes
    from django.core.files.base import ContentFile
    dummy_content = ContentFile(b"Sample note content", name="sample_note.txt")
    
    notes_data = [
        {'subject': 'Data Structures', 'title': 'Linked List Notes', 'description': 'Comprehensive notes on Singly and Doubly Linked Lists',
         'uploaded_by': faculty1, 'semester': 5, 'department': 'Computer Science'},
         {'subject': 'Operating Systems', 'title': 'Process Management', 'description': 'Notes on process scheduling algorithms',
         'uploaded_by': faculty1, 'semester': 5, 'department': 'Computer Science'},
         {'subject': 'Database Management', 'title': 'SQL Cheat Sheet', 'description': 'Quick reference for SQL commands',
         'uploaded_by': student1, 'semester': 5, 'department': 'Computer Science'},
    ]
    
    created_count = 0
    for note_data in notes_data:
        if not Note.objects.filter(title=note_data['title'], subject=note_data['subject']).exists():
            Note.objects.create(file=dummy_content, **note_data)
            created_count += 1
            
    print(f"  ✓ Created {created_count} notes")

def create_learning_resources():
    """Create sample learning resources"""
    print("\n[13/15] Creating learning resources...")
    
    admin = User.objects.get(username='admin')
    
    resources_data = [
        {'title': 'Introduction to Python', 'category': 'Programming', 'description': 'A complete course on Python for beginners.',
         'resource_type': 'video', 'url': 'https://www.youtube.com/watch?v=rfscVS0vtbw', 'posted_by': admin},
        {'title': 'Data Structures vs Algorithms', 'category': 'Computer Science', 'description': 'Article explaining the difference.',
         'resource_type': 'article', 'url': 'https://www.geeksforgeeks.org/data-structures/', 'posted_by': admin},
        {'title': 'Django Web Framework', 'category': 'Web Development', 'description': 'Official Django documentation.',
         'resource_type': 'tutorial', 'url': 'https://docs.djangoproject.com/en/5.0/', 'posted_by': admin},
    ]
    
    created_count = 0
    for res_data in resources_data:
        if not LearningResource.objects.filter(title=res_data['title']).exists():
            LearningResource.objects.create(**res_data)
            created_count += 1
            
    print(f"  ✓ Created {created_count} learning resources")

def create_academic_vault():
    """Create sample academic vault data (certificates and records)"""
    print("\n[14/15] Creating academic vault data...")
    
    student1 = User.objects.get(username='student1')
    
    # Certificates
    # Dummy file for certificates
    from django.core.files.base import ContentFile
    dummy_cert = ContentFile(b"Sample Certificate", name="certificate.pdf")
    
    certificates_data = [
        {'title': 'Python Bootcamp', 'issuer': 'Udemy', 'issue_date': timezone.now().date() - timedelta(days=100),
         'category': 'Course', 'user': student1},
        {'title': 'Web Development Internship', 'issuer': 'Tech Corp', 'issue_date': timezone.now().date() - timedelta(days=200),
         'category': 'Internship', 'user': student1},
    ]
    
    cert_count = 0
    for cert_data in certificates_data:
        if not Certificate.objects.filter(title=cert_data['title'], user=student1).exists():
            Certificate.objects.create(certificate_file=dummy_cert, **cert_data)
            cert_count += 1
            
    # Academic Records
    records_data = [
        {'semester': 1, 'subject': 'Mathematics I', 'marks_obtained': 85, 'total_marks': 100, 'grade': 'A', 'attendance_percentage': 90.0},
        {'semester': 1, 'subject': 'Physics', 'marks_obtained': 78, 'total_marks': 100, 'grade': 'B+', 'attendance_percentage': 85.0},
        {'semester': 2, 'subject': 'C Programming', 'marks_obtained': 92, 'total_marks': 100, 'grade': 'O', 'attendance_percentage': 95.0},
        {'semester': 3, 'subject': 'Data Structures', 'marks_obtained': 88, 'total_marks': 100, 'grade': 'A+', 'attendance_percentage': 88.0},
    ]
    
    record_count = 0
    for record_data in records_data:
        if not AcademicRecord.objects.filter(user=student1, semester=record_data['semester'], subject=record_data['subject']).exists():
            AcademicRecord.objects.create(user=student1, **record_data)
            record_count += 1
            
    print(f"  ✓ Created {cert_count} certificates and {record_count} academic records")

def create_hostel_complaints():
    """Create sample hostel complaints"""
    print("\n[15/19] Creating hostel complaints...")
    
    student1 = User.objects.get(username='student1')
    student2 = User.objects.get(username='student2')
    
    complaints_data = [
        {'title': 'Water cooler on 2nd floor malfunctioning', 'description': 'The water cooler on the 2nd floor is not cooling water properly. Please fix it.', 
         'category': 'Maintenance', 'hostel_block': 'Block A', 'room_number': 'Common Area', 'status': 'open', 'posted_by': student1},
        {'title': 'Fan making loud noise', 'description': 'The ceiling fan in my room is making a very loud clicking noise.',
         'category': 'Electrical', 'hostel_block': 'Block A', 'room_number': '201', 'status': 'in_progress', 'posted_by': student1},
        {'title': 'Bathroom tap leaking', 'description': 'The tap in the shared bathroom is leaking continuously.',
         'category': 'Plumbing', 'hostel_block': 'Block B', 'room_number': '305', 'status': 'resolved', 'posted_by': student2,
         'resolved_at': timezone.now() - timedelta(days=2), 'admin_response': 'Tap washer replaced.'},
         {'title': 'Internet connectivity issues', 'description': 'Wi-Fi signal is very weak in room 201.',
         'category': 'Internet', 'hostel_block': 'Block A', 'room_number': '201', 'status': 'open', 'posted_by': student1},
    ]
    
    created_count = 0
    for comp_data in complaints_data:
        if not HostelComplaint.objects.filter(title=comp_data['title'], posted_by=comp_data['posted_by']).exists():
            HostelComplaint.objects.create(**comp_data)
            created_count += 1
            
    print(f"  ✓ Created {created_count} hostel complaints")

def create_mess_ratings():
    """Create sample mess ratings"""
    print("\n[16/19] Creating mess ratings...")
    
    student1 = User.objects.get(username='student1')
    student2 = User.objects.get(username='student2')
    
    # Get some mess menus
    menus = MessMenu.objects.all()[:5]
    
    created_count = 0
    if len(menus) > 0:
        ratings_data = [
            {'menu': menus[0], 'user': student1, 'rating': 4, 'feedback': 'Good food today!'},
            {'menu': menus[0], 'user': student2, 'rating': 3, 'feedback': 'Dal was a bit salty.'},
            {'menu': menus[1], 'user': student1, 'rating': 5, 'feedback': 'Excellent breakfast.'},
        ]
        
        for rating_data in ratings_data:
            if not MessRating.objects.filter(menu=rating_data['menu'], user=rating_data['user']).exists():
                MessRating.objects.create(**rating_data)
                # Update average rating in menu
                menu = rating_data['menu']
                menu.total_ratings += 1
                current_total = (menu.rating * (menu.total_ratings - 1)) + rating_data['rating']
                menu.rating = current_total / menu.total_ratings
                menu.save()
                created_count += 1
                
    print(f"  ✓ Created {created_count} mess ratings")

def create_book_borrowings():
    """Create sample book borrowings"""
    print("\n[17/19] Creating book borrowings...")
    
    student1 = User.objects.get(username='student1')
    
    # Get some books
    books = Book.objects.all()
    
    created_count = 0
    if len(books) >= 2:
        borrowings_data = [
            {'book': books[0], 'user': student1, 'due_date': timezone.now().date() + timedelta(days=7), 'is_returned': False},
            {'book': books[1], 'user': student1, 'due_date': timezone.now().date() - timedelta(days=2), 'is_returned': True, 
             'returned_date': timezone.now().date() - timedelta(days=1)},
        ]
        
        for borrow_data in borrowings_data:
            # Check if this user has borrowed this book recently (simplified check)
            # Use filter().exists() with the specific fields to avoid duplicates
            if not BookBorrowing.objects.filter(book=borrow_data['book'], user=borrow_data['user'], is_returned=borrow_data['is_returned']).exists():
                # Decrement available copies if not returned
                if not borrow_data['is_returned']:
                    book = borrow_data['book']
                    if book.available_copies > 0:
                        book.available_copies -= 1
                        book.save()
                        BookBorrowing.objects.create(**borrow_data)
                        created_count += 1
                else:
                    BookBorrowing.objects.create(**borrow_data)
                    created_count += 1
                    
    print(f"  ✓ Created {created_count} book borrowings")

def create_notifications():
    """Create sample notifications"""
    print("\n[18/19] Creating notifications...")
    
    student1 = User.objects.get(username='student1')
    
    notifications_data = [
        {'user': student1, 'title': 'Exam Schedule Released', 'message': 'The mid-semester exam schedule has been released. Check the Exams section.', 
         'notification_type': 'academic', 'is_read': False},
        {'user': student1, 'title': 'Book Due Soon', 'message': 'Your book "Introduction to Algorithms" is due in 3 days.', 
         'notification_type': 'library', 'is_read': False},
        {'user': student1, 'title': 'Complaint Status Updated', 'message': 'Your complaint regarding "Fan making loud noise" is now In Progress.', 
         'notification_type': 'hostel', 'is_read': True},
    ]
    
    created_count = 0
    for notif_data in notifications_data:
        if not Notification.objects.filter(user=notif_data['user'], title=notif_data['title']).exists():
            Notification.objects.create(**notif_data)
            created_count += 1
            
    print(f"  ✓ Created {created_count} notifications")

def create_applications():
    """Create sample placement applications"""
    print("\n[19/19] Creating placement applications...")
    
    student1 = User.objects.get(username='student1')
    placements = Placement.objects.all()
    
    created_count = 0
    if len(placements) > 0:
        # Create a dummy resume
        from django.core.files.base import ContentFile
        dummy_resume = ContentFile(b"Sample Resume", name="resume.pdf")
        
        app_data = {
            'placement': placements[0],
            'user': student1,
            'cover_letter': 'I am very interested in this position and I have the required skills.',
            'status': 'applied'
        }
        
        if not PlacementApplication.objects.filter(placement=app_data['placement'], user=app_data['user']).exists():
            PlacementApplication.objects.create(resume=dummy_resume, **app_data)
            created_count += 1
            
    print(f"  ✓ Created {created_count} placement applications")

def main():
    """Main function to populate all sample data"""
    print("="*60)
    print("UniEase Sample Data Population".center(60))
    print("="*60)
    
    try:
        create_users()
        create_announcements()
        create_timetable()
        create_syllabus()
        create_exams()
        create_library_data()
        create_mess_menu()
        create_transport()
        create_placements()
        create_doubts()
        create_lost_and_found()
        create_notes()
        create_learning_resources()
        create_academic_vault()
        create_hostel_complaints()
        create_mess_ratings()
        create_book_borrowings()
        create_notifications()
        create_applications()
        
        print("\n" + "="*60)
        print("✓ Sample Data Created Successfully!".center(60))
        print("="*60)
        print("\nSample Login Credentials:")
        print("-" * 60)
        print("  Admin:           admin / admin123")
        print("  Student:         student1 / password123")
        print("  Faculty:         faculty1 / password123")
        print("  Warden:          warden / password123")
        print("  Mess Head:       messhead / password123")
        print("  Librarian:       librarian / password123")
        print("  Placement:       placement / password123")
        print("="*60)
        
        return True
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    if main():
        sys.exit(0)
    else:
        sys.exit(1)
