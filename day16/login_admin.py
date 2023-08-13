
import tkinter as ttk
from tkinter import font
login_app=ttk.Tk()
login_app.title('login')
login_app.geometry('600x400')
login_app.grid_columnconfigure(0,weight=2)
font_=font.Font(size=20)

ttk.Label(login_app,text='Enter your credentials').place(x=30,y=20)
ttk.Label(login_app,text='Usernmae').place(x=150,y=200)
ttk.Entry(login_app,font=font_).place(x=250,y=200)
ttk.Label(login_app,text='Password').place(x=150,y=300)
ttk.Entry(login_app,font=font_,show='$',textvariable=pwd ).place(x=250,y=300)

def submit():
    op=''
    with open('opr','r') as f:
        op=f.read()
    if len(op) >    
    print(op)    

ttk.Button(login_app,text='Submit',font=font_,width=10, height=2).place(x=300,y=500)

def back():
    login_app.destroy()
    with open('opr','w') as f:
        f.write('')
    import app

ttk.Button(login_app,text=' <- Back',font=font_,width=6, height=1).place(x=20,y=350)        

login_app.mainloop()
