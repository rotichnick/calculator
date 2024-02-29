
from tkinter import *
import ast 
i=0
def get_number(num):
    global i
    display.insert(i,num)
    i+=1

def clear_display():

    display.delete(0,END)

def display_result():
    display_string=display.get()
    try:
        #a = parser.expr(entire_string).compile()
        node = ast.parse(display_string,mode="eval")
        result = eval(compile(node,'<string>','eval'))
        clear_display()
        display.insert(0, result)
    except Exception:
        clear_display()
        display.insert(0, "Error")
root=Tk()

#display area
display=Entry(root)
display.grid(row=1, column=0, columnspan=7)

#buttons 1-9
numbers=[1,2,3,4,5,6,7,8,9]
count=0
for i in range(3):
    for y in range(3):
        button=Button(root, text=numbers[count], width=2, height=2, command=lambda text=numbers[count]:get_number(text))
        button.grid(row=i+2, column=y)
        count+=1

#adding the zero button:
zero=0
zero_button=Button(root, width=2, height=2, text=zero, command= lambda text=zero:get_number(text)).grid(row=5, column=1)

#adding the all clear (AC) button:
all_c="AC"
all_c_button=Button(root, width=2, height=2, text=all_c,command=lambda:clear_display()).grid(row=5, column=0)

#adding the equal sign (=) button:
equal="="
equal_button=Button(root, width=2, height=2, text=equal,command=display_result).grid(row=5, column=2)

#Adding the operators
operators=["+","-","*","/","%","(",")","**"]
index=0
for i in range(4):
    for y in range(2):
        if index<len(operators):
            op_button=Button(root, width=2, height=2, text=operators[index], command=lambda text=operators[index]:get_number(text))
            op_button.grid(row=i+2, column=y+3)
            index+=1
root.geometry("300x300")


root.mainloop()
