from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q, Avg
from django.utils import timezone
from datetime import datetime, timedelta
from .models import *


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        expected_role = request.POST.get('expected_role')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            try:
                profile = user.profile
                if not profile.is_approved:
                    messages.error(request, 'Your account is pending administrator approval.')
                    return redirect('login')
                
                role = profile.role
                if expected_role == 'student' and role != 'student':
                    messages.error(request, 'This is the Student Login portal. Staff please use Staff Login.')
                    return redirect(f'/login/?role={expected_role}')
                elif expected_role == 'staff' and role == 'student':
                     messages.error(request, 'This is the Staff Login portal. Students please use Student Login.')
                     return redirect(f'/login/?role={expected_role}')
            except UserProfile.DoesNotExist:
                # Handle edge case where profile doesn't exist yet
                pass

            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = request.POST.get('first_name', '')
            user.last_name = request.POST.get('last_name', '')
            user.save()
            
            # Handle optional fields safely
            raw_year = request.POST.get('year', '')
            year_val = int(raw_year) if raw_year.isdigit() else None
            
            # Determine if approval is needed (everyone except students needs approval)
            is_approved = True if role == 'student' else False
            
            UserProfile.objects.create(
                user=user,
                role=role,
                roll_number=request.POST.get('roll_number', ''),
                department=request.POST.get('department', ''),
                year=year_val,
                phone=request.POST.get('phone', ''),
                is_approved=is_approved
            )
            
            if is_approved:
                messages.success(request, 'Registration successful! Please login.')
            else:
                messages.success(request, 'Registration successful! Your account is pending administrator approval.')
            
            return redirect('login')
    
    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def create_profile(request):
    if hasattr(request.user, 'profile'):
        return redirect('edit_profile')

    if request.method == 'POST':
        role = request.POST.get('role', 'student')
        is_approved = True if role == 'student' else False
        
        UserProfile.objects.create(
            user=request.user,
            role=role,
            roll_number=request.POST.get('roll_number', ''),
            department=request.POST.get('department', ''),
            year=request.POST.get('year', None) if request.POST.get('year') else None,
            phone=request.POST.get('phone', ''),
            is_approved=is_approved
        )
        if is_approved:
            messages.success(request, 'Profile created successfully!')
        else:
            messages.success(request, 'Profile created! Your account is pending administrator approval.')
            logout(request)
            return redirect('login')
        
        return redirect('dashboard')

    return render(request, 'create_profile.html')


@login_required
def edit_profile(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('create_profile')

    if request.method == 'POST':
        profile.roll_number = request.POST.get('roll_number', '')
        profile.department = request.POST.get('department', '')
        
        year_val = request.POST.get('year')
        profile.year = int(year_val) if year_val and year_val.isdigit() else None
        
        profile.phone = request.POST.get('phone', '')
        profile.hostel_room = request.POST.get('hostel_room', '')
            
        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('dashboard')

    return render(request, 'edit_profile.html', {'profile': profile})


@login_required
def dashboard(request):
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        messages.warning(request, 'Please complete your profile to access all features.')
        return redirect('create_profile')

    context = {'user_profile': user_profile}
    role = user_profile.role

    # Common data: Notifications & Announcements
    context['notifications'] = Notification.objects.filter(user=request.user, is_read=False)[:5]
    context['announcements'] = Announcement.objects.filter(
        Q(target_audience='all') | Q(target_audience=role)
    )[:5]

    if role == 'student':
        # Student specific data
        context['upcoming_exams'] = Exam.objects.filter(
            date__gte=timezone.now().date(),
            department=user_profile.department,
            semester=user_profile.year * 2 if user_profile.year else 1
        )[:5]
        context['borrowed_books'] = BookBorrowing.objects.filter(user=request.user, is_returned=False).count()
        context['pending_complaints'] = HostelComplaint.objects.filter(
            posted_by=request.user,
            status__in=['open', 'in_progress']
        ).count()

    elif role == 'faculty':
        # Faculty specific data
        context['my_classes'] = Timetable.objects.filter(faculty__icontains=request.user.last_name).order_by('day', 'time_slot')[:5]
        context['pending_syllabus'] = Syllabus.objects.filter(department=user_profile.department, completed=False)[:5]
        context['unanswered_doubts'] = Doubt.objects.filter(answers__isnull=True).count()
        
    elif role == 'warden':
        # Warden specific data
        context['open_complaints'] = HostelComplaint.objects.filter(
            status__in=['open', 'in_progress']
        ).exclude(category='Mess').order_by('-created_at')[:10]
        context['total_complaints'] = HostelComplaint.objects.exclude(category='Mess').count()
        context['resolved_complaints'] = HostelComplaint.objects.filter(status='resolved').exclude(category='Mess').count()

    elif role == 'mess_head':
        # Mess Head specific data
        context['mess_complaints'] = HostelComplaint.objects.filter(
            status__in=['open', 'in_progress'],
            category='Mess'
        ).order_by('-created_at')[:10]
        context['todays_menu'] = MessMenu.objects.filter(day=timezone.now().strftime('%A'))
        context['average_rating'] = MessMenu.objects.aggregate(Avg('rating'))['rating__avg']

    elif role == 'librarian':
        # Librarian specific data
        context['overdue_books'] = BookBorrowing.objects.filter(
            due_date__lt=timezone.now().date(),
            is_returned=False
        )[:10]
        context['books_borrowed_today'] = BookBorrowing.objects.filter(borrowed_date=timezone.now().date()).count()

    elif role == 'placement_officer':
        # Placement Officer specific data
        context['recent_applications'] = PlacementApplication.objects.order_by('-applied_at')[:10]
        context['active_placements'] = Placement.objects.filter(application_deadline__gte=timezone.now().date()).count()

    if role == 'student':
        return render(request, 'dashboard_student.html', context)
    else:
        return render(request, 'dashboard_staff.html', context)

# ... (rest of the views) ...

@login_required
def hostel_complaints(request):
    role = request.user.profile.role
    
    if role == 'admin':
        complaints = HostelComplaint.objects.all()
    elif role == 'warden':
        complaints = HostelComplaint.objects.exclude(category='Mess')
    elif role == 'mess_head':
        complaints = HostelComplaint.objects.filter(category='Mess')
    elif role == 'student':
        complaints = HostelComplaint.objects.filter(posted_by=request.user)
    else:
        # Default fallback
        complaints = HostelComplaint.objects.filter(posted_by=request.user)
    
    return render(request, 'hostel_complaints.html', {'complaints': complaints})


@login_required
def create_complaint(request):
    if request.method == 'POST':
        HostelComplaint.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            category=request.POST.get('category'), # Ensure frontend sends 'Mess' for mess complaints
            hostel_block=request.POST.get('hostel_block'),
            room_number=request.POST.get('room_number'),
            posted_by=request.user
        )
        messages.success(request, 'Complaint submitted successfully')
        return redirect('hostel_complaints')
    
    return render(request, 'create_complaint.html')


@login_required
def update_complaint(request, complaint_id):
    complaint = get_object_or_404(HostelComplaint, id=complaint_id)
    role = request.user.profile.role
    
    # Check permissions
    allowed = False
    if role == 'admin':
        allowed = True
    elif role == 'warden' and complaint.category != 'Mess':
        allowed = True
    elif role == 'mess_head' and complaint.category == 'Mess':
        allowed = True
        
    if not allowed:
        messages.error(request, 'You do not have permission to update this complaint')
        return redirect('hostel_complaints')
    
    if request.method == 'POST':
        complaint.status = request.POST.get('status')
        complaint.admin_response = request.POST.get('admin_response')
        if complaint.status == 'resolved':
            complaint.resolved_at = timezone.now()
        complaint.save()
        messages.success(request, 'Complaint updated')
        return redirect('hostel_complaints')
    
    return render(request, 'update_complaint.html', {'complaint': complaint})


@login_required
def announcements(request):
    user_profile = request.user.profile
    announcements_list = Announcement.objects.filter(
        Q(target_audience='all') | Q(target_audience=user_profile.role)
    )
    return render(request, 'announcements.html', {'announcements': announcements_list})


@login_required
def create_announcement(request):
    if request.user.profile.role not in ['faculty', 'admin']:
        messages.error(request, 'Only faculty and admin can create announcements')
        return redirect('announcements')

    if request.method == 'POST':
        Announcement.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            posted_by=request.user,
            target_audience=request.POST.get('target_audience'),
            priority=request.POST.get('priority')
        )
        messages.success(request, 'Announcement created successfully')
        return redirect('announcements')

    return render(request, 'create_announcement.html')


@login_required
def edit_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    
    # Check permission: creator or admin
    if request.user != announcement.posted_by and request.user.profile.role != 'admin':
        messages.error(request, 'You do not have permission to edit this announcement.')
        return redirect('announcements')

    if request.method == 'POST':
        announcement.title = request.POST.get('title')
        announcement.content = request.POST.get('content')
        announcement.target_audience = request.POST.get('target_audience')
        announcement.priority = request.POST.get('priority')
        announcement.save()
        
        messages.success(request, 'Announcement updated successfully!')
        return redirect('announcements')
    
    return render(request, 'edit_announcement.html', {'announcement': announcement})


@login_required
def delete_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    
    # Check permission: creator or admin
    if request.user != announcement.posted_by and request.user.profile.role != 'admin':
        messages.error(request, 'You do not have permission to delete this announcement.')
    else:
        announcement.delete()
        messages.success(request, 'Announcement deleted successfully!')
    
    return redirect('announcements')


@login_required
def notes(request):
    user_profile = request.user.profile
    notes_list = Note.objects.filter(
        department=user_profile.department
    )
    
    subject_filter = request.GET.get('subject')
    if subject_filter:
        notes_list = notes_list.filter(subject=subject_filter)
    
    subjects = Note.objects.values_list('subject', flat=True).distinct()
    
    return render(request, 'notes.html', {'notes': notes_list, 'subjects': subjects})


@login_required
def upload_note(request):
    if request.method == 'POST':
        Note.objects.create(
            subject=request.POST.get('subject'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            file=request.FILES.get('file'),
            uploaded_by=request.user,
            semester=request.POST.get('semester'),
            department=request.user.profile.department
        )
        messages.success(request, 'Note uploaded successfully')
        return redirect('notes')
    
    return render(request, 'upload_note.html')


@login_required
def download_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.downloads += 1
    note.save()
    return redirect(note.file.url)


@login_required
def timetable(request):
    user_profile = request.user.profile
    timetable_data = Timetable.objects.filter(
        department=user_profile.department,
        year=user_profile.year
    ).order_by('day', 'time_slot')

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    return render(request, 'timetable.html', {'timetable': timetable_data, 'days': days})


@login_required
def create_timetable(request):
    if request.user.profile.role != 'admin':
        messages.error(request, 'Only admin can create timetable entries')
        return redirect('timetable')

    if request.method == 'POST':
        Timetable.objects.create(
            department=request.POST.get('department'),
            year=request.POST.get('year'),
            semester=request.POST.get('semester'),
            day=request.POST.get('day'),
            time_slot=request.POST.get('time_slot'),
            subject=request.POST.get('subject'),
            faculty=request.POST.get('faculty'),
            room=request.POST.get('room')
        )
        messages.success(request, 'Timetable entry created successfully')
        return redirect('timetable')

    return render(request, 'create_timetable.html')


@login_required
def syllabus(request):
    user_profile = request.user.profile
    semester = user_profile.semester if user_profile.semester else (user_profile.year * 2 if user_profile.year else 1)
    syllabus_data = Syllabus.objects.filter(
        department=user_profile.department,
        semester=semester
    )
    
    subjects = syllabus_data.values_list('subject', flat=True).distinct()
    
    return render(request, 'syllabus.html', {'syllabus': syllabus_data, 'subjects': subjects})


@login_required
def update_syllabus(request, topic_id):
    if request.user.profile.role != 'faculty':
        messages.error(request, 'Only faculty can update syllabus')
        return redirect('syllabus')
    
    topic = get_object_or_404(Syllabus, id=topic_id)
    topic.completed = not topic.completed
    if topic.completed:
        topic.completion_date = timezone.now().date()
    else:
        topic.completion_date = None
    topic.save()
    
    return redirect('syllabus')


@login_required
def exams(request):
    user_profile = request.user.profile
    semester = user_profile.semester if user_profile.semester else (user_profile.year * 2 if user_profile.year else 1)
    exams_list = Exam.objects.filter(
        department=user_profile.department,
        semester=semester
    )
    return render(request, 'exams.html', {'exams': exams_list})


@login_required
def create_exam(request):
    if request.user.profile.role not in ['faculty', 'admin']:
        messages.error(request, 'Only faculty and admin can create exams')
        return redirect('exams')
    
    if request.method == 'POST':
        Exam.objects.create(
            exam_name=request.POST.get('exam_name'),
            subject=request.POST.get('subject'),
            date=request.POST.get('date'),
            time=request.POST.get('time'),
            duration=request.POST.get('duration'),
            hall=request.POST.get('hall'),
            department=request.POST.get('department'),
            semester=request.POST.get('semester')
        )
        messages.success(request, 'Exam created successfully')
        return redirect('exams')
    
    return render(request, 'create_exam.html')


@login_required
def doubts(request):
    doubts_list = Doubt.objects.all()
    
    subject_filter = request.GET.get('subject')
    if subject_filter:
        doubts_list = doubts_list.filter(subject=subject_filter)
    
    subjects = Doubt.objects.values_list('subject', flat=True).distinct()
    
    return render(request, 'doubts.html', {'doubts': doubts_list, 'subjects': subjects})


@login_required
def ask_doubt(request):
    if request.method == 'POST':
        Doubt.objects.create(
            question=request.POST.get('question'),
            subject=request.POST.get('subject'),
            topic=request.POST.get('topic'),
            posted_by=request.user,
            is_anonymous=request.POST.get('is_anonymous') == 'on'
        )
        messages.success(request, 'Doubt posted successfully')
        return redirect('doubts')
    
    return render(request, 'ask_doubt.html')


@login_required
def doubt_detail(request, doubt_id):
    doubt = get_object_or_404(Doubt, id=doubt_id)
    doubt.views += 1
    doubt.save()
    
    answers = doubt.answers.all()
    
    return render(request, 'doubt_detail.html', {'doubt': doubt, 'answers': answers})


@login_required
def answer_doubt(request, doubt_id):
    doubt = get_object_or_404(Doubt, id=doubt_id)
    
    if request.method == 'POST':
        Answer.objects.create(
            doubt=doubt,
            answer=request.POST.get('answer'),
            answered_by=request.user
        )
        messages.success(request, 'Answer posted successfully')
        return redirect('doubt_detail', doubt_id=doubt_id)


@login_required
def upvote_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    
    upvote, created = AnswerUpvote.objects.get_or_create(answer=answer, user=request.user)
    
    if not created:
        upvote.delete()
        answer.upvotes -= 1
    else:
        answer.upvotes += 1
    
    answer.save()
    return redirect('doubt_detail', doubt_id=answer.doubt.id)


@login_required
def lost_found(request):
    items = LostItem.objects.all()
    
    status_filter = request.GET.get('status')
    if status_filter:
        items = items.filter(status=status_filter)
    
    return render(request, 'lost_found.html', {'items': items})


@login_required
def post_lost_item(request):
    if request.method == 'POST':
        LostItem.objects.create(
            item_name=request.POST.get('item_name'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
            location=request.POST.get('location'),
            status=request.POST.get('status'),
            posted_by=request.user,
            contact=request.POST.get('contact'),
            image=request.FILES.get('image')
        )
        messages.success(request, 'Item posted successfully')
        return redirect('lost_found')
    
    return render(request, 'post_lost_item.html')


@login_required
def update_lost_item_status(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)
    
    if request.user != item.posted_by:
        messages.error(request, 'You can only update your own items')
        return redirect('lost_found')
    
    if request.method == 'POST':
        item.status = request.POST.get('status')
        item.save()
        messages.success(request, 'Item status updated')
        return redirect('lost_found')





@login_required
def transport(request):
    routes = BusRoute.objects.all()
    return render(request, 'transport.html', {'routes': routes})


@login_required
def mess(request):
    if request.method == 'POST' and request.user.profile.role == 'mess_head':
        day = request.POST.get('day')
        meal_type = request.POST.get('meal_type')
        items = request.POST.get('items')
        
        MessMenu.objects.update_or_create(
            day=day,
            meal_type=meal_type,
            defaults={'items': items}
        )
        messages.success(request, f'Menu updated for {day} {meal_type}')
        return redirect('mess')

    menus = MessMenu.objects.all().order_by('day', 'meal_type')
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Pass user_profile for role calculation in template
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        user_profile = None

    return render(request, 'mess.html', {'menus': menus, 'days': days, 'user_profile': user_profile})


@login_required
def rate_mess(request, menu_id):
    menu = get_object_or_404(MessMenu, id=menu_id)
    
    if request.method == 'POST':
        rating_value = int(request.POST.get('rating'))
        feedback = request.POST.get('feedback', '')
        
        rating, created = MessRating.objects.get_or_create(
            menu=menu,
            user=request.user,
            defaults={'rating': rating_value, 'feedback': feedback}
        )
        
        if not created:
            rating.rating = rating_value
            rating.feedback = feedback
            rating.save()
        
        # Update average rating
        avg_rating = MessRating.objects.filter(menu=menu).aggregate(Avg('rating'))['rating__avg']
        menu.rating = round(avg_rating, 1)
        menu.total_ratings = MessRating.objects.filter(menu=menu).count()
        menu.save()
        
        messages.success(request, 'Rating submitted successfully')
        return redirect('mess')


@login_required
def library(request):
    # Handle Add Book (Librarian Only)
    if request.method == 'POST' and request.user.profile.role == 'librarian':
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        category = request.POST.get('category')
        total_copies = int(request.POST.get('total_copies', 1))
        
        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            category=category,
            total_copies=total_copies,
            available_copies=total_copies
        )
        messages.success(request, 'new book added to library')
        return redirect('library')

    books = Book.objects.all()
    
    search = request.GET.get('search')
    if search:
        books = books.filter(
            Q(title__icontains=search) | Q(author__icontains=search) | Q(isbn__icontains=search)
        )
    
    user_borrowings = BookBorrowing.objects.filter(user=request.user, is_returned=False)
    
    # Pass user_profile explicitly
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        user_profile = None

    return render(request, 'library.html', {'books': books, 'borrowings': user_borrowings, 'user_profile': user_profile})


@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if book.available_copies > 0:
        due_date = timezone.now().date() + timedelta(days=14)
        
        BookBorrowing.objects.create(
            book=book,
            user=request.user,
            due_date=due_date
        )
        
        book.available_copies -= 1
        book.save()
        
        messages.success(request, f'Book borrowed successfully! Due date: {due_date}')
    else:
        messages.error(request, 'Book not available')
    
    return redirect('library')


@login_required
def return_book(request, borrowing_id):
    borrowing = get_object_or_404(BookBorrowing, id=borrowing_id)
    
    if borrowing.user != request.user:
        messages.error(request, 'Invalid request')
        return redirect('library')
    
    borrowing.is_returned = True
    borrowing.returned_date = timezone.now().date()
    
    # Calculate fine if overdue
    if borrowing.returned_date > borrowing.due_date:
        days_overdue = (borrowing.returned_date - borrowing.due_date).days
        borrowing.fine = days_overdue * 5  # Rs. 5 per day
    
    borrowing.save()
    
    # Increase available copies
    borrowing.book.available_copies += 1
    borrowing.book.save()
    
    messages.success(request, 'Book returned successfully')
    return redirect('library')


@login_required
def library_seats(request):
    # Handle Live Counter Updates (Librarian Only)
    if request.method == 'POST' and request.user.profile.role == 'librarian':
        action = request.POST.get('action')
        
        if action == 'enter':
            # Find first available seat
            seat = LibrarySeat.objects.filter(is_available=True).first()
            if seat:
                seat.is_available = False
                seat.occupied_at = timezone.now()
                seat.save()
                messages.success(request, 'Student Entry Recorded (+1)')
            else:
                messages.error(request, 'Library is Full!')
                
        elif action == 'exit':
            # Find an occupied seat to free up
            seat = LibrarySeat.objects.filter(is_available=False).order_by('-occupied_at').first()
            if seat:
                seat.is_available = True
                seat.occupied_by = None
                seat.occupied_at = None
                seat.save()
                messages.success(request, 'Student Exit Recorded (-1)')
            else:
                messages.warning(request, 'Library is already empty!')
        
        return redirect('library_seats')

    # Statistics for the Dashboard
    total_seats = LibrarySeat.objects.count()
    occupied_seats = LibrarySeat.objects.filter(is_available=False).count()
    available_seats = total_seats - occupied_seats
    occupancy_rate = (occupied_seats / total_seats * 100) if total_seats > 0 else 0
    
    # Still pass individual seats if they want to see details, but focus is on stats
    seats = LibrarySeat.objects.all().order_by('floor', 'seat_number')
    
    # Pass user_profile explicitly
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        user_profile = None

    context = {
        'seats': seats,
        'user_profile': user_profile,
        'total_seats': total_seats,
        'occupied_seats': occupied_seats,
        'available_seats': available_seats,
        'occupancy_rate': round(occupancy_rate, 1)
    }

    return render(request, 'library_seats.html', context)


@login_required
def placements(request):
    placements_list = Placement.objects.all()
    
    job_type_filter = request.GET.get('job_type')
    if job_type_filter:
        placements_list = placements_list.filter(job_type=job_type_filter)
    
    user_applications = PlacementApplication.objects.filter(user=request.user).values_list('placement_id', flat=True)
    
    return render(request, 'placements.html', {'placements': placements_list, 'user_applications': user_applications})


@login_required
def create_placement(request):
    if request.user.profile.role not in ['faculty', 'admin']:
        messages.error(request, 'Only faculty and admin can create placements')
        return redirect('placements')

    if request.method == 'POST':
        Placement.objects.create(
            company_name=request.POST.get('company_name'),
            job_role=request.POST.get('job_role'),
            job_type=request.POST.get('job_type'),
            description=request.POST.get('description'),
            eligibility=request.POST.get('eligibility'),
            required_skills=request.POST.get('required_skills'),
            package=request.POST.get('package'),
            application_deadline=request.POST.get('application_deadline'),
            posted_by=request.user
        )
        messages.success(request, 'Placement created successfully')
        return redirect('placements')

    return render(request, 'create_placement.html')


@login_required
def placement_detail(request, placement_id):
    placement = get_object_or_404(Placement, id=placement_id)
    has_applied = PlacementApplication.objects.filter(placement=placement, user=request.user).exists()
    
    return render(request, 'placement_detail.html', {'placement': placement, 'has_applied': has_applied})


@login_required
def apply_placement(request, placement_id):
    placement = get_object_or_404(Placement, id=placement_id)
    
    if request.method == 'POST':
        PlacementApplication.objects.create(
            placement=placement,
            user=request.user,
            resume=request.FILES.get('resume'),
            cover_letter=request.POST.get('cover_letter')
        )
        messages.success(request, 'Application submitted successfully')
        return redirect('placement_detail', placement_id=placement_id)
    
    return render(request, 'apply_placement.html', {'placement': placement})


@login_required
def learning_resources(request):
    resources = LearningResource.objects.all()
    
    category_filter = request.GET.get('category')
    if category_filter:
        resources = resources.filter(category=category_filter)
    
    categories = LearningResource.objects.values_list('category', flat=True).distinct()
    
    return render(request, 'learning_resources.html', {'resources': resources, 'categories': categories})


@login_required
def academic_vault(request):
    certificates = Certificate.objects.filter(user=request.user)
    records = AcademicRecord.objects.filter(user=request.user)
    
    return render(request, 'academic_vault.html', {'certificates': certificates, 'records': records})


@login_required
def upload_certificate(request):
    if request.method == 'POST':
        Certificate.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            issuer=request.POST.get('issuer'),
            issue_date=request.POST.get('issue_date'),
            certificate_file=request.FILES.get('certificate_file'),
            category=request.POST.get('category')
        )
        messages.success(request, 'Certificate uploaded successfully')
        return redirect('academic_vault')
    
    return render(request, 'upload_certificate.html')


@login_required
def add_academic_record(request):
    if request.method == 'POST':
        AcademicRecord.objects.create(
            user=request.user,
            semester=request.POST.get('semester'),
            subject=request.POST.get('subject'),
            marks_obtained=request.POST.get('marks_obtained'),
            total_marks=request.POST.get('total_marks'),
            grade=request.POST.get('grade'),
            attendance_percentage=request.POST.get('attendance_percentage')
        )
        messages.success(request, 'Academic record added successfully')
        return redirect('academic_vault')
    
    return render(request, 'add_academic_record.html')


@login_required
def performance_insights(request):
    records = AcademicRecord.objects.filter(user=request.user)
    
    if not records.exists():
        return render(request, 'performance_insights.html', {'message': 'No records found'})
    
    # Calculate overall average
    total_marks = sum(r.marks_obtained for r in records)
    total_possible = sum(r.total_marks for r in records)
    overall_percentage = (total_marks / total_possible * 100) if total_possible > 0 else 0
    
    # Calculate semester-wise performance
    semesters = records.values_list('semester', flat=True).distinct()
    semester_data = []
    for sem in semesters:
        sem_records = records.filter(semester=sem)
        sem_total = sum(r.marks_obtained for r in sem_records)
        sem_possible = sum(r.total_marks for r in sem_records)
        sem_percentage = (sem_total / sem_possible * 100) if sem_possible > 0 else 0
        semester_data.append({
            'semester': sem,
            'percentage': round(sem_percentage, 2)
        })
    
    # Calculate average attendance
    avg_attendance = records.aggregate(Avg('attendance_percentage'))['attendance_percentage__avg']
    
    context = {
        'overall_percentage': round(overall_percentage, 2),
        'semester_data': semester_data,
        'avg_attendance': round(avg_attendance, 2) if avg_attendance else 0,
        'total_subjects': records.count()
    }
    
    return render(request, 'performance_insights.html', context)


@login_required
def notifications(request):
    notifications_list = Notification.objects.filter(user=request.user)
    return render(request, 'notifications.html', {'notifications': notifications_list})


@login_required
def mark_notification_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notifications')

# Admin Approval Views
@login_required
def pending_approvals(request):
    if request.user.profile.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('dashboard')
    
    pending_users = UserProfile.objects.filter(is_approved=False).select_related('user')
    return render(request, 'admin_approvals.html', {'pending_users': pending_users})

@login_required
def approve_user(request, user_id):
    if request.user.profile.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('dashboard')
    
    profile = get_object_or_404(UserProfile, id=user_id)
    profile.is_approved = True
    profile.save()
    
    # Notify user
    Notification.objects.create(
        user=profile.user,
        title='Account Approved',
        message='Your account has been approved by the administrator. You can now access all features.',
        notification_type='info'
    )
    
    messages.success(request, f'Account for {profile.user.username} has been approved.')
    return redirect('pending_approvals')

@login_required
def reject_user(request, user_id):
    if request.user.profile.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('dashboard')
    
    profile = get_object_or_404(UserProfile, id=user_id)
    user = profile.user
    username = user.username
    user.delete() # Deleting user will cascade to profile
    
    messages.warning(request, f'Account for {username} has been rejected and deleted.')
    return redirect('pending_approvals')
