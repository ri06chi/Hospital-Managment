from Tkinter import*
import sqlite3
import tkMessageBox
from tkMessageBox import *
root = Tk()

con = sqlite3.connect('rndb.sqlite')
cur=con.cursor()
var  = StringVar(root)
def appoint():
    doctor.destroy()
    show=Tk()
    def book():
        
        global showinfo,doct
        showinfo("Success",'Appointment booked!')
        show.destroy()
    if docti.get() == "Physician":
        cur.execute('select * from doct')
        y=cur.fetchall()
        Label(show,text="serialno.").grid(row=1,column=0)
        Label(show,text="name.").grid(row=2,column=0)
        Label(show,text="age.").grid(row=3,column=0)
        Label(show,text="specialist").grid(row=4,column=0)
        Label(show,text="qualify.").grid(row=5,column=0)
        Label(show,text="exp.").grid(row=6,column=0)
        Label(show,text="sitting.").grid(row=7,column=0)
        Label(show,text="contact.").grid(row=8,column=0)
                
        Label(show,text=y[0][0]).grid(row=1,column=1)
        Label(show,text=y[0][1]).grid(row=2,column=1)
        Label(show,text=y[0][2]).grid(row=3,column=1)
        Label(show,text=y[0][3]).grid(row=4,column=1)
        Label(show,text=y[0][4]).grid(row=5,column=1)
        Label(show,text=y[0][5]).grid(row=6,column=1)
        Label(show,text=y[0][6]).grid(row=7,column=1)
        Label(show,text=y[0][7]).grid(row=8,column=1)

    if  docti.get() == "Surgeon":
        cur.execute('select * from doct')
        y=cur.fetchall()
        Label(show,text="serialno.").grid(row=1,column=0)
        Label(show,text="name.").grid(row=2,column=0)
        Label(show,text="age.").grid(row=3,column=0)
        Label(show,text="specialist").grid(row=4,column=0)
        Label(show,text="qualify.").grid(row=4,column=0)
        Label(show,text="exp.").grid(row=5,column=0)
        Label(show,text="sitting.").grid(row=6,column=0)
        Label(show,text="contact.").grid(row=7,column=0)
            
        Label(show,text=y[1][0]).grid(row=1,column=1)
        Label(show,text=y[1][1]).grid(row=2,column=1)
        Label(show,text=y[1][2]).grid(row=3,column=1)
        Label(show,text=y[1][3]).grid(row=4,column=1)
        Label(show,text=y[1][4]).grid(row=5,column=1)
        Label(show,text=y[1][5]).grid(row=6,column=1)
        Label(show,text=y[1][6]).grid(row=7,column=1)
        Label(show,text=y[1][7]).grid(row=8,column=1)
       
        
    if  docti.get() == "Allergist":
        cur.execute('select * from doct')
        y=cur.fetchall()
        Label(show,text="serialno.").grid(row=1,column=0)
        Label(show,text="name.").grid(row=2,column=0)
        Label(show,text="age.").grid(row=3,column=0)
        Label(show,text="specialist").grid(row=4,column=0)
        Label(show,text="qualify.").grid(row=4,column=0)
        Label(show,text="exp.").grid(row=5,column=0)
        Label(show,text="sitting.").grid(row=6,column=0)
        Label(show,text="contact.").grid(row=7,column=0)
            
        Label(show,text=y[2][0]).grid(row=1,column=1)
        Label(show,text=y[2][1]).grid(row=2,column=1)
        Label(show,text=y[2][2]).grid(row=3,column=1)
        Label(show,text=y[2][3]).grid(row=4,column=1)
        Label(show,text=y[2][4]).grid(row=5,column=1)#2
        Label(show,text=y[2][5]).grid(row=6,column=1)
        Label(show,text=y[2][6]).grid(row=7,column=1)
        Label(show,text=y[2][7]).grid(row=8,column=1)


    if  docti.get() == "Gynocologist":
        cur.execute('select * from doct')
        y=cur.fetchall()
        Label(show,text="serialno.").grid(row=1,column=0)
        Label(show,text="name.").grid(row=2,column=0)
        Label(show,text="age.").grid(row=3,column=0)
        Label(show,text="specialist").grid(row=4,column=0)
        Label(show,text="qualify.").grid(row=5,column=0)
        Label(show,text="exp.").grid(row=6,column=0)
        Label(show,text="sitting.").grid(row=7,column=0)
        Label(show,text="contact.").grid(row=8,column=0)

        Label(show,text=y[3][0]).grid(row=1,column=1)
        Label(show,text=y[3][1]).grid(row=2,column=1)
        Label(show,text=y[3][2]).grid(row=3,column=1)#3
        Label(show,text=y[3][3]).grid(row=4,column=1)
        Label(show,text=y[3][4]).grid(row=5,column=1)
        Label(show,text=y[3][5]).grid(row=6,column=1)
        Label(show,text=y[3][6]).grid(row=7,column=1)
        Label(show,text=y[3][7]).grid(row=8,column=1)


    if  docti.get() == "Cardiologist":
        cur.execute('select * from doct')
        y=cur.fetchall()
        Label(show,text="serialno.").grid(row=1,column=0)
        Label(show,text="name.").grid(row=2,column=0)
        Label(show,text="age.").grid(row=3,column=0)
        Label(show,text="specialist").grid(row=4,column=0)
        Label(show,text="qualify.").grid(row=5,column=0)
        Label(show,text="exp.").grid(row=6,column=0)
        Label(show,text="sitting.").grid(row=7,column=0)
        Label(show,text="contact.").grid(row=8,column=0)
        
        Label(show,text=y[4][0]).grid(row=1,column=1)
        Label(show,text=y[4][1]).grid(row=2,column=1)
        Label(show,text=y[4][2]).grid(row=3,column=1)
        Label(show,text=y[4][3]).grid(row=4,column=1)#4
        Label(show,text=y[4][4]).grid(row=5,column=1)
        Label(show,text=y[4][5]).grid(row=6,column=1)
        Label(show,text=y[4][6]).grid(row=7,column=1)
        Label(show,text=y[4][7]).grid(row=8,column=1)
        
    if  docti.get() == "Dentist":
        cur.execute('select * from doct')
        y=cur.fetchall()
        Label(show,text="serialno.").grid(row=1,column=0)
        Label(show,text="name.").grid(row=2,column=0)
        Label(show,text="age.").grid(row=3,column=0)
        Label(show,text="specialist").grid(row=4,column=0)
        Label(show,text="qualify.").grid(row=5,column=0)
        Label(show,text="exp.").grid(row=6,column=0)
        Label(show,text="sitting.").grid(row=7,column=0)
        Label(show,text="contact.").grid(row=8,column=0)
            
        Label(show,text=y[5][0]).grid(row=1,column=1)#5
        Label(show,text=y[5][1]).grid(row=2,column=1)
        Label(show,text=y[5][2]).grid(row=3,column=1)
        Label(show,text=y[5][3]).grid(row=4,column=1)
        Label(show,text=y[5][4]).grid(row=5,column=1)
        Label(show,text=y[5][5]).grid(row=6,column=1)
        Label(show,text=y[5][6]).grid(row=7,column=1)
        Label(show,text=y[5][7]).grid(row=8,column=1)

        
    Button(show,text="Book appointment ",fg  =  'red',font = 'times 15 bold',command =book).grid(row=9,column=0,columnspan=3)
    
    show.mainloop()
    
def inserts():
    global doct
    cur.execute("create table if not exists doct( ID INTEGER PRIMARY KEY AUTOINCREMENT ,DR_name varchar(30),age number(3),Specialist varchar(20),Qualificaton varchar(30),experience number(2) ,Sitting_time varchar(20), Contact_No number(10))")
    cur.execute("insert into doct(DR_name,age,Specialist,Qualificaton,experience,sitting_time,contact_No)values('DR.N.C Gupta', 35,'Physician','MBBS',5,'9:00Am-1:00Pm',9630670056)")
    cur.execute("insert into doct(DR_name,age,Specialist,Qualificaton,experience,sitting_time,contact_No) values('DR.Sachin Gupta',40,'Surgeon','MBBS',7,'10:00Am-2:00Pm',9685158293)")
    cur.execute("insert into doct (DR_name,age,Specialist,Qualificaton,experience,sitting_time,contact_No)values('DR.Saurav Mittal',28,'Allergist','MBBS',1,'11:00Am-2:00Pm',9210819179)")
    cur.execute("insert into doct (DR_name,age,Specialist,Qualificaton,experience,sitting_time,contact_No)values('DR.Kusum sharma',36,'Gynocologist','MBBS',4,'10:00Am-5:00Pm',9212127711)")
    cur.execute("insert into doct (DR_name,age,Specialist,Qualificaton,experience,sitting_time,contact_No)values('DR.Achraj singh',33,'Cardiologist','MBBS',6,'12:00PM-6:00Pm',9211411094)")
    cur.execute("insert into doct(DR_name,age,Specialist,Qualificaton,experience,sitting_time,contact_No) values('DR. Ankur Goyal',29,'Dentist','MBBS',0,'11:00Am-4:00Pm',7728971230)")

    
    
def inserte():
     

    
    v=[(e.get(),a.get(),b.get(),var.get(),c.get(),var1.get())]
    cur.executemany("insert into emp values(?,?,?,?,?,?)",v)
    Label(doctor,text="record created").grid(row=16,column=1)
    con.commit()
    if e.get()or a.get()or b.get()or var.get()or c.get()or var1.get() == ' ':
        tkMessageBox.showinfo('Insert','Sucessfully Inserted')
    else:
        cur.execute("Select * from emp")
        v= cur.fetchall()
        showerror('Error','Enter the  values') 
        

def sec(hospital):
    global e ,a,b,var,c,var1,docti,doctor,doct
    hospital.destroy()
    doctor=Tk()
    v2 = IntVar()
    v1  = IntVar()

    var1 = StringVar(doctor)
    var  = StringVar(doctor)
    e=Entry(doctor)
    a=Entry(doctor)
    b = Entry(doctor)
    c = Entry(doctor)
    cur.execute("create table if not exists emp(patient_id varchar(10) , name varchar(15),age number(5) ,Gender varchar(15), contact number(10), problem varchar(15))")
    doctor.title("APOLLO HOSPITAL")
    Label(doctor,text = "PATIENT DETAILS",bd = 5,font = 'times 30 bold ',fg = 'blue').grid(row = 0,column = 0,columnspan = 8)
    Label(doctor,text="Enter Patient ID",bd = 3,font = 'times 20 bold').grid(row=1,column=0)
    e.grid(row=1,column=1)
    Label(doctor,text= "Full Name",bd = 3,font='times 20 bold').grid(row = 2,column = 0)
    
    a.grid(row= 2,column =1)
    Label(doctor,text=" Age",bd = 3,font='times 20 bold').grid(row=3,column=0)
  
    b.grid(row= 3,column =1)
    Label(doctor,text="Gender",bd = 3,font='times 20 bold').grid(row=4,column=0)
    var1.set("Select you Gender")
    y =OptionMenu(doctor,var1,"Male","Female","Others").grid(row= 4,column =1)
    Label(doctor,text="Contact no:-",bd = 3,font='times 20 bold').grid(row=5,column=0)
    c.grid(row = 5,column = 1)
    Label(doctor,text ="Problem",bd = 3,font ='times 20 bold').grid(row = 6 ,column = 0)
    docti=StringVar(doctor)
    docti.set("Select")
    OptionMenu(doctor,docti,"Physician","Surgeon","Allergist","Gynocologist","Cardiologist","Dentist").grid(row  =6,column =1)    
    Button(doctor,text="Make Appointment",fg =  'red',font = 'times 15 bold',bd = 3,relief = 'ridge',command =appoint).grid(row=17,column=1)
    def show():
           n =[(e.get())]
           cur.execute("select * from emp where patient_id=(?)",(n))
           b=cur.fetchall()
           tkMessageBox.showinfo('show',b)
    def showall():
           cur.execute('select * from emp')
           l=cur.fetchall()
           Label(doctor,text="Fetch record is:")
           tkMessageBox.showinfo('showall',l)
    Button(doctor,text='INSERT',bd = 3,fg = 'purple',relief = 'ridge',command=inserte).grid(row=15,column=0)
    Button(doctor,text='SHOW',bd = 3,fg = 'purple',relief = 'ridge',command=show).grid(row=15,column=1)
    Button(doctor,text='SHOW ALL',bd = 3,fg = 'purple',relief = 'ridge',command=showall).grid(row=15,column=3)     
    doctor.mainloop()
    
def first():
    root.destroy()
    hospital=Tk()    
    hospital.title("WELCOME TO THE APOLLO HOSPITAL DELHI")
    hospital.geometry('+0+0')
    a = PhotoImage(file="apollo-home.gif")
    l=Label(hospital,image= a).grid(row =1,column =0,columnspan= 5,rowspan = 1,sticky= E+N+S+W)
    Label(hospital,text =" Apollo Hospital",fg = 'purple',font = "Arial 15 bold").grid(row = 2,column= 0,sticky = W)
    Label(hospital,text =" Email-Id:-apollohospital@gmail.com",fg = 'purple',font = "Arial 15 bold").grid(row = 4,column= 0,sticky = W)
    Label(hospital,text =" Contact No:- 011-56789455/56/58/59",fg = 'purple',font = "Arial 15 bold").grid(row = 5,column= 0,sticky = W)
    Button(hospital,text = "Click for Enter",bd= 7,bg = 'orange',font = "arial 10 bold",relief =RAISED,command=lambda:sec(hospital)).grid(row= 6,column= 2)
    hospital.mainloop()

#first window
root.title("Submission Details")    
Label(root,text = "Welcome to the Project",font = 'times 25 bold',fg='red',justify = 'center').grid(row = 0,column = 0,columnspan = 4)
Label(root,text = "Name",font = 'times 15 bold',width = 25).grid(row = 1,column = 0,sticky = W)
Label(root,text = "Richa aggarwal",font = 'times 15 bold',fg = 'blue',width = 25).grid(row = 1,column = 2,sticky = W)
Label(root,text = "Batch",font = 'times 15 bold',width = 25).grid(row = 2,column = 0,sticky = W)
Label(root,text = "B6",font = 'times 15 bold',fg = 'blue',width = 25).grid(row = 2,column = 2,sticky = W)
Label(root,text = "Enrollment no.",font = 'times 15 bold',width = 25).grid(row = 3,column = 0,sticky = W)
Label(root,text = "161B173",font = 'times 15 bold',fg = 'blue',width = 25).grid(row = 3,column = 2,sticky = W)
Label(root,text = "Email-Id",font ='times 15 bold',width = 25).grid(row = 4,column =0,sticky = W)
Label(root,text ="aggarwalricha80@gmail.com",font = 'times 15 bold',fg = 'blue',width = 25).grid(row= 4,column =2,sticky = W)
Label(root,text ="Contact No.",font ='times 15 bold',width = 25).grid(row =5,column =0,sticky = W)
Label(root,text ="9685158293",font  ='times 15 bold',fg = 'blue',width = 25).grid(row = 5,column =2,sticky = W)
Label(root,text = "Project Name",font = 'times 15 bold',width = 25).grid(row = 6,column = 0,sticky = W)
Label(root,text = "Hospital Managment",font = 'times 15 bold',fg = 'blue',width = 25).grid(row = 6,column = 2,sticky = W)
Label(root,text = "Submitted to",font = 'times 15 bold',width = 25).grid(row = 7,column = 0,sticky = W)
Label(root,text = "Dr. Mahesh Kumar",font = 'times 15 bold',fg ='blue' ,width = 25).grid(row = 7,column = 2,sticky = W)
root.after(4000,first)
root.after(00,inserts)
root.mainloop()
