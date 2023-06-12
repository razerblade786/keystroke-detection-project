from tkinter import *
import time

def key_up(key_event):
    print("Up", key_event.char)
    time_stamp = time.time()
    print(time_stamp)

def key_down(key_event):
    print("down", key_event.char)
    time_stamp = time.time()
    print(time_stamp)

root = Tk()
frame = Frame(root, width = 100, height = 100)
frame.bind("<KeyPress>", key_down)
frame.bind("<KeyRelease>", key_up)
frame.pack()
frame.focus_set()
root.mainloop()
