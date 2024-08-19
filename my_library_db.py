# Import Module
from tkinter import *
from tkinter import messagebox
import json
import sys

class MyLibraryApp:
    def __init__(self, root):

        # Create the main window
        self.root = root
        self.root.title("Welcome to My Library")
        self.root.geometry('600x1000')

        # Create labels and entry fields
        self.book_txt = self.create_entry_field(root, "Book title", 10, 10, 15, 10, 50)
        self.author_txt = self.create_entry_field(root, "Book author", 10, 15, 15, 15, 50)
        self.isbn_txt = self.create_entry_field(root, "ISBN", 10, 20, 15, 20, 50)
        self.publish_txt = self.create_entry_field(root, "Publishing year", 10, 25, 15, 25, 50)

        def on_click_add_book():
            messagebox.askquestion("Confirm","Are you sure you want to add a book?")
        # Create button to add a book to the library
        self.btn_add_book = self.create_button(root, "Add Book", "green", on_click_add_book, 20, 15, 150)

        # Text field for showing library content
        self.T = Text(root, height=40, width=50)
        self.T.grid(column=15, row=200)

        def on_click_display():
            self.T.delete("1.0", END)
            self.print_library_content(sys.argv[1])
        # Create button to print current library content
        self.btn_print = self.create_button(root, "Display Library Content", "blue", on_click_display, 20, 15, 175)

    def create_entry_field(self, root, type, l_col, l_row, t_col, t_row, t_width):
        lbl = Label(root, text=type)
        lbl.grid(column=l_col, row=l_row)
        txt = Entry(root, width=t_width)
        txt.grid(column=t_col, row=t_row)
        return txt
    
    def create_button(self, root, type, color, com, width, col, row):
        btn = Button(root, text=type, fg=color, command=com, width=width)
        btn.grid(column=col, row=row)
        return btn

    def print_library_content(self, json_file):
        with open(json_file, 'r') as file:
            books=json.load(file)
        sorted_books = sorted(books['library'], key=lambda x: x['year'])
        for book in sorted_books:
            one_book = str(book['title']) + ", " + str(book['author']) + ", " + str(book['isbn']) + ", " + str(book['year'])
            self.T.insert(END, one_book + '\n')
            self.T.insert(END, '--------------------------------------------------\n')

if __name__ == "__main__":
    # create root window
    root = Tk()
    app = MyLibraryApp(root)
    root.mainloop()