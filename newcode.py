import csv
from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    current_val = scvalue.get()

    if len(current_val)<8:
        scvalue.set(scvalue.get() + text)
        screen.update()

#method to save string
def save_to_csv():
    entry_text = screen.get()
    data = [entry_text]

    with open('output.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

root = Tk()

root.geometry('744x400')

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 20 bold")
screen.pack(fill=X, ipadx=10,pady=10,padx=10)

#creating a frame
f=Frame(root,bg='grey')
#creating buttons
b1 = Button(f,text="1",padx=8,pady=8, font="lucida 8 bold")
b1.pack(side=LEFT, padx=8,pady=8)
b1.bind("<Button-1>", click)

b2 = Button(f,text="2",padx=8,pady=8, font="lucida 8 bold")
b2.pack(side=LEFT, padx=8,pady=8)
b2.bind("<Button-1>", click)

b3 = Button(f,text="3",padx=8,pady=8, font="lucida 8 bold")
b3.pack(side=LEFT, padx=8,pady=8)
b3.bind("<Button-1>", click)

b4 = Button(f,text="4",padx=8,pady=8, font="lucida 8 bold")
b4.pack(side=LEFT, padx=8,pady=8)
b4.bind("<Button-1>", click)

b5 = Button(f,text="5",padx=8,pady=8, font="lucida 8 bold")
b5.pack(side=LEFT, padx=8,pady=8)
b5.bind("<Button-1>", click)

b6 = Button(f,text="6",padx=8,pady=8, font="lucida 8 bold")
b6.pack(side=LEFT, padx=8,pady=8)
b6.bind("<Button-1>", click)

b7 = Button(f,text="7",padx=8,pady=8, font="lucida 8 bold")
b7.pack(side=LEFT, padx=8,pady=8)
b7.bind("<Button-1>", click)

b8 = Button(f,text="8",padx=8,pady=8, font="lucida 8 bold")
b8.pack(side=LEFT, padx=8,pady=8)
b8.bind("<Button-1>", click)

b9 = Button(f,text="9",padx=8,pady=8, font="lucida 8 bold")
b9.pack(side=LEFT, padx=8,pady=8)
b9.bind("<Button-1>", click)

b0 = Button(f,text="0",padx=8,pady=8, font="lucida 8 bold")
b0.pack(side=LEFT, padx=8,pady=8)
b0.bind("<Button-1>", click)

f.pack()
#Frame 2...
ff = Frame(root,bg = 'grey')

bu = Button(ff, text="A",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(ff, text="B",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(ff, text="C",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(ff, text="D",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(ff, text="E",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(ff, text="F",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(ff, text="G",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(ff, text="H",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(ff, text="I",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(ff, text="J",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(ff, text="K",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(ff, text="L",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

ff.pack()
#Frame 3 ....
fr = Frame(root,bg='grey')

bu = Button(fr, text="M",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(fr, text="N",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(fr, text="O",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(fr, text="P",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(fr, text="Q",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(fr, text="R",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(fr, text="S",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(fr, text="T",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(fr, text="U",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(fr, text="V",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(fr, text="W",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(fr, text="X",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(fr, text="Y",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

bu = Button(fr, text="Z",padx=8,pady=8, font="lucida 8 bold")
bu.pack(side=LEFT, padx=8,pady=8)
bu.bind("<Button-1>", click)

fr.pack()
#OK button...
but = Button(root,text="Ok", background='grey',font="lucida 12", command=save_to_csv)
but.pack(padx=10,pady=10)

root.mainloop()

