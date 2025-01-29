# Music Library Management System

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Technologies Used](#technologies-used)
4. [Project Structure](#project-structure)
5. [Setup and Installation](#setup-and-installation)
   - [Prerequisites](#prerequisites)
   - [Steps to Run the Project](#steps-to-run-the-project)
6. [Usage](#usage)
7. [References](#references)
8. [Contributors](#contributors)

## Project Overview
The **Music Library Management System** is a Python-based application that allows users to manage a music library. This system integrates a GUI front-end with Python's Tkinter and a MySQL database back-end to provide functionalities such as adding, searching, viewing, and deleting songs. It also includes features like user authentication and playlist management.

## Key Features
- **User Authentication:** Sign up and log in functionality to secure access.
- **Song Management:** Add, search, view, and delete songs with ease.
- **Database Integration:** MySQL database for robust data storage and management.
- **GUI:** A user-friendly interface built using Tkinter.
- **Genre-Specific Views:** View songs based on genres like Electronic Dance Music (EDM).

## Technologies Used
- **Frontend:** Tkinter (Python GUI toolkit), Pillow (for image handling)
- **Backend:** MySQL (Database management)
- **Programming Language:** Python 3

## Project Structure
```
MusicLibraryManagementSystem/
├── README.md             # Overview of the project with instructions to run it
├── requirements.txt      # Python dependencies for the project
├── config.py             # Configuration for database and other settings
├── src/                  # Source code for the project
│   ├── main.py           # Entry point of the project (login page)
│   ├── add.py            # Logic for adding a song
│   ├── delete.py         # Logic for deleting a song
│   ├── search.py         # Logic for searching songs
│   ├── signup.py         # User signup functionality
│   ├── view.py           # Main view for the application
│   ├── viewallsongs.py   # View all songs logic
│   └── viewedm.py        # Logic for viewing EDM songs
├── db/                   # Database-related files
│   ├── init.sql          # SQL script for creating and populating tables
│   ├── artist.sql        # Schema and example data for the artist table
│   ├── genre.sql         # Schema and example data for the genre table
│   ├── album.sql         # Schema and example data for the album table
│   └── track.sql         # Schema and example data for the track table
├── docs/                 # Documentation and reports
│    └── ERDiagram.png    # ER diagram of the database
├── Output/               # Documentation and reports
    └── Output.pdf        # Screenshots of the application
```

## Setup and Installation
### Prerequisites
- Python 3.x
- MySQL Server

### Steps to Run the Project
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/anna123venkat/Music-Management-System.git
   cd Music-Management-System
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Database:**
   - Create a MySQL database named `project`.
   - Run the SQL scripts in the `db/` directory to set up the necessary tables.

4. **Update Configuration:**
   - Modify `config.py` with your MySQL credentials.

5. **Run the Application:**
   ```bash
   python src/main.py
   ```

## Usage
- Log in using your credentials or sign up as a new user.
- Use the GUI to add, search, view, or delete songs.
- Explore the genre-specific views for a customized experience.

## References
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [MySQL Connector for Python](https://dev.mysql.com/doc/connector-python/en/)
- [Pillow (PIL) Library](https://pillow.readthedocs.io/en/stable/)
- [Python MySQL Tutorial](https://realpython.com/python-mysql/)

## Contributors
- **[Dharunraj P](https://github.com/Dharun1504)**
- Muthu Nitheesh R
- **[Prasanna Venkatesh S](https://github.com/anna123venkat)**

