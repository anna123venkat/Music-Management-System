Music Library Management System

This is a mini project that implements a **Music Library Management System** using Python and MySQL. It provides a user-friendly interface for managing music records, including adding, viewing, searching, and deleting songs. The project uses various Python libraries such as Tkinter, PyMySQL, and Pillow to create the GUI and manage the MySQL database.

# Features

- **User Login/Signup**: Allows users to log in or subscribe to the system.
- **Add Song**: Users can add new songs by providing details like title, artist, album, genre, and release year.
- **View Songs**: Users can view all songs or filter by specific playlists like EDM or Pop Music.
- **Search Song**: Enables searching for songs based on the title.
- **Delete Song**: Allows removal of songs from the library.
- **Data Normalization**: Ensures the music database follows 3NF and BCNF for efficient data management.

# Technologies Used

- **Frontend**: Python (Tkinter for GUI)
- **Backend**: MySQL (PyMySQL for database interaction)
- **Libraries**: 
  - **Tkinter**: For GUI development.
  - **PyMySQL**: For MySQL database interaction.
  - **Pillow**: For handling images in the GUI.

# How to Run the Project

1. Clone the repository.
2. Install the required Python modules:
   ```bash
   pip install pymysql pillow
   ```
3. Set up the MySQL database:
   - Create a MySQL database called `project`.
   - Import the provided SQL schema to create the necessary tables.
4. Run the Python scripts:
   - Start with `main.py` for login/signup.
   - Use the add, delete, and search functionalities from the GUI.

# Database Schema

- **Artist Table**: Contains artist details.
- **Genre Table**: Stores genres.
- **Album Table**: Holds album information.
- **Track Table**: Stores track details linked with artist, album, and genre tables.

# ER Diagram

An ER diagram is included to provide a visual representation of the database structure.

# Contributors

- **Dharunraj P**
- **Muthu Nitheesh R**
- **S Prasanna Venkatesh**

# Acknowledgments

Special thanks to our mentors and peers for their guidance and support in completing this project.
