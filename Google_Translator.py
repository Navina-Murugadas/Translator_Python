from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0, END)
    textget = change(text = msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.resizable(0,0)

backgroundImage = PhotoImage(file='blue.png')
bgLabel = Label(root, image=backgroundImage)
bgLabel.place(x=0, y=0)

lab_txt = Label(root, text="Translator", font=("Algerian",34,"bold"), bg="alice blue", fg="blue4")
lab_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=("Algerian",17,"bold"), bg="deep sky blue", fg="black")
lab_txt.place(x=140, y=120, height=20, width=220)

sor_txt = Text(frame, font=("Times New Roman",20,"bold"), wrap=WORD)
sor_txt.place(x=10, y=160, height=150, width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, value=list_text)
comb_sor.place(x=10, y=340, height=40, width=150)
comb_sor.set("English")

button_change = Button(frame,text="Translate", relief=RAISED, bg='turquoise1', command=data)
button_change.place(x=170, y=340, height=40,  width=160)

comb_dest = ttk.Combobox(frame, value=list_text)
comb_dest.place(x=340, y=340, height=40, width=150)
comb_dest.set("English")

lab_txt = Label(root, text="Output Text", font=("Algerian",17,"bold"), bg="deep sky blue", fg="black")
lab_txt.place(x=150, y=410, height=20, width=200)

dest_txt = Text(frame, font=("Times New Roman",20,"bold"), wrap=WORD)
dest_txt.place(x=10, y=450, height=150, width=480)

root.mainloop()