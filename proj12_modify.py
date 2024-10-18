import mysql.connector muku likes sex
from tkinter import * 
import tkinter as tk
admin= Tk()
admin.geometry("800x800")
admin.configure(bg='pink')


label = Label(admin, text='Admin Page') 
label.pack(pady = 10)

def disable_button():
    btn2.config(state=DISABLED)

def elect(T):
 
    elect= Toplevel(admin)
    elect.title("Electoral List")
    elect.geometry("800x800")
    elect.configure(bg='pink')
    label = Label(elect, text ="Electoral List") 
    label.pack(pady = 10)
    
    if T == True:
        #enter teacher names
        label = Label(elect, text ="Teacher Electoral List") 
        label.pack(pady = 15)
        conn = mysql.connector.connect(host='localhost',user='root',password="9535245671",database='teacher_db')                     
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM teachers")
        teacher_names=cursor.fetchall()
        
        for name in teacher_names:
            button = tk.Button(elect, text=name, command=lambda n=name: print(f"Selected: {n}"))
            button.pack(padx=10, pady=5)
    else:
        label = Label(elect, text ="Student Electoral List") 
        label.pack(pady = 10)
        conn = mysql.connector.connect(host='localhost',user='root',password="9535245671",database='student_db')                     
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM students")
        student_names=cursor.fetchall()
        
        for name in student_names:
            button = tk.Button(elect, text=name, command=lambda n=name: print(f"Selected: {n}"))
            button.pack(padx=10, pady=5)
        #put buttons with voter names
        
    btn2 = Button(elect, text ="voter name", command = choice)
    btn2.pack(pady = 10)
    
    btn3 = Button(elect, text ='All Done',command = elect.destroy)
    btn3.pack(pady=10)

    
def choice():

    final= Toplevel(admin)
    final.title("Electoral List")
    final.geometry("1000x1000")
    final.configure(bg='pink')
    label = Label(final, text ="Make your choice") 
    label.pack(pady = 10)
    #insert images/ buttons
    btn3 = Button(final, text ="Done", command = final.destroy )
    btn3.pack(pady = 10)



label = Label(admin, text='Choose teacher or student') 
label.pack(pady = 10)


btnT = Button(admin, text ="Teacher Electoral List", command =lambda:elect(T=True))
btnT.pack(pady = 10)
btnS = Button(admin, text ="Student Electoral List", command =lambda:elect(T=False))
btnS.pack(pady = 10)


btn2= Button(admin,text="Close",command= admin.destroy)
btn2.pack(pady = 10)

mainloop()
