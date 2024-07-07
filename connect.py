from tkinter import *

from tkinter import messagebox
from PIL import ImageTk,Image
import os

# Construct an absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

graduated_png_path = os.path.join(script_dir, "assets", "graduated.png")
bg_png_path = os.path.join(script_dir, "assets", "bg.jpg")
eye_png_path = os.path.join(script_dir, "assets", "eye.png")
eyeclose_png_path = os.path.join(script_dir, "assets", "eyeclose.png")
user_png_path = os.path.join(script_dir, "assets", "user.png")
lock_png_path = os.path.join(script_dir, "assets", "lock.png")

ico_path = os.path.join(script_dir, "assets", "icon.ico")
graduates_png_path = os.path.join(script_dir, "assets", "graduates.png")







def hide():
    eyeimg.config(file=eyeclose_png_path)
    lock_entry.config(show='*')
    eye.config(command=show)

def show():
    eyeimg.config(file=eye_png_path)
    lock_entry.config(show='')
    eye.config(command=hide)


def login():
    if user_entry.get()=='' or lock_entry.get()=='':
        messagebox.showerror("Error","All fields are required!")
    elif user_entry.get()=='Hamza' and lock_entry.get()=='0000':
        messagebox.showinfo("Success" ,"Welcome Hamza")
        root.destroy()
        import sms

    else:
        messagebox.showerror("Error","You enter wrong credentials")





root = Tk()

root.title("Login")
root.resizable(0,0)

root.geometry("1368x720+0+0")

img = Image.open(bg_png_path)
bg_img=ImageTk.PhotoImage(img)

bg_label = Label(root,image=bg_img)
bg_label.place(x=0,y=0)


style= Frame(root,bg="white")
style.place(x=550,y=210)

stu = PhotoImage(file=graduated_png_path)

stu_label = Label(style,image=stu,bg="white")
stu_label.grid(pady=20,row=0,column=0,columnspan=2)

user= PhotoImage(file=user_png_path)
user_label = Label(style,image=user,bg="white",text="Username",compound="left",font="ARial 16 bold")
user_label.grid(row=1,column=0,padx=20,pady=10)

user_entry=Entry(style,bd=6,relief="groove",font="helvatica 12 bold")

user_entry.grid(row=1,column=1,pady=10)


lock= PhotoImage(file=lock_png_path)
lock_label = Label(style,image=lock,bg="white",text="Password",compound="left",font="ARial 16 bold")
lock_label.grid(row=2,column=0,padx=10,pady=10)

lock_entry=Entry(style,bd=6,relief="groove",font="helvatica 12 bold")

lock_entry.grid(row=2,column=1,pady=10)


eyeimg=PhotoImage(file=eye_png_path)
eye=Button(lock_entry,image=eyeimg,bd=0,cursor='hand2',relief='groove',command=hide)
eye.place(x=170,anchor=CENTER,y=9)

log = Button(style,text="Login",font="times 14 bold",bg="cornflowerblue",fg="white",
             activebackground="cornflowerblue",activeforeground="white",padx=25,cursor='hand2',command=login)
log.grid(row=3,column=1,padx=10,pady=10)

root.mainloop()