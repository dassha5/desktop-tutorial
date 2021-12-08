from tkinter import *
from data import *
from graph import graph
from table import opentable
from to_json import convertToJSON
from to_json import convertInJSON

columns = len(nounlist)
columns2 = len(nounlist2)



def openTable():
        opentable()
        root = Tk()
        root.geometry('200x100')
        root.title('Таблиця.')
        lbl = Label(root)
        lbl.configure(font=(7), text="Таблиця в консолі.")
        lbl.place(x=0, y=0)
        root.mainloop()


def toJSON():
    convertToJSON()
    root_2 = Tk()
    root_2.geometry('356x70')
    root_2.resizable(False, False)
    root.title('файл ')
    lbl = Label(root_2)
    lbl.configure(font=(8), text='Файл у форматі JSON сформовано.')
    lbl.place(x=4, y=2)
    root_2.mainloop()

def create_JSON():
    convertInJSON()
    root_3 = Tk()
    root_3.geometry('356x50')
    root_3.resizable(False, False)
    root_3.title('Повідомлення.')
    lbl = Label(root_3)
    lbl.configure(font = (10), text = 'Файл у форматі JSON сформовано.')
    lbl.place(x = 4, y = 2)
    root_3.mainloop()


def selection(event):
    searchbtn.selection_range(0, END)


root = Tk()
root.title("Аналіз руху основних засобів")
root.geometry("700x450")
btn1 = Button(root, text='Переглянути таблиці \nта зберегти у .txt', bg='#FFFFFF', fg='#5C5C64', borderwidth=0,
              command=openTable)
btn1.place(x=250, y=10, height=35, width=200)
search = StringVar()
btn2 = Button(root, text='Сформувати JSON файл таблиці \n руху основних засобів', bg='#FFFFFF', fg='#5C5C64',
              borderwidth=0, command=toJSON)
btn2.place(x=250, y=50, height=35, width=200)
btn3 = Button(root, text='Сформувати JSON файл таблиці \nдовіднику', bg='#FFFFFF', fg='#5C5C64', borderwidth=0,
              command=create_JSON)
btn3.place(x=250, y=90, height=35, width=200)
btn4 = Button(root, text='Подивитися графік', bg='#FFFFFF', fg='#5C5C64', borderwidth=0, command=graph)
btn4.place(x=250, y=130, height=35, width=200)

root.mainloop()