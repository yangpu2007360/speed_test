import tkinter
from tkinter import *
from time import time
from tkinter import messagebox
import sys
import os

root = Tk()
root.geometry("600x400")

stime = time()

correct_text = "Hi My name is Pu Yang and I am a self taught programmer I am good at coding I am currently working as a software engineer in Bay Area San Francisco California USA"

correct_text_list = correct_text.split()

error = 0


def start_timer():
    global stime
    print("start counting time")
    startButton["state"] = "disabled"
    finishButton["state"] = "normal"
    inputtxt.focus_set()
    stime = time()


def calculate_st():
    etime = time()
    time_took = etime - stime
    rounded_time = round(time_took, 2)
    print(f"The time you spent to finish typing is {rounded_time}")
    finishButton["state"] = "disabled"
    inputtxt["state"] = "disabled"

    text_entered = inputtxt.get("1.0", END)
    entered_words = text_entered.split()
    number_of_words = len(text_entered.split())
    speed = round(number_of_words / rounded_time, 2)
    print(f"Your typing speed is {speed} words per second.")

    for num in range(0, len(entered_words)):
        global error
        if correct_text_list[num] != entered_words[num]:
            error = error + 1
    error_rate = round(error / len(entered_words), 2)
    print(f"Your typing error rate is {error_rate}")
    message = f"Your typing speed is {speed} words per second and Your typing error rate is {error_rate}"
    tkinter.messagebox.showinfo(title="test result", message=message)


myLabel = Label(root, text="Please type the words below", font=("Arial", 24, "bold"), pady=15)

testingLabel = Label(root, pady=10, fg='red',
                     text="Hi My name is Pu Yang and I am a self taught programmer\n I am good at coding I am currently working as a software engineer\n in Bay Area San Francisco California USA",
                     font=("Arial", 18,))


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, *sys.argv)


restartButton = Button(root, text="Restart", command=restart_program)

startButton = Button(root, text="Click when you are ready to start the test", command=start_timer)
finishButton = Button(root, text="Click here when you finished!", command=calculate_st, state=DISABLED)
inputtxt = Text(root, height=100, width=300, bg="light yellow")

myLabel.pack()
testingLabel.pack()
startButton.pack()
finishButton.pack()
restartButton.pack()
inputtxt.pack()
root.mainloop()
