from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils import timezone
from .models import (
    UserProfile, Announcement, Note, Timetable, Syllabus, Exam,
    Doubt, Answer, LostItem, HostelComplaint, BusRoute, MessMenu,
    Book, BookBorrowing, LibrarySeat, Placement, PlacementApplication,
    LearningResource, Certificate, AcademicRecord, Notification, AnswerUpvote, MessRating
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'department', 'year', 'roll_number', 'phone', 'is_approved')
    list_filter = ('role', 'is_approved', 'department', 'year')
    search_fields = ('user__username', 'user__email', 'roll_number', 'phone')
    readonly_fields = ('user',)
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'role', 'is_approved')
        }),
        ('Academic Details', {
            'fields': ('roll_number', 'department', 'year')
        }),
        ('Contact & Accommodation', {
            'fields': ('phone', 'hostel_room', 'profile_picture')
        }),
    )


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_by', 'target_audience', 'priority', 'created_at', 'priority_badge')
    list_filter = ('priority', 'target_audience', 'created_at')
    search_fields = ('title', 'content', 'posted_by__username')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Announcement Details', {
            'fields': ('title', 'content', 'priority')
        }),
        ('Targeting', {
            'fields': ('target_audience',)
        }),
        ('Meta Information', {
            'fields': ('posted_by', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    
    def priority_badge(self, obj):
        colors = {'low': 'gray', 'medium': 'orange', 'high': 'red'}
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 3px;">{}</span>',
            colors.get(obj.priority, 'gray'),
            obj.priority.upper()
        )
    priority_badge.short_description = 'Priority Status'
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.posted_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'department', 'semester', 'uploaded_by', 'downloads', 'created_at')
    list_filter = ('department', 'semester', 'subject', 'created_at')
    search_fields = ('title', 'subject', 'description')
    readonly_fields = ('downloads', 'created_at', 'uploaded_by')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Note Information', {
            'fields': ('title', 'subject', 'description', 'file')
        }),
        ('Academic Details', {
            'fields': ('department', 'semester')
        }),
        ('Statistics', {
            'fields': ('uploaded_by', 'downloads', 'created_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('department', 'year', 'semester', 'day', 'time_slot', 'subject', 'faculty', 'room')
    list_filter = ('department', 'year', 'semester', 'day')
    search_fields = ('subject', 'faculty', 'room')
    
    fieldsets = (
        ('Class Information', {
            'fields': ('department', 'year', 'semester')
        }),
        ('Schedule', {
            'fields': ('day', 'time_slot', 'subject', 'faculty', 'room')
        }),
    )


@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('subject', 'topic', 'department', 'semester', 'completed', 'completion_status')
    list_filter = ('completed', 'department', 'semester')
    search_fields = ('subject', 'topic')
    actions = ['mark_as_completed', 'mark_as_incomplete']
    
    def completion_status(self, obj):
        if obj.completed:
            return format_html('<span style="color: green;">✓ Completed</span>')
        return format_html('<span style="color: orange;">○ Pending</span>')
    completion_status.short_description = 'Status'
    
    def mark_as_completed(self, request, queryset):
        queryset.update(completed=True, completion_date=timezone.now().date())
        self.message_user(request, f'{queryset.count()} topics marked as completed.')
    mark_as_completed.short_description = 'Mark selected as completed'
    
    def mark_as_incomplete(self, request, queryset):
        queryset.update(completed=False, completion_date=None)
        self.message_user(request, f'{queryset.count()} topics marked as incomplete.')
    mark_as_incomplete.short_description = 'Mark selected as incomplete'


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'subject', 'date', 'time', 'hall', 'department', 'semester')
    list_filter = ('department', 'semester', 'date')
    search_fields = ('exam_name', 'subject', 'hall')
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Exam Details', {
            'fields': ('exam_name', 'subject', 'date', 'time', 'duration')
        }),
        ('Academic Information', {
            'fields': ('department', 'semester')
        }),
        ('Venue', {
            'fields': ('hall', 'seat_number')
        }),
    )


@admin.register(Doubt)
class DoubtAdmin(admin.ModelAdmin):
    list_display = ('subject', 'topic', 'posted_by', 'is_anonymous', 'views', 'answer_count', 'created_at')
    list_filter = ('subject', 'is_anonymous', 'created_at')
    search_fields = ('question', 'subject', 'topic')
    readonly_fields = ('views', 'created_at', 'posted_by')
    date_hierarchy = 'created_at'
    
    def answer_count(self, obj):
        count = obj.answers.count()
        return format_html('<span style="font-weight: bold;">{}</span>', count)
    answer_count.short_description = 'Answers'


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('doubt', 'answered_by', 'upvotes', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('answer', 'answered_by__username')
    readonly_fields = ('upvotes', 'created_at', 'answered_by')
    date_hierarchy = 'created_at'


@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'category', 'status', 'location', 'posted_by', 'status_badge', 'created_at')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('item_name', 'description', 'location')
    actions = ['mark_as_found', 'mark_as_returned']
    date_hierarchy = 'created_at'
    
    def status_badge(self, obj):
        colors = {'lost': 'red', 'found': 'orange', 'returned': 'green'}
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 3px;">{}</span>',
            colors.get(obj.status, 'gray'),
            obj.status.upper()
        )
    status_badge.short_description = 'Status'
    
    def mark_as_found(self, request, queryset):
        queryset.update(status='found')
        self.message_user(request, f'{queryset.count()} items marked as found.')
    mark_as_found.short_description = 'Mark as found'
    
    def mark_as_returned(self, request, queryset):
        queryset.update(status='returned')
        self.message_user(request, f'{queryset.count()} items marked as returned.')
    mark_as_returned.short_description = 'Mark as returned'


@admin.register(HostelComplaint)
class HostelComplaintAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'hostel_block', 'room_number', 'status', 'posted_by', 'status_badge', 'created_at')
    list_filter = ('status', 'category', 'hostel_block', 'created_at')
    search_fields = ('title', 'description', 'room_number')
    actions = ['mark_in_progress', 'mark_resolved']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Complaint Details', {
            'fields': ('title', 'description', 'category')
        }),
        ('Location', {
            'fields': ('hostel_block', 'room_number')
        }),
        ('Status & Response', {
            'fields': ('status', 'admin_response', 'resolved_at')
        }),
        ('Meta', {
            'fields': ('posted_by', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    
    def status_badge(self, obj):
        colors = {'open': 'red', 'in_progress': 'orange', 'resolved': 'green'}
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 3px;">{}</span>',
            colors.get(obj.status, 'gray'),
            obj.status.replace('_', ' ').upper()
        )
    status_badge.short_description = 'Status'
    
    def mark_in_progress(self, request, queryset):
        queryset.update(status='in_progress')
        self.message_user(request, f'{queryset.count()} complaints marked as in progress.')
    mark_in_progress.short_description = 'Mark as in progress'
    
    def mark_resolved(self, request, queryset):
        queryset.update(status='resolved', resolved_at=timezone.now())
        self.message_user(request, f'{queryset.count()} complaints marked as resolved.')
    mark_resolved.short_description = 'Mark as resolved'


@admin.register(BusRoute)
class BusRouteAdmin(admin.ModelAdmin):
    list_display = ('route_number', 'route_name', 'departure_time', 'arrival_time', 'is_delayed', 'delay_status')
    list_filter = ('is_delayed',)
    search_fields = ('route_number', 'route_name', 'stops')
    actions = ['mark_delayed', 'clear_delay']
    
    def delay_status(self, obj):
        if obj.is_delayed:
            return format_html('<span style="color: red;">⚠ Delayed by {} min</span>', obj.delay_minutes)
        return format_html('<span style="color: green;">✓ On Time</span>')
    delay_status.short_description = 'Status'
    
    def mark_delayed(self, request, queryset):
        queryset.update(is_delayed=True)
        self.message_user(request, f'{queryset.count()} routes marked as delayed.')
    mark_delayed.short_description = 'Mark as delayed'
    
    def clear_delay(self, request, queryset):
        queryset.update(is_delayed=False, delay_minutes=0)
        self.message_user(request, f'{queryset.count()} routes cleared from delay.')
    clear_delay.short_description = 'Clear delay'


@admin.register(MessMenu)
class MessMenuAdmin(admin.ModelAdmin):
    list_display = ('day', 'meal_type', 'rating', 'total_ratings')
    list_filter = ('day', 'meal_type')
    search_fields = ('items',)
    
    fieldsets = (
        ('Menu Details', {
            'fields': ('day', 'meal_type', 'items')
        }),
        ('Ratings', {
            'fields': ('rating', 'total_ratings'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'category', 'total_copies', 'available_copies', 'availability_status')
    list_filter = ('category', 'year')
    search_fields = ('title', 'author', 'isbn', 'publisher')
    
    def availability_status(self, obj):
        if obj.available_copies > 0:
            percentage = (obj.available_copies / obj.total_copies) * 100
            color = 'green' if percentage > 50 else 'orange' if percentage > 0 else 'red'
            return format_html('<span style="color: {};">{}/{} available</span>', color, obj.available_copies, obj.total_copies)
        return format_html('<span style="color: red;">Out of Stock</span>')
    availability_status.short_description = 'Availability'


@admin.register(BookBorrowing)
class BookBorrowingAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrowed_date', 'due_date', 'returned_date', 'is_returned', 'fine', 'return_status')
    list_filter = ('is_returned', 'borrowed_date', 'due_date')
    search_fields = ('user__username', 'book__title')
    date_hierarchy = 'borrowed_date'
    actions = ['mark_as_returned']
    
    def return_status(self, obj):
        if obj.is_returned:
            return format_html('<span style="color: green;">✓ Returned</span>')
        elif obj.due_date < timezone.now().date():
            return format_html('<span style="color: red;">⚠ Overdue</span>')
        return format_html('<span style="color: orange;">○ Borrowed</span>')
    return_status.short_description = 'Status'
    
    def mark_as_returned(self, request, queryset):
        queryset.update(is_returned=True, returned_date=timezone.now().date())
        self.message_user(request, f'{queryset.count()} books marked as returned.')
    mark_as_returned.short_description = 'Mark as returned'


@admin.register(LibrarySeat)
class LibrarySeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'floor', 'is_available', 'occupied_by', 'occupied_at', 'occupancy_status')
    list_filter = ('is_available', 'floor')
    search_fields = ('seat_number', 'occupied_by__username')
    actions = ['release_seats']
    
    def occupancy_status(self, obj):
        if not obj.is_available:
            return format_html('<span style="color: red;">● Occupied</span>')
        return format_html('<span style="color: green;">○ Available</span>')
    occupancy_status.short_description = 'Status'
    
    def release_seats(self, request, queryset):
        queryset.update(is_available=True, occupied_by=None, occupied_at=None)
        self.message_user(request, f'{queryset.count()} seats released.')
    release_seats.short_description = 'Release selected seats'


@admin.register(Placement)
class PlacementAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'job_role', 'job_type', 'package', 'application_deadline', 'applications_count', 'created_at')
    list_filter = ('job_type', 'application_deadline', 'created_at')
    search_fields = ('company_name', 'job_role', 'description')
    date_hierarchy = 'application_deadline'
    
    fieldsets = (
        ('Job Details', {
            'fields': ('company_name', 'job_role', 'job_type', 'description')
        }),
        ('Requirements', {
            'fields': ('eligibility', 'required_skills', 'package')
        }),
        ('Timeline', {
            'fields': ('application_deadline', 'interview_date')
        }),
        ('Meta', {
            'fields': ('posted_by', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    
    def applications_count(self, obj):
        count = PlacementApplication.objects.filter(placement=obj).count()
        return format_html('<span style="font-weight: bold;">{} applications</span>', count)
    applications_count.short_description = 'Applications'


@admin.register(PlacementApplication)
class PlacementApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'placement', 'status', 'status_badge', 'applied_at')
    list_filter = ('status', 'applied_at')
    search_fields = ('user__username', 'placement__company_name', 'placement__job_role')
    date_hierarchy = 'applied_at'
    actions = ['shortlist_candidates', 'reject_candidates', 'select_candidates']
    
    def status_badge(self, obj):
        colors = {'applied': 'blue', 'shortlisted': 'orange', 'rejected': 'red', 'selected': 'green'}
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 3px;">{}</span>',
            colors.get(obj.status, 'gray'),
            obj.status.upper()
        )
    status_badge.short_description = 'Status'
    
    def shortlist_candidates(self, request, queryset):
        queryset.update(status='shortlisted')
        self.message_user(request, f'{queryset.count()} candidates shortlisted.')
    shortlist_candidates.short_description = 'Shortlist selected candidates'
    
    def reject_candidates(self, request, queryset):
        queryset.update(status='rejected')
        self.message_user(request, f'{queryset.count()} candidates rejected.')
    reject_candidates.short_description = 'Reject selected candidates'
    
    def select_candidates(self, request, queryset):
        queryset.update(status='selected')
        self.message_user(request, f'{queryset.count()} candidates selected.')
    select_candidates.short_description = 'Select candidates'


@admin.register(LearningResource)
class LearningResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'resource_type', 'posted_by', 'created_at')
    list_filter = ('resource_type', 'category', 'created_at')
    search_fields = ('title', 'description', 'category')
    date_hierarchy = 'created_at'


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'issuer', 'issue_date', 'category')
    list_filter = ('category', 'issue_date')
    search_fields = ('user__username', 'title', 'issuer')
    date_hierarchy = 'issue_date'


@admin.register(AcademicRecord)
class AcademicRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'semester', 'subject', 'marks_obtained', 'total_marks', 'grade', 'percentage', 'attendance_percentage')
    list_filter = ('semester', 'grade')
    search_fields = ('user__username', 'subject')
    
    def percentage(self, obj):
        if obj.total_marks > 0:
            pct = (obj.marks_obtained / obj.total_marks) * 100
            color = 'green' if pct >= 75 else 'orange' if pct >= 50 else 'red'
            return format_html('<span style="color: {};">{:.2f}%</span>', color, pct)
        return '-'
    percentage.short_description = 'Percentage'


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'notification_type', 'is_read', 'read_status', 'created_at')
    list_filter = ('is_read', 'notification_type', 'created_at')
    search_fields = ('user__username', 'title', 'message')
    date_hierarchy = 'created_at'
    actions = ['mark_as_read', 'mark_as_unread']
    
    def read_status(self, obj):
        if obj.is_read:
            return format_html('<span style="color: green;">✓ Read</span>')
        return format_html('<span style="color: orange;">○ Unread</span>')
    read_status.short_description = 'Status'
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, f'{queryset.count()} notifications marked as read.')
    mark_as_read.short_description = 'Mark as read'
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
        self.message_user(request, f'{queryset.count()} notifications marked as unread.')
    mark_as_unread.short_description = 'Mark as unread'


# Register remaining models with basic admin
admin.site.register(AnswerUpvote)
admin.site.register(MessRating)

# Customize admin site header and title
admin.site.site_header = 'UniiEase Admin Panel'
admin.site.site_title = 'UniiEase Admin'
admin.site.index_title = 'Welcome to UniiEase Administration'
