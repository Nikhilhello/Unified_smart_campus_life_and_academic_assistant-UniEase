from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Announcements & Notes
    path('announcements/', views.announcements, name='announcements'),
    path('announcements/create/', views.create_announcement, name='create_announcement'),
    path('announcements/edit/<int:announcement_id>/', views.edit_announcement, name='edit_announcement'),
    path('announcements/delete/<int:announcement_id>/', views.delete_announcement, name='delete_announcement'),
    path('notes/', views.notes, name='notes'),
    path('notes/upload/', views.upload_note, name='upload_note'),
    path('notes/download/<int:note_id>/', views.download_note, name='download_note'),
    
    # Timetable & Syllabus
    path('timetable/', views.timetable, name='timetable'),
    path('timetable/create/', views.create_timetable, name='create_timetable'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('syllabus/update/<int:topic_id>/', views.update_syllabus, name='update_syllabus'),
    
    # Exams
    path('exams/', views.exams, name='exams'),
    path('exams/create/', views.create_exam, name='create_exam'),
    
    # Doubts
    path('doubts/', views.doubts, name='doubts'),
    path('doubts/ask/', views.ask_doubt, name='ask_doubt'),
    path('doubts/<int:doubt_id>/', views.doubt_detail, name='doubt_detail'),
    path('doubts/<int:doubt_id>/answer/', views.answer_doubt, name='answer_doubt'),
    path('answer/<int:answer_id>/upvote/', views.upvote_answer, name='upvote_answer'),
    
    # Lost & Found
    path('lost-found/', views.lost_found, name='lost_found'),
    path('lost-found/post/', views.post_lost_item, name='post_lost_item'),
    path('lost-found/update/<int:item_id>/', views.update_lost_item_status, name='update_lost_item_status'),
    
    # Hostel Complaints
    path('hostel-complaints/', views.hostel_complaints, name='hostel_complaints'),
    path('hostel-complaints/create/', views.create_complaint, name='create_complaint'),
    path('hostel-complaints/update/<int:complaint_id>/', views.update_complaint, name='update_complaint'),
    
    # Transport & Mess
    path('transport/', views.transport, name='transport'),
    path('mess/', views.mess, name='mess'),
    path('mess/rate/<int:menu_id>/', views.rate_mess, name='rate_mess'),
    
    # Library
    path('library/', views.library, name='library'),
    path('library/borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('library/return/<int:borrowing_id>/', views.return_book, name='return_book'),
    path('library/seats/', views.library_seats, name='library_seats'),
    
    # Placements
    path('placements/', views.placements, name='placements'),
    path('placements/create/', views.create_placement, name='create_placement'),
    path('placements/<int:placement_id>/', views.placement_detail, name='placement_detail'),
    path('placements/<int:placement_id>/apply/', views.apply_placement, name='apply_placement'),
    path('resources/', views.learning_resources, name='learning_resources'),
    
    # Academic Vault
    path('vault/', views.academic_vault, name='academic_vault'),
    path('vault/upload-certificate/', views.upload_certificate, name='upload_certificate'),
    path('vault/add-record/', views.add_academic_record, name='add_academic_record'),
    path('vault/performance/', views.performance_insights, name='performance_insights'),
    
    # Notifications
    path('notifications/', views.notifications, name='notifications'),
    path('notifications/mark-read/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),

    # Admin Approvals
    path('admin-approvals/', views.pending_approvals, name='pending_approvals'),
    path('admin-approvals/approve/<int:user_id>/', views.approve_user, name='approve_user'),
    path('admin-approvals/reject/<int:user_id>/', views.reject_user, name='reject_user'),
]
