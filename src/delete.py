from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from config import get_connection

def delete_song():
    title = song_info1.get()

    if not title:
        messagebox.showerror('Error', 'Please enter the title of the song to delete')
        return

    connection = get_connection()
    if connection is None:
        messagebox.showerror('Error', 'Database connection failed')
        return

    try:
        cursor = connection.cursor()
        query = '''DELETE FROM track 
                   USING track
                   INNER JOIN album ON track.album_id = album.id
                   INNER JOIN artist ON track.artist_id = artist.id
                   WHERE track.title = %s'''
        cursor.execute(query, (title,))
        connection.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo('Success', 'Song deleted successfully!')
        else:
            messagebox.showinfo('Info', 'No song found with the provided title')

    except Exception as e:
        messagebox.showerror('Error', f"Failed to delete song: {e}")

    finally:
        connection.close()
        root.destroy()

def delete_song_window():
    global root, song_info1

    root = Toplevel()
    root.title('Delete Song')
    root.geometry('800x600')

    background_image = Image.open('assets/delete.jpg')
    background_image = background_image.resize((800, 600), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(background_image)

    canvas = Canvas(root, width=800, height=600)
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor=NW)

    heading_label = Label(root, text="Delete Song", font=('Helvetica', 18, 'bold'), bg='#dfdee2', fg='black')
    heading_label.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.1)

    label_frame = Frame(root, bg='#dfdee2')
    label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.3)

    Label(label_frame, text="Title:", font=('Helvetica', 13, 'bold'), bg='#dfdee2').place(relx=0.05, rely=0.4)
    song_info1 = Entry(label_frame, font=('Helvetica', 11))
    song_info1.place(relx=0.3, rely=0.4, relwidth=0.6)

    Button(root, text="Delete", font=('Helvetica', 12, 'bold'), bg='#dfdee2', fg='black', command=delete_song).place(
        relx=0.3, rely=0.7, relwidth=0.2)
    Button(root, text="Cancel", font=('Helvetica', 12, 'bold'), bg='#dfdee2', fg='black', command=root.destroy).place(
        relx=0.6, rely=0.7, relwidth=0.2)

    root.mainloop()

if __name__ == "__main__":
    delete_song_window()
