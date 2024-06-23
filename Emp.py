from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox



def getData():
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global i
    i=data['values']
    id.set(i[1])
    name.set(i[2])
    dept.set(i[3])
    salary.set(i[4])

def DisplayAll():
    tv.delete(*tv.get_children())
    for i in fetch():
        tv.insert("",END, value=i)


def clearAll():
    id.set("")
    name.set("")
    dept.set("")
    salary.set("")


conn=sqlite3.connect('Details.db')
cursor=conn.cursor()
cursor.execute("""create table if  not exists 'Emp_details'
            (Id int primary key,Name text,Dept text,salary text)""")
conn.commit()

def insert():
    conn=sqlite3.connect('Details.db')
    cursor=conn.cursor()
    cursor.execute("""insert into 'Emp_details' values(?,?,?,?)""",
                   (str(id.get()),str(name.get()),str(dept.get()),str(salary.get())))
    conn.commit()
def add_data():
    if id.get() == "" or name.get() == "" or dept.get() == "" or salary.get() == "" :
        messagebox.showerror('error','fill all the details')
    else:
        insert()
        clearAll()
        DisplayAll()


def fetch():
    conn=sqlite3.connect('Details.db')
    cursor=conn.cursor()
    cursor.execute("select * from 'Emp_details' ")
    conn.commit()

def remove():
    conn=sqlite3.connect('Details.db')
    cursor=conn.cursor()
    cursor.execute("delete from 'Emp_details' where id=?",(id.get(),))
    conn.commit()
    clearAll()
    DisplayAll()

def update():
    conn=sqlite3.connect('Details.db')
    cursor=conn.cursor()
    cursor.execute("update 'Emp_details' set name=?,dept=?,salary=? where id=?",
                   (name.get(),dept.get(),salary.get(),id.get()))
    conn.commit()
    clearAll()
    DisplayAll()

window=Tk()
window.geometry("900x600+0+0")
window.title("practice session")
window.config(bg="black")
photo=PhotoImage(file=".venv/icon.ico")
window.iconphoto(False,photo)
# window.state("zoomed")

id=StringVar()
name=StringVar()
dept=StringVar()
salary=StringVar()

head_frame=Frame(window,bg="white")
head_frame.pack(side=TOP,fill=X,pady=20)

frame_lbl=Label(head_frame,text="SAMPLE LABEL FOR PRACTICE",font=('clibri',20,'bold'),bg="white",fg="red")
frame_lbl.grid(row=0,column=0,columnspan=4,padx=200)

main_frame=Frame(window,bg="white")
main_frame.pack(side=TOP)

id_lbl=Label(main_frame,text='ID :',bg='white',fg='red', font=('ROMAN NEW TIMES',14,'bold'))
id_lbl.grid(row=0,column=0,padx=10,pady=10)
id_entry=Entry(main_frame,font=('ROMAN NEW TIMES',14,'bold'),bd=5,textvariable=id)
id_entry.grid(row=0,column=1 ,padx=10,pady=10)

id_lbl=Label(main_frame,text='Name :',bg='white',fg='red',
             font=('ROMAN NEW TIMES',14,'bold'))
id_lbl.grid(row=0,column=2,padx=10,pady=10)
id_entry=Entry(main_frame,font=('ROMAN NEW TIMES',14,'bold'),textvariable=name,bd=5)
id_entry.grid(row=0,column=3 ,padx=10,pady=10)

id_lbl=Label(main_frame,text='Dept :',bg='white',fg='red',
             font=('ROMAN NEW TIMES',14,'bold'))
id_lbl.grid(row=1,column=0,padx=10,pady=10)
id_entry=Entry(main_frame,font=('ROMAN NEW TIMES',14,'bold'),textvariable=dept,bd=5)
id_entry.grid(row=1,column=1 ,padx=10,pady=10)

id_lbl=Label(main_frame,text='Salary :',bg='white',fg='red',
             font=('ROMAN NEW TIMES',14,'bold'))
id_lbl.grid(row=1,column=2,padx=10,pady=10)
id_entry=Entry(main_frame,font=('ROMAN NEW TIMES',14,'bold'),textvariable=salary,bd=5)
id_entry.grid(row=1,column=3 ,padx=10,pady=10)

add_btn=Button(main_frame,text='Create',command=add_data,bg='white',fg='blue',font=('ROMAN NEW TIMES',14,'bold'))
add_btn.grid(row=2,column=0,padx=10,pady=10)

retrive_btn=Button(main_frame,text='Retrive',command=fetch,bg='white',fg='blue',font=('ROMAN NEW TIMES',14,'bold'))
retrive_btn.grid(row=2,column=1,padx=10,pady=10)

update_btn=Button(main_frame,text='Update',command=update,bg='white',fg='blue',font=('ROMAN NEW TIMES',14,'bold'))
update_btn.grid(row=2,column=2,padx=10,pady=10)

delete_btn=Button(main_frame,text='Delete',command=remove,bg='white',fg='blue',font=('ROMAN NEW TIMES',14,'bold'))
delete_btn.grid(row=2,column=3,padx=10,pady=10)

clear_btn=Button(main_frame,text='Clear',command=clearAll,bg='white',fg='blue',font=('ROMAN NEW TIMES',14,'bold'))
clear_btn.grid(row=2,column=4,padx=10,pady=10)

tv_tree=Frame(window,bg='white',height=100,width=700)
tv_tree.pack(side=TOP)
style=ttk.Style()
style.configure('mystyle.Treeview.heading',font=('calibri',14,'bold'))
tv=ttk.Treeview(tv_tree,columns=(1,2,3,4),style='mystyle.Treeview')
tv.heading('1',text='ID')
tv.heading('2',text='Name')
tv.heading('3',text='Dept')
tv.heading('4',text='Salary')
tv['show']='headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

DisplayAll()


window.mainloop()