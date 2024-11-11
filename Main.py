import re
from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import pandas as pd
from tkinter import filedialog
import matplotlib.pyplot as plt
import random

import joblib
model = joblib.load("model_RandomForest.pkl")

# Testing Data
test_df = pd.read_csv("mitbih_test.csv", header=None)
X_test = test_df.iloc[:, :186].values
y_test = test_df[187]

class Beat:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Heart Beat")
        
        # Title section
        title_lb1 = Label(text="Arrhythmia on ECG Classification", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        self.var_index = StringVar()

        # Section Creating
        main_frame = Frame(bg="white")
        main_frame.place(x=5, y=55, width=1355, height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Heart Beat", font=("verdana", 12, "bold"), fg="navyblue")
        left_frame.place(x=10, y=10, width=660, height=480)

        studentId_label = Label(left_frame, text="Test_set", font=("verdana", 12, "bold"), fg="navyblue", bg="white")
        studentId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        studentId_entry = ttk.Entry(left_frame, textvariable=self.var_index, width=15, font=("verdana", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Create a label widget with long text
        long_text = "Classes: ['N': 0, 'S': 1, 'V': 2, 'F': 3, 'Q': 4]"
        text_label = Label(left_frame, text=long_text, wraplength=300, justify='left')
        text_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        descriptions = [
            "-N : Non-ecotic beats (normal beat)",
            "-S : Supraventricular ectopic beats",
            "-V : Ventricular ectopic beats",
            "-F : Fusion Beats",
            "-Q : Unknown Beats"
        ]

        for i, desc in enumerate(descriptions, start=2):
            label = Label(left_frame, text=desc)
            label.grid(row=i, column=0, padx=5, pady=5, sticky=W)

        # Button Frame
        btn_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=10, y=390, width=635, height=60)

        save_btn = Button(btn_frame, command=self.predict, text="Predict", width=12, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        save_btn.grid(row=0, column=0, padx=6, pady=10, sticky=W)

        pt_btn = Button(btn_frame, command=self.on_button_click, text="Plot Data", width=12, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        pt_btn.grid(row=0, column=1, padx=6, pady=10, sticky=W)

        # Right Label Frame
        global right_frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="BEAT PLOT", font=("verdana", 12, "bold"), fg="navyblue")
        right_frame.place(x=680, y=10, width=660, height=480)

        self.image_label = Label(right_frame)
        self.image_label.pack(pady=10)

    def predict(self):
        index = self.var_index.get()
        index = int(index)

        # Plot
        some = X_test[index]
        plt.plot(some)
        global filename
        filename = "ex" + str(random.random()) + ".png"
        print(filename)
        plt.savefig(filename)
        plt.clf()

        some = X_test[index].reshape(1, -1)
        output = model.predict(some)

        if output[0] == 0.0:
            messagebox.showinfo("Beat", "Beat is predicted as Normal", parent=self.root)
        elif output[0] == 1.0:
            messagebox.showinfo("Beat", "Bear is predicted as Supraventricular ectopic", parent=self.root)
        elif output[0] == 2.0:
            messagebox.showinfo("Beat", "Beat is predicted as Ventricular ectopic", parent=self.root)
        elif output[0] == 3.0:
            messagebox.showinfo("Beat", "Beat is predicted as Ventricular ectopic", parent=self.root)
        elif output[0] == 4.0:
            messagebox.showinfo("Beat", "Beat is predicted as Unknown", parent=self.root)

    def on_button_click(self):
        global filename
        file_path = filename
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.photo = photo  # To prevent the image from being garbage collected

if __name__ == "__main__":
    root = Tk()
    obj = Beat(root)
    root.mainloop()