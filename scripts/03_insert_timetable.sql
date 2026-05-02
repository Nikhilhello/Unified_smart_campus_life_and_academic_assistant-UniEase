-- ============================================
-- INSERT TIMETABLE FOR CS YEAR 3
-- ============================================

INSERT INTO campus_timetable (department, year, semester, day, time_slot, subject, faculty, room)
VALUES
-- Monday
('Computer Science', 3, 5, 'Monday', '09:00 AM - 10:00 AM', 'Data Structures', 'Dr. Priya Mehta', 'CS-101'),
('Computer Science', 3, 5, 'Monday', '10:00 AM - 11:00 AM', 'Database Management Systems', 'Prof. Rajesh Kumar', 'CS-102'),
('Computer Science', 3, 5, 'Monday', '11:30 AM - 12:30 PM', 'Operating Systems', 'Dr. Amit Singh', 'CS-101'),
('Computer Science', 3, 5, 'Monday', '02:00 PM - 03:00 PM', 'Computer Networks Lab', 'Dr. Sneha Patel', 'CS-Lab-1'),

-- Tuesday
('Computer Science', 3, 5, 'Tuesday', '09:00 AM - 10:00 AM', 'Computer Networks', 'Dr. Sneha Patel', 'CS-103'),
('Computer Science', 3, 5, 'Tuesday', '10:00 AM - 11:00 AM', 'Software Engineering', 'Prof. Vikram Desai', 'CS-102'),
('Computer Science', 3, 5, 'Tuesday', '11:30 AM - 12:30 PM', 'Theory of Computation', 'Dr. Ravi Sharma', 'CS-104'),
('Computer Science', 3, 5, 'Tuesday', '02:00 PM - 04:00 PM', 'DBMS Lab', 'Prof. Rajesh Kumar', 'CS-Lab-2'),

-- Wednesday
('Computer Science', 3, 5, 'Wednesday', '09:00 AM - 10:00 AM', 'Data Structures', 'Dr. Priya Mehta', 'CS-101'),
('Computer Science', 3, 5, 'Wednesday', '10:00 AM - 11:00 AM', 'Operating Systems', 'Dr. Amit Singh', 'CS-102'),
('Computer Science', 3, 5, 'Wednesday', '11:30 AM - 12:30 PM', 'Database Management Systems', 'Prof. Rajesh Kumar', 'CS-103'),
('Computer Science', 3, 5, 'Wednesday', '02:00 PM - 03:00 PM', 'Seminar', 'All Faculty', 'CS-Auditorium'),

-- Thursday
('Computer Science', 3, 5, 'Thursday', '09:00 AM - 10:00 AM', 'Software Engineering', 'Prof. Vikram Desai', 'CS-101'),
('Computer Science', 3, 5, 'Thursday', '10:00 AM - 11:00 AM', 'Computer Networks', 'Dr. Sneha Patel', 'CS-102'),
('Computer Science', 3, 5, 'Thursday', '11:30 AM - 12:30 PM', 'Theory of Computation', 'Dr. Ravi Sharma', 'CS-103'),
('Computer Science', 3, 5, 'Thursday', '02:00 PM - 04:00 PM', 'Data Structures Lab', 'Dr. Priya Mehta', 'CS-Lab-1'),

-- Friday
('Computer Science', 3, 5, 'Friday', '09:00 AM - 10:00 AM', 'Operating Systems', 'Dr. Amit Singh', 'CS-101'),
('Computer Science', 3, 5, 'Friday', '10:00 AM - 11:00 AM', 'Database Management Systems', 'Prof. Rajesh Kumar', 'CS-102'),
('Computer Science', 3, 5, 'Friday', '11:30 AM - 12:30 PM', 'Software Engineering', 'Prof. Vikram Desai', 'CS-103'),
('Computer Science', 3, 5, 'Friday', '02:00 PM - 03:00 PM', 'Tutorial', 'All Faculty', 'CS-101');
