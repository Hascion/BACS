from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image


class APAHelpCitation:
    def __init__(self, helptab):
        self.help1 = ImageTk.PhotoImage(Image.open("images/book.png"))
        self.help2 = ImageTk.PhotoImage(Image.open("images/website.png"))
        self.help3 = ImageTk.PhotoImage(Image.open("images/journal1.png"))
        self.help4 = ImageTk.PhotoImage(Image.open("images/journal2.png"))
        self.help5 = ImageTk.PhotoImage(Image.open("images/magazine.png"))
        self.help6 = ImageTk.PhotoImage(Image.open("images/film.png"))
        self.help7 = ImageTk.PhotoImage(Image.open("images/thesis1.png"))
        self.help8 = ImageTk.PhotoImage(Image.open("images/thesis2.png"))
        self.help9 = ImageTk.PhotoImage(Image.open("images/filipino1.png"))
        self.help10 = ImageTk.PhotoImage(Image.open("images/filipino2.png"))
        self.help11 = ImageTk.PhotoImage(Image.open("images/filipino3.png"))

        self.help_list = [self.help1, self.help2, self.help3, self.help4, self.help5, self.help6, self.help7, self.help8, self.help9, self.help10, self.help11]

        self.image_show = Label(helptab, image=self.help1)
        self.image_show.grid(row=0, column=1, padx=20, pady=100)

        self.next_button = Button(helptab, text="Next ->", command=lambda: self.next(2))
        self.back_button = Button(helptab, text="<- Back", command=lambda: self.back(1), state=DISABLED)

        self.next_button.grid(row=0, column=2)
        self.back_button.grid(row=0, column=0)

    def back(self, image_number):
        self.next_button.configure(state=NORMAL)
        self.image_show.configure(image=self.help_list[image_number - 1])
        self.next_button.configure(command=lambda: self.next(image_number + 1))
        self.back_button.configure(command=lambda: self.back(image_number - 1))

        if image_number == 1:
            self.back_button.configure(state=DISABLED)
        return

    def next(self, image_number):
        self.back_button.configure(state=NORMAL)
        self.image_show.configure(image=self.help_list[image_number-1])
        self.next_button.configure(command=lambda: self.next(image_number+1))
        self.back_button.configure(command=lambda: self.back(image_number-1))

        if image_number == 11:
            self.next_button.configure(state=DISABLED)
        return
