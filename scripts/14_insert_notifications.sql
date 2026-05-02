-- ============================================
-- INSERT NOTIFICATIONS
-- ============================================

INSERT INTO campus_notification (user_id, title, message, notification_type, is_read, link, created_at)
VALUES
(@student1_id, 'Exam Schedule Updated',
 'The mid-semester exam schedule has been updated. Please check the exam section for your updated seat numbers and timings.',
 'exam', 0, '/exams/', DATE_SUB(NOW(), INTERVAL 2 HOUR)),

(@student1_id, 'New Placement Opportunity',
 'Google is recruiting for Software Engineer positions. Application deadline: March 20th, 2024. Apply now!',
 'placement', 1, '/placements/', DATE_SUB(NOW(), INTERVAL 5 HOUR)),

(@student1_id, 'Hostel Complaint Update',
 'Your complaint "Broken Window Pane" status has been updated to In Progress. Admin response added.',
 'hostel', 0, '/hostel/complaints/', DATE_SUB(NOW(), INTERVAL 3 HOUR)),

(@student1_id, 'Library Book Due Reminder',
 'Your borrowed book "Introduction to Algorithms" is due in 4 days. Please return or renew it to avoid fine.',
 'library', 0, '/library/borrowed/', DATE_SUB(NOW(), INTERVAL 1 HOUR)),

(@student1_id, 'New Answer to Your Doubt',
 'Dr. Priya Mehta answered your doubt about Binary Search Trees complexity. Check it out!',
 'doubt', 1, '/doubts/', DATE_SUB(NOW(), INTERVAL 6 HOUR)),

(@student1_id, 'Application Shortlisted',
 'Congratulations! Your application for Amazon SDE Intern has been shortlisted. Interview details will be shared soon.',
 'placement', 0, '/placements/applications/', DATE_SUB(NOW(), INTERVAL 4 HOUR)),

(@student1_id, 'Mess Menu Updated',
 'This week''s mess menu has been updated. Friday special: Veg Biryani!',
 'mess', 1, '/mess/menu/', DATE_SUB(NOW(), INTERVAL 1 DAY)),

(@student1_id, 'Bus Delay Alert',
 'Bus B3 (University to Airport) is delayed by 15 minutes. Updated departure time: 06:15 AM.',
 'transport', 1, '/transport/', DATE_SUB(NOW(), INTERVAL 30 MINUTE));
