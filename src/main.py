from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
from config import get_connection

def signup_page():
    root.destroy()
    import signup

def login_user():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    else:
        connection = get_connection()
        if connection is None:
            messagebox.showerror('Error', 'Database connection failed')
            return

        try:
            cursor = connection.cursor()
            cursor.execute('USE project')

            query = 'SELECT * FROM subscription WHERE username=%s AND password=%s'
            cursor.execute(query, (username_entry.get(), password_entry.get()))
            row = cursor.fetchone()

            if row is None:
                messagebox.showerror('Error', 'Invalid username or password')
            else:
                messagebox.showinfo('Welcome', 'Login successful')
                import view

        except Exception as e:
            messagebox.showerror('Error', f"Error: {e}")
        finally:
            connection.close()

def show_password():
    password_entry.config(show='')
    eye_button.config(command=hide_password)

def hide_password():
    password_entry.config(show='*')
    eye_button.config(command=show_password)

def user_enter(event):
    if username_entry.get() == 'Username':
        username_entry.delete(0, END)

def password_enter(event):
    if password_entry.get() == 'Password':
        password_entry.delete(0, END)
        password_entry.config(show='*')

# Tkinter Setup
root = Tk()
root.title('Login Page')
root.state('zoomed')

bg_image = ImageTk.PhotoImage(file='assets/login.jpg')
bg_label = Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

heading = Label(root, text='LOGIN', font=('Helvetica', 23, 'bold'), bg='black', fg='firebrick1')
heading.place(x=605, y=120)

username_entry = Entry(root, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick3')
username_entry.place(x=580, y=200)
username_entry.insert(0, 'Username')
username_entry.bind('<FocusIn>', user_enter)

Frame(root, width=226.5, height=2).place(x=580, y=222)

password_entry = Entry(root, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick3')
password_entry.place(x=580, y=260)
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>', password_enter)

Frame(root, width=226.5, height=2).place(x=580, y=282)

open_eye_img = PhotoImage(file='assets/closeye.png')
close_eye_img = PhotoImage(file='assets/openeye.png')
eye_button = Button(root, image=open_eye_img, bd=0, bg='white', activebackground='white', cursor='hand2', command=show_password)
eye_button.place(x=830, y=256.5)

login_button = Button(root, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1',
                       activebackground='firebrick1', cursor='hand2', bd=0, width=19,
                       activeforeground='white', command=login_user)
login_button.place(x=578, y=350)

quit_button = Button(root, text='Quit', font=('Open Sans', 16, 'bold'), fg='white', bg='green',
                      activebackground='firebrick1', cursor='hand2', bd=0, width=19,
                      activeforeground='white', command=root.destroy)
quit_button.place(x=578, y=410)

signup_label = Label(root, bg='black', text='Not subscribed?', font=('Helvetica', 9, 'bold'), fg='firebrick1')
signup_label.place(x=590, y=500)

new_account_button = Button(root, text='Subscribe now', font=('Open Sans', 9, 'underline'), fg='white', bg='red',
                             activebackground='blue', cursor='hand2', bd=0, activeforeground='firebrick1',
                             command=signup_page)
new_account_button.place(x=722, y=500)

root.mainloop()
