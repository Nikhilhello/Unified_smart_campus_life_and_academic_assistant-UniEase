-- ============================================
-- INSERT HOSTEL COMPLAINTS
-- ============================================

INSERT INTO campus_hostelcomplaint (title, description, category, hostel_block, room_number, status, posted_by_id, created_at, resolved_at, admin_response)
VALUES
('Water Leakage in Bathroom',
 'There is continuous water leakage from the bathroom ceiling. The problem started 2 days ago and is getting worse. Water is dripping constantly and creating puddles on the floor.',
 'Plumbing', 'H-Block', '301', 'resolved', @student1_id, DATE_SUB(NOW(), INTERVAL 7 DAY), DATE_SUB(NOW(), INTERVAL 3 DAY),
 'The plumbing issue has been fixed. Our maintenance team has replaced the faulty pipe. Please let us know if the problem persists.'),

('Broken Window Pane',
 'The window pane in my room is broken. It''s creating a safety hazard and also allowing insects to enter the room. Need urgent replacement.',
 'Maintenance', 'H-Block', '301', 'in_progress', @student1_id, DATE_SUB(NOW(), INTERVAL 3 DAY), NULL,
 'Window replacement has been ordered. Our team will install it within 2 days.'),

('Wi-Fi Not Working',
 'The Wi-Fi connection in H-Block 3rd floor is extremely slow and keeps disconnecting. Unable to attend online classes or submit assignments.',
 'Internet', 'H-Block', '301', 'open', @student1_id, DATE_SUB(NOW(), INTERVAL 1 DAY), NULL, NULL),

('Electrical Socket Not Working',
 'Two electrical sockets in my room are not working. Cannot charge laptop and phone simultaneously. This is affecting my studies.',
 'Electrical', 'H-Block', '301', 'open', @student1_id, NOW(), NULL, NULL),

('Mess Food Quality Poor',
 'The food quality in the mess has deteriorated significantly. Meals are often cold and lack proper nutrition. Many students are falling sick.',
 'Mess', 'Mess Hall', 'N/A', 'open', @student1_id, DATE_SUB(NOW(), INTERVAL 2 DAY), NULL, NULL),

('Hostel Room Cleaning',
 'The hostel rooms are not being cleaned properly. Dust accumulation and unclean bathrooms are common issues.',
 'Cleaning', 'H-Block', '301', 'in_progress', @student1_id, DATE_SUB(NOW(), INTERVAL 4 DAY), NULL,
 'Cleaning schedule has been revised. Daily cleaning will be ensured from tomorrow.'),

('Broken Study Table',
 'The study table in my room is broken and wobbly. Cannot study properly due to this inconvenience.',
 'Furniture', 'H-Block', '301', 'resolved', @student1_id, DATE_SUB(NOW(), INTERVAL 5 DAY), DATE_SUB(NOW(), INTERVAL 1 DAY),
 'Study table has been repaired and reinforced. Please check and confirm.'),

('Power Cuts Frequent',
 'Frequent power cuts in the hostel affecting studies and charging of devices. Need backup generator or better power supply.',
 'Electrical', 'H-Block', '301', 'open', @student1_id, DATE_SUB(NOW(), INTERVAL 6 DAY), NULL, NULL),

('Water Heater Not Working',
 'The water heater in the bathroom is not functioning. Getting cold water for bath during winter is very uncomfortable.',
 'Electrical', 'H-Block', '301', 'resolved', @student1_id, DATE_SUB(NOW(), INTERVAL 8 DAY), DATE_SUB(NOW(), INTERVAL 2 DAY),
 'Water heater has been repaired. Please test and inform if any issues.'),

('Pest Problem',
 'Cockroaches and ants infestation in the room. Need immediate pest control measures.',
 'Cleaning', 'H-Block', '301', 'in_progress', @student1_id, DATE_SUB(NOW(), INTERVAL 9 DAY), NULL,
 'Pest control team has been informed. Treatment will be done this weekend.'),

('Room Lock Broken',
 'The door lock of my room is faulty. Cannot lock the room properly when going out.',
 'Maintenance', 'H-Block', '301', 'resolved', @student1_id, DATE_SUB(NOW(), INTERVAL 10 DAY), DATE_SUB(NOW(), INTERVAL 4 DAY),
 'Door lock has been replaced with a new one. Security has been informed.'),

('Mess Timing Issues',
 'Mess timing is not proper. Breakfast ends early and dinner starts late. Students are facing difficulties.',
 'Mess', 'Mess Hall', 'N/A', 'open', @student1_id, DATE_SUB(NOW(), INTERVAL 11 DAY), NULL, NULL),

('Gym Equipment Broken',
 'Several gym equipment are not working. Treadmill and weights are faulty.',
 'Maintenance', 'Gym', 'N/A', 'in_progress', @student1_id, DATE_SUB(NOW(), INTERVAL 12 DAY), NULL,
 'Gym equipment maintenance team has been contacted. Repairs will be done soon.'),

('Laundry Service Poor',
 'Laundry service is very slow and clothes are not returned on time. Quality of washing is also poor.',
 'Services', 'Laundry', 'N/A', 'open', @student1_id, DATE_SUB(NOW(), INTERVAL 13 DAY), NULL, NULL),

('Common Room TV Not Working',
 'The TV in the common room is not functioning. Students cannot watch news or relax.',
 'Entertainment', 'Common Room', 'N/A', 'resolved', @student1_id, DATE_SUB(NOW(), INTERVAL 14 DAY), DATE_SUB(NOW(), INTERVAL 7 DAY),
 'TV has been repaired. Cable connection has been checked and restored.');
