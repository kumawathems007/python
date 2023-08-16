
import tkinter as ttk
from tkinter import font
from tkinter import messagebox as mb
from tkinter import PhotoImage
login_app=ttk.Tk()
login_app.title('login')
login_app.geometry('600x400')
#background_image = PhotoImage(file="faceregister.jpg")

#background_label = ttk.Label(login_app, image=background_image)
#background_label.place(relwidth=1, relheight=1)
font_=font.Font(size=15)
ttk.Label(login_app,text='Enter your credentials',font=font_,bg='#1e8583').place(x=30,y=20)
uname = ttk.Variable(login_app)
pwd = ttk.Variable(login_app)

ttk.Label(login_app,text='Username',font=font_,bg='#1e8583').place(x=30,y=200)
ttk.Entry(login_app,font=font_,textvariable=uname).place(x=200,y=200)
ttk.Label(login_app,text='Password',font=font_,bg='#1e8583').place(x=30,y=300)
ttk.Entry(login_app,font=font_,show='$',textvariable=pwd).place(x=200,y=300)

def submit():
    op=''
    with open('opr','r') as f:
        op=f.read()
    if len(op) > 0:
        userid = uname.get() 
        password = pwd.get()
        #p = open('pwd').read()
        uname.set('')
        pwd.set('')
        if userid == 'admin' and password == 'pass':
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
  

ttk.Button(login_app,text='Submit',command=submit,font=font_,width=5, height=1,bg='#1e8583').place(x=300,y=400)

def back():
    login_app.destroy()
    with open('opr','w') as f:
        f.write('')
    import app

ttk.Button(login_app,text=' <- Back',command=back,font=font_,width=7, height=1,bg='#1e8583').place(x=20,y=600)        

login_app.mainloop()
