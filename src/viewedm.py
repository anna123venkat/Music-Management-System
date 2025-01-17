from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from config import get_connection

def view_edm():
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
        WHERE g.genre_name = 'EDM'
        ORDER BY t.title
        '''
        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            messagebox.showinfo('Info', 'No EDM songs found')
            return

        # Create a new window for displaying the results
        result_window = Toplevel()
        result_window.title("EDM Songs")
        result_window.geometry("800x400")

        # Create a Treeview widget
        tree = ttk.Treeview(result_window, columns=("Title", "Artist", "Album", "Genre", "Release Year"), show='headings')
        tree.heading("Title", text="Title")
        tree.heading("Artist", text="Artist")
        tree.heading("Album", text="Album")
        tree.heading("Genre", text="Genre")
        tree.heading("Release Year", text="Release Year")

        # Insert rows into the Treeview
        for row in rows:
            tree.insert('', END, values=row)

        tree.pack(fill=BOTH, expand=True)

    except Exception as e:
        messagebox.showerror('Error', f"Failed to fetch EDM songs: {e}")

    finally:
        connection.close()

if __name__ == "__main__":
    view_edm()
