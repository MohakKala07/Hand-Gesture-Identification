# For GUI
import tkinter
from PIL import ImageTk, Image
from tkinter import *
from tkinter import messagebox
import snake_game
import main

# QUIT Function


def quit_window():
    if messagebox.askyesno("Quit", "You are exiting window.Do you want to quit?"):
        window.destroy()

# contact


def contact():
    messagebox._show(title="Contact Me", message="If you find you need any help contact me on 'mohakkala07@gmail.com'!")


# about
def about():
    messagebox._show(title="About", message="This Hand Gesture Identification System is designed by Mohak Kala!")


def HandGesture():
    main.HandGesture()
    mainWindow()


def SnakeGame():
    snake_game.SnakeGame()
    mainWindow()


def mainWindow():
    # Help menubar----------------------------------------------
    menubar = Menu(window)
    help = Menu(menubar, tearoff=0)
    help.add_command(label="Contact Us", command=contact)
    help.add_separator()
    help.add_command(label="Exit", command=quit_window)
    menubar.add_cascade(label="Help", menu=help)
    menubar.add_command(label="About", command=about)
    window.config(menu=menubar)
    message3 = tkinter.Label(window, text="Hand Gesture Identification", fg="white", bg="#355454", width=60, height=1,
                             font=('times', 29, ' bold '))
    message3.place(x=5, y=20, relwidth=1)

    canvas = Canvas(window, width=500, height=350)
    canvas.place(relx=0.05, rely=0.23)
    img = PhotoImage(file="C:/Users/DELL/PycharmProjects/Hand_Gesture_Identification/HandGesture.png")
    canvas.create_image(0, 0, anchor=NW, image=img)
    frame1 = tkinter.Frame(window, bg="PaleTurquoise4")
    frame1.place(relx=0.5, rely=0.23, relwidth=0.40, relheight=0.52)

    HandGestureButton = tkinter.Button(frame1, text="Hand Gesture Identification", command=HandGesture, fg="black",
                                       bg="light grey", width=60,
                                       activebackground="white", font=('times', 10, ' bold '))
    HandGestureButton.place(x=170, y=50, relwidth=0.35, relheight=0.15)

    GameButton = tkinter.Button(frame1, text="Snake Game", fg="black", command=SnakeGame, bg="light grey", width=60,
                                activebackground="white", font=('times', 10, ' bold '))
    GameButton.place(x=170, y=150, relwidth=0.35, relheight=0.15)

    quit = tkinter.Button(frame1, text="Quit", command=quit_window, fg="black", bg="light grey", width=60,
                          activebackground="white", font=('times', 10, ' bold '))
    quit.place(x=170, y=250, relwidth=0.35, relheight=0.15)

    window.protocol("WM_DELETE_WINDOW", quit_window)
    window.mainloop()

# GUI
window = tkinter.Tk()


window.title("Hand Gesture Identification")
window.geometry("1280x720")
window.resizable(True, True)
window.configure(background='#355454')
mainWindow()