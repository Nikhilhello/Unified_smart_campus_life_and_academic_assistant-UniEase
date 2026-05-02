-- ============================================
-- INSERT DOUBTS AND ANSWERS
-- ============================================

INSERT INTO campus_doubt (question, subject, topic, posted_by_id, is_anonymous, views, created_at)
VALUES
('What is the time complexity of inserting an element in a balanced BST?', 
 'Data Structures', 'Binary Search Trees', @student1_id, 0, 45, DATE_SUB(NOW(), INTERVAL 3 DAY)),

('Can someone explain the difference between INNER JOIN and LEFT JOIN with examples?',
 'Database Management Systems', 'SQL Joins', @student1_id, 0, 62, DATE_SUB(NOW(), INTERVAL 5 DAY)),

('How does the Banker''s Algorithm prevent deadlock in operating systems?',
 'Operating Systems', 'Deadlock Prevention', @student1_id, 0, 38, DATE_SUB(NOW(), INTERVAL 2 DAY)),

('What is the difference between TCP and UDP protocols?',
 'Computer Networks', 'Transport Layer', @student1_id, 0, 71, DATE_SUB(NOW(), INTERVAL 6 DAY)),

('How to implement the Singleton design pattern in Java?',
 'Software Engineering', 'Design Patterns', @student1_id, 1, 29, DATE_SUB(NOW(), INTERVAL 1 DAY));

-- Get doubt IDs
SET @doubt1_id = (SELECT id FROM campus_doubt WHERE topic = 'Binary Search Trees');
SET @doubt2_id = (SELECT id FROM campus_doubt WHERE topic = 'SQL Joins');
SET @doubt3_id = (SELECT id FROM campus_doubt WHERE topic = 'Deadlock Prevention');
SET @doubt4_id = (SELECT id FROM campus_doubt WHERE topic = 'Transport Layer');

-- Insert answers
INSERT INTO campus_answer (doubt_id, answer, answered_by_id, upvotes, created_at)
VALUES
(@doubt1_id, 
 'The time complexity of inserting an element in a balanced BST is O(log n) where n is the number of nodes. This is because the tree maintains its balance property, ensuring the height remains logarithmic. In a balanced BST like AVL or Red-Black tree, after insertion, rotation operations are performed to maintain balance, which also take O(log n) time.',
 @admin_id, 12, DATE_SUB(NOW(), INTERVAL 2 DAY)),

(@doubt2_id,
 'INNER JOIN returns only the rows where there is a match in both tables. LEFT JOIN returns all rows from the left table and matching rows from the right table. If no match is found, NULL values are returned for right table columns.\n\nExample:\nSELECT * FROM students INNER JOIN courses ON students.course_id = courses.id;\n-- Returns only students who are enrolled in a course\n\nSELECT * FROM students LEFT JOIN courses ON students.course_id = courses.id;\n-- Returns all students, even those not enrolled in any course',
 @admin_id, 18, DATE_SUB(NOW(), INTERVAL 4 DAY)),

(@doubt3_id,
 'Banker''s Algorithm is a deadlock avoidance algorithm. It works by simulating resource allocation before actually allocating them. The system maintains information about available resources, maximum demand, and current allocation. Before granting a request, it checks if the system will remain in a safe state. A safe state means there exists at least one sequence of process execution that allows all processes to complete without deadlock.',
 @admin_id, 9, DATE_SUB(NOW(), INTERVAL 1 DAY)),

(@doubt4_id,
 'TCP (Transmission Control Protocol) is connection-oriented, provides reliable data transfer with error checking and retransmission. It guarantees ordered delivery and has flow control. Used for applications requiring reliability (HTTP, FTP, Email).\n\nUDP (User Datagram Protocol) is connectionless, faster but unreliable. No error checking or retransmission. Used for applications where speed is critical and some data loss is acceptable (video streaming, online gaming, DNS).',
 @admin_id, 15, DATE_SUB(NOW(), INTERVAL 5 DAY));
