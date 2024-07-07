from tkinter import *
import time
from tkinter import ttk
import pymysql
from tkinter import messagebox,filedialog
import pandas

import sqlite3
import os

# Construct an absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct an absolute path to the files
ico_path = os.path.join(script_dir, "assets", "icon.ico")
graduates_png_path = os.path.join(script_dir, "assets", "graduates.png")


def add_stu():
    def add_data():
        if id_entry.get()==''or name_entry.get()==''or phone_entry.get()==''or gender_entry.get()==''or address_entry.get()==''or Dob_entry.get()=='':
            messagebox.showerror('Error','All fields are required!',parent= add_window)
        else:
            # columns=["ID","Name","Address","Phone","Gender","DOB",'Time','date']
            try:
                
                query='insert into student (ID,Name,Address, Phone, Gender, DOB,Time,date) values(%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(id_entry.get(),name_entry.get(),address_entry.get(),phone_entry.get(),gender_entry.get(),Dob_entry.get(),curr_time,date))
                res=messagebox.askyesno('Confirm','Data is added suucessfully. Do you want to clean the form?',parent=add_window)
                if res:
                    id_entry.delete(0,END)
                    phone_entry.delete(0,END)
                    address_entry.delete(0,END)
                    Dob_entry.delete(0,END)
                    name_entry.delete(0,END)
                    gender_entry.delete(0,END)
                    query='select *from student'
                    mycursor.execute(query)
                    fetch = mycursor.fetchall()
                    data.delete(*data.get_children())
                    for mat in fetch:
                        data.insert('',END,values=mat)
                    con.commit()

                else:
                    pass
            except:
                messagebox.showerror('Error','\u2022 Make sure Id is not repeated \n\u2022 Enter Phone number of 11 digits only',parent=add_window)
    add_window= Toplevel()
    add_window.grab_set()
    add_window.resizable(0,0)
    add_window.title("Add student")
    id_label= Label(add_window,text="Id",font="arial 18 bold",fg="red",padx=10,pady=8)
    id_label.grid(row=0,column=0,padx=10,pady=8,sticky="w")
    id_entry = Entry(add_window,font="times 12 bold",bd=2,width=25)
    id_entry.grid(row=0,column=1,padx=15,pady=8)

    name_label= Label(add_window,text="Name",font="arial 18 bold",fg="red",padx=10,pady=8)
    name_label.grid(row=1,column=0,padx=10,pady=8,sticky="w")
    name_entry = Entry(add_window,font="times 12 bold",bd=2,width=25)
    name_entry.grid(row=1,column=1,padx=15,pady=8)
   

    phone_label= Label(add_window,text="Phone No",font="arial 18 bold",fg="red",padx=10,pady=8)
    phone_label.grid(row=2,column=0,padx=10,pady=8,sticky="w")
    phone_entry = Entry(add_window,font="times 12 bold",bd=2,width=25)
    phone_entry.grid(row=2,column=1,padx=15,pady=8)



    address_label= Label(add_window,text="Address",font="arial 18 bold",fg="red",padx=10,pady=8)
    address_label.grid(row=3,column=0,padx=10,pady=8,sticky="w")
    address_entry = Entry(add_window,font="times 12 bold",bd=2,width=25)
    address_entry.grid(row=3,column=1,padx=15,pady=8)



    Dob_label= Label(add_window,text="D.O.B",font="arial 18 bold",fg="red",padx=10,pady=8)
    Dob_label.grid(row=5,column=0,padx=10,pady=8,sticky="w")
    Dob_entry = Entry(add_window,font="times 12 bold",bd=2,width=25)
    Dob_entry.grid(row=5,column=1,padx=15,pady=8)

    gender_label= Label(add_window,text="Gender",font="arial 18 bold",fg="red",padx=10,pady=8)
    gender_label.grid(row=4,column=0,padx=10,pady=8,sticky="w")
    gender_entry = Entry(add_window,font="times 12 bold",bd=2,width=25)
    gender_entry.grid(row=4,column=1,padx=15,pady=8)


    add_btn= Button(add_window,text="ADD",cursor='hand2',font="Arial 12 italic bold",command=add_data,padx=40,bd=5,relief="raised" ,bg="royalblue2",fg="white",activebackground="royalblue2",activeforeground="white")
    add_btn.grid(row=6,columnspan=2,pady=20)

def update_stu():
    
    
    def update_data():
        query='update student set name=%s,address=%s,phone= %s,gender=%s,dob =%s,date=%s,time=%s where id = %s'
        mycursor.execute(query,(name_entry.get(),address_entry.get(),phone_entry.get(),gender_entry.get(),Dob_entry.get(),date,curr_time,id_entry.get()))
        messagebox.showinfo('Success',f'Id {id_entry.get()} is modified successfully!',parent=update_window)
        update_window.destroy()
        query='select *from student'
        mycursor.execute(query)
        fetch=mycursor.fetchall()
        data.delete(*data.get_children())
        
        for mat in fetch:
            data.insert('',END,values=mat)
        con.commit()
    index=data.focus()
    if index != '': 
        update_window= Toplevel()
        update_window.grab_set()
        update_window.resizable(0,0)
        update_window.title("Update student")
        id_label= Label(update_window,text="Id",font="arial 18 bold",fg="red",padx=10,pady=8)
        id_label.grid(row=0,column=0,padx=10,pady=8,sticky="w")
        id_entry = Entry(update_window,font="times 12 bold",bd=2,width=25)
        id_entry.grid(row=0,column=1,padx=10,pady=8)

        name_label= Label(update_window,text="Name",font="arial 18 bold",fg="red",padx=10,pady=8)
        name_label.grid(row=1,column=0,padx=10,pady=8,sticky="w")
        name_entry = Entry(update_window,font="times 12 bold",bd=2,width=25)
        name_entry.grid(row=1,column=1,padx=15,pady=8)


        phone_label= Label(update_window,text="Phone No",font="arial 18 bold",fg="red",padx=10,pady=8)
        phone_label.grid(row=2,column=0,padx=10,pady=8,sticky="w")
        phone_entry = Entry(update_window,font="times 12 bold",bd=2,width=25)
        phone_entry.grid(row=2,column=1,padx=15,pady=8)



        address_label= Label(update_window,text="Address",font="arial 18 bold",fg="red",padx=10,pady=8)
        address_label.grid(row=3,column=0,padx=10,pady=8,sticky="w")
        address_entry = Entry(update_window,font="times 12 bold",bd=2,width=25)
        address_entry.grid(row=3,column=1,padx=15,pady=8)



        Dob_label= Label(update_window,text="D.O.B",font="arial 18 bold",fg="red",padx=10,pady=8)
        Dob_label.grid(row=5,column=0,padx=10,pady=8,sticky="w")
        Dob_entry = Entry(update_window,font="times 12 bold",bd=2,width=25)
        Dob_entry.grid(row=5,column=1,padx=15,pady=8)
        gender_label= Label(update_window,text="Gender",font="arial 18 bold",fg="red",padx=10,pady=8)
        gender_label.grid(row=4,column=0,padx=10,pady=8,sticky="w")
        gender_entry = Entry(update_window,font="times 12 bold",bd=2,width=25)
        gender_entry.grid(row=4,column=1,padx=15,pady=8)


        update_btn= Button(update_window,text="UPDATE",cursor='hand2',command=update_data,font="Arial 12 italic bold",padx=40,bd=5,relief="raised" ,bg="royalblue2",fg="white",activebackground="royalblue2",activeforeground="white")
        update_btn.grid(row=6,columnspan=2,pady=20)
        # index= data.focus()
        content= data.item(index)
        contentid=content['values']   
        id_entry.insert(END,contentid[0])
        name_entry.insert(END,contentid[1])
        address_entry.insert(END,contentid[2])
        phone_entry.insert(END,contentid[3])
        gender_entry.insert(END,contentid[4])
        Dob_entry.insert(END,contentid[5])
    else:
        messagebox.showerror('Error','No data is selected!')
def search_stu():
    def search_data():
        query='select *from student where id=%s or name = %s or address =%s or phone =%s or gender =%s or dob =%s'
        mycursor.execute(query,(id_entry.get(),name_entry.get(),address_entry.get(),phone_entry.get(),gender_entry.get(),Dob_entry.get()))
        fetch = mycursor.fetchall()
        
        if fetch != ():
            data.delete(*data.get_children())
            for mat in fetch:
                data.insert('',END,values=mat)
            con.commit()
        else:
            messagebox.showerror('Error','No Data Found!',parent=search_window)
            



    search_window= Toplevel()
    search_window.resizable(0,0)
    search_window.grab_set()
    search_window.title("Search student")
    id_label= Label(search_window,text="Id",font="arial 18 bold",fg="red",padx=10,pady=8)
    id_label.grid(row=0,column=0,padx=10,pady=8,sticky="w")
    id_entry = Entry(search_window,font="times 12 bold",bd=2,width=25)
    id_entry.grid(row=0,column=1,padx=15,pady=8)

    name_label= Label(search_window,text="Name",font="arial 18 bold",fg="red",padx=10,pady=8)
    name_label.grid(row=1,column=0,padx=10,pady=8,sticky="w")
    name_entry = Entry(search_window,font="times 12 bold",bd=2,width=25)
    name_entry.grid(row=1,column=1,padx=15,pady=8)


    phone_label= Label(search_window,text="Phone No",font="arial 18 bold",fg="red",padx=10,pady=8)
    phone_label.grid(row=2,column=0,padx=10,pady=8,sticky="w")
    phone_entry = Entry(search_window,font="times 12 bold",bd=2,width=25)
    phone_entry.grid(row=2,column=1,padx=15,pady=8)



    address_label= Label(search_window,text="Address",font="arial 18 bold",fg="red",padx=10,pady=8)
    address_label.grid(row=3,column=0,padx=10,pady=8,sticky="w")
    address_entry = Entry(search_window,font="times 12 bold",bd=2,width=25)
    address_entry.grid(row=3,column=1,padx=15,pady=8)



    Dob_label= Label(search_window,text="D.O.B",font="arial 18 bold",fg="red",padx=10,pady=8)
    Dob_label.grid(row=5,column=0,padx=10,pady=8,sticky="w")
    Dob_entry = Entry(search_window,font="times 12 bold",bd=2,width=25)
    Dob_entry.grid(row=5,column=1,padx=15,pady=8)

    gender_label= Label(search_window,text="Gender",font="arial 18 bold",fg="red",padx=10,pady=8)
    gender_label.grid(row=4,column=0,padx=10,pady=8,sticky="w")
    gender_entry = Entry(search_window,font="times 12 bold",bd=2,width=25)
    gender_entry.grid(row=4,column=1,padx=15,pady=8)


    search_btn= Button(search_window,text="SEARCH",cursor='hand2',command=search_data,font="Arial 12 italic bold",padx=40,bd=5,relief="raised" ,bg="royalblue2",fg="white",activebackground="royalblue2",activeforeground="white")
    search_btn.grid(row=6,columnspan=2,pady=20)
def delete_stu():
    
    index= data.focus()
    if index !='':
        content= data.item(index)
        contentId=content['values'][0]
        query='delete from student where id=%s'
        mycursor.execute(query,contentId)
        
        messagebox.showinfo('Success',f'Id {contentId} has been deleted successfully!')
        query='select *from student'
        mycursor.execute(query)
        fetch = mycursor.fetchall()
        data.delete(*data.get_children())
        for mat in fetch:
            data.insert('',END,values=mat)
        con.commit()
    else:
        messagebox.showerror('Error','No data is selected!')
        return
def export_stu():
    indexing=data.get_children()
    if indexing != ():
        url=filedialog.asksaveasfilename(defaultextension='.csv')
        new=[]
        for index in indexing:
            datalist = data.item(index)
            new.append(datalist["values"])
        table=pandas.DataFrame(new,columns=('Id','Name','Address','Phone','Gender','DOB','Time','date'))
        table.to_csv(url,index=False)
        messagebox.showinfo('Success','File created Successfully!')
    else:
        messagebox.showerror('Error','No data found!')
def exiting():
    get=messagebox.askyesno('Confirm','Do you want to exit?')
    if get:
        root1.destroy()
    else:
        pass
    
def show_stu():
    
    query='select *from student'
    mycursor.execute(query)
    fetch = mycursor.fetchall()
    if fetch != ():
        data.delete(*data.get_children())
        for mat in fetch:
            data.insert('',END,values=mat)
        con.commit()
    else:
        messagebox.showinfo('Info','Data Table is Empty. Add some data!')








def connect():

    def check():
        global mycursor,con
        try:
            con= pymysql.connect(host=hostentry.get(), user = userentry.get(),password= passwordentry.get())
            
            mycursor= con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=window)
            return
        query='create database if not exists studentmanagementsystem'
        mycursor.execute(query)
       
        query='use studentmanagementsystem'
        mycursor.execute(query)
       
        query='''create table if not exists student(
        ID int not null primary key,
        Name varchar(20),
        Address varchar(50),
        Phone varchar(11),
        Gender varchar(10),
        DOB varchar(20),
        Time varchar(20),
        date varchar(20)
        
            )'''
        mycursor.execute(query)
        
        con.commit()
        
        messagebox.showinfo("Success",'You are connected to Database',parent=window)
        window.destroy()
        add.config(state=NORMAL)
        Delete.config(state=NORMAL)
        Update.config(state=NORMAL)
        search.config(state=NORMAL)
        Export.config(state=NORMAL)
        Show.config(state=NORMAL)
        connector.config(state=DISABLED)
        
    window = Toplevel()
    window.geometry("420x250+865+300")
    window.grab_set()
    window.resizable(0,0)
    window.title("Database Connection")

    hostname= Label(window,text="Host Name:",font="arial 18 bold",fg="red")
    hostname.grid(row=0,column=0,padx=20)

    hostentry = Entry(window,font="helvatice 12 bold")
    hostentry.grid(row=0,column=1,padx=40,pady=20)

    username= Label(window,text="User Name:",font="arial 18 bold",fg="red")
    username.grid(row=1,column=0,padx=20)
    userentry = Entry(window,font="helvatice 12 bold")
    userentry.grid(row=1,column=1,padx=40,pady=20)

    password= Label(window,text="Password:",font="arial 18 bold",fg="red")
    password.grid(row=2,column=0,padx=20)
    passwordentry = Entry(window,font="helvatice 12 bold")
    passwordentry.grid(row=2,column=1,padx=40,pady=20)

    connectbtn = Button(window,text="CONNECT",font="Arial 12 italic bold",padx=40,bd=5,relief="raised" 
                        ,bg="royalblue2",fg="white",activebackground="royalblue2",activeforeground="white",
                        command=check,cursor='hand2')
    connectbtn.grid(row=3,columnspan=2)

    


def clock():
    global date,curr_time
    date = time.strftime("%d/%m/%Y")
    curr_time = time.strftime("%I :%M :%S")
    datetime.config(text=f"   Date {date} \n Time {curr_time}")
    datetime.after(1000,clock)
count=0
text1=''
def slider():
    global text1,count
    if count==len(s):
        count=0
        text1=''     
    text1=text1+s[count]
    slide.config(text=text1)
    count+=1
    slide.after(200,slider)
    



root1= Tk()
# style= ttk.Style()
# # ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

# style.theme_use("alt")
# style.configure('.')
root1.title("Student Management System created by Hamza Meer")
root1.geometry("1368x720+0+0")
root1.resizable(0,0)
root1.iconbitmap(ico_path)
root1.config(bg='')
datetime = Label(root1,font=("times new roman",18,"bold"),fg="royalblue",bg='white')
datetime.place(x=0,y=0)
clock()
s="Student Management System"
slide = Label(root1,font=("times new roman",28,"bold"),fg="royalblue",bg='white',width=25)
slide.place(x=300,y=0)
slider()

connector =Button(root1,text="Connect Database",cursor='hand2',font=("times new roman",16,"bold"),bg="royalblue2",fg="white"
                  ,activebackground="royalblue2",activeforeground="white",bd=5,command=connect)
connector.place(x=1165,y=0)




left_frame = Frame(root1,bg='white')
left_frame.place(x=140,y=80)

img = PhotoImage(file=graduates_png_path)
stu = Label(left_frame,image=img,bg='white')
stu.grid(row=0,column=0,padx=40,pady=20)



add = Button(left_frame,text="Add Student",cursor='hand2',state = DISABLED,command=add_stu,font="Arial 12 italic bold",padx=50,bd=5,relief="raised" ,bg="royalblue2",fg="white",activebackground="royalblue2",activeforeground="white")
add.grid(row=1,column=0,pady=12)

Update = Button(left_frame,text="Update Student",cursor='hand2',command=update_stu,state = DISABLED,font="Arial 12 italic bold",padx=40,bd=5,relief="raised" ,bg="royalblue2",fg="white",activebackground="royalblue2",activeforeground="white")
Update.grid(row=2,column=0,pady=12)

Delete = Button(left_frame,text="Delete Student",cursor='hand2',command=delete_stu,state = DISABLED,font="Arial 12 italic bold",padx=45,bd=5,relief="raised" ,bg="royalblue2",fg="white",activebackground="royalblue2",activeforeground="white")
Delete.grid(row=3,column=0,pady=12)

Show = Button(left_frame,text="Show All Student",cursor='hand2',command=show_stu,state = DISABLED,font="Arial 12 italic bold",padx=35,bd=5,relief="raised" ,bg="royalblue2",fg="white",activebackground="royalblue2",activeforeground="white")
Show.grid(row=4,column=0,pady=12)

Exit = Button(left_frame,text="Exit",cursor='hand2',font="Arial 12 italic bold",command=exiting,padx=90,bd=5,relief="raised" ,bg="royalblue2",fg="white",activebackground="royalblue2",activeforeground="white")
Exit.grid(row=7,column=0,pady=12)

search = Button(left_frame,text="Search Student",cursor='hand2',command=search_stu,state = DISABLED,font="Arial 12 italic bold",padx=45,bd=5,relief="raised" ,bg="royalblue2",fg="white",activebackground="royalblue2",activeforeground="white")
search.grid(row=5,column=0,pady=12)

Export = Button(left_frame,text="Export Student",cursor='hand2',command=export_stu,state = DISABLED,font="Arial 12 italic bold",padx=45,bd=5,relief="raised" ,bg="royalblue2",fg="white",activebackground="royalblue2",activeforeground="white")
Export.grid(row=6,column=0,pady=12)


right_frame = Frame(root1)
right_frame.place(x=500,y=120,height=550,width=850)

xscroll = Scrollbar(right_frame,orient=HORIZONTAL)
yscroll = Scrollbar(right_frame,orient=VERTICAL)

data = ttk.Treeview(right_frame
                    ,columns=["ID","Name","Address","Phone","Gender","DOB",'Time','date']
                    ,xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
xscroll.pack(side=BOTTOM,fill=X)
yscroll.pack(side=RIGHT,fill=Y)
xscroll.configure(command=data.xview)
yscroll.configure(command=data.yview)


data.pack(fill=BOTH,expand=1)

data.heading('ID',text="Id")
data.heading('Name',text="Name")
data.heading('Address',text="Address")
data.heading('Phone',text="Phone No.")
data.heading('Gender',text="Gender")
data.heading('DOB',text="D.O.B")
data.heading('Time',text="Added Time")
data.heading('date',text="Added Date")


data.column('ID',width=50,anchor='center')
data.column('Name',width=200,anchor='center')
data.column('Address',width=100,anchor='center')
data.column('Phone',width=200,anchor='center')
data.column('Gender',width=100,anchor='center')
data.column('DOB',width=100,anchor='center')
data.column('Time',width=150,anchor='center')
data.column('date',width=150,anchor='center')


style = ttk.Style()

style.configure('Treeview',rowheight=50,foreground='gray20',font="Arial 10 bold")

style.configure('Treeview.Heading',foreground='red',font="Helvatica 15 bold")





data.config(show="headings")


root1.mainloop()
