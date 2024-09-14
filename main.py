from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql
def signup_page():
    root.destroy()
    import signup

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get() =='':
        messagebox.showerror('error','All fields are required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='dharun1504')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Connection not estabilished')
            return
        query = 'use project'
        mycursor.execute(query)
        query = 'select * from subscription where username=%s and password=%s'
        username = usernameEntry.get()
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row = mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login successful')
            import main
            
            
            

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
        passwordEntry.config(show='*')

root = Tk()
#login_window.resizable(0,0)
root.state('zoomed')
root.title('Login Page')

bgImage = ImageTk.PhotoImage(file='login.jpg')

bgLabel = Label(root,image=bgImage)
bgLabel.grid(row=0,column=0)

heading = Label(root,text='****LOGIN****',font = ('Helvetica',23,'bold'),bg='black',fg='firebrick1')
heading.place(x=605,y=120)

usernameEntry = Entry(root,width = 25, font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick3' )
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Name Of User')
usernameEntry.bind('<FocusIn>',user_enter)

Frame(root,width=226.5,height=2).place(x=580,y=222)

passwordEntry = Entry(root,width = 25, font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick3' )
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Security Key')
passwordEntry.bind('<FocusIn>',password_enter)

Frame(root,width=226.5,height=2).place(x=580,y=282)

openeye=PhotoImage(file='closeye.png')
eyeButton = Button(root,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=show)
eyeButton.place(x=830,y=256.5)

loginButton=Button(root,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',
                   activebackground='firebrick1',cursor='hand2',bd=0,width=19,activeforeground='white'
                   ,command=login_user)
loginButton.place(x=578,y=350)

quitButton=Button(root,text='Quit',font=('Open Sans',16,'bold'),fg='white',bg='green',
                   activebackground='firebrick1',cursor='hand2',bd=0,width=19,activeforeground='white'
                   ,command=root.destroy)
quitButton.place(x=578,y=410)


signupLabel = Label(root,bg='black',text='Not subscribed?',font=('Helvetica',9,'bold'),fg='firebrick1')
signupLabel.place(x=590,y=500)

newaccountButton=Button(root,text='Subscribe now',font=('Open Sans',9,'underline'),fg='white',bg='red',
                        activebackground='blue',cursor='hand2',bd=0,activeforeground='firebrick1',
                        command=signup_page)
newaccountButton.place(x=722,y=500)

root.mainloop()

