
import pandas as pd
from tkinter import *
import time

def key_up(key_event):
    global entered_password, user_data
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
    authenticate()
    save_user_data()

def key_down(key_event):
    global entered_password
    time_stamp = time.time()
    entered_password.append([key_event.char, time_stamp])  # Add key and key down time
    print("Key Down:", key_event.char)

def authenticate():
    global entered_password, model, user_data
    password = "techiscool123"
    if len(entered_password) >= len(password):
        entered_chars = [entry[0] for entry in entered_password]
        if "".join(entered_chars[-len(password):]) == password:
            print("Authentication successful!")
            user_input = [entry[2] for entry in entered_password[:-1]]  # Extract features from entered password
            authenticate_user(user_input)  # Use the trained model for authentication
        else:
            print("Authentication failed!")
        entered_password = []

def authenticate_user(user_input):
    label = model.predict([user_input])[0]
    if label == "correct_user":
        print("User authentication successful!")
    else:
        print("User authentication failed!")
        
def save_user_data():
    global user_data
    file_path = r"C:\Users\musta\OneDrive\Documents\OTU History\Second Year Uni\Spring + Summer 2023\Special Topics In Internet Of Things\keystroke-detection-project\user_data.csv"
    user_data.to_csv(file_path, index=False)

# Create an empty DataFrame to store user data
user_data = pd.DataFrame(columns=["key_down_time", "key_up_time", "time_difference", "flight_time"])

# Step 1: Initialize user data DataFrame
user_data = pd.DataFrame(columns=["key_down_time", "key_up_time", "time_difference", "flight_time"])

root = Tk()
frame = Frame(root, width=100, height=100)
frame.bind("<KeyPress>", key_down)
frame.bind("<KeyRelease>", key_up)
frame.pack()
frame.focus_set()

entered_password = []
start_time = 0.0

root.mainloop()


