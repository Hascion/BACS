from tkinter import *
from tkinter import messagebox
from ttkthemes import ThemedStyle
import tkinter as tk
from tkinter import ttk

class APABookCitation:
    def __init__(self, booktab):
        self.author_number_book = 1
        self.corporate_author_true_book = False
        self.no_author_true_book = False
        self.no_date_true_book = False
        self.no_middle_true_book = False

        self.last_name_book = Label(booktab, text="Last Name/Surname:", background="#74E1CA")
        self.last_name_book.grid()
        self.i_last_name_book = Entry(booktab)
        self.i_last_name_book.grid(row=1, column=0, padx=5)

        self.first_name_book = Label(booktab, text="First Name:", background="#74E1CA")
        self.first_name_book.grid(row=0, column=1)
        self.i_first_name_book = Entry(booktab)
        self.i_first_name_book.grid(row=1, column=1)

        self.middle_initial_book = Label(booktab, text="Middle Initial/Name:", background="#74E1CA")
        self.middle_initial_book.grid(row=0, column=2)
        self.i_middle_initial_book = Entry(booktab)
        self.i_middle_initial_book.grid(row=1, column=2, padx=5)

        self.add_author_button_book = Button(booktab, text="Add Author", command=self.add_author_book)
        self.add_author_button_book.grid(row=8, column=1, pady=10, padx=5)

        self.corporate_author_button_book = Button(booktab, text="Corporate Author", command=self.corporate_author_book)
        self.corporate_author_button_book.grid(row=8, column=0, pady=5)

        self.no_author_button_book = Button(booktab, text="Unknown Author", command=self.no_author_book)
        self.no_author_button_book.grid(row=8, column=2, pady=5)

        self.no_middle_button_book = Button(booktab, text="No Middle Initial/Name", command=self.no_middle_book)
        self.no_middle_button_book.grid(row=9, column=1, pady=5)

        self.reset_button_book = Button(booktab, text="Reset Authors", command=self.reset_authors_book)
        self.reset_button_book.grid(row=10, column=1, pady=5)

        self.year_book = Label(booktab, text="Year of Publication:", background="#74E1CA")
        self.year_book.grid(row=11, column=1, pady=5)
        self.i_year_book = Entry(booktab)
        self.i_year_book.grid(row=12, column=1, pady=5)

        self.no_date_button_book = Button(booktab, text="No Date", command=self.no_date_book)
        self.no_date_button_book.grid(row=13, column=1, pady=5)

        self.title_book = Label(booktab, text="Title of Book:", background="#74E1CA")
        self.title_book.grid(row=14, column=1)
        self.i_title_book = Entry(booktab)
        self.i_title_book.grid(row=15, column=1, pady=5)

        self.location_book = Label(booktab, text="Location of Publisher:", background="#74E1CA")
        self.location_book.grid(row=16, column=1)
        self.i_location_book = Entry(booktab)
        self.i_location_book.grid(row=17, column=1, pady=5, padx=220)

        self.publisher_book = Label(booktab, text="Name of Publisher:", background="#74E1CA")
        self.publisher_book.grid(row=18, column=1)
        self.i_publisher_book = Entry(booktab)
        self.i_publisher_book.grid(row=19, column=1, pady=5)

        self.bc = Label(booktab, text="Citation:", background="#74E1CA")
        self.bc.grid(row=21, column=1)
        self.i_bc = Text(booktab, height=5, width=50, font="times 12")
        self.i_bc.grid(row=22, column=1, pady=5)

        self.display_output_book = Button(booktab, text="Cite!", command=self.book_citation)
        self.display_output_book.grid(row=20, column=1, pady=5)

        self.clear = Button(booktab, text="Clear All Entries", command=self.clearallentries_book)
        self.clear.grid(row=24, column=1, pady=10)

        self.i_middle_initial7_book = Entry(booktab)
        self.i_first_name7_book = Entry(booktab)
        self.i_last_name7_book = Entry(booktab)
        self.i_middle_initial6_book = Entry(booktab)
        self.i_first_name6_book = Entry(booktab)
        self.i_last_name6_book = Entry(booktab)
        self.i_middle_initial5_book = Entry(booktab)
        self.i_first_name5_book = Entry(booktab)
        self.i_last_name5_book = Entry(booktab)
        self.i_middle_initial4_book = Entry(booktab)
        self.i_first_name4_book = Entry(booktab)
        self.i_last_name4_book = Entry(booktab)
        self.i_middle_initial3_book = Entry(booktab)
        self.i_first_name3_book = Entry(booktab)
        self.i_last_name3_book = Entry(booktab)
        self.i_middle_initial2_book = Entry(booktab)
        self.i_first_name2_book = Entry(booktab)
        self.i_last_name2_book = Entry(booktab)

    def corporate_author_book(self):
        if not self.corporate_author_true_book:
            self.last_name_book.grid_forget()
            self.i_last_name_book.grid_forget()
            self.middle_initial_book.grid_forget()
            self.i_middle_initial_book.grid_forget()
            self.first_name_book.configure(text="Corporate Author Name:")
            self.corporate_author_button_book.configure(text="Normal Author/s")
            self.add_author_button_book.configure(state=DISABLED)
            self.no_author_button_book.configure(state=DISABLED)
            self.corporate_author_true_book = True
            return
        elif self.corporate_author_true_book:
            self.last_name_book.grid(row=0, column=0)
            self.i_last_name_book.grid(row=1, column=0)
            self.middle_initial_book.grid(row=0, column=2)
            self.i_middle_initial_book.grid(row=1, column=2)
            self.first_name_book.configure(text="First Name:")
            self.corporate_author_button_book.configure(text="Corporate Author")
            self.add_author_button_book.configure(state=NORMAL)
            self.no_author_button_book.configure(state=NORMAL)
            self.corporate_author_true_book = False
            return

    def add_author_book(self):
        self.corporate_author_button_book.configure(state=DISABLED)
        self.no_author_button_book.configure(state=DISABLED)
        if self.author_number_book == 1:
            self.i_last_name2_book.grid(row=2, column=0, pady=10)
            self.i_first_name2_book.grid(row=2, column=1, pady=10)
            self.i_middle_initial2_book.grid(row=2, column=2, pady=10)
            self.author_number_book += 1
            return

        elif self.author_number_book == 2:
            self.i_last_name3_book.grid(row=3, column=0)
            self.i_first_name3_book.grid(row=3, column=1)
            self.i_middle_initial3_book.grid(row=3, column=2)
            self.author_number_book += 1
            return

        elif self.author_number_book == 3:
            self.i_last_name4_book.grid(row=4, column=0, pady=10)
            self.i_first_name4_book.grid(row=4, column=1, pady=10)
            self.i_middle_initial4_book.grid(row=4, column=2, pady=10)
            self.author_number_book += 1
            return

        elif self.author_number_book == 4:
            self.i_last_name5_book.grid(row=5, column=0)
            self.i_first_name5_book.grid(row=5, column=1)
            self.i_middle_initial5_book.grid(row=5, column=2)
            self.author_number_book += 1
            return

        elif self.author_number_book == 5:
            self.i_last_name6_book.grid(row=6, column=0, pady=10)
            self.i_first_name6_book.grid(row=6, column=1, pady=10)
            self.i_middle_initial6_book.grid(row=6, column=2, pady=10)
            self.author_number_book += 1
            return

        elif self.author_number_book == 6:
            self.i_last_name7_book.grid(row=7, column=0)
            self.i_first_name7_book.grid(row=7, column=1)
            self.i_middle_initial7_book.grid(row=7, column=2)
            self.author_number_book += 1
            return

        elif self.author_number_book == 7:
            self.response = messagebox.askquestion("Too many names!", '''
The limit of names to be placed in a citation is 7.

For works with more than 7 names please input the 
last author's name into the last set of boxes.

Continue inputting citation for more than 7 authors?''')
            if self.response == "yes":
                self.author_number_book += 1
            elif self.response == "no":
                self.author_number_book += 0
            self.add_author_button_book.configure(state=DISABLED)

    def no_author_book(self):
        if not self.no_author_true_book:
            self.last_name_book.grid_forget()
            self.i_last_name_book.grid_forget()
            self.first_name_book.grid_forget()
            self.i_first_name_book.grid_forget()
            self.middle_initial_book.grid_forget()
            self.i_middle_initial_book.grid_forget()
            self.no_author_button_book.configure(text="With Author/s")
            self.add_author_button_book.configure(state=DISABLED)
            self.corporate_author_button_book.configure(state=DISABLED)
            self.no_author_true_book = True
        elif self.no_author_true_book:
            self.last_name_book.grid(row=0, column=0)
            self.i_last_name_book.grid(row=1, column=0)
            self.first_name_book.grid(row=0, column=1)
            self.i_first_name_book.grid(row=1, column=1, padx=210)
            self.middle_initial_book.grid(row=0, column=2)
            self.i_middle_initial_book.grid(row=1, column=2)
            self.no_author_button_book.configure(text="Unknown Author")
            self.add_author_button_book.configure(state=NORMAL)
            self.corporate_author_button_book.configure(state=NORMAL)
            self.no_author_true_book = False

    def reset_authors_book(self):
        self.first_name_book.configure(text="First Name:")
        self.add_author_button_book.configure(state=NORMAL)
        self.corporate_author_button_book.configure(state=NORMAL)
        self.no_author_button_book.configure(state=NORMAL)
        self.corporate_author_button_book.configure(text="Corporate Author")
        self.no_author_button_book.configure(text="Unknown Author")
        self.author_number_book = 1
        self.corporate_author_true_book = False
        self.no_author_true_book = False
        self.last_name_book.grid(row=0, column=0)
        self.i_last_name_book.grid(row=1, column=0)
        self.first_name_book.grid(row=0, column=1)
        self.i_first_name_book.grid(row=1, column=1, padx=210)
        self.middle_initial_book.grid(row=0, column=2)
        self.i_middle_initial_book.grid(row=1, column=2)
        self.i_last_name2_book.grid_forget()
        self.i_first_name2_book.grid_forget()
        self.i_middle_initial2_book.grid_forget()
        self.i_last_name3_book.grid_forget()
        self.i_first_name3_book.grid_forget()
        self.i_middle_initial3_book.grid_forget()
        self.i_last_name4_book.grid_forget()
        self.i_first_name4_book.grid_forget()
        self.i_middle_initial4_book.grid_forget()
        self.i_last_name5_book.grid_forget()
        self.i_first_name5_book.grid_forget()
        self.i_middle_initial5_book.grid_forget()
        self.i_last_name6_book.grid_forget()
        self.i_first_name6_book.grid_forget()
        self.i_middle_initial6_book.grid_forget()
        self.i_last_name7_book.grid_forget()
        self.i_first_name7_book.grid_forget()
        self.i_middle_initial7_book.grid_forget()

    def no_date_book(self):
        if not self.no_date_true_book:
            self.year_book.grid_forget()
            self.i_year_book.grid_forget()
            self.no_date_button_book.configure(text="With Date")
            self.no_date_true_book = True
            self.display_output_book.configure(command=self.book_citation_nd)
        elif self.no_date_true_book:
            self.year_book.grid(row=11, column=1, pady=5)
            self.i_year_book.grid(row=12, column=1, pady=5)
            self.no_date_button_book.configure(text="No Date")
            self.no_date_true_book = False
            self.display_output_book.configure(command=self.book_citation)

    def no_middle_book(self):
        if not self.no_middle_true_book:
            self.i_middle_initial_book.configure(state=DISABLED)
            self.i_middle_initial2_book.configure(state=DISABLED)
            self.i_middle_initial4_book.configure(state=DISABLED)
            self.i_middle_initial3_book.configure(state=DISABLED)
            self.i_middle_initial5_book.configure(state=DISABLED)
            self.i_middle_initial6_book.configure(state=DISABLED)
            self.i_middle_initial7_book.configure(state=DISABLED)
            self.no_middle_button_book.configure(text="With Middle Initial/Name")
            self.no_middle_true_book = True
        elif self.no_middle_true_book:
            self.i_middle_initial_book.configure(state=NORMAL)
            self.i_middle_initial2_book.configure(state=NORMAL)
            self.i_middle_initial4_book.configure(state=NORMAL)
            self.i_middle_initial3_book.configure(state=NORMAL)
            self.i_middle_initial5_book.configure(state=NORMAL)
            self.i_middle_initial6_book.configure(state=NORMAL)
            self.i_middle_initial7_book.configure(state=NORMAL)
            self.no_middle_button_book.configure(text="No Middle Initial/Name")
            self.no_middle_true_book = False

    def book_citation(self):
        self.i_bc.delete(1.0, END)
        self.i_bc.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_bc.tag_config("title_italics", font="times 12 italic")
        if self.corporate_author_true_book and self.author_number_book == 1:
            self.output1 = f"{self.i_first_name_book.get()}. ({self.i_year_book.get()}). "
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.no_author_true_book and self.author_number_book == 1:
            self.output1 = f"{self.i_title_book.get()}. "
            self.output2 = f"({self.i_year_book.get()}). {self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1, "title_italics")
            self.i_bc.insert(INSERT, self.output2)
        elif self.author_number_book == 1:
            if not self.no_middle_true_book:
                self.output1 = f"{str(self.i_last_name_book.get()).capitalize()}, \
{str(self.i_first_name_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial_book.get()).capitalize()[:1]}. \
({self.i_year_book.get()}). "
            else:
                self.output1 = f"{str(self.i_last_name_book.get()).capitalize()}, \
{str(self.i_first_name_book.get()).capitalize()[:1]}. \
({self.i_year_book.get()}). "
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.author_number_book == 2:
            if not self.no_middle_true_book:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial_book.get()).capitalize()[:1]}. & {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. {str(self.i_middle_initial2_book.get()).capitalize()[:1]}. \
({self.i_year_book.get()}). "
            else:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}. \
& {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. \
({self.i_year_book.get()}). "
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.author_number_book == 3:
            if not self.no_middle_true_book:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}.\
{str(self.i_middle_initial_book.get()).capitalize()[:1]}., {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. {str(self.i_middle_initial2_book.get()).capitalize()[:1]}. & \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial3_book.get()).capitalize()[:1]}. ({self.i_year_book.get()}). "
            else:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}.\
, {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. & \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
({self.i_year_book.get()}). "
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.author_number_book == 4:
            if not self.no_middle_true_book:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial_book.get()).capitalize()[:1]}., {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. {str(self.i_middle_initial2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial3_book.get()).capitalize()[:1]}. & \
{self.i_last_name4_book.get()}, {str(self.i_first_name4_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial4_book.get()).capitalize()[:1]}. ({self.i_year_book.get()}). "
            else:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}.\
, {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
& \
{self.i_last_name4_book.get()}, {str(self.i_first_name4_book.get()).capitalize()[:1]}. \
({self.i_year_book.get()}). "
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.author_number_book == 5:
            if not self.no_middle_true_book:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial_book.get()).capitalize()[:1]}., {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. {str(self.i_middle_initial2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial3_book.get()).capitalize()[:1]}., {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}. {str(self.i_middle_initial4_book.get()).capitalize()[:1]}. & \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial5_book.get()).capitalize()[:1]}. ({self.i_year_book.get()}). "
            else:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}.\
, {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}.\
, {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}. & \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}. \
({self.i_year_book.get()}). "
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.author_number_book == 6:
            if not self.no_middle_true_book:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial_book.get()).capitalize()[:1]}., {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. {str(self.i_middle_initial2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial3_book.get()).capitalize()[:1]}., {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}. {str(self.i_middle_initial4_book.get()).capitalize()[:1]}., \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial5_book.get()).capitalize()[:1]}. & {self.i_last_name6_book.get()}, \
{str(self.i_first_name6_book.get()).capitalize()[:1]}. {str(self.i_middle_initial6_book.get()).capitalize()[:1]}. \
({self.i_year_book.get()}). "
            else:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}.\
, {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}.\
, {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}., \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}. \
& {self.i_last_name6_book.get()}, \
{str(self.i_first_name6_book.get()).capitalize()[:1]}. \
({self.i_year_book.get()}). "
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.author_number_book == 7:
            if not self.no_middle_true_book:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial_book.get()).capitalize()[:1]}., {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. {str(self.i_middle_initial2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial3_book.get()).capitalize()[:1]}., {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}. {str(self.i_middle_initial4_book.get()).capitalize()[:1]}., \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial5_book.get()).capitalize()[:1]}., {self.i_last_name6_book.get()}, \
{str(self.i_first_name6_book.get()).capitalize()[:1]}. {str(self.i_middle_initial6_book.get()).capitalize()[:1]}. & \
{self.i_last_name7_book.get()}, {str(self.i_first_name7_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial7_book.get()).capitalize()[:1]}. ({self.i_year_book.get()}). "
            else:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}.\
, {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}.\
, {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}., \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}.\
, {self.i_last_name6_book.get()}, \
{str(self.i_first_name6_book.get()).capitalize()[:1]}. & \
{self.i_last_name7_book.get()}, {str(self.i_first_name7_book.get()).capitalize()[:1]}. \
({self.i_year_book.get()}). "
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.author_number_book == 8:
            if not self.no_middle_true_book:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial_book.get()).capitalize()[:1]}., {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. {str(self.i_middle_initial2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial3_book.get()).capitalize()[:1]}., {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}. {str(self.i_middle_initial4_book.get()).capitalize()[:1]}., \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial5_book.get()).capitalize()[:1]}., {self.i_last_name6_book.get()}, \
{str(self.i_first_name6_book.get()).capitalize()[:1]}. {str(self.i_middle_initial6_book.get()).capitalize()[:1]}., ... \
{self.i_last_name7_book.get()}, {str(self.i_first_name7_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial7_book.get()).capitalize()[:1]}. ({self.i_year_book.get()}). "
            else:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}.\
, {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}.\
, {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}., \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}.\
, {self.i_last_name6_book.get()}, \
{str(self.i_first_name6_book.get()).capitalize()[:1]}., ... \
{self.i_last_name7_book.get()}, {str(self.i_first_name7_book.get()).capitalize()[:1]}. \
({self.i_year_book.get()}). "
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)

    def book_citation_nd(self):
        self.i_bc.delete(1.0, END)
        self.i_bc.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_bc.tag_config("title_italics", font="times 12 italic")
        if self.corporate_author_true_book and self.author_number_book == 1 and self.no_date_true_book:
            self.output1 = f"{self.i_first_name_book.get()}. (n.d.). "
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.no_author_true_book and self.author_number_book == 1 and self.no_date_true_book:
            self.output1 = f"{self.i_title_book.get()}. "
            self.output2 = f"(n.d.). {self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1, "title_italics")
            self.i_bc.insert(INSERT, self.output2)
        elif self.author_number_book == 1 and self.no_date_true_book:
            if not self.no_middle_true_book:
                self.output1 = f"{str(self.i_last_name_book.get()).capitalize()}, \
{str(self.i_first_name_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial_book.get()).capitalize()[:1]}. (n.d.).\
"
            else:
                self.output1 = f"{str(self.i_last_name_book.get()).capitalize()}, \
{str(self.i_first_name_book.get()).capitalize()[:1]}. (n.d.).\
"
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.author_number_book == 2 and self.no_date_true_book:
            if not self.no_middle_true_book:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial_book.get()).capitalize()[:1]}. & {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. {str(self.i_middle_initial2_book.get()).capitalize()[:1]}. (n.d.).\
"
            else:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}. \
& {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. (n.d.).\
"
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.author_number_book == 3 and self.no_date_true_book:
            if not self.no_middle_true_book:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}.\
{str(self.i_middle_initial_book.get()).capitalize()[:1]}., {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. {str(self.i_middle_initial2_book.get()).capitalize()[:1]}. & \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial3_book.get()).capitalize()[:1]}. (n.d.)."
            else:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}.\
, {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. & \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. (n.d.).\
"
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.author_number_book == 4 and self.no_date_true_book:
            if not self.no_middle_true_book:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial_book.get()).capitalize()[:1]}., {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. {str(self.i_middle_initial2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial3_book.get()).capitalize()[:1]}. & \
{self.i_last_name4_book.get()}, {str(self.i_first_name4_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial4_book.get()).capitalize()[:1]}. (n.d.)."
            else:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}.\
, {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
& \
{self.i_last_name4_book.get()}, {str(self.i_first_name4_book.get()).capitalize()[:1]}. (n.d.).\
"
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.author_number_book == 5 and self.no_date_true_book:
            if not self.no_middle_true_book:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial_book.get()).capitalize()[:1]}., {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. {str(self.i_middle_initial2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial3_book.get()).capitalize()[:1]}., {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}. {str(self.i_middle_initial4_book.get()).capitalize()[:1]}. & \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial5_book.get()).capitalize()[:1]}. (n.d.)."
            else:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}.\
, {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}.\
, {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}. & \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}. (n.d.).\
"
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.author_number_book == 6 and self.no_date_true_book:
            if not self.no_middle_true_book:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial_book.get()).capitalize()[:1]}., {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. {str(self.i_middle_initial2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial3_book.get()).capitalize()[:1]}., {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}. {str(self.i_middle_initial4_book.get()).capitalize()[:1]}., \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial5_book.get()).capitalize()[:1]}. & {self.i_last_name6_book.get()}, \
{str(self.i_first_name6_book.get()).capitalize()[:1]}. {str(self.i_middle_initial6_book.get()).capitalize()[:1]}. (n.d.).\
"
            else:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}.\
, {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}.\
, {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}., \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}. \
& {self.i_last_name6_book.get()}, \
{str(self.i_first_name6_book.get()).capitalize()[:1]}. (n.d.).\
"
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.author_number_book == 7 and self.no_date_true_book:
            if not self.no_middle_true_book:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial_book.get()).capitalize()[:1]}., {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. {str(self.i_middle_initial2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial3_book.get()).capitalize()[:1]}., {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}. {str(self.i_middle_initial4_book.get()).capitalize()[:1]}., \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial5_book.get()).capitalize()[:1]}., {self.i_last_name6_book.get()}, \
{str(self.i_first_name6_book.get()).capitalize()[:1]}. {str(self.i_middle_initial6_book.get()).capitalize()[:1]}. & \
{self.i_last_name7_book.get()}, {str(self.i_first_name7_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial7_book.get()).capitalize()[:1]}. (n.d.)."
            else:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}.\
, {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}.\
, {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}., \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}.\
, {self.i_last_name6_book.get()}, \
{str(self.i_first_name6_book.get()).capitalize()[:1]}. & \
{self.i_last_name7_book.get()}, {str(self.i_first_name7_book.get()).capitalize()[:1]}. (n.d.).\
"
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)
        elif self.author_number_book == 8 and self.no_date_true_book:
            if not self.no_middle_true_book:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial_book.get()).capitalize()[:1]}., {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}. {str(self.i_middle_initial2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial3_book.get()).capitalize()[:1]}., {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}. {str(self.i_middle_initial4_book.get()).capitalize()[:1]}., \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial5_book.get()).capitalize()[:1]}., {self.i_last_name6_book.get()}, \
{str(self.i_first_name6_book.get()).capitalize()[:1]}. {str(self.i_middle_initial6_book.get()).capitalize()[:1]}., ... \
{self.i_last_name7_book.get()}, {str(self.i_first_name7_book.get()).capitalize()[:1]}. \
{str(self.i_middle_initial7_book.get()).capitalize()[:1]}. (n.d.)."
            else:
                self.output1 = f"{self.i_last_name_book.get()}, {str(self.i_first_name_book.get()).capitalize()[:1]}.\
, {self.i_last_name2_book.get()}, \
{str(self.i_first_name2_book.get()).capitalize()[:1]}., \
{self.i_last_name3_book.get()}, {str(self.i_first_name3_book.get()).capitalize()[:1]}.\
, {self.i_last_name4_book.get()}, \
{str(self.i_first_name4_book.get()).capitalize()[:1]}., \
{self.i_last_name5_book.get()}, {str(self.i_first_name5_book.get()).capitalize()[:1]}.\
, {self.i_last_name6_book.get()}, \
{str(self.i_first_name6_book.get()).capitalize()[:1]}., ... \
{self.i_last_name7_book.get()}, {str(self.i_first_name7_book.get()).capitalize()[:1]}. (n.d.).\
"
            self.output2 = f"{self.i_title_book.get()}. "
            self.output3 = f"{self.i_location_book.get()} : {self.i_publisher_book.get()}"
            self.i_bc.insert(INSERT, self.output1)
            self.i_bc.insert(INSERT, self.output2, "title_italics")
            self.i_bc.insert(INSERT, self.output3)

    def clearallentries_book(self):
        self.output1 = ""
        self.output2 = ""
        self.output3 = ""
        self.i_year_book.delete(0, END)
        self.i_publisher_book.delete(0, END)
        self.i_title_book.delete(0, END)
        self.i_location_book.delete(0, END)
        self.i_first_name_book.delete(0, END)
        self.i_middle_initial_book.delete(0, END)
        self.i_last_name_book.delete(0, END)
        self.i_bc.delete(1.0, END)
        if self.author_number_book >= 2:
            self.i_last_name2_book.delete(0, END)
            self.i_first_name2_book.delete(0, END)
            self.i_middle_initial2_book.delete(0, END)
            if self.author_number_book >= 3:
                self.i_last_name3_book.delete(0, END)
                self.i_first_name3_book.delete(0, END)
                self.i_middle_initial3_book.delete(0, END)
                if self.author_number_book >= 4:
                    self.i_last_name4_book.delete(0, END)
                    self.i_first_name4_book.delete(0, END)
                    self.i_middle_initial4_book.delete(0, END)
                    if self.author_number_book >= 5:
                        self.i_last_name5_book.delete(0, END)
                        self.i_first_name5_book.delete(0, END)
                        self.i_middle_initial5_book.delete(0, END)
                        if self.author_number_book >= 6:
                            self.i_last_name6_book.delete(0, END)
                            self.i_first_name6_book.delete(0, END)
                            self.i_middle_initial6_book.delete(0, END)
                            if self.author_number_book >= 7:
                                self.i_last_name7_book.delete(0, END)
                                self.i_first_name7_book.delete(0, END)
                                self.i_middle_initial7_book.delete(0, END)
