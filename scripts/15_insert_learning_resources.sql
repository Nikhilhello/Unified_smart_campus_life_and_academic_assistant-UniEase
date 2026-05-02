-- ============================================
-- INSERT LEARNING RESOURCES
-- ============================================

INSERT INTO campus_learningresource (title, category, description, resource_type, url, posted_by_id, created_at)
VALUES
('MIT OpenCourseWare - Introduction to Algorithms',
 'Computer Science', 
 'Complete video lectures from MIT on algorithms including sorting, searching, graph algorithms, dynamic programming, and more.',
 'course', 'https://ocw.mit.edu/courses/introduction-to-algorithms/',
 @admin_id, DATE_SUB(NOW(), INTERVAL 15 DAY)),

('CS50 - Harvard University',
 'Computer Science',
 'Harvard''s introduction to computer science. Covers programming fundamentals, data structures, web development, and more.',
 'course', 'https://cs50.harvard.edu/',
 @admin_id, DATE_SUB(NOW(), INTERVAL 20 DAY)),

('FreeCodeCamp - Full Stack Development',
 'Web Development',
 'Learn full-stack web development with hands-on projects. Covers HTML, CSS, JavaScript, React, Node.js, and databases.',
 'tutorial', 'https://www.freecodecamp.org/',
 @student1_id, DATE_SUB(NOW(), INTERVAL 10 DAY)),

('Geeks for Geeks - Interview Preparation',
 'Interview Prep',
 'Comprehensive collection of coding problems, algorithms, and interview questions with detailed explanations.',
 'article', 'https://www.geeksforgeeks.org/interview-preparation/',
 @admin_id, DATE_SUB(NOW(), INTERVAL 12 DAY)),

('Khan Academy - Mathematics',
 'Mathematics',
 'Free mathematics courses covering algebra, calculus, statistics, and discrete mathematics.',
 'course', 'https://www.khanacademy.org/math',
 @admin_id, DATE_SUB(NOW(), INTERVAL 18 DAY)),

('Coursera - Machine Learning by Andrew Ng',
 'Artificial Intelligence',
 'Popular machine learning course covering supervised learning, unsupervised learning, neural networks, and best practices.',
 'course', 'https://www.coursera.org/learn/machine-learning',
 @admin_id, DATE_SUB(NOW(), INTERVAL 8 DAY));
