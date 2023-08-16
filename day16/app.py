# GUI for face recognition


import tkinter as ttk
from tkinter import font
from tkinter import PhotoImage
app=ttk.Tk()
app.title('Attendance System')
app.geometry('600x400')
app.config(background='#590535')
#background_image = PhotoImage(file="C:\Users\Lenovo\Desktop\python AIDP\day16\dog2.png")

#background_label = ttk.Label(app, image=background_image)
#background_label.place(relwidth=1, relheight=1)
font_= font.Font(size=25)

ttk.Label(app,text='Face Recognition based Attendance System',font=font_,height=1, width=100, bg='#1e8583').pack()

def register():
    app.destroy()
    with open('opr','w') as f:
        f.write('register')

    import login_admin    

def attendance():
    print('Attendance')
    import attendance
    attendance.attendance()

def clear_data():
    app.destroy()
    with open('opr','w') as f:
        f.write('clear')
    import login_admin    

ttk.Button(app, text='Register',command=register, font=font_,height=1, width=10, bg='#1e8583').place(x=50,y=550)    
ttk.Button(app, text='Attendance',command=attendance, font=font_,height=1, width=10, bg='#1e8583').place(x=600,y=550)
ttk.Button(app, text='Clear Data',command=clear_data, font=font_,height=1, width=10, bg='#1e8583').place(x=1100,y=550)         

app.mainloop()



