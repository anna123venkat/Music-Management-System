from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from tkinter import ttk

mypass = "dharun1504"
mydatabase="project"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

def searchsong():

root = Tk()
root.title("Searched Songs")
root.minsize(width=40,height=4)
root.geometry("1000x400")
title = songInfo1.get()
tree = ttk.Treeview(root, column=("c1","c2","c3","c4","c5",),show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="Title")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="Artist")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Album")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="Genre")
tree.column("#5", anchor=tk.CENTER)
tree.heading("#5", text="Release Year")
tree.grid(sticky = (N,S,W,E))
# root.treeview = tree
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)
#tree.pack(expand=True,fill=BOTH)
tree.pack()
try:
cur.execute("select t.title,a.album_name,ar.artist_name,g.genre_name,t.rlsyr from track t, album a, artist ar,genre g where t.album_id=a.id and t.artist_id=ar.id and t.genre_id=g.id and t.title = '"+title+"';")
rows = cur.fetchall()
con.commit()
if(rows):
for i in rows:
tree.insert("", tk.END, values=i)
else:
raise
except:
messagebox.showinfo('Error',"Failed To Fetch Songs From The Database")
root.destroy

quitBtn = Button(root,text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
root.mainloop()

'''try:
cur.execute("select t.title,a.album_name,ar.artist_name,g.genre_name,t.rlsyr from track t, album a, artist ar,genre g where t.album_id=a.id and t.artist_id=ar.id and t.genre_id=g.id and t.title = '"+title+"';")
con.commit()
messagebox.showinfo('Success',"Song Record Found")
except:
messagebox.showinfo("Please Check Song Title")

songInfo1.delete(0, END)
root.destroy()'''

def search():

global img,songInfo1,songInfo2,songInfo3,songInfo4,songInfo5,Canvas1,con,cur,root

root = Toplevel()
root.title("Search Music Recordd")
root.minsize(width=400,height=400)
root.geometry("800x600")
root.state('zoomed')
root.configure(bg='maroon')
headingFrame1 = Frame(root,bg="#dfdee2",bd=5)
headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

headingLabel = Label(headingFrame1, text="Search Song Record",font='Helvetica 14 bold', bg="#010103", fg='white',)
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

labelFrame = Frame(root,bg="#010103")
labelFrame.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.2)

lb2 = Label(labelFrame,text="Song Title:", font='Helvetica 11 bold', bg="#000000", fg='white')
lb2.place(relx=0.05,rely=0.5)

songInfo1 = Entry(labelFrame)
songInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
lb2 = Label(labelFrame,text="Song Title:", font='Helvetica 11 bold', bg="#000000", fg='white')
lb2.place(relx=0.05,rely=0.5)

songInfo1 = Entry(labelFrame)
songInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)

SubmitBtn = Button(root,text="Submit",font='Helvetica 11 bold',bg="#010103", fg='white',command=searchsong)
SubmitBtn.place(relx=0.28,rely=0.75, relwidth=0.18,relheight=0.08)

quitBtn = Button(root,text="Quit",font='Helvetica 11 bold',bg="#010103", fg='white', command=root.destroy)
quitBtn.place(relx=0.53,rely=0.75, relwidth=0.18,relheight=0.08)

root.mainloop()
