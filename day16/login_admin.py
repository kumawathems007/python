
import tkinter as ttk
from tkinter import font
from tkinter import messagebox as mb
login_app=ttk.Tk()
login_app.title('login')
login_app.geometry('600x400')
font_=font.Font(size=20)
ttk.Label(login_app,text='Enter your credentials').place(x=30,y=20)
uname = ttk.Variable(login_app)
pwd = ttk.Variable(login_app)

ttk.Label(login_app,text='Username').place(x=150,y=200)
ttk.Entry(login_app,font=font_,textvariable=uname).place(x=250,y=200)
ttk.Label(login_app,text='Password').place(x=150,y=300)
ttk.Entry(login_app,font=font_,show='$',textvariable=pwd).place(x=250,y=300)

def submit():
    op=''
    with open('opr','r') as f:
        op=f.read()
    if len(op) > 0:
        userid = uname.get() 
        password = pwd.get()
        p = open('pwd').read()
        uname.set('')
        pwd.set('')
        if userid == 'admin' and password == p:
            print('login successful')
            mb.showinfo('Success','Login Successful')

            if op == 'register':
                from tkinter.simpledialog import askstring 
                name = askstring('Name','For whom you want to register? ')
                import register_face as rf
                rf.register(name)
            elif op == 'clear':
                import clear_data   
        else:
            print('login failed')
            mb.showerror('Error','Login Failed')    
  

ttk.Button(login_app,text='Submit',font=font_,width=6, height=1).place(x=300,y=500)

def back():
    login_app.destroy()
    with open('opr','w') as f:
        f.write('')
    import app

ttk.Button(login_app,text=' <- Back',font=font_,width=6, height=1).place(x=20,y=350)        

login_app.mainloop()
