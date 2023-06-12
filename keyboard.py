from tkinter import *
import time

def key_up(e):
    print("Up", e.char)
    ts = time.time()
    print(ts)

def key_down(e):
    print("down", e.char)
    ts = time.time()
    print(ts)

root = Tk()
frame = Frame(root, width = 100, height = 100)
frame.bind("<KeyPress>", key_down)
frame.bind("<KeyRelease>", key_up)
frame.pack()
frame.focus_set()
root.mainloop()
