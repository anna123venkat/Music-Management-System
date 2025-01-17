from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from viewallsongs import view_all_songs
from viewedm import view_edm

def main_view():
    root = Tk()
    root.title("Music Library Management System")
    root.geometry("800x600")

    # Background Image
    background_image = ImageTk.PhotoImage(file='assets/view.jpg')
    bg_label = Label(root, image=background_image)
    bg_label.place(relwidth=1, relheight=1)

    # Heading
    heading_label = Label(root, text="Music Library Management System", font=('Helvetica', 18, 'bold'), bg='#d4b890', fg='black')
    heading_label.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

    # Buttons for Views
    Button(root, text="View All Songs", font=('Helvetica', 12, 'bold'), bg='blue', fg='white', command=view_all_songs).place(
        relx=0.3, rely=0.3, relwidth=0.4, relheight=0.1)
    Button(root, text="View EDM Songs", font=('Helvetica', 12, 'bold'), bg='green', fg='white', command=view_edm).place(
        relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)

    Button(root, text="Exit", font=('Helvetica', 12, 'bold'), bg='red', fg='white', command=root.destroy).place(
        relx=0.3, rely=0.7, relwidth=0.4, relheight=0.1)

    root.mainloop()

if __name__ == "__main__":
    main_view()
