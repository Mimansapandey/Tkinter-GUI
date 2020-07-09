from tkinter import *
box = Tk()
fr1 = Frame(box)
fr1.pack()
fr2 = Frame(box)
fr2.pack()
box.title('Shopping Window')
box.geometry('400x400')
Available_items = ['Pen','Pencil','Notebook','Eraser','Apple','Mango']
print(f'The items that are currently available are : {Available_items}')
Sell = Label(fr1, text = 'Sell', bg = 'yellow')
Sell.pack(side = 'left')
Buy = Label(fr2, text = 'Buy', bg = 'blue')
Buy.pack(side = 'left')
Selle = Entry(fr1, width = 20)
Selle.pack()
Buye = Entry(fr2, width = 20)
Buye.pack()
def buy():
    S = Buye.get()
    Buye.delete(0,END)
    Available_items.append(S)
    print(f'Heres the list of available items : {Available_items}')

def sell():
    B = Selle.get()
    Selle.delete(0,END)
    Available_items.remove(B)
    print(f'Heres the list of available items : {Available_items}')


Sellbut = Button(box, text = 'Sell', bg = 'red', fg = 'white', command = sell)
Sellbut.pack()
Buybut = Button(box, text = 'Buy', bg = 'white', fg = 'red', command = buy)
Buybut.pack()

from tkinter import messagebox

def msg():
    m = messagebox.showwarning('Do you want to quit?', 'Yes or No?')
    print(m)
    
bu = Button(box, text = 'Test Button', command = msg)
bu.pack()
box.mainloop()
