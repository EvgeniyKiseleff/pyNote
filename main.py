from tkinter import *
from tkinter.filedialog import *
import tkinter as tk

canvas = tk.Tk()
canvas.geometry("400x600")
canvas.resizable(width=True, height=True)

canvas.title("pyNote")
canvas.config(bg="white")
top = Frame(canvas)
top.pack(padx=5, pady=2, anchor="nw")

cs = "Comic Sans MS"
size = 15

def open_file():
    file = askopenfile(mode='r', filetypes=[('text files', '*.*')])
    if file is not None:
        content_note = file.read()
    entry.insert(INSERT, content_note)


def clear():
    entry.delete(1.0, END)


def note_quit():
    entry.delete(1.0, END)
    canvas.quit()


def save_file():
    new_file = asksaveasfile(mode='w', filetypes=[('text files', '.txt'), ('Python', '.py')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()


def size_plus():
    global size
    global entry
    size += 10


def size_minus():
    global size
    size += 10


b1 = Button(canvas, text="Open", bg="white", command=open_file)
b1.pack(in_=top, side=LEFT)

b2 = Button(canvas, text="Save", bg="white", command=save_file)
b2.pack(in_=top, side=LEFT)

b3 = Button(canvas, text="Clear", bg="white", command=clear)
b3.pack(in_=top, side=LEFT)

b4 = Button(canvas, text="Exit", bg="white", command=note_quit)
b4.pack(in_=top, side=LEFT)

entry = Text(canvas, wrap=WORD, bg="#FAE9B3", font=(cs, size))

entry.pack(padx=5, pady=5, expand=TRUE, fill=BOTH)

canvas.mainloop()
