from tkinter import *
import time

def key_up(key_event):
    global start_time
    print("Up", key_event.char)
    time_stamp = time.time()
    time_difference = time_stamp - start_time
    print("Time Difference:", time_difference)

def key_down(key_event):
    global start_time
    print("Down", key_event.char)
    start_time = time.time()

root = Tk()
frame = Frame(root, width=100, height=100)
frame.bind("<KeyPress>", key_down)
frame.bind("<KeyRelease>", key_up)
frame.pack()
frame.focus_set()
root.mainloop()
