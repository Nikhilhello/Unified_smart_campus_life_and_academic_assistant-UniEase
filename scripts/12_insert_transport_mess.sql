-- ============================================
-- INSERT TRANSPORT AND MESS DATA
-- ============================================

-- Insert bus routes
INSERT INTO campus_busroute (route_number, route_name, departure_time, arrival_time, stops, is_delayed, delay_minutes)
VALUES
('B1', 'University to MG Road Area', '08:00:00', '08:45:00',
 'Main Gate → Library Stop → Science Block → Engineering Block → Medical Center → MG Road → Brigade Road',
 0, 0),

('B2', 'University to Koramangala', '07:30:00', '08:15:00',
 'Main Gate → Hostel Complex → Academic Block → Sports Complex → Koramangala → HSR Layout → BTM Layout',
 0, 0),

('B3', 'University to Whitefield', '06:00:00', '07:30:00',
 'Main Gate → City Center → Highway Junction → Whitefield → ITPL → Marathahalli',
 1, 15),

('B4', 'Campus Shuttle (Morning)', '08:30:00', '09:00:00',
 'Hostel Block A → Hostel Block B → Hostel Block C → Academic Complex → Library',
 0, 0),

('B5', 'Campus Shuttle (Evening)', '17:00:00', '17:30:00',
 'Academic Complex → Library → Sports Ground → Hostel Block A → Hostel Block B → Hostel Block C',
 0, 0);

-- Insert mess menu
INSERT INTO campus_messmenu (day, meal_type, items, rating, total_ratings)
VALUES
-- Monday
('Monday', 'breakfast', 'Idli, Sambar, Coconut Chutney, Poha, Tea/Coffee, Banana', 4.2, 156),
('Monday', 'lunch', 'Rice, Dal Tadka, Aloo Gobhi, Chapati, Salad, Curd, Pickle', 3.8, 198),
('Monday', 'snacks', 'Samosa, Green Chutney, Tea/Coffee', 4.5, 142),
('Monday', 'dinner', 'Rice, Rajma Curry, Mix Veg, Chapati, Dal, Salad, Sweet (Gulab Jamun)', 4.1, 187),

-- Tuesday  
('Tuesday', 'breakfast', 'Aloo Paratha, Curd, Pickle, Upma, Tea/Coffee, Apple', 4.4, 163),
('Tuesday', 'lunch', 'Rice, Dal Fry, Paneer Butter Masala, Chapati, Salad, Raita', 4.6, 205),
('Tuesday', 'snacks', 'Bread Pakora, Sauce, Tea/Coffee', 3.9, 128),
('Tuesday', 'dinner', 'Rice, Chole, Bhindi Fry, Chapati, Dal, Salad, Papad', 3.7, 174),

-- Wednesday
('Wednesday', 'breakfast', 'Dosa, Sambar, Coconut Chutney, Poha, Tea/Coffee, Orange', 4.7, 189),
('Wednesday', 'lunch', 'Rice, Dal Makhani, Egg Curry, Chapati, Salad, Curd', 4.3, 192),
('Wednesday', 'snacks', 'Vada Pav, Chutney, Tea/Coffee', 4.8, 167),
('Wednesday', 'dinner', 'Rice, Kadhi Pakora, Aloo Jeera, Chapati, Dal, Salad, Sweet (Kheer)', 4.2, 183),

-- Thursday
('Thursday', 'breakfast', 'Puri Bhaji, Upma, Tea/Coffee, Banana', 4.1, 152),
('Thursday', 'lunch', 'Rice, Dal Tadka, Chicken Curry, Chapati, Salad, Raita', 4.5, 211),
('Thursday', 'snacks', 'Spring Roll, Sauce, Tea/Coffee', 4.0, 135),
('Thursday', 'dinner', 'Rice, Palak Paneer, Mix Veg, Chapati, Dal, Salad, Papad', 4.4, 195),

-- Friday
('Friday', 'breakfast', 'Masala Dosa, Sambar, Chutney, Poha, Tea/Coffee, Apple', 4.9, 201),
('Friday', 'lunch', 'Veg Biryani, Raita, Papad, Salad, Sweet (Gulab Jamun)', 4.8, 234),
('Friday', 'snacks', 'Pani Puri, Tea/Coffee', 4.7, 178),
('Friday', 'dinner', 'Rice, Dal Fry, Mushroom Masala, Chapati, Salad, Ice Cream', 4.6, 198),

-- Saturday
('Saturday', 'breakfast', 'Chole Bhature, Pickle, Tea/Coffee, Orange', 4.5, 186),
('Saturday', 'lunch', 'Rice, Dal, Fish Fry, Veg Curry, Chapati, Salad, Curd', 4.2, 176),
('Saturday', 'snacks', 'Burger, Fries, Cold Drink', 4.4, 193),
('Saturday', 'dinner', 'Rice, Kadhi, Aloo Paratha, Curd, Salad, Sweet', 4.1, 169),

-- Sunday
('Sunday', 'breakfast', 'Bread Butter Jam, Cornflakes, Milk, Fruits, Tea/Coffee', 3.8, 145),
('Sunday', 'lunch', 'Special Thali: Rice, 3 Sabzi, Dal, Chapati, Papad, Raita, Sweet, Salad', 4.9, 256),
('Sunday', 'snacks', 'Pizza, Cold Drink', 4.8, 189),
('Sunday', 'dinner', 'Rice, Rajma, Paneer Tikka, Chapati, Dal, Salad, Ice Cream', 4.7, 213);
