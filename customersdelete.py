import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showcustomersdelete():
 
    t=tkinter.Tk() 
    t.geometry('700x700')
    t.title('customers')
    r=Label(t,text='Customer Delete Form',font=('arial',15),fg='red',bg='yellow')
    r.place(x=120,y=10)
    t.config(bg='orange')
    a=Label(t,text='Custid')
    a.place(x=50,y=100)
    e1=Entry(t,width=20)
    e1.place(x=400,y=100)
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from customers where custid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','deleted')
        e1.delete(0,END)
        
    b1=Button(t,text='Delete',width=20,command=deletedata)
    b1.place(x=50,y=300)
    t.mainloop()