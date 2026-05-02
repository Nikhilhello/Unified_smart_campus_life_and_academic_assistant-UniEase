from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('admin', 'Admin'),
        ('warden', 'Warden'),
        ('mess_head', 'Mess Head'),
        ('librarian', 'Librarian'),
        ('placement_officer', 'Placement Officer'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='student')
    roll_number = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    hostel_room = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_approved = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    target_audience = models.CharField(max_length=100, default='all')
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium')
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Note(models.Model):
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='notes/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.IntegerField()
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    downloads = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.subject} - {self.title}"


class Timetable(models.Model):
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    semester = models.IntegerField()
    day = models.CharField(max_length=20)
    time_slot = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    room = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.department} - Year {self.year} - {self.day} - {self.time_slot}"


class Syllabus(models.Model):
    subject = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()
    topic = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    completion_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.subject} - {self.topic}"


class Exam(models.Model):
    exam_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    duration = models.CharField(max_length=50)
    hall = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()
    
    class Meta:
        ordering = ['date', 'time']
    
    def __str__(self):
        return f"{self.exam_name} - {self.subject}"


class Doubt(models.Model):
    question = models.TextField()
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.subject} - {self.topic}"


class Answer(models.Model):
    doubt = models.ForeignKey(Doubt, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-upvotes', '-created_at']
    
    def __str__(self):
        return f"Answer to {self.doubt.id}"


class AnswerUpvote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('answer', 'user')


class LostItem(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
        ('returned', 'Returned'),
    ]
    
    item_name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='lost')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)
    image = models.ImageField(upload_to='lost_found/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.item_name} - {self.status}"


class HostelComplaint(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    hostel_block = models.CharField(max_length=50)
    room_number = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
    admin_response = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.status}"


class BusRoute(models.Model):
    route_number = models.CharField(max_length=20)
    route_name = models.CharField(max_length=200)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    stops = models.TextField()
    is_delayed = models.BooleanField(default=False)
    delay_minutes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.route_number} - {self.route_name}"


class MessMenu(models.Model):
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('snacks', 'Snacks'),
        ('dinner', 'Dinner'),
    ]
    
    day = models.CharField(max_length=20)
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)
    items = models.TextField()
    rating = models.FloatField(default=0.0)
    total_ratings = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.day} - {self.meal_type}"


class MessRating(models.Model):
    menu = models.ForeignKey(MessMenu, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('menu', 'user')


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=100)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    publisher = models.CharField(max_length=200, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class BookBorrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    returned_date = models.DateField(blank=True, null=True)
    is_returned = models.BooleanField(default=False)
    fine = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    class Meta:
        ordering = ['-borrowed_date']
    
    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


class LibrarySeat(models.Model):
    seat_number = models.CharField(max_length=20, unique=True)
    floor = models.IntegerField(default=1)
    is_available = models.BooleanField(default=True)
    occupied_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    occupied_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"Seat {self.seat_number} - Floor {self.floor}"


class Placement(models.Model):
    company_name = models.CharField(max_length=200)
    job_role = models.CharField(max_length=200)
    job_type = models.CharField(max_length=50, choices=[('internship', 'Internship'), ('fulltime', 'Full Time')], default='fulltime')
    description = models.TextField()
    eligibility = models.TextField()
    required_skills = models.TextField(blank=True, null=True)
    package = models.CharField(max_length=100)
    application_deadline = models.DateField()
    interview_date = models.DateField(blank=True, null=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.company_name} - {self.job_role}"


class PlacementApplication(models.Model):
    placement = models.ForeignKey(Placement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    status = models.CharField(max_length=50, choices=[('applied', 'Applied'), ('shortlisted', 'Shortlisted'), ('rejected', 'Rejected'), ('selected', 'Selected')], default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('placement', 'user')
        ordering = ['-applied_at']


class LearningResource(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    resource_type = models.CharField(max_length=50, choices=[('video', 'Video'), ('article', 'Article'), ('course', 'Course'), ('tutorial', 'Tutorial')])
    url = models.URLField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    issue_date = models.DateField()
    certificate_file = models.FileField(upload_to='certificates/')
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-issue_date']
    
    def __str__(self):
        return f"{self.user.username} - {self.title}"


class AcademicRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.IntegerField()
    subject = models.CharField(max_length=100)
    marks_obtained = models.FloatField()
    total_marks = models.FloatField()
    grade = models.CharField(max_length=5)
    attendance_percentage = models.FloatField()
    
    class Meta:
        ordering = ['-semester']
    
    def __str__(self):
        return f"{self.user.username} - Sem {self.semester} - {self.subject}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    notification_type = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.title}"
