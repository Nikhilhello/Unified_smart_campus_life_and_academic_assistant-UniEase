-- ============================================
-- INSERT SYLLABUS
-- ============================================

INSERT INTO campus_syllabus (subject, department, semester, topic, completed, completion_date)
VALUES
-- Data Structures
('Data Structures', 'Computer Science', 5, 'Introduction to Data Structures', 1, '2024-01-15'),
('Data Structures', 'Computer Science', 5, 'Arrays and Linked Lists', 1, '2024-01-25'),
('Data Structures', 'Computer Science', 5, 'Stacks and Queues', 1, '2024-02-05'),
('Data Structures', 'Computer Science', 5, 'Trees and Binary Search Trees', 1, '2024-02-20'),
('Data Structures', 'Computer Science', 5, 'Graph Algorithms', 0, NULL),
('Data Structures', 'Computer Science', 5, 'Hashing and Hash Tables', 0, NULL),

-- DBMS
('Database Management Systems', 'Computer Science', 5, 'Introduction to DBMS', 1, '2024-01-18'),
('Database Management Systems', 'Computer Science', 5, 'ER Model and Relational Model', 1, '2024-01-28'),
('Database Management Systems', 'Computer Science', 5, 'SQL and Query Processing', 1, '2024-02-10'),
('Database Management Systems', 'Computer Science', 5, 'Normalization', 1, '2024-02-22'),
('Database Management Systems', 'Computer Science', 5, 'Transaction Management', 0, NULL),
('Database Management Systems', 'Computer Science', 5, 'Concurrency Control', 0, NULL),

-- Operating Systems
('Operating Systems', 'Computer Science', 5, 'Introduction to OS', 1, '2024-01-20'),
('Operating Systems', 'Computer Science', 5, 'Process Management', 1, '2024-02-01'),
('Operating Systems', 'Computer Science', 5, 'CPU Scheduling', 1, '2024-02-15'),
('Operating Systems', 'Computer Science', 5, 'Memory Management', 0, NULL),
('Operating Systems', 'Computer Science', 5, 'File Systems', 0, NULL),
('Operating Systems', 'Computer Science', 5, 'Deadlock Handling', 0, NULL),

-- Computer Networks
('Computer Networks', 'Computer Science', 5, 'Network Fundamentals', 1, '2024-01-12'),
('Computer Networks', 'Computer Science', 5, 'Data Link Layer', 1, '2024-01-22'),
('Computer Networks', 'Computer Science', 5, 'Network Layer and Routing', 1, '2024-02-02'),
('Computer Networks', 'Computer Science', 5, 'Transport Layer', 0, NULL),
('Computer Networks', 'Computer Science', 5, 'Application Layer', 0, NULL),

-- Software Engineering
('Software Engineering', 'Computer Science', 6, 'Software Development Life Cycle', 1, '2024-01-10'),
('Software Engineering', 'Computer Science', 6, 'Requirements Engineering', 1, '2024-01-20'),
('Software Engineering', 'Computer Science', 6, 'Software Design Patterns', 1, '2024-02-01'),
('Software Engineering', 'Computer Science', 6, 'Software Testing', 0, NULL),
('Software Engineering', 'Computer Science', 6, 'Project Management', 0, NULL),

-- Mathematics
('Mathematics', 'Computer Science', 3, 'Discrete Mathematics', 1, '2024-01-08'),
('Mathematics', 'Computer Science', 3, 'Linear Algebra', 1, '2024-01-18'),
('Mathematics', 'Computer Science', 3, 'Probability and Statistics', 1, '2024-01-28'),
('Mathematics', 'Computer Science', 3, 'Calculus', 0, NULL),

-- Physics
('Physics', 'Science', 1, 'Mechanics', 1, '2024-01-05'),
('Physics', 'Science', 1, 'Thermodynamics', 1, '2024-01-15'),
('Physics', 'Science', 1, 'Electricity and Magnetism', 1, '2024-01-25'),
('Physics', 'Science', 1, 'Optics', 0, NULL),
('Physics', 'Science', 1, 'Modern Physics', 0, NULL),

-- Chemistry
('Chemistry', 'Science', 1, 'Basic Concepts', 1, '2024-01-06'),
('Chemistry', 'Science', 1, 'Atomic Structure', 1, '2024-01-16'),
('Chemistry', 'Science', 1, 'Chemical Bonding', 1, '2024-01-26'),
('Chemistry', 'Science', 1, 'Organic Chemistry', 0, NULL),
('Chemistry', 'Science', 1, 'Physical Chemistry', 0, NULL);
