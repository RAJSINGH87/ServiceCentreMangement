import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showservicesfind():

    t=tkinter.Tk()
    t.geometry ('700x700')
    t.title('services')
    t.config(bg='purple')
    r=Label(t,text='Service Find Form',font=('arial',20),fg='black',bg='yellow')
    r.place(x=120,y=10)
        
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select servicename,catid,charge,description  from services where serviceid=%d" %(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        db.close()
    def newdata():
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        sql="select serviceid from services"
        cur.execute(sql)
        m=[]
        data=cur.fetchall()
        for r in data:
            m.append(r[0])
            db.close()
            e1['values']=m
            
        
    a=Label(t,text='serviceid',bg='teal',fg='white')
    a.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=400,y=50)
    b=Label(t,text='servicename',bg='teal',fg='white')
    b.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=400,y=90)
    c=Label(t,text='catid',bg='teal',fg='white')
    c.place(x=50,y=180)
    e3=Entry(t,width=30)
    e3.place(x=400,y=180)
    d=Label(t,text='charge',bg='teal',fg='white')
    d.place(x=50,y=280)
    e4=Entry(t,width=30)
    e4.place(x=400,y=280)
    f=Label(t,text='description',bg='teal',fg='white')
    f.place(x=50,y=380)
    e5=Entry(t,width=40)
    e5.place(x=400,y=380)    
    b1=Button(t,text='find',bg='green',command=finddata,width=20)
    b1.place(x=50,y=450)
    b2=Button(t,text='new',command=newdata,bg='red',width=20)
    b2.place(x=400,y=450)
    t.mainloop()
    
