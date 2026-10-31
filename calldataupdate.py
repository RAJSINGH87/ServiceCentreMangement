import tkinter 
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
def showcalldataupdate():

    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('calldata')
    t.config(bg='purple')
    r=Label(t,text='Calldata Update Form',font=('arial',20),fg='black',bg='yellow')
    r.place(x=120,y=10)
        
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=e6.get()
             
        sql="update calldata set custid='%s',serviceid='%s',calldata='%s',problem='%s',priority='%s' where callid=%d"%(xb,xc,xd,xe,xf,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','done')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select custid,serviceid,calldata,problem,priority  from calldata where callid=%d" %(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        db.close()
    def newdata():
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        sql="select callid from calldata"
        cur.execute(sql)
        m=[]
        data=cur.fetchall()
        for r in data:
            m.append(r[0])
            db.close()
            e1['values']=m
            
        
    a=Label(t,text='callid',bg='teal',fg='white')
    a.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=400,y=50)
    b=Label(t,text='catid',bg='teal',fg='white')
    b.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=400,y=90)
    c=Label(t,text='serviceid',bg='teal',fg='white')
    c.place(x=50,y=180)
    e3=Entry(t,width=30)
    e3.place(x=400,y=180)
    d=Label(t,text='calldata',bg='teal',fg='white')
    d.place(x=50,y=280)
    e4=Entry(t,width=30)
    e4.place(x=400,y=280)
    f=Label(t,text='problem',bg='teal',fg='white')
    f.place(x=50,y=380)
    e5=Entry(t,width=40)
    e5.place(x=400,y=380) 
    g=Label(t,text='priority',bg='teal',fg='white')
    g.place(x=50,y=480)
    e6=Entry(t,width=20)
    e6.place(x=400,y=480)   
    b1=Button(t,text='find',bg='green',command=finddata,width=20)
    b1.place(x=50,y=550)
    b2=Button(t,text='update',command=updatedata,bg='red',width=20)
    b2.place(x=400,y=550)
    t.mainloop()
    
