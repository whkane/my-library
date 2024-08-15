# Import Module
from tkinter import *
from tkinter import messagebox

content = "This is the dummy content of my library!"

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to My Library")
# Set geometry (widthxheight)
root.geometry('600x1000')

# Book label and entry field
lbl = Label(root, text = "Book title")
lbl.grid(column=10, row=10)
txt = Entry(root, width=50)
txt.grid(column=15, row=10)

# Author label and entry field
lbl = Label(root, text = "Book author")
lbl.grid(column=10, row=15)
txt = Entry(root, width=50)
txt.grid(column=15, row=15)

# ISBN label and entry field
lbl = Label(root, text = "ISBN")
lbl.grid(column=10, row=20)
txt = Entry(root, width=50)
txt.grid(column=15, row=20)

# Publishing year label and entry field
lbl = Label(root, text = "Publishing year")
lbl.grid(column=10, row=25)
txt = Entry(root, width=50)
txt.grid(column=15, row=25)

# function to add a book to the library
def on_click_add_book():
    messagebox.askquestion("Confirm","Are you sure you want to add a book?")
btn_add_book = Button(root, text="Add Book",
             fg="green", command=on_click_add_book, width=20)
btn_add_book.grid(column=15, row=150)

# Text field for showing library content
T = Text(root, height=40, width=50)
T.grid(column=15, row=200)

# function to display current library content
def on_click_display():
    T.insert(END, content)
btn_display = Button(root, text="Display Library Content",
            fg="blue", command=on_click_display, width=20)
btn_display.grid(column=15, row=175)

# all widgets will be here
# Execute Tkinter
root.mainloop()
