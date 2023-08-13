# GUI for face recognition


import tkinter as ttk
from tkinter import font
app=ttk.Tk()
app.title('Attendance System')
app.geometry('600x400')

font_= font.Font(size=15)

ttk.Label(app,text='Face Recognition based Attendance System',).pack()

def register():
    app.destroy()
    with open('opr','w') as f:
        f.write('register')

    import login_admin    

def attendance():
    print('Attendance')

def clear_data():
    app.destroy()
    with open('opr','w') as f:
        f.write('clear')
    import login_admin    

ttk.Button(app, text='Register',command=register, font=font_,height=3, width=15, bg='red').place(x=50,y=550)    
ttk.Button(app, text='Attendance',command=attendance, font=font_,height=3, width=15, bg='#0033ff').place(x=600,y=550)
ttk.Button(app, text='Clear Data',command=clear_data, font=font_,height=3, width=15, bg='red').place(x=1100,y=550)         

app.mainloop()



