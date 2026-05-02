-- ============================================
-- INSERT ANNOUNCEMENTS
-- ============================================

INSERT INTO campus_announcement (title, content, posted_by_id, target_audience, priority, created_at)
VALUES
('Mid-Semester Exam Schedule Released', 
 'The mid-semester examination schedule for all departments has been released. Students are requested to check the exam timetable section for detailed information. Exams will commence from March 15th, 2024.',
 @admin_id, 'all', 'high', DATE_SUB(NOW(), INTERVAL 2 DAY)),

('Library Timing Extension During Exams',
 'The central library will remain open 24/7 during the examination period from March 10th to March 25th. Students can book seats in advance through the portal.',
 @admin_id, 'student', 'medium', DATE_SUB(NOW(), INTERVAL 3 DAY)),

('Campus Placement Drive - Tech Giants',
 'Major tech companies including Google, Microsoft, and Amazon will be visiting campus for placement drives next month. Eligible students should register through the placement portal by March 20th.',
 @admin_id, 'student', 'high', DATE_SUB(NOW(), INTERVAL 1 DAY)),

('Hostel Maintenance Notice',
 'Routine maintenance work will be carried out in H-Block hostels on March 18th. Water supply may be affected between 10 AM to 2 PM.',
 @admin_id, 'student', 'medium', DATE_SUB(NOW(), INTERVAL 5 DAY)),

('Guest Lecture on AI and Machine Learning',
 'Prof. Anil Kumar from IIT Delhi will deliver a guest lecture on "Future of AI in Healthcare" on March 22nd at 4 PM in Auditorium A. All students are invited.',
 @admin_id, 'all', 'low', NOW());
