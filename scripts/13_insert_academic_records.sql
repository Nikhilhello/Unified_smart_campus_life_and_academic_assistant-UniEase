-- ============================================
-- INSERT ACADEMIC RECORDS
-- ============================================

INSERT INTO campus_academicrecord (user_id, semester, subject, marks_obtained, total_marks, grade, attendance_percentage)
VALUES
-- Semester 5 (Current)
(@student1_id, 5, 'Data Structures', 85, 100, 'A', 92.5),
(@student1_id, 5, 'Database Management Systems', 88, 100, 'A', 95.0),
(@student1_id, 5, 'Operating Systems', 82, 100, 'A', 88.0),
(@student1_id, 5, 'Computer Networks', 90, 100, 'A+', 94.0),
(@student1_id, 5, 'Software Engineering', 87, 100, 'A', 91.5),
(@student1_id, 5, 'Theory of Computation', 84, 100, 'A', 89.0),

-- Semester 4
(@student1_id, 4, 'Design and Analysis of Algorithms', 92, 100, 'A+', 96.0),
(@student1_id, 4, 'Computer Organization', 88, 100, 'A', 93.5),
(@student1_id, 4, 'Discrete Mathematics', 85, 100, 'A', 90.0),
(@student1_id, 4, 'Object Oriented Programming', 91, 100, 'A+', 95.5),
(@student1_id, 4, 'Web Technologies', 89, 100, 'A', 92.0),
(@student1_id, 4, 'Microprocessors', 83, 100, 'A', 87.5),

-- Semester 3
(@student1_id, 3, 'Data Structures Fundamentals', 87, 100, 'A', 91.0),
(@student1_id, 3, 'Digital Logic Design', 90, 100, 'A+', 94.5),
(@student1_id, 3, 'Computer Networks Basics', 86, 100, 'A', 89.5),
(@student1_id, 3, 'Probability and Statistics', 84, 100, 'A', 88.0),
(@student1_id, 3, 'Programming in C++', 93, 100, 'A+', 97.0),
(@student1_id, 3, 'Linear Algebra', 82, 100, 'A', 86.5);
