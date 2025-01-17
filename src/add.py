from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from config import get_connection

def add_song():
    title = song_info1.get()
    artist = song_info2.get()
    album = song_info3.get()
    genre = song_info4.get()
    release_year = song_info5.get()

    connection = get_connection()
    if connection is None:
        messagebox.showerror('Error', 'Database connection failed')
        return

    try:
        cursor = connection.cursor()

        cursor.execute('INSERT IGNORE INTO artist (artist_name) VALUES (%s)', (artist,))
        cursor.execute("SELECT id FROM artist WHERE artist_name = %s", (artist,))
        artist_id = cursor.fetchone()[0]

        cursor.execute('INSERT IGNORE INTO album (album_name, artist_id) VALUES (%s, %s)', (album, artist_id))
        cursor.execute("SELECT id FROM album WHERE album_name = %s", (album,))
        album_id = cursor.fetchone()[0]

        cursor.execute('INSERT IGNORE INTO genre (genre_name) VALUES (%s)', (genre,))
        cursor.execute("SELECT id FROM genre WHERE genre_name = %s", (genre,))
        genre_id = cursor.fetchone()[0]

        cursor.execute(
            'INSERT IGNORE INTO track (title, album_id, genre_id, artist_id, rlsyr) VALUES (%s, %s, %s, %s, %s)',
            (title, album_id, genre_id, artist_id, release_year)
        )

        connection.commit()
        messagebox.showinfo('Success', 'Song added successfully!')

    except Exception as e:
        messagebox.showerror('Error', f"Failed to add song: {e}")

    finally:
        connection.close()
        root.destroy()

def add_song_window():
    global root, song_info1, song_info2, song_info3, song_info4, song_info5

    root = Toplevel()
    root.title('Add Song')
    root.geometry('800x600')

    background_image = Image.open('assets/add.jpg')
    background_image = background_image.resize((800, 600), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(background_image)

    canvas = Canvas(root, width=800, height=600)
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor=NW)

    heading_label = Label(root, text="Add Song", font=('Helvetica', 18, 'bold'), bg='#d7a26c', fg='black')
    heading_label.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.1)

    label_frame = Frame(root, bg='#d7a26c')
    label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    Label(label_frame, text="Title:", font=('Helvetica', 13, 'bold'), bg='#d7a26c').place(relx=0.05, rely=0.1)
    song_info1 = Entry(label_frame, font=('Helvetica', 11))
    song_info1.place(relx=0.3, rely=0.1, relwidth=0.6)

    Label(label_frame, text="Artist:", font=('Helvetica', 13, 'bold'), bg='#d7a26c').place(relx=0.05, rely=0.25)
    song_info2 = Entry(label_frame, font=('Helvetica', 11))
    song_info2.place(relx=0.3, rely=0.25, relwidth=0.6)

    Label(label_frame, text="Album:", font=('Helvetica', 13, 'bold'), bg='#d7a26c').place(relx=0.05, rely=0.4)
    song_info3 = Entry(label_frame, font=('Helvetica', 11))
    song_info3.place(relx=0.3, rely=0.4, relwidth=0.6)

    Label(label_frame, text="Genre:", font=('Helvetica', 13, 'bold'), bg='#d7a26c').place(relx=0.05, rely=0.55)
    song_info4 = Entry(label_frame, font=('Helvetica', 11))
    song_info4.place(relx=0.3, rely=0.55, relwidth=0.6)

    Label(label_frame, text="Release Year:", font=('Helvetica', 13, 'bold'), bg='#d7a26c').place(relx=0.05, rely=0.7)
    song_info5 = Entry(label_frame, font=('Helvetica', 11))
    song_info5.place(relx=0.3, rely=0.7, relwidth=0.6)

    Button(root, text="Submit", font=('Helvetica', 12, 'bold'), bg='#d7a26c', fg='black', command=add_song).place(
        relx=0.3, rely=0.9, relwidth=0.2)
    Button(root, text="Cancel", font=('Helvetica', 12, 'bold'), bg='#d7a26c', fg='black', command=root.destroy).place(
        relx=0.6, rely=0.9, relwidth=0.2)

    root.mainloop()

if __name__ == "__main__":
    add_song_window()
