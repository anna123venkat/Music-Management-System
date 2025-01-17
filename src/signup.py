from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from config import get_connection

def clear():
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    confirm_password_entry.delete(0, END)
    signup_window.destroy()

def connect_database():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not username or not password or not confirm_password:
        messagebox.showerror('Error', 'All fields are required')
        return

    if password != confirm_password:
        messagebox.showerror('Error', 'Passwords do not match')
        return

    connection = get_connection()
    if connection is None:
        messagebox.showerror('Error', 'Database connection failed')
        return

    try:
        cursor = connection.cursor()
        cursor.execute('USE project')

        # Check if username already exists
        cursor.execute('SELECT * FROM subscription WHERE username = %s', (username,))
        if cursor.fetchone():
            messagebox.showerror('Error', 'Username already exists')
        else:
            cursor.execute('INSERT INTO subscription (username, password) VALUES (%s, %s)', (username, password))
            connection.commit()
            messagebox.showinfo('Success', 'Signup successful')
            clear()

    except Exception as e:
        messagebox.showerror('Error', f"An error occurred: {e}")

    finally:
        connection.close()

def signup_window():
    global signup_window, username_entry, password_entry, confirm_password_entry

    signup_window = Tk()
    signup_window.title("Signup")
    signup_window.geometry("800x600")

    background_image = ImageTk.PhotoImage(file='assets/signup.jpg')
    bg_label = Label(signup_window, image=background_image)
    bg_label.place(relwidth=1, relheight=1)

    frame = Frame(signup_window, bg='black')
    frame.place(x=200, y=150, width=400, height=300)

    heading = Label(frame, text='Signup', font=('Helvetica', 18, 'bold'), bg='black', fg='white')
    heading.pack(pady=10)

    Label(frame, text='Username:', font=('Helvetica', 12), bg='black', fg='white').place(x=20, y=70)
    username_entry = Entry(frame, width=30)
    username_entry.place(x=150, y=70)

    Label(frame, text='Password:', font=('Helvetica', 12), bg='black', fg='white').place(x=20, y=110)
    password_entry = Entry(frame, width=30, show='*')
    password_entry.place(x=150, y=110)

    Label(frame, text='Confirm Password:', font=('Helvetica', 12), bg='black', fg='white').place(x=20, y=150)
    confirm_password_entry = Entry(frame, width=30, show='*')
    confirm_password_entry.place(x=150, y=150)

    Button(frame, text='Signup', font=('Helvetica', 12, 'bold'), bg='green', fg='white',
           command=connect_database).place(x=100, y=200)
    Button(frame, text='Cancel', font=('Helvetica', 12, 'bold'), bg='red', fg='white',
           command=signup_window.destroy).place(x=200, y=200)

    signup_window.mainloop()

if __name__ == "__main__":
    signup_window()
