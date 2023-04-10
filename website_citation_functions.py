from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class APAWebsiteCitation:
    def __init__(self, websitetab):
        self.author_number_website = 1
        self.corporate_author_true_website = False
        self.unknown_author_true_website = False
        self.no_day_true_website = False
        self.no_month_true_website = False
        self.no_date_true_website = False
        self.filipino_cite = False
        self.no_middle_true_website = False

        self.last_name_website = Label(websitetab, text="Last Name/Surname:", background='#58A7FA')
        self.last_name_website.grid(row=0, column=1)
        self.i_last_name_website = Entry(websitetab)
        self.i_last_name_website.grid(row=1, column=1, padx=5)

        self.first_name_website = Label(websitetab, text="First Name:", background='#58A7FA')
        self.first_name_website.grid(row=0, column=2, padx=5)
        self.i_first_name_website = Entry(websitetab)
        self.i_first_name_website.grid(row=1, column=2, padx=5)

        self.middle_initial_website = Label(websitetab, text="Middle Initial/Name:", background='#58A7FA')
        self.middle_initial_website.grid(row=0, column=3, padx=5)
        self.i_middle_initial_website = Entry(websitetab)
        self.i_middle_initial_website.grid(row=1, column=3, padx=5)

        self.corporate_author_button_website = Button(websitetab, text="Corporate Author",
                                                      command=self.corporate_author_website)
        self.corporate_author_button_website.grid(row=8, column=1, pady=5)

        self.add_author_button_website = Button(websitetab, text="Add Author", command=self.add_author_website)
        self.add_author_button_website.grid(row=8, column=2, pady=10, padx=5)

        self.unknown_author_button_website = Button(websitetab, text="Unknown Author",
                                                    command=self.unknown_author_website)
        self.unknown_author_button_website.grid(row=8, column=3, pady=5, padx=5)

        self.no_middle_button_website = Button(websitetab, text="No Middle Initial", command = self.no_middle_website)
        self.no_middle_button_website.grid(row=9, column=2, pady=5)

        self.reset_button_website = Button(websitetab, text="Reset Authors", command=self.reset_authors_website)
        self.reset_button_website.grid(row=10, column=2, pady=5)

        self.date_month_website = Label(websitetab, text="Month:", background='#58A7FA')
        self.date_month_website.grid(row=11, column=1)
        self.i_date_month_website = ttk.Combobox(websitetab,
                                                     values=["January", "February", "March", "April", "May", "June"
                                                         , "July", "August", "September", "October", "November",
                                                             "December"])
        self.i_date_month_website.grid(row=12, column=1, pady=5)

        self.i_date_month_filipino_website = ttk.Combobox(websitetab,
                                                 values=["Enero", "Pebrero", "Marso", "Abril", "Mayo", "Hunyo"
                                                     , "Hulyo", "Agosto", "Setyembre", "Oktubre", "Nobyembre",
                                                         "Disyembre"])

        self.i_date_month_filipino_website = ttk.Combobox(websitetab,
                                                           values=["Enero", "Pebrero", "Marso", "Abril", "Mayo", "Hunyo"
                                                               , "Hulyo", "Agosto", "Setyembre", "Oktubre", "Nobyembre",
                                                                   "Disyembre"])

        self.filipino_activate_button = Button(websitetab, text="Filipino Dates", command=self.filipino_activate_action)
        self.filipino_activate_button.grid(row=13, column=1, pady=5)

        self.date_day_website = Label(websitetab, text="Day (Numerical Form):", background='#58A7FA')
        self.date_day_website.grid(row=11, column=2)
        self.i_date_day_website = ttk.Combobox(websitetab,
                                                 values=["1", "2", "3", "4", "5", "6"
                                                     , "7", "8", "9", "10", "11",
                                                         "12", "13", "14", "15", "16",
                                                         "17", "18", "19", "20", "21",
                                                         "22", "23", "24", "25", "26", "27",
                                                         "28", "29", "30", "31"])
        self.i_date_day_website.grid(row=12, column=2, pady=5)

        self.date_year_website = Label(websitetab, text="Year:", background='#58A7FA')
        self.date_year_website.grid(row=11, column=3)
        self.i_date_year_website = Entry(websitetab)
        self.i_date_year_website.grid(row=12, column=3, pady=5)

        self.no_date_day_website = Button(websitetab, text="No Day", command=self.no_day_website)
        self.no_date_day_website.grid(row=13, column=2, pady=5)

        self.no_date_monthday_website = Button(websitetab, text="Year Only", command=self.no_monthday_website)
        self.no_date_monthday_website.grid(row=14, column=1, pady=5)

        self.no_all_date_button_website = Button(websitetab, text="No Date", command=self.no_date_website)
        self.no_all_date_button_website.grid(row=13, column=3, pady=5)

        self.title_website = Label(websitetab, text="Title of Website Article:", background='#58A7FA')
        self.title_website.grid(row=14, column=2, pady=5)
        self.i_title_website = Entry(websitetab)
        self.i_title_website.grid(row=15, column=2, pady=5)

        self.link_Website = Label(websitetab, text="Link:", background='#58A7FA')
        self.link_Website.grid(row=16, column=2, pady=5)
        self.i_link_website = Entry(websitetab)
        self.i_link_website.grid(row=17, column=2, pady=5, padx=220)

        self.display_output_website = Button(websitetab, text="English Cite!", command=self.website_citation)
        self.display_output_website.grid(row=18, column=1, pady=5)
        self.display_output_website_filipino = Button(websitetab, text = " Filipino Cite!", command=self.website_citation_filipino)
        self.display_output_website_filipino.grid(row=18, column=3 ,pady=5)

        self.website_citation = Label(websitetab, text="Citation:", background='#58A7FA')
        self.website_citation.grid(row=19, column=2)
        self.i_website_citation = Text(websitetab, height=5, width=50, font="times 12")
        self.i_website_citation.grid(row=20, column=2, pady=5)

        self.clear = Button(websitetab, text="Clear All Entries", command=self.clearallentries_website)
        self.clear.grid(row=24, column=2, pady=10)

        self.i_middle_initial7_website = Entry(websitetab)
        self.i_first_name7_website = Entry(websitetab)
        self.i_last_name7_website = Entry(websitetab)
        self.i_middle_initial6_website = Entry(websitetab)
        self.i_first_name6_website = Entry(websitetab)
        self.i_last_name6_website = Entry(websitetab)
        self.i_middle_initial5_website = Entry(websitetab)
        self.i_first_name5_website = Entry(websitetab)
        self.i_last_name5_website = Entry(websitetab)
        self.i_middle_initial4_website = Entry(websitetab)
        self.i_first_name4_website = Entry(websitetab)
        self.i_last_name4_website = Entry(websitetab)
        self.i_middle_initial3_website = Entry(websitetab)
        self.i_first_name3_website = Entry(websitetab)
        self.i_last_name3_website = Entry(websitetab)
        self.i_middle_initial2_website = Entry(websitetab)
        self.i_first_name2_website = Entry(websitetab)
        self.i_last_name2_website = Entry(websitetab)

    def add_author_website(self):
        self.add_author_button_website.configure(state=ACTIVE)
        self.corporate_author_button_website.configure(state=DISABLED)
        self.unknown_author_button_website.configure(state=DISABLED)
        if self.author_number_website == 1:
            self.i_last_name2_website.grid(row=2, column=1, pady=5)
            self.i_first_name2_website.grid(row=2, column=2, pady=5)
            self.i_middle_initial2_website.grid(row=2, column=3, pady=10)
            self.author_number_website += 1
            return
        elif self.author_number_website == 2:
            self.i_last_name3_website.grid(row=3, column=1, pady=5)
            self.i_first_name3_website.grid(row=3, column=2, pady=5)
            self.i_middle_initial3_website.grid(row=3, column=3, pady=5)
            self.author_number_website += 1
            return
        elif self.author_number_website == 3:
            self.i_last_name4_website.grid(row=4, column=1, pady=5)
            self.i_first_name4_website.grid(row=4, column=2, pady=5)
            self.i_middle_initial4_website.grid(row=4, column=3, pady=5)
            self.author_number_website += 1
            return
        elif self.author_number_website == 4:
            self.i_last_name5_website.grid(row=5, column=1, pady=5)
            self.i_first_name5_website.grid(row=5, column=2, pady=5)
            self.i_middle_initial5_website.grid(row=5, column=3, pady=5)
            self.author_number_website += 1
            return
        elif self.author_number_website == 5:
            self.i_last_name6_website.grid(row=6, column=1, pady=5)
            self.i_first_name6_website.grid(row=6, column=2, pady=5)
            self.i_middle_initial6_website.grid(row=6, column=3, pady=5)
            self.author_number_website += 1
            return
        elif self.author_number_website == 6:
            self.i_last_name7_website.grid(row=7, column=1, pady=5)
            self.i_first_name7_website.grid(row=7, column=2, pady=5)
            self.i_middle_initial7_website.grid(row=7, column=3, pady=5)
            self.author_number_website += 1
            return
        elif self.author_number_website == 7:
            self.response = messagebox.askquestion("Too many names!", '''
The limit of names to be placed in a citation is 7.

For works with more than 7 names please input the
last author's name into the last set of boxes.

Continue inputting citation for more than 7 authors?''')
            if self.response == "yes":
                self.author_number_website = 7
            elif self.response == "no":
                self.author_number_website = 7
                return
            self.add_author_button_website.configure(state=DISABLED)

    def reset_authors_website(self):
        self.author_number_website = 1
        self.i_last_name2_website.grid_forget()
        self.i_first_name2_website.grid_forget()
        self.i_middle_initial2_website.grid_forget()
        self.i_last_name3_website.grid_forget()
        self.i_first_name3_website.grid_forget()
        self.i_middle_initial3_website.grid_forget()
        self.i_last_name4_website.grid_forget()
        self.i_first_name4_website.grid_forget()
        self.i_middle_initial4_website.grid_forget()
        self.i_last_name5_website.grid_forget()
        self.i_first_name5_website.grid_forget()
        self.i_middle_initial5_website.grid_forget()
        self.i_last_name6_website.grid_forget()
        self.i_first_name6_website.grid_forget()
        self.i_middle_initial6_website.grid_forget()
        self.i_last_name7_website.grid_forget()
        self.i_first_name7_website.grid_forget()
        self.i_middle_initial7_website.grid_forget()

        self.corporate_author_button_website.configure(state=ACTIVE)
        self.add_author_button_website.configure(state=ACTIVE)
        self.unknown_author_button_website.configure(state=ACTIVE)

    def no_day_website(self):
        if not self.no_day_true_website:
            self.date_day_website.grid_forget()
            self.i_date_day_website.grid_forget()
            self.no_date_day_website.configure(text="With Day")
            self.no_day_true_website = True
        elif self.no_day_true_website:
            self.date_day_website.grid(row=11, column=2, pady=5)
            self.i_date_day_website.grid(row=12, column=2, pady=5)
            self.no_date_day_website.configure(text="No Day")
            self.no_day_true_website = False

    def no_monthday_website(self):
        if not self.no_month_true_website:
            self.date_month_website.grid_forget()
            self.i_date_month_website.grid_forget()
            self.i_date_month_filipino_website.grid_forget()
            self.date_day_website.grid_forget()
            self.i_date_day_website.grid_forget()
            self.no_date_day_website.configure(state=DISABLED)
            self.no_month_true_website = True
            self.no_day_true_website = True
        elif self.no_month_true_website:
            if self.filipino_cite:
                self.date_month_website.grid(row=11, column=1, pady=5)
                self.i_date_month_filipino_website.grid(row=12, column=1, pady=5)
            else:
                self.date_month_website.grid(row=11, column=1, pady=5)
                self.i_date_month_website.grid(row=12, column=1, pady=5)
            self.date_day_website.grid(row=11, column=2, pady=5)
            self.i_date_day_website.grid(row=12, column=2, pady=5)
            self.no_date_day_website.configure(state=NORMAL)
            self.no_month_true_website = False
            self.no_day_true_website = False

    def no_date_website(self):
        if not self.no_date_true_website:
            self.date_month_website.grid_forget()
            self.i_date_month_website.grid_forget()
            self.date_day_website.grid_forget()
            self.i_date_day_website.grid_forget()
            self.date_year_website.grid_forget()
            self.i_date_year_website.grid_forget()
            self.no_all_date_button_website.configure(text="With Date")
            self.no_date_day_website.configure(state=DISABLED)
            self.no_date_monthday_website.configure(state=DISABLED)
            self.no_month_true_website = True
            self.no_day_true_website = True
            self.no_date_true_website = True
            if self.filipino_cite == True:
                self.i_date_month_filipino_website.grid_forget()
        elif self.no_date_true_website:
            self.date_month_website.grid(row=11, column=1, pady=5)
            self.i_date_month_website.grid(row=12, column=1, pady=5)
            self.date_day_website.grid(row=11, column=2, pady=5)
            self.i_date_day_website.grid(row=12, column=2, pady=5)
            self.date_year_website.grid(row=11, column=3, pady=5)
            self.i_date_year_website.grid(row=12, column=3, pady=5)
            self.no_all_date_button_website.configure(text="No Date")
            self.no_date_day_website.configure(state=NORMAL)
            self.no_date_monthday_website.configure(state=NORMAL)
            if self.filipino_cite == True:
                self.i_date_month_filipino_website.grid(row=12, column=1, pady=5)
            self.no_month_true_website = False
            self.no_day_true_website = False
            self.no_date_true_website = False

    def corporate_author_website(self):
        if not self.corporate_author_true_website:
            self.last_name_website.grid_forget()
            self.middle_initial_website.grid_forget()
            self.i_last_name_website.grid_forget()
            self.i_middle_initial_website.grid_forget()
            self.first_name_website.configure(text="Corporate Author:")
            self.corporate_author_button_website.configure(text="Regular Author/s:")
            self.add_author_button_website.configure(state=DISABLED)
            self.unknown_author_button_website.configure(state=DISABLED)
            self.corporate_author_true_website = True
        elif self.corporate_author_true_website:
            self.last_name_website.grid(row=0, column=1)
            self.middle_initial_website.grid(row=0, column=3, padx=5)
            self.i_middle_initial_website.grid(row=1, column=3, padx=5)
            self.i_last_name_website.grid(row=1, column=1, padx=5)
            self.first_name_website.configure(text="First Name:")
            self.corporate_author_button_website.configure(text="Corporate Author")
            self.add_author_button_website.configure(state=NORMAL)
            self.unknown_author_button_website.configure(state=NORMAL)
            self.corporate_author_true_website = False

    def unknown_author_website(self):
        if not self.unknown_author_true_website:
            self.last_name_website.grid_forget()
            self.middle_initial_website.grid_forget()
            self.i_last_name_website.grid_forget()
            self.i_middle_initial_website.grid_forget()
            self.first_name_website.grid_forget()
            self.i_first_name_website.grid_forget()
            self.unknown_author_button_website.configure(text="With Authors")
            self.add_author_button_website.configure(state=DISABLED)
            self.corporate_author_button_website.configure(state=DISABLED)
            self.unknown_author_true_website = True
        elif self.unknown_author_true_website:
            self.first_name_website.grid(row=0, column=2, padx=5)
            self.i_first_name_website.grid(row=1, column=2, padx=5)
            self.last_name_website.grid(row=0, column=1)
            self.middle_initial_website.grid(row=0, column=3, padx=5)
            self.i_middle_initial_website.grid(row=1, column=3, padx=5)
            self.i_last_name_website.grid(row=1, column=1, padx=5)
            self.unknown_author_button_website.configure(text="No Authors")
            self.add_author_button_website.configure(state=NORMAL)
            self.corporate_author_button_website.configure(state=NORMAL)
            self.unknown_author_true_website = False

    def no_middle_website(self):
        if not self.no_middle_true_website:
            self.i_middle_initial_website.configure(state=DISABLED)
            self.i_middle_initial2_website.configure(state=DISABLED)
            self.i_middle_initial4_website.configure(state=DISABLED)
            self.i_middle_initial3_website.configure(state=DISABLED)
            self.i_middle_initial5_website.configure(state=DISABLED)
            self.i_middle_initial6_website.configure(state=DISABLED)
            self.i_middle_initial7_website.configure(state=DISABLED)
            self.no_middle_button_website.configure(text="With Middle Initial/Name")
            self.no_middle_true_website = True
        elif self.no_middle_true_website:
            self.i_middle_initial_website.configure(state=NORMAL)
            self.i_middle_initial2_website.configure(state=NORMAL)
            self.i_middle_initial4_website.configure(state=NORMAL)
            self.i_middle_initial3_website.configure(state=NORMAL)
            self.i_middle_initial5_website.configure(state=NORMAL)
            self.i_middle_initial6_website.configure(state=NORMAL)
            self.i_middle_initial7_website.configure(state=NORMAL)
            self.no_middle_button_website.configure(text="No Middle Initial/Name")
            self.no_middle_true_website = False

    def website_citation(self):
        self.nodate = "n.d."
        self.i_website_citation.delete(1.0, END)
        self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_website_citation.tag_config("title_italics", font="times 12 italic")

        # Corporate Author

        if self.corporate_author_true_website and self.author_number_website == 1:
            self.outputcorporate1 = f"{self.i_first_name_website.get()}. " \
                                    f"({self.i_date_year_website.get()}, {self.i_date_month_website.get()} {self.i_date_day_website.get()}). "
            self.outputcorporate2 = f"{self.i_title_website.get()}. "
            self.outputcorporate3 = f"Retrieved from {self.i_link_website.get()} "
            self.i_website_citation.insert(INSERT, self.outputcorporate1)
            self.i_website_citation.insert(INSERT, self.outputcorporate2, "title_italics")
            self.i_website_citation.insert(INSERT, self.outputcorporate3)

        # Corporate Author no Day

        if self.corporate_author_true_website and self.author_number_website == 1 and self.no_day_true_website and not self.unknown_author_true_website and not self.no_month_true_website \
                and not self.no_date_true_website:
            self.i_website_citation.delete(1.0, END)
            self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
            self.i_website_citation.tag_config("title_italics", font="times 12 italic")
            self.outputnoday1 = f"{self.i_first_name_website.get()}. ({self.i_date_year_website.get()}, {self.i_date_month_website.get()}). "
            self.outputnoday2 = f"{self.i_title_website.get()}. "
            self.outputnoday3 = f"Retrieved from {self.i_link_website.get()} "
            self.i_website_citation.insert(INSERT, self.outputnoday1)
            self.i_website_citation.insert(INSERT, self.outputnoday2, "title_italics")
            self.i_website_citation.insert(INSERT, self.outputnoday3)

        # Corporate Author No Month

        if self.corporate_author_true_website and self.author_number_website == 1 and self.no_month_true_website:
            self.i_website_citation.delete(1.0, END)
            self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
            self.i_website_citation.tag_config("title_italics", font="times 12 italic")
            self.outputnoyear1 = f"{self.i_first_name_website.get()}. ({self.i_date_year_website.get()}). "
            self.outputnoyear2 = f"{self.i_title_website.get()}. "
            self.outputnoyear3 = f"Retrieved from {self.i_link_website.get()} "
            self.i_website_citation.insert(INSERT, self.outputnoyear1)
            self.i_website_citation.insert(INSERT, self.outputnoyear2, "title_italics")
            self.i_website_citation.insert(INSERT, self.outputnoyear3)

        # Corporate Author No Date

        if self.corporate_author_true_website and self.author_number_website == 1 and self.no_date_true_website:
            self.i_website_citation.delete(1.0, END)
            self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
            self.i_website_citation.tag_config("title_italics", font="times 12 italic")
            self.outputcorporatenodate1 = f"{self.i_first_name_website.get()}. (n.d.). "
            self.outputcorporatenodate2 = f"{self.i_title_website.get()}. "
            self.outputcorporatenodate3 = f"Retrieved from {self.i_link_website.get()} "
            self.i_website_citation.insert(INSERT, self.outputcorporatenodate1)
            self.i_website_citation.insert(INSERT, self.outputcorporatenodate2, "title_italics")
            self.i_website_citation.insert(INSERT, self.outputcorporatenodate3)

            # NORMAL CITATIONS NO DATE

        # Unknown Author

        if self.unknown_author_true_website and self.author_number_website == 1:
            self.i_website_citation.delete(1.0, END)
            self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
            self.i_website_citation.tag_config("title_italics", font="times 12 italic")
            self.outputunknownauthor2 = f"({self.i_date_year_website.get()}, {self.i_date_month_website.get()} \
{self.i_date_day_website.get()}). "
            self.outputunknownauthor1 = f" {self.i_title_website.get()}. "
            self.outputunknownauthor3 = f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.outputunknownauthor1, "title_italics")
            self.i_website_citation.insert(INSERT, self.outputunknownauthor2)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor3)

        # unknown author no day

        if self.unknown_author_true_website and self.no_day_true_website and self.author_number_website == 1 and not \
                self.corporate_author_true_website and not self.no_month_true_website and not self.no_date_true_website:
            self.i_website_citation.delete(1.0, END)
            self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
            self.i_website_citation.tag_config("title_italics", font="times 12 italic")
            self.outputunknownauthor5 = f"({self.i_date_year_website.get()}, {self.i_date_month_website.get()}). "
            self.outputunknownauthor4 = f" {self.i_title_website.get()}. "
            self.outputunknownauthor6 = f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.outputunknownauthor4)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor5)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor6)

        # unknown author YEAR ONLY

        if self.unknown_author_true_website and self.no_month_true_website and self.author_number_website == 1:
            self.i_website_citation.delete(1.0, END)
            self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
            self.i_website_citation.tag_config("title_italics", font="times 12 italic")
            self.outputunknownauthor7 = f"({self.i_date_year_website.get()}). "
            self.outputunknownauthor8 = f"{self.i_title_website.get()}. "
            self.outputunknownauthor9 = f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.outputunknownauthor8)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor7)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor9)

        # unknown author no date

        if self.unknown_author_true_website and self.no_date_true_website and self.author_number_website == 1:
            self.i_website_citation.delete(1.0, END)
            self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
            self.i_website_citation.tag_config("title_italics", font="times 12 italic")
            self.outputunknownauthor10 = f"(n.d.) "
            self.outputunknownauthor11 = f"{self.i_title_website.get()}. "
            self.outputunknownauthor12 = f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.outputunknownauthor11)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor10)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor12)

        # NORMAL AUTHORS NO DAY
    # 1 Normal Author NO DAY
        if self.no_day_true_website and self.author_number_website == 1 and not self.no_date_true_website and not self.no_month_true_website \
        and not self.unknown_author_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.outputnormalnoday1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()}). "
            elif self.no_middle_true_website:
                self.outputnormalnoday1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()}). "
            self.outputnormalnoday2 = \
                f"{self.i_title_website.get()}. "
            self.outputnormalnoday3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.outputnormalnoday1)
            self.i_website_citation.insert(INSERT, self.outputnormalnoday2, "title_italics")
            self.i_website_citation.insert(INSERT, self.outputnormalnoday3)

    # 2 Normal Author NO DAY
        if self.no_day_true_website and self.author_number_website == 2 and not self.no_date_true_website and not self.no_month_true_website and not \
        self.unknown_author_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_day_true_website and self.author_number_website == 3 and not self.no_date_true_website and not self.no_month_true_website and not \
        self.unknown_author_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_day_true_website and self.author_number_website == 4 and not self.no_date_true_website and not self.no_month_true_website and not \
                self.unknown_author_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_day_true_website and self.author_number_website == 5 and not self.no_date_true_website and not self.no_month_true_website and not \
                self.unknown_author_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_day_true_website and self.author_number_website == 6 and not self.no_date_true_website and not self.no_month_true_website and not \
                self.unknown_author_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_day_true_website and self.author_number_website == 7 and not self.no_date_true_website and not self.no_month_true_website and not \
                self.unknown_author_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. {str(self.i_middle_initial7_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. {str(self.i_middle_initial7_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        # NORMAL CITATIONS YEAR ONLY 1 - 7

        if self.no_month_true_website and self.author_number_website == 1 and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_month_true_website and self.author_number_website == 2 and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_month_true_website and self.author_number_website == 3 and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_month_true_website and self.author_number_website == 4 and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_month_true_website and self.author_number_website == 5 and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_month_true_website and self.author_number_website == 6 and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
 f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
 {str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
 {str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
 {str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
 {str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., & \
 {str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. \
 ({self.i_date_year_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_month_true_website and self.author_number_website == 7 and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. {str(self.i_middle_initial7_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        # NORMAL CITATIONS

        if self.author_number_website == 1 and not self.no_day_true_website and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.no_month_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        elif self.author_number_website == 2 and not self.no_day_true_website and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.no_month_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
 f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., & \
 {str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. \
 ({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        elif self.author_number_website == 3 and not self.no_day_true_website and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.no_month_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        elif self.author_number_website == 4 and not self.no_day_true_website and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.no_month_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        elif self.author_number_website == 5 and not self.no_day_true_website and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.no_month_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        elif self.author_number_website == 6 and not self.no_day_true_website and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.no_month_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        elif self.author_number_website == 7 and not self.no_day_true_website and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.no_month_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. {str(self.i_middle_initial7_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        # NORMAL AUTHORS NO DATE 1 - 7

        if self.author_number_website == 1 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.author_number_website == 2 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.author_number_website == 3 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.author_number_website == 4 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.author_number_website == 5 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.author_number_website == 6 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
 f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
 {str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
 {str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
 {str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
 {str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., & \
 {str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. \
 ({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.author_number_website == 7 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. {str(self.i_middle_initial7_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Retrieved from {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

    def filipino_activate_action(self):
        if not self.filipino_cite:
            self.filipino_cite = True
            self.filipino_activate_button.configure(text="English Dates")
            self.date_month_website.configure(text="Month:")
            self.date_month_website.grid(row=11, column=1)
            self.i_date_month_website.grid_forget()
            self.i_date_month_filipino_website.grid(row=12, column=1, pady=5)
            self.display_output_website.configure(state=DISABLED)
            self.display_output_website_filipino.configure(state=NORMAL)
        elif self.filipino_cite:
            self.display_output_website.configure(state=NORMAL)
            self.display_output_website_filipino.configure(state=DISABLED)
            self.filipino_cite = False
            self.date_month_website.configure(text="Month:")
            self.date_month_website.grid(row=11, column=1)
            self.filipino_activate_button.configure(text="Filipino Dates")
            self.i_date_month_filipino_website.grid_forget()
            self.i_date_month_website.grid(row=12, column=1, pady=5)

    def website_citation_filipino(self):
        self.nodate = "n.d."
        self.i_website_citation.delete(1.0, END)
        self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_website_citation.tag_config("title_italics", font="times 12 italic")

        # Corporate Author

        if self.corporate_author_true_website and self.author_number_website == 1:
            self.outputcorporate1 = f"{self.i_first_name_website.get()}. " \
                                    f"({self.i_date_year_website.get()}, {self.i_date_month_filipino_website.get()} {self.i_date_day_website.get()}). "
            self.outputcorporate2 = f"{self.i_title_website.get()}. "
            self.outputcorporate3 = f"Kinuha mula sa {self.i_link_website.get()} "
            self.i_website_citation.insert(INSERT, self.outputcorporate1)
            self.i_website_citation.insert(INSERT, self.outputcorporate2, "title_italics")
            self.i_website_citation.insert(INSERT, self.outputcorporate3)

        # Corporate Author no Day

        if self.corporate_author_true_website and self.author_number_website == 1 and self.no_day_true_website and not self.unknown_author_true_website and not self.no_month_true_website \
                and not self.no_date_true_website:
            self.i_website_citation.delete(1.0, END)
            self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
            self.i_website_citation.tag_config("title_italics", font="times 12 italic")
            self.outputnoday1 = f"{self.i_first_name_website.get()}. ({self.i_date_year_website.get()}, {self.i_date_month_filipino_website.get()}). "
            self.outputnoday2 = f"{self.i_title_website.get()}. "
            self.outputnoday3 = f"Kinuha mula sa {self.i_link_website.get()} "
            self.i_website_citation.insert(INSERT, self.outputnoday1)
            self.i_website_citation.insert(INSERT, self.outputnoday2, "title_italics")
            self.i_website_citation.insert(INSERT, self.outputnoday3)

        # Corporate Author No Month

        if self.corporate_author_true_website and self.author_number_website == 1 and self.no_month_true_website:
            self.i_website_citation.delete(1.0, END)
            self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
            self.i_website_citation.tag_config("title_italics", font="times 12 italic")
            self.outputnoyear1 = f"{self.i_first_name_website.get()}. ({self.i_date_year_website.get()}). "
            self.outputnoyear2 = f"{self.i_title_website.get()}. "
            self.outputnoyear3 = f"Kinuha mula sa {self.i_link_website.get()} "
            self.i_website_citation.insert(INSERT, self.outputnoyear1)
            self.i_website_citation.insert(INSERT, self.outputnoyear2, "title_italics")
            self.i_website_citation.insert(INSERT, self.outputnoyear3)

        # Corporate Author No Date

        if self.corporate_author_true_website and self.author_number_website == 1 and self.no_date_true_website:
            self.i_website_citation.delete(1.0, END)
            self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
            self.i_website_citation.tag_config("title_italics", font="times 12 italic")
            self.outputcorporatenodate1 = f"{self.i_first_name_website.get()}. (n.d.). "
            self.outputcorporatenodate2 = f"{self.i_title_website.get()}. "
            self.outputcorporatenodate3 = f"Kinuha mula sa {self.i_link_website.get()} "
            self.i_website_citation.insert(INSERT, self.outputcorporatenodate1)
            self.i_website_citation.insert(INSERT, self.outputcorporatenodate2, "title_italics")
            self.i_website_citation.insert(INSERT, self.outputcorporatenodate3)

            # NORMAL CITATIONS NO DATE

        # Unknown Author

        if self.unknown_author_true_website and self.author_number_website == 1:
            self.i_website_citation.delete(1.0, END)
            self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
            self.i_website_citation.tag_config("title_italics", font="times 12 italic")
            self.outputunknownauthor1 = f"({self.i_date_year_website.get()}, {self.i_date_month_filipino_website.get()} \
{self.i_date_day_website.get()}). "
            self.outputunknownauthor2 = f"{self.i_title_website.get()}. "
            self.outputunknownauthor3 = f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.outputunknownauthor2)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor1)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor3)

        # unknown author no day

        if self.unknown_author_true_website and self.no_day_true_website and self.author_number_website == 1 and not \
                self.corporate_author_true_website and not self.no_month_true_website and not self.no_date_true_website:
            self.i_website_citation.delete(1.0, END)
            self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
            self.i_website_citation.tag_config("title_italics", font="times 12 italic")
            self.outputunknownauthor4 = f"({self.i_date_year_website.get()}, {self.i_date_month_filipino_website.get()}). "
            self.outputunknownauthor5 = f"{self.i_title_website.get()}. "
            self.outputunknownauthor6 = f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.outputunknownauthor5)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor4)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor6)

        # unknown author YEAR ONLY

        if self.unknown_author_true_website and self.no_month_true_website and self.author_number_website == 1:
            self.i_website_citation.delete(1.0, END)
            self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
            self.i_website_citation.tag_config("title_italics", font="times 12 italic")
            self.outputunknownauthor7 = f"({self.i_date_year_website.get()}). "
            self.outputunknownauthor8 = f"{self.i_title_website.get()}. "
            self.outputunknownauthor9 = f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.outputunknownauthor8)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor7)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor9)

        # unknown author no date

        if self.unknown_author_true_website and self.no_date_true_website and self.author_number_website == 1:
            self.i_website_citation.delete(1.0, END)
            self.i_website_citation.tag_add("title_italics", "1.0", "1.0 lineend")
            self.i_website_citation.tag_config("title_italics", font="times 12 italic")
            self.outputunknownauthor10 = f"(n.d.). "
            self.outputunknownauthor11 = f"{self.i_title_website.get()}. "
            self.outputunknownauthor12 = f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.outputunknownauthor11)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor10)
            self.i_website_citation.insert(INSERT, self.outputunknownauthor12)

        # NORMAL AUTHORS NO DAY

        if self.no_day_true_website and self.author_number_website == 1 and not self.no_date_true_website and not self.no_month_true_website and not \
                self.unknown_author_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.outputnormalnoday1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()}). "
            elif self.no_middle_true_website:
                self.outputnormalnoday1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()}). "
            self.outputnormalnoday2 = \
                f"{self.i_title_website.get()}. "
            self.outputnormalnoday3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.outputnormalnoday1)
            self.i_website_citation.insert(INSERT, self.outputnormalnoday2, "title_italics")
            self.i_website_citation.insert(INSERT, self.outputnormalnoday3)

        if self.no_day_true_website and self.author_number_website == 2 and not self.no_date_true_website and not self.no_month_true_website and not \
                self.unknown_author_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_day_true_website and self.author_number_website == 3 and not self.no_date_true_website and not self.no_month_true_website and not \
                self.unknown_author_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_day_true_website and self.author_number_website == 4 and not self.no_date_true_website and not self.no_month_true_website and not \
                self.unknown_author_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_day_true_website and self.author_number_website == 5 and not self.no_date_true_website and not self.no_month_true_website and not \
                self.unknown_author_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_day_true_website and self.author_number_website == 6 and not self.no_date_true_website and not self.no_month_true_website and not \
                self.unknown_author_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_day_true_website and self.author_number_website == 7 and not self.no_date_true_website and not self.no_month_true_website and not \
                self.unknown_author_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. {str(self.i_middle_initial7_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        # NORMAL CITATIONS YEAR ONLY 1 - 7

        if self.no_month_true_website and self.author_number_website == 1 and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_month_true_website and self.author_number_website == 2 and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_month_true_website and self.author_number_website == 3 and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_month_true_website and self.author_number_website == 4 and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_month_true_website and self.author_number_website == 5 and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_month_true_website and self.author_number_website == 6 and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.no_month_true_website and self.author_number_website == 7 and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. {str(self.i_middle_initial7_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. {str(self.i_middle_initial7_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        # NORMAL CITATIONS

        if self.author_number_website == 1 and not self.no_day_true_website and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.no_month_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        elif self.author_number_website == 2 and not self.no_day_true_website and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.no_month_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        elif self.author_number_website == 3 and not self.no_day_true_website and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.no_month_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        elif self.author_number_website == 4 and not self.no_day_true_website and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.no_month_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        elif self.author_number_website == 5 and not self.no_day_true_website and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.no_month_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        elif self.author_number_website == 6 and not self.no_day_true_website and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.no_month_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        elif self.author_number_website == 7 and not self.no_day_true_website and not self.no_date_true_website and not self.unknown_author_true_website \
                and not self.no_month_true_website and not self.corporate_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. {str(self.i_middle_initial7_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. \
({self.i_date_year_website.get()}, {str(self.i_date_month_filipino_website.get()).capitalize()} {self.i_date_day_website.get()}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        # NORMAL AUTHORS NO DATE 1 - 7

        if self.author_number_website == 1 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.author_number_website == 2 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.author_number_website == 3 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.author_number_website == 4 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.author_number_website == 5 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.author_number_website == 6 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}.\
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}.\
({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.author_number_website == 7 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. {str(self.i_middle_initial7_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

        if self.author_number_website == 8 and self.no_date_true_website and not self.corporate_author_true_website and not self.unknown_author_true_website:
            if not self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}. {str(self.i_middle_initial_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}. {str(self.i_middle_initial2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}. {str(self.i_middle_initial3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}. {str(self.i_middle_initial4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}. {str(self.i_middle_initial5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}. {str(self.i_middle_initial6_website.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. {str(self.i_middle_initial7_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            elif self.no_middle_true_website:
                self.output1 = \
f"{str(self.i_last_name_website.get()).capitalize()}, {str(self.i_first_name_website.get()).capitalize()[:1]}., \
{str(self.i_last_name2_website.get()).capitalize()}, {str(self.i_first_name2_website.get()).capitalize()[:1]}., \
{str(self.i_last_name3_website.get()).capitalize()}, {str(self.i_first_name3_website.get()).capitalize()[:1]}., \
{str(self.i_last_name4_website.get()).capitalize()}, {str(self.i_first_name4_website.get()).capitalize()[:1]}., \
{str(self.i_last_name5_website.get()).capitalize()}, {str(self.i_first_name5_website.get()).capitalize()[:1]}., \
{str(self.i_last_name6_website.get()).capitalize()}, {str(self.i_first_name6_website.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_website.get()).capitalize()}, {str(self.i_first_name7_website.get()).capitalize()[:1]}. \
({self.nodate}). "
            self.output2 = \
                f"{self.i_title_website.get()}. "
            self.output3 = \
                f"Kinuha mula sa {self.i_link_website.get()}"
            self.i_website_citation.insert(INSERT, self.output1)
            self.i_website_citation.insert(INSERT, self.output2, "title_italics")
            self.i_website_citation.insert(INSERT, self.output3)

    def clearallentries_website(self):
        self.i_last_name_website.delete(0, END)
        self.i_middle_initial_website.delete(0, END)
        self.i_first_name_website.delete(0, END)
        self.i_date_month_website.delete(0, END)
        self.i_date_year_website.delete(0, END)
        self.i_date_day_website.delete(0, END)
        self.i_title_website.delete(0, END)
        self.i_link_website.delete(0, END)
        self.i_website_citation.delete(1.0, END)
        if self.author_number_website >= 2:
            self.i_last_name2_website.delete(0,END)
            self.i_middle_initial2_website.delete(0, END)
            self.i_first_name2_website.delete(0, END)
            if self.author_number_website >= 3:
                self.i_last_name3_website.delete(0, END)
                self.i_middle_initial3_website.delete(0, END)
                self.i_first_name3_website.delete(0, END)
                if self.author_number_website >= 4:
                    self.i_last_name4_website.delete(0, END)
                    self.i_middle_initial4_website.delete(0, END)
                    self.i_first_name4_website.delete(0, END)
                    if self.author_number_website >= 5:
                        self.i_last_name5_website.delete(0, END)
                        self.i_middle_initial5_website.delete(0, END)
                        self.i_first_name5_website.delete(0, END)
                        if self.author_number_website >= 6:
                            self.i_last_name6_website.delete(0, END)
                            self.i_middle_initial6_website.delete(0, END)
                            self.i_first_name6_website.delete(0, END)
                            if self.author_number_website >= 7:
                                self.i_last_name7_website.delete(0, END)
                                self.i_middle_initial7_website.delete(0, END)
                                self.i_first_name7_website.delete(0, END)














