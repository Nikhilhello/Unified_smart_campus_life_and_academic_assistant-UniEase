-- ============================================
-- INSERT LOST AND FOUND ITEMS
-- ============================================

INSERT INTO campus_lostitem (item_name, description, category, location, status, posted_by_id, contact, created_at)
VALUES
('Blue Backpack', 
 'Lost a blue colored JanSport backpack near the library on March 10th. Contains textbooks and a calculator. Has a small keychain attached.',
 'Bag', 'Central Library', 'lost', @student1_id, '+91-9876543211', DATE_SUB(NOW(), INTERVAL 4 DAY)),

('Black Wallet',
 'Found a black leather wallet near the cafeteria. Contains ID cards and some cash. Please contact to claim with proof of ownership.',
 'Wallet', 'Main Cafeteria', 'found', @admin_id, '+91-9876543210', DATE_SUB(NOW(), INTERVAL 2 DAY)),

('Silver Water Bottle',
 'Lost a silver colored insulated water bottle with "CS Dept" sticker on it. Last seen in CS Lab 1.',
 'Bottle', 'CS Lab 1', 'lost', @student1_id, '+91-9876543211', DATE_SUB(NOW(), INTERVAL 6 DAY)),

('iPhone 13',
 'Found an iPhone 13 (blue color) near the sports ground. Device is locked. Contact to claim with proof of ownership.',
 'Electronics', 'Sports Ground', 'found', @admin_id, '+91-9876543210', DATE_SUB(NOW(), INTERVAL 1 DAY)),

('Textbook - Operating Systems',
 'Lost Operating Systems textbook by Silberschatz. Has my name written inside the cover. Last seen in lecture hall CS-101.',
 'Books', 'CS-101 Lecture Hall', 'lost', @student1_id, '+91-9876543211', DATE_SUB(NOW(), INTERVAL 5 DAY));
