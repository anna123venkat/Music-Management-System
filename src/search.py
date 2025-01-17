from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
from config import get_connection

def search_song():
    title = song_info1.get()

    if not title:
        messagebox.showerror('Error', 'Please enter a song title to search')
        return

    connection = get_connection()
    if connection is None:
        messagebox.showerror('Error', 'Database connection failed')
        return

    try:
        cursor = connection.cursor()
        query = '''
        SELECT t.title, ar.artist_name, al.album_name, g.genre_name, t.rlsyr 
        FROM track t 
        JOIN artist ar ON t.artist_id = ar.id 
        JOIN album al ON t.album_id = al.id 
        JOIN genre g ON t.genre_id = g.id 
        WHERE t.title = %s
        '''
        cursor.execute(query, (title,))
        rows = cursor.fetchall()

        if not rows:
            messagebox.showinfo('Info', 'No songs found with the provided title')
            return

        results_window = Toplevel()
        results_window.title("Search Results")
        results_window.geometry("800x400")

        tree = ttk.Treeview(results_window, columns=("Title", "Artist", "Album", "Genre", "Release Year"), show='headings')
        tree.heading("Title", text="Title")
        tree.heading("Artist", text="Artist")
        tree.heading("Album", text="Album")
        tree.heading("Genre", text="Genre")
        tree.heading("Release Year", text="Release Year")

        for row in rows:
            tree.insert('', END, values=row)

        tree.pack(fill=BOTH, expand=True)

    except Exception as e:
        messagebox.showerror('Error', f"Failed to search for the song: {e}")

    finally:
        connection.close()

def search_song_window():
    global root, song_info1

    root = Toplevel()
    root.title('Search Song')
    root.geometry('800x600')

    background_image = ImageTk.PhotoImage(file='assets/search.jpg')
    bg_label = Label(root, image=background_image)
    bg_label.place(relwidth=1, relheight=1)

    heading_label = Label(root, text="Search Song", font=('Helvetica', 18, 'bold'), bg='#dfdee2', fg='black')
    heading_label.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.1)

    label_frame = Frame(root, bg='#dfdee2')
    label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.3)

    Label(label_frame, text="Title:", font=('Helvetica', 13, 'bold'), bg='#dfdee2').place(relx=0.05, rely=0.4)
    song_info1 = Entry(label_frame, font=('Helvetica', 11))
    song_info1.place(relx=0.3, rely=0.4, relwidth=0.6)

    Button(root, text="Search", font=('Helvetica', 12, 'bold'), bg='#dfdee2', fg='black', command=search_song).place(
        relx=0.3, rely=0.7, relwidth=0.2)
    Button(root, text="Cancel", font=('Helvetica', 12, 'bold'), bg='#dfdee2', fg='black', command=root.destroy).place(
        relx=0.6, rely=0.7, relwidth=0.2)

    root.mainloop()

if __name__ == "__main__":
    search_song_window()
