-- Track Table Data Script for Music Library Management System

-- Use the database
USE project;

-- Insert data into track table
INSERT IGNORE INTO track (title, album_id, genre_id, artist_id, rlsyr) VALUES
('Shake It Off', 
 (SELECT id FROM album WHERE album_name = '1989'),
 (SELECT id FROM genre WHERE genre_name = 'Pop'),
 (SELECT id FROM artist WHERE artist_name = 'Taylor Swift'),
 2014),

('Shape of You', 
 (SELECT id FROM album WHERE album_name = 'Divide'),
 (SELECT id FROM genre WHERE genre_name = 'Pop'),
 (SELECT id FROM artist WHERE artist_name = 'Ed Sheeran'),
 2017),

('Formation', 
 (SELECT id FROM album WHERE album_name = 'Lemonade'),
 (SELECT id FROM genre WHERE genre_name = 'Hip Hop'),
 (SELECT id FROM artist WHERE artist_name = 'Beyonce'),
 2016),

('Hello', 
 (SELECT id FROM album WHERE album_name = '25'),
 (SELECT id FROM genre WHERE genre_name = 'Soul'),
 (SELECT id FROM artist WHERE artist_name = 'Adele'),
 2015),

('Blinding Lights', 
 (SELECT id FROM album WHERE album_name = 'After Hours'),
 (SELECT id FROM genre WHERE genre_name = 'Pop'),
 (SELECT id FROM artist WHERE artist_name = 'The Weeknd'),
 2020),

('Adventure of a Lifetime', 
 (SELECT id FROM album WHERE album_name = 'A Head Full of Dreams'),
 (SELECT id FROM genre WHERE genre_name = 'Rock'),
 (SELECT id FROM artist WHERE artist_name = 'Coldplay'),
 2015),

('God's Plan', 
 (SELECT id FROM album WHERE album_name = 'Scorpion'),
 (SELECT id FROM genre WHERE genre_name = 'Hip Hop'),
 (SELECT id FROM artist WHERE artist_name = 'Drake'),
 2018),

('No Tears Left to Cry', 
 (SELECT id FROM album WHERE album_name = 'Sweetener'),
 (SELECT id FROM genre WHERE genre_name = 'Pop'),
 (SELECT id FROM artist WHERE artist_name = 'Ariana Grande'),
 2018),

('Happier Than Ever', 
 (SELECT id FROM album WHERE album_name = 'Happier Than Ever'),
 (SELECT id FROM genre WHERE genre_name = 'Pop'),
 (SELECT id FROM artist WHERE artist_name = 'Billie Eilish'),
 2021),

('Uptown Funk', 
 (SELECT id FROM album WHERE album_name = '24K Magic'),
 (SELECT id FROM genre WHERE genre_name = 'Funk'),
 (SELECT id FROM artist WHERE artist_name = 'Bruno Mars'),
 2014);
