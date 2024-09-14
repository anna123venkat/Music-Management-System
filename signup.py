from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from pymysql import*

def clear():
# emailEntry.delete(0,END)
passwordEntry.delete(0,END)
confirmEntry.delete(0,END)
usernameEntry.delete(0,END)
check.set(0)
signup_window.destroy()
import main

def connect_database():
if usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
messagebox.showerror('Error','All fields or required')
elif passwordEntry.get() != confirmEntry.get():
messagebox.showerror('Error','Confirm password again')

else:
try:
con=connect(host='localhost',user='root',password='dharun1504')
mycursor = con.cursor()
except:
messagebox.showerror('Error','Network issue, Try again')
return
try:
#query = 'create database userdata'
#mycursor.execute(query)
query = 'use project'
mycursor.execute(query)
query = 'create table subscription(id int auto_increment primary key not null,username varchar(100),password varchar(20))'
mycursor.execute(query)
except:
mycursor.execute('use project')
query = 'select* from subscription where username=%s'
mycursor.execute(query,(usernameEntry.get()))
row = mycursor.fetchone()
if row != None:
messagebox.showerror('Error','Username already exists')
else: 
query = 'insert into subscription(username,password) values(%s,%s)'
mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
con.commit()
con.close()
clear()


signup_window = Tk()
signup_window.title("Signup page")

signup_window.state('zoomed')

background = ImageTk.PhotoImage(file ='main.jpg' )

bgLabel = Label(signup_window,image=background)
bgLabel.grid()

frame = Frame(signup_window,bg='black')
frame.place(x=630,y=250)

headingFrame1 = Frame(signup_window,bg="#dfdee2",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="\n .....MUSIX .....", bg="black", fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

heading = Label(frame,text='JOIN US',
font = ('Helvetica',18,'italic'),
bg='white',fg='black')
heading.grid(row=0,column=0,padx=11,pady=11)

usernameLabel = Label(frame,text='Username',
font=('Helvetica',10,'bold'),
bg = 'black',fg='white')
usernameLabel.grid(row=3,column=0,sticky='w',padx = 25,pady=(10,0))

usernameEntry = Entry(frame,width=30,
font=('Microsoft Yahei UI Light',10,'bold'))
usernameEntry.grid(row=5,column=0,sticky='w',padx = 25 )

passwordLabel = Label(frame,text='Password',
font=('Helvetica',10,'bold'),
bg = 'black',fg='white')
passwordLabel.grid(row=6,column=0,sticky='w',padx = 25,pady=(10,0))

passwordEntry = Entry(frame,width=30,
font=('Microsoft Yahei UI Light',10,'bold'))
passwordEntry.grid(row=8,column=0,sticky='w',padx = 25 )
passwordEntry.configure(show='*')
confirmLabel = Label(frame,text='Confirm Password',
font=('Helvetica',10,'bold'),
bg = 'black',fg='white')
confirmLabel.grid(row=9,column=0,sticky='w',padx = 25,pady=(10,0))

confirmEntry = Entry(frame,width=30,
font=('Microsoft Yahei UI Light',10,'bold'))
confirmEntry.grid(row=11,column=0,sticky='w',padx = 25,pady=(0,10))

check = IntVar()

signupButton=Button(frame,text='JOIN',font=('Open Sans',16,'bold'),
fg='white',bg='red',activebackground='black',
cursor='hand2',bd=0,width=19,activeforeground='white',
command=connect_database)
signupButton.grid(row=60,column=0)

signup_window.mainloop()
