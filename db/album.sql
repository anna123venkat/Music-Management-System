-- Album Table Data Script for Music Library Management System

-- Use the database
USE project;

-- Insert data into album table
INSERT IGNORE INTO album (album_name, artist_id) VALUES
('1989', (SELECT id FROM artist WHERE artist_name = 'Taylor Swift')),
('Divide', (SELECT id FROM artist WHERE artist_name = 'Ed Sheeran')),
('Lemonade', (SELECT id FROM artist WHERE artist_name = 'Beyonce')),
('25', (SELECT id FROM artist WHERE artist_name = 'Adele')),
('After Hours', (SELECT id FROM artist WHERE artist_name = 'The Weeknd')),
('A Head Full of Dreams', (SELECT id FROM artist WHERE artist_name = 'Coldplay')),
('Scorpion', (SELECT id FROM artist WHERE artist_name = 'Drake')),
('Sweetener', (SELECT id FROM artist WHERE artist_name = 'Ariana Grande')),
('Happier Than Ever', (SELECT id FROM artist WHERE artist_name = 'Billie Eilish')),
('24K Magic', (SELECT id FROM artist WHERE artist_name = 'Bruno Mars'));
