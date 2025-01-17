-- Database Initialization Script for Music Library Management System

-- Create the database
CREATE DATABASE IF NOT EXISTS project;
USE project;

-- Create the artist table
CREATE TABLE IF NOT EXISTS artist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    artist_name VARCHAR(255) UNIQUE NOT NULL
);

-- Create the album table
CREATE TABLE IF NOT EXISTS album (
    id INT AUTO_INCREMENT PRIMARY KEY,
    album_name VARCHAR(255) NOT NULL,
    artist_id INT NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist(id) ON DELETE CASCADE
);

-- Create the genre table
CREATE TABLE IF NOT EXISTS genre (
    id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(255) UNIQUE NOT NULL
);

-- Create the track table
CREATE TABLE IF NOT EXISTS track (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    album_id INT NOT NULL,
    genre_id INT NOT NULL,
    artist_id INT NOT NULL,
    rlsyr INT,
    FOREIGN KEY (album_id) REFERENCES album(id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genre(id) ON DELETE CASCADE,
    FOREIGN KEY (artist_id) REFERENCES artist(id) ON DELETE CASCADE
);

-- Create the subscription table for user authentication
CREATE TABLE IF NOT EXISTS subscription (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Insert initial data into genre table
INSERT IGNORE INTO genre (genre_name) VALUES
('Pop'),
('Rock'),
('Jazz'),
('Classical'),
('EDM');
