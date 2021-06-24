import tkinter as tk
from tkinter import ttk

app=tk.Tk()
app.title('Vowel')

input_label=ttk.Label(app,text='Input:')
input_label.grid(row=0,column=0)

input_field_var=tk.StringVar()
input_field=ttk.Entry(app,width=30,textvariable=input_field_var)
input_field.grid(row=0,column=1)

def action():
    field=input_field_var.get()
    length=len(field)
    for i in range (length):
        if field[i]=='a' or field[i]=='e' or field[i]=='i' or field[i]=='o' or field[i]=='u':
            label1=ttk.Label(app,text=field[i])
            label1.grid(row=i+1,column=0)
        else:
            continue
bttn1=ttk.Button(app,text='Find it',command=action)
bttn1.grid(row=1,column=1)

app.mainloop()