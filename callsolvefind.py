import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showcallsolvefind():

    t=tkinter.Tk()
    t.geometry ('700x700')
    t.title('callsolve')
    t.config(bg='purple')
    r=Label(t,text='Callsolve Find Form',font=('arial',20),fg='black',bg='yellow')
    r.place(x=120,y=10)
        
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select callid,engid,solvedate,solution  from callsolve where solveid=%d" %(xa)
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
        sql="select solveid from callsolve"
        cur.execute(sql)
        m=[]
        data=cur.fetchall()
        for r in data:
            m.append(r[0])
            db.close()
            e1['values']=m
            
        
    a=Label(t,text='solveid',bg='teal',fg='white')
    a.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=400,y=50)
    b=Label(t,text='callid',bg='teal',fg='white')
    b.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=400,y=90)
    c=Label(t,text='engid',bg='teal',fg='white')
    c.place(x=50,y=180)
    e3=Entry(t,width=30)
    e3.place(x=400,y=180)
    d=Label(t,text='solvedate',bg='teal',fg='white')
    d.place(x=50,y=280)
    e4=Entry(t,width=30)
    e4.place(x=400,y=280)
    f=Label(t,text='solution',bg='teal',fg='white')
    f.place(x=50,y=380)
    e5=Entry(t,width=40)
    e5.place(x=400,y=380)    
    b1=Button(t,text='find',bg='green',command=finddata,width=20)
    b1.place(x=50,y=550)
    b2=Button(t,text='new',command=newdata,bg='red',width=20)
    b2.place(x=400,y=550)
    t.mainloop()
    
