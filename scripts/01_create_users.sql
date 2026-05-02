-- ============================================
-- CREATE USERS AND PROFILES
-- ============================================

-- Note: First create superuser using Django command:
-- python manage.py createsuperuser
-- Username: admin, Password: admin123

-- Create student user
INSERT INTO auth_user (username, first_name, last_name, email, is_staff, is_active, is_superuser, password, date_joined)
VALUES 
('student1', 'Rahul', 'Sharma', 'rahul.sharma@university.edu', 0, 1, 0, 
 'pbkdf2_sha256$600000$saltvalue$hashedpassword', NOW());

-- Get the user IDs (adjust based on your actual IDs)
SET @admin_id = (SELECT id FROM auth_user WHERE username = 'admin');
SET @student1_id = (SELECT id FROM auth_user WHERE username = 'student1');

-- Create user profiles
INSERT INTO campus_userprofile (user_id, role, roll_number, department, year, phone, hostel_room)
VALUES 
(@admin_id, 'admin', NULL, 'Administration', NULL, '+91-9876543210', NULL),
(@student1_id, 'student', 'CS2021001', 'Computer Science', 3, '+91-9876543211', 'H-Block-301');
