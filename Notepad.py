from email.policy import default
from tkinter import *
import tkinter
from tkinter import filedialog
from zipfile import sizeEndCentDir

from mysql.connector import connect

root=tkinter.Tk()
root.geometry("500x500")
root.title("NotePad")



def back_home():
    home()
def New_data():
    f1=Frame(bg="pink")
    f1.place(x=0,width=500,height=500)
    Label(text="What You Things ...........",bg="pink",font=("comic sans ms",25)).place(x=150,y=0)

    # ============= Text Area --------------------

    def old_data():
        global content
        file = filedialog.askopenfile(mode='r', filetypes=[('text files', '*.text')])
        if file is not None:
            content = file.read()
        entry_data.insert(INSERT, content)

    def data_save():
        open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if open_file is None:
            return
        test=str(entry_data.get(1.0,END))
        open_file.write(text)
        open_file.close()



    entry_data=Text(f1,bg="white",font=("comic sans ms",15),width=40,height=14)
    entry_data.place(x=5,y=50)


    # =============== Buttons_______________

    open=Button(f1,text="Old",bg="sky blue",fg="green",width=10,font=("comic sans ms",11),cursor="hand2",relief=RAISED,borderwidth=5,command=old_data)
    open.place(x=100,y=450)

    back=Button(text="<<< ",bg="red",fg="white",font=("comic sans ms",10),cursor="hand2",command=back_home)
    back.place(x=0,y=10)

    save=Button(text="Save Me ",bg="red",fg="white",font=("comic sans ms",11),relief=RAISED,borderwidth=5,cursor="hand2",command=data_save)
    save.place(x=250,y=450)


def home():
    Frame(bg="pink").place(x=0,width=500, height=500)
    Label(text="NotePad",bg="pink",fg="green",font=("comic sans ms",25)).place(x=120,y=100)
    Button(text="New",bg="sky blue",fg="green",width=10,font=("comic sans ms",25),cursor="hand2",relief=RAISED,borderwidth=5,command=New_data).place(x=150,y=190)

home()









root.mainloop()