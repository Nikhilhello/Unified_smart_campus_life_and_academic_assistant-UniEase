-- ============================================
-- INSERT NOTES
-- ============================================

INSERT INTO campus_note (subject, title, description, file, uploaded_by_id, semester, department, downloads, created_at)
VALUES
('Data Structures', 'Complete Notes on Binary Trees',
 'Comprehensive notes covering all aspects of binary trees including traversal techniques, BST operations, AVL trees, and Red-Black trees with examples and practice problems.',
 'notes/binary_trees_complete.pdf', @admin_id, 5, 'Computer Science', 156, DATE_SUB(NOW(), INTERVAL 15 DAY)),

('Database Management Systems', 'SQL Query Cheat Sheet',
 'Quick reference guide for SQL queries including SELECT, JOIN, subqueries, aggregate functions, and window functions with practical examples.',
 'notes/sql_cheatsheet.pdf', @admin_id, 5, 'Computer Science', 203, DATE_SUB(NOW(), INTERVAL 20 DAY)),

('Operating Systems', 'Process Synchronization Notes',
 'Detailed notes on process synchronization covering semaphores, monitors, critical section problem, and classic synchronization problems with solutions.',
 'notes/process_sync.pdf', @admin_id, 5, 'Computer Science', 142, DATE_SUB(NOW(), INTERVAL 10 DAY)),

('Computer Networks', 'Network Layer Protocols',
 'Complete guide to network layer protocols including IP addressing, subnetting, routing algorithms (OSPF, BGP, RIP), and ICMP.',
 'notes/network_layer.pdf', @student1_id, 5, 'Computer Science', 98, DATE_SUB(NOW(), INTERVAL 8 DAY)),

('Software Engineering', 'Software Testing Techniques',
 'Comprehensive notes on various software testing techniques including unit testing, integration testing, system testing, and test automation frameworks.',
 'notes/testing_techniques.pdf', @admin_id, 5, 'Computer Science', 87, DATE_SUB(NOW(), INTERVAL 5 DAY)),

('Theory of Computation', 'Turing Machines Explained',
 'Detailed explanation of Turing machines, Church-Turing thesis, decidability, and computational complexity with examples.',
 'notes/turing_machines.pdf', @admin_id, 5, 'Computer Science', 124, DATE_SUB(NOW(), INTERVAL 12 DAY)),

('Mathematics', 'Linear Algebra Fundamentals',
 'Complete coverage of vectors, matrices, determinants, eigenvalues, eigenvectors, and their applications in computer science.',
 'notes/linear_algebra.pdf', @admin_id, 3, 'Computer Science', 189, DATE_SUB(NOW(), INTERVAL 25 DAY)),

('Web Development', 'HTML5 and CSS3 Guide',
 'Modern web development with HTML5 semantic elements, CSS3 animations, responsive design, and best practices.',
 'notes/html5_css3.pdf', @student1_id, 4, 'Computer Science', 234, DATE_SUB(NOW(), INTERVAL 18 DAY)),

('Java Programming', 'Object-Oriented Programming Concepts',
 'Detailed explanation of OOP principles, inheritance, polymorphism, abstraction, and encapsulation with Java examples.',
 'notes/oop_java.pdf', @admin_id, 4, 'Computer Science', 167, DATE_SUB(NOW(), INTERVAL 22 DAY)),

('Machine Learning', 'Introduction to ML Algorithms',
 'Overview of supervised and unsupervised learning, regression, classification, clustering, and neural networks.',
 'notes/ml_intro.pdf', @admin_id, 6, 'Computer Science', 145, DATE_SUB(NOW(), INTERVAL 7 DAY)),

('Physics', 'Quantum Mechanics Basics',
 'Fundamental concepts of quantum mechanics including wave-particle duality, uncertainty principle, and quantum states.',
 'notes/quantum_mechanics.pdf', @admin_id, 2, 'Physics', 98, DATE_SUB(NOW(), INTERVAL 30 DAY)),

('Chemistry', 'Organic Chemistry Reactions',
 'Comprehensive guide to organic reactions, mechanisms, and synthesis with detailed reaction pathways.',
 'notes/organic_chemistry.pdf', @admin_id, 2, 'Chemistry', 112, DATE_SUB(NOW(), INTERVAL 28 DAY)),

('English Literature', 'Shakespearean Plays Analysis',
 'Critical analysis of major Shakespearean plays including themes, characters, and literary devices.',
 'notes/shakespeare_analysis.pdf', @student1_id, 1, 'Arts', 76, DATE_SUB(NOW(), INTERVAL 35 DAY)),

('Economics', 'Microeconomics Principles',
 'Fundamental principles of microeconomics including supply and demand, market structures, and consumer behavior.',
 'notes/microeconomics.pdf', @admin_id, 3, 'Commerce', 134, DATE_SUB(NOW(), INTERVAL 20 DAY));
