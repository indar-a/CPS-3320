from tkinter import *
#this creates the window
window=Tk()

#this creates a label inside of the window
l=Label(window, text="I Am a Sample GUI Designed Using Tkinter", fg='black', font=("Courier", 12))

#this indicates where the label will be positioned in the window
l.place(x=20, y=50)

#this creates a button inside the window (clickable, but does not lead to anywhere)
b=Button(window, text="Click Me!", fg='blue', font=("Courier", 12))

#this indicates where the button will be positioned in the window
b.place(x=180, y=200)

#this creates a textbox where a user can enter information (will not execute any commands)
t=Entry(window, text="Entry Box", bd=5)

#this indicates where the textbox will be positioned in the window
t.place(x=160, y=350)

#this creates the title for the window
window.title('Sample Tkinter GUI')

#this sets the dimensions of the window
window.geometry("450x450+20+20")

#this method is used to run the code thus opening the window and display everything
#as outlined above
window.mainloop()