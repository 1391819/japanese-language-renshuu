#!/usr/bin/python3.8
# -*-coding: utf8 -*-

# Japanese Verbs Quiz
# Last update: 13/11/2020 - Lesson 17

# Entry boxes and Text boxes
# Input boxes are known as Entry
# Output boxes are known as Text

# Import the Tkinter module
from tkinter import *
import os
import random
import time

total_verbs = "101"
last_lesson = "17"
next_lesson = "18"

# Start the root
root = Tk()

# Set the parameters for the root
root.title("Japanese Verbs Quiz")
root.geometry("800x500")

prevBtn = Button(root, text='Previous', command=lambda s=self: s.getImgOpen('prev'),
                bg='blue', fg='red').place(relx=0.85, rely=0.99, anchor=SE)


nextBtn = Button(root, text='Next', command=lambda s=self: s.getImgOpen('next'),
                bg='green', fg='black').place(relx=0.90, rely=0.99, anchor=SE)


# Sub-routine
def copy():
    temp = inputBox.get()
    output.insert(END, temp)
    inputBox.delete(0, END)

# Input box
inputBox = Entry(root, width=20, bg="light grey")
inputBox.grid(row=0, column=0, sticky=W)

# Button
Button(root, width=10, text="copy me", command = copy).grid(row=1, column=0, sticky=W)

# Output box
output = Text(root, width=20, height=5, bg="light grey")
output.grid(row=2, column=0, sticky=W)

# Kickstart the loop
root.mainloop()
