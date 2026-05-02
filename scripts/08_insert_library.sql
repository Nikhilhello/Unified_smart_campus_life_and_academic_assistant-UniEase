-- ============================================
-- INSERT LIBRARY BOOKS AND SEATS
-- ============================================

-- Insert books
INSERT INTO campus_book (title, author, isbn, category, total_copies, available_copies, publisher, year)
VALUES
('Introduction to Algorithms', 'Thomas H. Cormen', '9780262033848', 'Computer Science', 10, 7, 'MIT Press', 2009),
('Database System Concepts', 'Abraham Silberschatz', '9780078022159', 'Computer Science', 8, 5, 'McGraw-Hill', 2019),
('Operating System Concepts', 'Abraham Silberschatz', '9781118063330', 'Computer Science', 12, 9, 'Wiley', 2018),
('Computer Networks', 'Andrew S. Tanenbaum', '9780132126953', 'Computer Science', 15, 12, 'Pearson', 2010),
('Design Patterns', 'Erich Gamma', '9780201633610', 'Software Engineering', 6, 4, 'Addison-Wesley', 1994),
('Clean Code', 'Robert C. Martin', '9780132350884', 'Software Engineering', 8, 6, 'Prentice Hall', 2008),
('The Pragmatic Programmer', 'Andrew Hunt', '9780135957059', 'Software Engineering', 5, 3, 'Addison-Wesley', 2019),
('Artificial Intelligence: A Modern Approach', 'Stuart Russell', '9780136042594', 'Artificial Intelligence', 10, 8, 'Pearson', 2020);

-- Get book IDs
SET @book1_id = (SELECT id FROM campus_book WHERE isbn = '9780262033848');
SET @book2_id = (SELECT id FROM campus_book WHERE isbn = '9780078022159');

-- Insert book borrowing records
INSERT INTO campus_bookborrowing (book_id, user_id, borrowed_date, due_date, returned_date, is_returned, fine)
VALUES
(@book1_id, @student1_id, DATE_SUB(NOW(), INTERVAL 10 DAY), DATE_ADD(NOW(), INTERVAL 4 DAY), NULL, 0, 0.00),
(@book2_id, @student1_id, DATE_SUB(NOW(), INTERVAL 5 DAY), DATE_ADD(NOW(), INTERVAL 9 DAY), NULL, 0, 0.00);

-- Insert library seats
INSERT INTO campus_libraryseat (seat_number, section, is_occupied, occupied_by_id, occupied_at)
VALUES
('A-001', 'Reading Area A', 0, NULL, NULL),
('A-002', 'Reading Area A', 0, NULL, NULL),
('A-003', 'Reading Area A', 1, @student1_id, NOW()),
('A-004', 'Reading Area A', 0, NULL, NULL),
('A-005', 'Reading Area A', 0, NULL, NULL),
('B-001', 'Silent Study Zone B', 0, NULL, NULL),
('B-002', 'Silent Study Zone B', 0, NULL, NULL),
('B-003', 'Silent Study Zone B', 0, NULL, NULL),
('B-004', 'Silent Study Zone B', 0, NULL, NULL),
('C-001', 'Computer Lab C', 0, NULL, NULL),
('C-002', 'Computer Lab C', 0, NULL, NULL),
('C-003', 'Computer Lab C', 0, NULL, NULL);
