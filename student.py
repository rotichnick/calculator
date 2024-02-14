from tkinter import *
import tkinter.messagebox
import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="localhost", port="5432")
cur = conn.cursor()

def insert_data():
    name = name_e.get()
    age = age_e.get()
    address = address_e.get()
    query = '''INSERT INTO student(name, age, address) VALUES (%s, %s, %s);'''
    cur.execute(query, (name, age, address))
    conn.commit()
    tkinter.messagebox.showinfo("Data Inserted!")
    display_all()

def search_database(name):
    query = '''SELECT * FROM student where name=%s;'''
    cur.execute(query, (name,))
    row = cur.fetchone()

    if row:
        listbox=Listbox(frame, width=15, height=3)
        listbox.grid(row=7, column=1)
        listbox.insert(END,row)
    else:
        listbox=Listbox(frame, width=8, height=1, text="No data found")
        listbox.grid(row=8, column=3)
def display_all():
    query = '''SELECT * FROM student;'''
    cur.execute(query)
    row = cur.fetchall()

    
    listbox=Listbox(frame, width=20, height=10)
    listbox.grid(row=7, column=1)
    if row:

         for x in row:
             listbox.insert(END,x)
    else:
        listbox.insert(END,"Database is empty")

        
root = Tk()
canvas=Canvas(root, height=480, width=900)
canvas.pack()
frame=Frame()
frame.place(relx=0.3, rely=0.1)
title = Label(frame, text="Add Data")
title.grid(row=0, column=3)

name_l = Label(frame, text="Name: ")
name_l.grid(row=1, column=0)

name_e = Entry(frame)
name_e.grid(row=1, column=1)

age_l = Label(frame, text="Age: ")  # Fix label text
age_l.grid(row=2, column=0)

age_e = Entry(frame)
age_e.grid(row=2, column=1)

address_l = Label(frame, text="Address: ")  # Fix label text
address_l.grid(row=3, column=0)

address_e = Entry(frame)
address_e.grid(row=3, column=1)

submit = Button(frame, text="Submit", command=insert_data)
submit.grid(row=4, column=1)


search = Label(frame, text="Search by Name")
search.grid(row=5, column=1)

search_e = Entry(frame)
search_e.grid(row=6, column=1)

search_b = Button(frame, width=7, height=1, text="Find", command=lambda: search_database(search_e.get()))
search_b.grid(row=6, column=2)
display_all()


root.mainloop()
