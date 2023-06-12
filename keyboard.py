# from tkinter import *
# import time

# def key_up(key_event):
    # global start_time
    # print("Up", key_event.char)
    # time_stamp = time.time()
    # time_difference = time_stamp - start_time
    # print("Time Difference:", time_difference)

# def key_down(key_event):
    # global start_time
    # print("Down", key_event.char)
    # start_time = time.time()

# root = Tk()
# frame = Frame(root, width=100, height=100)
# frame.bind("<KeyPress>", key_down)
# frame.bind("<KeyRelease>", key_up)
# frame.pack()
# frame.focus_set()
# root.mainloop()

from tkinter import *
import time

def key_up(key_event):
    global start_time, entered_password
    time_stamp = time.time()
    entered_password[-1].append(time_stamp)  # Add key up time
    time_diff = time_stamp - entered_password[-1][1]  # Calculate time difference
    entered_password[-1].append(time_diff)
    if len(entered_password) > 1:
        flight_time = time_stamp - entered_password[-2][1]  # Calculate flight time
        entered_password[-2].append(flight_time)
        print("Flight Time:", flight_time)
    print("Key Up:", key_event.char)
    print("Time Difference:", time_diff)

def key_down(key_event):
    global start_time, entered_password
    time_stamp = time.time()
    entered_password.append([key_event.char, time_stamp])  # Add key and key down time
    print("Key Down:", key_event.char)

root = Tk()
frame = Frame(root, width=100, height=100)
frame.bind("<KeyPress>", key_down)
frame.bind("<KeyRelease>", key_up)
frame.pack()
frame.focus_set()

entered_password = []
start_time = 0.0

root.mainloop()





