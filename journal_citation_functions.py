from tkinter import *
from tkinter import messagebox
from tkinter import ttk
# from PIL import ImageTk
# from PIL import Image


class APAJournalCitation:
    def __init__(self, journaltab):
        self.author_number_journal = 1
        self.corporate_author_true_journal = False
        self.no_author_true_journal = False
        self.no_date_true_journal = False
        self.online_true_journal = False
        self.no_month_true_journal = False
        self.no_day_true_journal = False
        self.normal_author = True
        self.filipino_cite = False
        self.no_middle_true_journal = False

        self.last_name_journal = Label(journaltab, text="Last Name/Surname:", background="#DC6ADB")
        self.last_name_journal.grid(row=0, column=0)
        self.i_last_name_journal = Entry(journaltab)
        self.i_last_name_journal.grid(row=1, column=0)

        self.first_name_journal = Label(journaltab, text="First Name:", background="#DC6ADB")
        self.first_name_journal.grid(row=0, column=1)
        self.i_first_name_journal = Entry(journaltab)
        self.i_first_name_journal.grid(row=1, column=1, padx=10)

        self.middle_initial_journal = Label(journaltab, text="Middle Initial/Name:", background="#DC6ADB")
        self.middle_initial_journal.grid(row=0, column=2)
        self.i_middle_initial_journal = Entry(journaltab)
        self.i_middle_initial_journal.grid(row=1, column=2)

        self.add_author_button_journal = Button(journaltab, text="Add Author", command=self.add_author_journal)
        self.add_author_button_journal.grid(row=8, column=1, pady=10, padx=5)

        self.corporate_author_button_journal = Button(journaltab, text="Corporate Author", command=self.corporate_author_journal)
        self.corporate_author_button_journal.grid(row=8, column=0, pady=5)

        self.no_author_button_journal = Button(journaltab, text="Unknown Author", command=self.no_author_journal)
        self.no_author_button_journal.grid(row=8, column=2, pady=5)

        self.no_middle_button_journal = Button(journaltab, text="No Middle Initial/Name", command=self.no_middle_journal)
        self.no_middle_button_journal.grid(row=9, column=1, pady=5)

        self.reset_button_journal = Button(journaltab, text="Reset Authors", command=self.reset_authors_journal)
        self.reset_button_journal.grid(row=10, column=1)

        self.month_journal = Label(journaltab, text="Month:", background="#DC6ADB")
        self.month_journal.grid(row=11, column=0)
        self.i_month_journal = ttk.Combobox(journaltab, values =["January", "February", "March", "April", "May", "June"
                     ,"July", "August", "September", "October", "November", "December"])

        self.i_month_journal_filipino = ttk.Combobox(journaltab,
                                                 values=["Enero", "Pebrero", "Marso", "Abril", "Mayo", "Hunyo"
                                                     , "Hulyo", "Agosto", "Setyembre", "Oktubre", "Nobyembre",
                                                         "Disyembre"])
        self.i_month_journal.current(1)
        self.i_month_journal.grid(row=12, column=0, pady=5)

        self.journal_filipino_month_activate = Button(journaltab, text="Filipino Months", command=self.filipino_activate_action)
        self.journal_filipino_month_activate.grid(row=14, column=0, pady=5)

        self.i_no_month_button_journal = Button(journaltab, text="Year Only", command=self.no_month_journal)
        self.i_no_month_button_journal.grid(row=13, column=0, pady=5)

        self.date_journal = Label(journaltab, text="Day: (Numerical form)", background="#DC6ADB")
        self.date_journal.grid(row=11, column=1)
        self.i_date_journal = ttk.Combobox(journaltab,
                                                 values=["1", "2", "3", "4", "5", "6"
                                                     , "7", "8", "9", "10", "11",
                                                         "12", "13", "14", "15", "16",
                                                         "17", "18", "19", "20", "21",
                                                         "22", "23", "24", "25", "26", "27",
                                                         "28", "29", "30", "31"])
        self.i_date_journal.grid(row=12, column=1, pady=5)

        self.year_journal = Label(journaltab, text="Year of Publication:", background="#DC6ADB")
        self.year_journal.grid(row=11, column=2, pady=5)
        self.i_year_journal = Entry(journaltab)
        self.i_year_journal.grid(row=12, column=2, pady=5)

        self.i_no_day_journal_button = Button(journaltab, text="No Day", command=self.no_day_journal)
        self.i_no_day_journal_button.grid(row=13, column=2, pady=5)

        self.no_date_button_journal = Button(journaltab, text="No Date", command=self.no_date_journal)
        self.no_date_button_journal.grid(row=13, column=1, pady=5)

        self.article_title_journal = Label(journaltab, text="Title of Article:", background="#DC6ADB")
        self.article_title_journal.grid(row=14, column=1)
        self.i_article_title_journal = Entry(journaltab)
        self.i_article_title_journal.grid(row=15, column=1, pady=5)

        self.periodical_title_journal = Label(journaltab, text="Title of Periodical:", background="#DC6ADB")
        self.periodical_title_journal.grid(row=16, column=1)
        self.i_periodical_title_journal = Entry(journaltab)
        self.i_periodical_title_journal.grid(row=17, column=1, pady=5, padx=220)

        self.volume_number_journal = Label(journaltab, text="Volume Number:", background="#DC6ADB")
        self.volume_number_journal.grid(row=18, column=0)
        self.i_volume_number_journal = Entry(journaltab)
        self.i_volume_number_journal.grid(row=19, column=0, pady=5)

        self.issue_number_journal = Label(journaltab, text="Issue Number:", background="#DC6ADB")
        self.issue_number_journal.grid(row=18, column=1)
        self.i_issue_number_journal = Entry(journaltab)
        self.i_issue_number_journal.grid(row=19, column=1, pady=5)

        self.page_number_journal = Label(journaltab, text='''Page Number/s:''', background="#DC6ADB")
        self.page_number_journal.grid(row=18, column=2)
        self.i_page_number_journal = Entry(journaltab)
        self.i_page_number_journal.grid(row=19, column=2, pady=5)

        self.i_middle_initial7_journal = Entry(journaltab)
        self.i_first_name7_journal = Entry(journaltab)
        self.i_last_name7_journal = Entry(journaltab)
        self.i_middle_initial6_journal = Entry(journaltab)
        self.i_first_name6_journal = Entry(journaltab)
        self.i_last_name6_journal = Entry(journaltab)
        self.i_middle_initial5_journal = Entry(journaltab)
        self.i_first_name5_journal = Entry(journaltab)
        self.i_last_name5_journal = Entry(journaltab)
        self.i_middle_initial4_journal = Entry(journaltab)
        self.i_first_name4_journal = Entry(journaltab)
        self.i_last_name4_journal = Entry(journaltab)
        self.i_middle_initial3_journal = Entry(journaltab)
        self.i_first_name3_journal = Entry(journaltab)
        self.i_last_name3_journal = Entry(journaltab)
        self.i_middle_initial2_journal = Entry(journaltab)
        self.i_first_name2_journal = Entry(journaltab)
        self.i_last_name2_journal = Entry(journaltab)

        self.display_output_journal = Button(journaltab, text="Cite!", command=self.printed_journal_citation)
        self.display_output_journal.grid(row=23, column=1, pady=5)

        self.online_button_journal = Button(journaltab, text="Online Journal", command=self.online_journal)
        self.online_button_journal.grid(row=20, column=1, pady=10)

        self.doi_link_journal = Label(journaltab, text="D.O.I./Link:", background="#DC6ADB")
        self.i_doi_link_journal = Entry(journaltab)

        self.jn = Label(journaltab, text="Citation:", background="#DC6ADB")
        self.jn.grid(row=24, column=1)
        self.i_jn = Text(journaltab, height=5, width=50, font="times 12")
        self.i_jn.grid(row=25, column=1, pady=5)

        self.clear = Button(journaltab, text="Clear All Entries", command=self.clearallentries_journal)
        self.clear.grid(row=26, column=1, pady=10)

    def add_author_journal(self):
        self.corporate_author_button_journal.configure(state=DISABLED)
        self.no_author_button_journal.configure(state=DISABLED)
        if self.author_number_journal == 1:
            self.i_last_name2_journal.grid(row=2, column=0, pady=10)
            self.i_first_name2_journal.grid(row=2, column=1, pady=10)
            self.i_middle_initial2_journal.grid(row=2, column=2, pady=10)
            self.author_number_journal += 1
            return

        elif self.author_number_journal == 2:
            self.i_last_name3_journal.grid(row=3, column=0)
            self.i_first_name3_journal.grid(row=3, column=1)
            self.i_middle_initial3_journal.grid(row=3, column=2)
            self.author_number_journal += 1
            return

        elif self.author_number_journal == 3:
            self.i_last_name4_journal.grid(row=4, column=0, pady=10)
            self.i_first_name4_journal.grid(row=4, column=1, pady=10)
            self.i_middle_initial4_journal.grid(row=4, column=2, pady=10)
            self.author_number_journal += 1
            return

        elif self.author_number_journal == 4:
            self.i_last_name5_journal.grid(row=5, column=0)
            self.i_first_name5_journal.grid(row=5, column=1)
            self.i_middle_initial5_journal.grid(row=5, column=2)
            self.author_number_journal += 1
            return

        elif self.author_number_journal == 5:
            self.i_last_name6_journal.grid(row=6, column=0, pady=10)
            self.i_first_name6_journal.grid(row=6, column=1, pady=10)
            self.i_middle_initial6_journal.grid(row=6, column=2, pady=10)
            self.author_number_journal += 1
            return

        elif self.author_number_journal == 6:
            self.i_last_name7_journal.grid(row=7, column=0)
            self.i_first_name7_journal.grid(row=7, column=1)
            self.i_middle_initial7_journal.grid(row=7, column=2)
            self.author_number_journal += 1
            return

        elif self.author_number_journal == 7:
            self.response = messagebox.askquestion("Too many names!", '''
            The limit of names to be placed in a citation is 7.

            For works with more than 7 names please input the
            last author's name into the last set of boxes.

            Continue inputting citation for more than 7 authors?''')
            if self.response == "yes":
                self.author_number_journal += 1
            elif self.response == "no":
                self.author_number_journal -= 1
            self.add_author_button_journal.configure(state=DISABLED)

    def corporate_author_journal(self):
        if not self.corporate_author_true_journal:
            self.last_name_journal.grid_forget()
            self.i_last_name_journal.grid_forget()
            self.middle_initial_journal.grid_forget()
            self.i_middle_initial_journal.grid_forget()
            self.first_name_journal.configure(text="Corporate Author Name:")
            self.corporate_author_button_journal.configure(text="Normal Author/s")
            self.add_author_button_journal.configure(state=DISABLED)
            self.no_author_button_journal.configure(state=DISABLED)
            self.corporate_author_true_journal = True
            self.normal_author = False
        elif self.corporate_author_true_journal:
            self.last_name_journal.grid(row=0, column=0)
            self.i_last_name_journal.grid(row=1, column=0)
            self.middle_initial_journal.grid(row=0, column=2)
            self.i_middle_initial_journal.grid(row=1, column=2)
            self.first_name_journal.configure(text="First Name:")
            self.corporate_author_button_journal.configure(text="Corporate Author")
            self.add_author_button_journal.configure(state=NORMAL)
            self.no_author_button_journal.configure(state=NORMAL)
            self.corporate_author_true_journal = False
            self.normal_author = True

    def no_author_journal(self):
        if not self.no_author_true_journal:
            self.last_name_journal.grid_forget()
            self.i_last_name_journal.grid_forget()
            self.first_name_journal.grid_forget()
            self.i_first_name_journal.grid_forget()
            self.middle_initial_journal.grid_forget()
            self.i_middle_initial_journal.grid_forget()
            self.no_author_button_journal.configure(text="With Author/s")
            self.add_author_button_journal.configure(state=DISABLED)
            self.corporate_author_button_journal.configure(state=DISABLED)
            self.no_author_true_journal = True
            self.normal_author = False
        elif self.no_author_true_journal:
            self.last_name_journal.grid(row=0, column=0)
            self.i_last_name_journal.grid(row=1, column=0)
            self.first_name_journal.grid(row=0, column=1)
            self.i_first_name_journal.grid(row=1, column=1, padx=10)
            self.middle_initial_journal.grid(row=0, column=2)
            self.i_middle_initial_journal.grid(row=1, column=2)
            self.no_author_button_journal.configure(text="Unknown Author")
            self.add_author_button_journal.configure(state=NORMAL)
            self.corporate_author_button_journal.configure(state=NORMAL)
            self.no_author_true_journal = False
            self.normal_author = True

    def no_month_journal(self):
        if not self.no_month_true_journal:
            self.i_month_journal.grid_forget()
            self.i_date_journal.grid_forget()
            self.month_journal.grid_forget()
            self.date_journal.grid_forget()
            self.i_no_month_button_journal.configure(text="With Month")
            self.i_no_day_journal_button.configure(text="With Day")
            self.i_no_day_journal_button.configure(state=DISABLED)
            self.no_month_true_journal = True
            self.no_day_true_journal = True
            if self.filipino_cite:
                self.i_month_journal_filipino.grid_forget()
        elif self.no_month_true_journal:
            self.i_month_journal.grid(row=12, column=0, pady=5)
            self.i_date_journal.grid(row=12, column=1, pady=5)
            self.month_journal.grid(row=11, column=0)
            self.date_journal.grid(row=11, column=1)
            self.i_no_day_journal_button.configure(state=NORMAL)
            self.i_no_month_button_journal.configure(text="Year Only")
            self.i_no_day_journal_button.configure(text="No Day")
            self.no_month_true_journal = False
            self.no_day_true_journal = False
            if self.filipino_cite:
                self.i_month_journal_filipino.grid(row=12, column=0)

    def no_day_journal(self):
        if not self.no_day_true_journal:
            self.no_day_true_journal = True
            self.i_date_journal.grid_forget()
            self.date_journal.grid_forget()
            self.i_no_day_journal_button.configure(text="With Day")

        elif self.no_day_true_journal:
            self.no_day_true_journal = False
            self.i_date_journal.grid(row=12, column=1, pady=5)
            self.date_journal.grid(row=11, column=1)
            self.i_no_day_journal_button.configure(text="No Day")

    def reset_authors_journal(self):
        self.first_name_journal.configure(text="First Name:")
        self.add_author_button_journal.configure(state=NORMAL)
        self.corporate_author_button_journal.configure(state=NORMAL)
        self.no_author_button_journal.configure(state=NORMAL)
        self.corporate_author_button_journal.configure(text="Corporate Author")
        self.no_author_button_journal.configure(text="Unknown Author")
        self.author_number_journal = 1
        self.corporate_author_true_journal = False
        self.no_author_true_journal = False
        self.last_name_journal.grid(row=0, column=0)
        self.i_last_name_journal.grid(row=1, column=0)
        self.first_name_journal.grid(row=0, column=1)
        self.i_first_name_journal.grid(row=1, column=1, padx=10)
        self.middle_initial_journal.grid(row=0, column=2)
        self.i_middle_initial_journal.grid(row=1, column=2)
        self.i_last_name2_journal.grid_forget()
        self.i_first_name2_journal.grid_forget()
        self.i_middle_initial2_journal.grid_forget()
        self.i_last_name3_journal.grid_forget()
        self.i_first_name3_journal.grid_forget()
        self.i_middle_initial3_journal.grid_forget()
        self.i_last_name4_journal.grid_forget()
        self.i_first_name4_journal.grid_forget()
        self.i_middle_initial4_journal.grid_forget()
        self.i_last_name5_journal.grid_forget()
        self.i_first_name5_journal.grid_forget()
        self.i_middle_initial5_journal.grid_forget()
        self.i_last_name6_journal.grid_forget()
        self.i_first_name6_journal.grid_forget()
        self.i_middle_initial6_journal.grid_forget()
        self.i_last_name7_journal.grid_forget()
        self.i_first_name7_journal.grid_forget()
        self.i_middle_initial7_journal.grid_forget()

    def no_date_journal(self):
        if not self.no_date_true_journal:
            self.year_journal.grid_forget()
            self.i_year_journal.grid_forget()
            self.month_journal.grid_forget()
            self.i_month_journal.grid_forget()
            self.date_journal.grid_forget()
            self.i_date_journal.grid_forget()
            self.no_date_button_journal.configure(text="With Date")
            self.no_date_true_journal = True
            self.i_no_day_journal_button.configure(state=DISABLED)
            self.i_no_month_button_journal.configure(state=DISABLED)
            if self.filipino_cite:
                self.i_month_journal_filipino.grid_forget()
            if self.online_true_journal:
                self.display_output_journal.configure(command=self.online_journal_citation_nd)
            elif not self.online_true_journal:
                self.display_output_journal.configure(command=self.printed_journal_citation_nd)
        elif self.no_date_true_journal:
            self.year_journal.grid(row=11, column=2, pady=5)
            self.i_year_journal.grid(row=12, column=2, pady=5)
            self.month_journal.grid(row=11, column=0)
            self.i_month_journal.grid(row=12, column=0, pady=5)
            self.date_journal.grid(row=11, column=1)
            self.i_date_journal.grid(row=12, column=1, pady=5)
            self.no_date_button_journal.configure(text="No Date")
            self.i_no_day_journal_button.configure(state=NORMAL)
            self.i_no_month_button_journal.configure(state=NORMAL)
            self.no_date_true_journal = False
            self.no_month_true_journal = False
            self.no_day_true_journal = False
            if self.filipino_cite:
                self.i_month_journal_filipino.grid(row=12, column=0)
                self.i_month_journal.grid_forget()
            if self.online_true_journal:
                self.display_output_journal.configure(command=self.online_journal_citation)
            elif not self.online_true_journal:
                self.display_output_journal.configure(command=self.printed_journal_citation)

    def online_journal(self):
        if not self.online_true_journal:
            self.doi_link_journal.grid(row=21, column=1)
            self.i_doi_link_journal.grid(row=22, column=1, pady=5)
            self.online_button_journal.configure(text="Printed Journal")
            self.online_true_journal = True
            if self.no_date_true_journal:
                self.display_output_journal.configure(command=self.online_journal_citation_nd)
            elif not self.no_date_true_journal:
                self.display_output_journal.configure(command=self.online_journal_citation)
        elif self.online_true_journal:
            self.doi_link_journal.grid_forget()
            self.i_doi_link_journal.grid_forget()
            self.online_button_journal.configure(text="Online Journal")
            self.online_true_journal = False
            if self.no_date_true_journal:
                self.display_output_journal.configure(command=self.printed_journal_citation_nd)
            elif not self.no_date_true_journal:
                self.display_output_journal.configure(command=self.printed_journal_citation)

    def no_middle_journal(self):
        if not self.no_middle_true_journal:
            self.i_middle_initial_journal.configure(state=DISABLED)
            self.i_middle_initial2_journal.configure(state=DISABLED)
            self.i_middle_initial3_journal.configure(state=DISABLED)
            self.i_middle_initial4_journal.configure(state=DISABLED)
            self.i_middle_initial5_journal.configure(state=DISABLED)
            self.i_middle_initial6_journal.configure(state=DISABLED)
            self.i_middle_initial7_journal.configure(state=DISABLED)
            self.no_middle_button_journal.configure(text="With Middle Initial/Name")
            self.no_middle_true_journal = True
        elif self.no_middle_true_journal:
            self.i_middle_initial_journal.configure(state=NORMAL)
            self.i_middle_initial2_journal.configure(state=NORMAL)
            self.i_middle_initial3_journal.configure(state=NORMAL)
            self.i_middle_initial4_journal.configure(state=NORMAL)
            self.i_middle_initial5_journal.configure(state=NORMAL)
            self.i_middle_initial6_journal.configure(state=NORMAL)
            self.i_middle_initial7_journal.configure(state=NORMAL)
            self.no_middle_button_journal.configure(text="No Middle Initial/Name")
            self.no_middle_true_journal = False

    def online_journal_citation(self):
        self.i_jn.delete(1.0, END)
        self.i_jn.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_jn.tag_config("title_italics", font="times 12 italic")

    #CORPORATE
        if self.corporate_author_true_journal and self.author_number_journal == 1 and not self.no_day_true_journal and not self.no_month_true_journal and not self.no_author_true_journal \
        and not self.normal_author and not self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #CORPORATE NO DAY

        elif self.corporate_author_true_journal and self.author_number_journal == 1 and not self.no_month_true_journal and self.no_day_true_journal and not self.no_author_true_journal\
                and not self.normal_author and not self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #CORPORATE NO MONTH

        elif self.corporate_author_true_journal and self.author_number_journal == 1 and self.no_month_true_journal and not self.no_author_true_journal and not self.normal_author\
                and not self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_journal.get()}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #UNKNOWN

        if self.no_author_true_journal and self.author_number_journal == 1 and not self.no_month_true_journal and not self.no_day_true_journal\
                and not self.corporate_author_true_journal and not self.normal_author and not self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #UNKNOWN NO DAY

        elif self.author_number_journal and not self.no_month_true_journal and self.no_day_true_journal and self.author_number_journal == 1 and not self.corporate_author_true_journal\
                and not self.no_author_true_journal and not self.normal_author and not self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #UNKNOWN NO MONTH

        elif self.no_author_true_journal == 1 and self.no_month_true_journal and not self.corporate_author_true_journal and not self.no_author_true_journal and not self.normal_author \
        and not self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_journal.get()}. \
({self.i_year_journal.get()}). "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE 1 AUTHOR

        if self.author_number_journal == 1 and not self.no_month_true_journal and not self.no_day_true_journal and not self.corporate_author_true_journal\
        and not self.no_author_true_journal and self.normal_author and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY 1 AUTHOR

        elif self.author_number_journal == 1 and not self.no_month_true_journal and self.no_day_true_journal and self.normal_author and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH 1 AUTHOR

        elif self.author_number_journal == 1 and self.no_month_true_journal and self.normal_author and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE 2 AUTHORS

        if self.author_number_journal == 2 and not self.corporate_author_true_journal and not self.no_author_true_journal and not self.no_month_true_journal \
        and not self.no_day_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY 2 AUTHORS

        elif self.author_number_journal == 2 and self.no_day_true_journal and not self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH 2 AUTHORS

        elif self.author_number_journal == 2 and self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}.{str(self.i_middle_initial_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}.{str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE 3 AUTHORS

        if self.author_number_journal == 3 and not self.no_author_true_journal and not self.corporate_author_true_journal and not self.no_month_true_journal \
        and not self.no_day_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}.  {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}.  {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}.  {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY 3 AUTHORS

        elif self.author_number_journal == 3 and self.no_day_true_journal and not self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH 3 AUTHORS

        elif self.author_number_journal == 3 and self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE 4 AUTHORS

        if self.author_number_journal == 4 and not self.no_author_true_journal and not self.corporate_author_true_journal\
        and not self.no_day_true_journal and not self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY 4 AUTHORS

        elif self.author_number_journal == 4 and self.no_day_true_journal and not self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH 4 AUTHORS

        elif self.author_number_journal == 4 and self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}.. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE 5 AUTHORS

        if self.author_number_journal == 5 and not self.no_author_true_journal and not self.corporate_author_true_journal\
        and not self.no_day_true_journal and not self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}.. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY 5 AUTHORS

        elif self.author_number_journal == 5 and self.no_day_true_journal and not self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH 5 AUTHORS

        elif self.author_number_journal == 5 and self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)


    #NORMAL ONLINE 6 AUTHORS

        if self.author_number_journal == 6 and not self.corporate_author_true_journal and not self.no_author_true_journal \
        and not self.no_month_true_journal and not self.no_day_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY 6 AUTHORS

        elif self.author_number_journal == 6 and self.no_day_true_journal and not self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH 6 AUTHORS

        elif self.author_number_journal == 6 and self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        #NORMAL ONLINE 7 AUTHORS

        if self.author_number_journal == 7 and not self.corporate_author_true_journal and not self.no_author_true_journal\
        and not self.no_month_true_journal and not self.no_day_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY 7 DAY

        elif self.author_number_journal == 7 and self.no_day_true_journal and not self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH 7 AUTHORS

        elif self.author_number_journal == 7 and self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                    self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        #NORMAL ONLINE FINAL AUTHORS

        if self.author_number_journal == 8 and not self.corporate_author_true_journal and not self.no_author_true_journal\
        and not self.no_month_true_journal and not self.no_day_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY FINAL AUTHORS

        elif self.author_number_journal == 8 and not self.no_month_true_journal and self.no_day_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}.  {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}.  {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}.  {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}.  {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}.  {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}.  {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}.  {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH FINAL AUTHORS

        elif self.author_number_journal == 8 and self.no_month_true_journal:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
      # FILIPINO CITE!!!!
      # CORPORATE
        if self.corporate_author_true_journal and self.author_number_journal == 1 and not self.no_day_true_journal and not self.no_month_true_journal and not self.no_author_true_journal \
        and not self.normal_author and self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # CORPORATE NO DAY

        elif self.corporate_author_true_journal and self.author_number_journal == 1 and not self.no_month_true_journal and self.no_day_true_journal and not self.no_author_true_journal \
        and not self.normal_author and self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # CORPORATE NO MONTH

        elif self.corporate_author_true_journal and self.author_number_journal == 1 and self.no_month_true_journal and not self.no_author_true_journal and not self.normal_author \
        and self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_journal.get()}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # UNKNOWN

        if self.no_author_true_journal and self.author_number_journal == 1 and not self.no_month_true_journal and not self.no_day_true_journal \
        and not self.corporate_author_true_journal and not self.normal_author and self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # UNKNOWN NO DAY

        elif self.author_number_journal and not self.no_month_true_journal and self.no_day_true_journal and self.author_number_journal == 1 and not self.corporate_author_true_journal \
        and not self.no_author_true_journal and not self.normal_author and self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # UNKNOWN NO MONTH

        elif self.no_author_true_journal == 1 and self.no_month_true_journal and not self.corporate_author_true_journal and not self.no_author_true_journal and not self.normal_author \
        and self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_journal.get()}. \
({self.i_year_journal.get()}). "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE 1 AUTHOR

        if self.author_number_journal == 1 and not self.no_month_true_journal and not self.no_day_true_journal and not self.corporate_author_true_journal \
        and not self.no_author_true_journal and self.normal_author and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY 1 AUTHOR

        elif self.author_number_journal == 1 and not self.no_month_true_journal and self.no_day_true_journal and self.normal_author \
        and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH 1 AUTHOR

        elif self.author_number_journal == 1 and self.no_month_true_journal and self.normal_author and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE 2 AUTHORS

        if self.author_number_journal == 2 and not self.corporate_author_true_journal and not self.no_author_true_journal and not self.no_month_true_journal \
        and not self.no_day_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY 2 AUTHORS

        elif self.author_number_journal == 2 and self.no_day_true_journal and not self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                    self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH 2 AUTHORS

        elif self.author_number_journal == 2 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE 3 AUTHORS

        if self.author_number_journal == 3 and not self.no_author_true_journal and not self.corporate_author_true_journal \
        and not self.no_month_true_journal and not self.no_day_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}, \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}, \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY 3 AUTHORS

        elif self.author_number_journal == 3 and self.no_day_true_journal and not self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH 3 AUTHORS

        elif self.author_number_journal == 3 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}.,\
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE 4 AUTHORS

        if self.author_number_journal == 4 and not self.no_author_true_journal and not self.corporate_author_true_journal \
        and not self.no_day_true_journal and not self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY 4 AUTHORS

        elif self.author_number_journal == 4 and self.no_day_true_journal and not self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH 4 AUTHORS

        elif self.author_number_journal == 4 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE 5 AUTHORS

        if self.author_number_journal == 5 and not self.no_author_true_journal and not self.corporate_author_true_journal \
        and not self.no_day_true_journal and not self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY 5 AUTHORS

        elif self.author_number_journal == 5 and self.no_day_true_journal and not self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}, \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}.., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}.., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}.., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}.. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH 5 AUTHORS

        elif self.author_number_journal == 5 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE 6 AUTHORS

        if self.author_number_journal == 6 and not self.corporate_author_true_journal and not self.no_author_true_journal \
        and not self.no_month_true_journal and not self.no_day_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY 6 AUTHORS

        elif self.author_number_journal == 6 and self.no_day_true_journal and not self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH 6 AUTHORS

        elif self.author_number_journal == 6 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE 7 AUTHORS

        if self.author_number_journal == 7 and not self.corporate_author_true_journal and not self.no_author_true_journal \
        and not self.no_month_true_journal and not self.no_day_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]},, \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]},, \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]},, \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]},, \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]},, & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY 7 DAY

        elif self.author_number_journal == 7 and self.no_day_true_journal and not self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH 7 AUTHORS

        elif self.author_number_journal == 7 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE FINAL AUTHORS

        if self.author_number_journal == 8 and not self.corporate_author_true_journal and not self.no_author_true_journal \
        and not self.no_month_true_journal and not self.no_day_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY FINAL AUTHORS

        elif self.author_number_journal == 8 and not self.no_month_true_journal and self.no_day_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH FINAL AUTHORS

        elif self.author_number_journal == 8 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    def online_journal_citation_nd(self):
        self.i_jn.delete(1.0, END)
        self.i_jn.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_jn.tag_config("title_italics", font="times 12 italic")

    # CORPORATE AUTHOR ND
        if self.corporate_author_true_journal and self.author_number_journal == 1:
            self.output1 = \
f"{self.i_first_name_journal.get()}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # NO AUTHOR ND
        elif self.no_author_true_journal and self.author_number_journal == 1:
            self.output1 = \
f"{self.i_article_title_journal.get()}. \
(n.d.). "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 1 AUTHOR ND
        elif self.author_number_journal == 1:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 2 AUTHOR ND
        elif self.author_number_journal == 2:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 3 AUTHOR ND
        elif self.author_number_journal == 3:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 4 AUTHOR ND
        elif self.author_number_journal == 4:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 5 AUTHOR ND
        elif self.author_number_journal == 5:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 6 AUTHOR ND
        elif self.author_number_journal == 6:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 7 AUTHOR ND
        elif self.author_number_journal == 7:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                    self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 8 OR MORE AUTHORS ND
        elif self.author_number_journal == 8:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. {self.i_doi_link_journal.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    def printed_journal_citation(self):
        self.i_jn.delete(1.0, END)
        self.i_jn.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_jn.tag_config("title_italics", font="times 12 italic")

    #Corporate NORMAL
        if self.corporate_author_true_journal and self.author_number_journal == 1 and not self.no_day_true_journal\
                and not self.no_month_true_journal and not self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #Corporate NO DAY

        elif self.corporate_author_true_journal and self.author_number_journal == 1 and self.no_day_true_journal\
            and not self.no_month_true_journal and not self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #Corporate NO MONTH

        elif self.corporate_author_true_journal and self.author_number_journal == 1 and self.no_month_true_journal\
                and not self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_journal.get()}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #Unknown Author

        elif self.no_author_true_journal and self.author_number_journal == 1 and not self.no_month_true_journal\
                and not self.no_day_true_journal and not self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #Unknown Author NO DAY

        elif self.no_author_true_journal and self.author_number_journal == 1 and not self.no_month_true_journal \
                 and self.no_day_true_journal and not self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #Unknown Author NO MONTH

        elif self.no_author_true_journal and self.author_number_journal == 1 and self.no_month_true_journal\
                and not self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_journal.get()}. \
({self.i_year_journal.get()}). "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL CITATIONS

        if self.author_number_journal == 1 and not self.corporate_author_true_journal and not self.no_day_true_journal and not self.no_author_true_journal\
        and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NOMRAL NO DAY 1 AUTHOR

        elif self.author_number_journal == 1 and not self.corporate_author_true_journal and not self.no_author_true_journal\
        and not self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO MONTH 1 AUTHOR

        elif self.author_number_journal == 1 and not self.corporate_author_true_journal and not self.no_author_true_journal\
        and self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL 2 AUTHORS

        elif self.author_number_journal == 2 and not self.no_month_true_journal and not self.no_day_true_journal\
        and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO DAY 2 AUTHORS

        elif self.author_number_journal == 2 and self.no_day_true_journal and not self.no_month_true_journal\
        and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO MONTH 2 AUTHORS

        elif self.author_number_journal == 2 and self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL 3 AUTHORS

        elif self.author_number_journal == 3 and not self.no_month_true_journal and not self.no_day_true_journal\
        and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO DAY 3 AUTHORS

        elif self.author_number_journal == 3 and not self.no_month_true_journal and self.no_day_true_journal\
        and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO MONTH 3 AUTHORS

        elif self.author_number_journal == 3 and self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). {self.i_article_title_journal.get()}. "
            elif self. no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). {self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL 4 AUTHORS

        elif self.author_number_journal == 4 and not self.no_month_true_journal and not self.no_day_true_journal\
        and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO DAY 4 AUTHORS

        elif self.author_number_journal == 4 and not self.no_month_true_journal and self.no_day_true_journal\
        and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            if not self.no_middle_true_journal:
                self.output1 = \
 f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
 {str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
 {str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., & \
 {str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. \
 ({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
 {self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)


    #NORMAL NO MONTH 4 AUTHORS

        elif self.author_number_journal == 4 and self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL 5 AUTHORS

        elif self.author_number_journal == 5 and not self.no_month_true_journal and not self.no_day_true_journal\
        and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO DAY 5 AUTHORS

        elif self.author_number_journal == 5 and self.no_day_true_journal and not self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO MONTH 5 AUTHORS

        elif self.author_number_journal == 5 and self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL 6 AUTHORS


        elif self.author_number_journal == 6 and not self.no_month_true_journal and not self.no_day_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)


    #NORMAL NO DAY 6 AUTHORS

        elif self.author_number_journal == 6 and not self.no_month_true_journal and self.no_day_true_journal\
        and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO MONTH 6 AUTHORS

        elif self.author_number_journal == 6 and self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)


    #NORMAL 7 AUTHORS

        elif self.author_number_journal == 7 and not self.no_month_true_journal and not self.no_day_true_journal\
        and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}, \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}, \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}, \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}, \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}, \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO DAY 7 AUTHORS

        elif self.author_number_journal == 7 and not self.no_month_true_journal and self.no_day_true_journal\
        and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO MONTH 7 AUTHORS
        elif self.author_number_journal == 7 and self.no_month_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}, \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}, \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}, \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}, \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}, \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}.. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL FINAL

        elif self.author_number_journal == 8 and not self.no_month_true_journal and not self.no_day_true_journal and not self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        #FILIPINO CITE

            #Corporate NORMAL
        if self.corporate_author_true_journal and self.author_number_journal == 1 and not self.no_day_true_journal \
        and not self.no_month_true_journal and self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # Corporate NO DAY

        elif self.corporate_author_true_journal and self.author_number_journal == 1 and self.no_day_true_journal \
                and not self.no_month_true_journal and self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # Corporate NO MONTH

        elif self.corporate_author_true_journal and self.author_number_journal == 1 and self.no_month_true_journal\
                and self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_journal.get()}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # Unknown Author

        elif self.no_author_true_journal and self.author_number_journal == 1 and not self.no_month_true_journal \
                and not self.no_day_true_journal and self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # Unknown Author NO DAY

        elif self.no_author_true_journal and self.author_number_journal == 1 and not self.no_month_true_journal \
                and self.no_day_true_journal and self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_journal.get()}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # Unknown Author NO MONTH

        elif self.no_author_true_journal and self.author_number_journal == 1 and self.no_month_true_journal\
                and self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_journal.get()}. \
({self.i_year_journal.get()}). "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL CITATIONS

            # NORMAL NO DAY 1 Author
        if self.author_number_journal == 1 and not self.corporate_author_true_journal and not self.no_day_true_journal and not self.no_author_true_journal\
        and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NOMRAL NO DAY 1 AUTHOR

        elif self.author_number_journal == 1 and not self.corporate_author_true_journal and not self.no_author_true_journal \
        and not self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH 1 AUTHOR

        elif self.author_number_journal == 1 and not self.corporate_author_true_journal and not self.no_author_true_journal \
        and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL 2 AUTHORS

        elif self.author_number_journal == 2 and not self.no_month_true_journal and not self.no_day_true_journal\
        and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO DAY 2 AUTHORS

        elif self.author_number_journal == 2 and self.no_day_true_journal and not self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH 2 AUTHORS

        elif self.author_number_journal == 2 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL 3 AUTHORS

        elif self.author_number_journal == 3 and not self.no_month_true_journal and not self.no_day_true_journal\
        and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                    self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO DAY 3 AUTHORS

        elif self.author_number_journal == 3 and not self.no_month_true_journal and self.no_day_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH 3 AUTHORS

        elif self.author_number_journal == 3 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). {self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). {self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL 4 AUTHORS

        elif self.author_number_journal == 4 and not self.no_month_true_journal and not self.no_day_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO DAY 4 AUTHORS

        elif self.author_number_journal == 4 and not self.no_month_true_journal and self.no_day_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH 4 AUTHORS

        elif self.author_number_journal == 4 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL 5 AUTHORS

        elif self.author_number_journal == 5 and not self.no_month_true_journal and not self.no_day_true_journal\
        and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO DAY 5 AUTHORS

        elif self.author_number_journal == 5 and self.no_day_true_journal and not self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH 5 AUTHORS

        elif self.author_number_journal == 5 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}.. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL 6 AUTHORS

        elif self.author_number_journal == 6 and not self.no_month_true_journal and not self.no_day_true_journal\
        and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO DAY 6 AUTHORS

        elif self.author_number_journal == 6 and not self.no_month_true_journal and self.no_day_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH 6 AUTHORS

        elif self.author_number_journal == 6 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL 7 AUTHORS

        elif self.author_number_journal == 7 and not self.no_month_true_journal and not self.no_day_true_journal\
        and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO DAY 7 AUTHORS

        elif self.author_number_journal == 7 and not self.no_month_true_journal and self.no_day_true_journal\
        and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH 7 AUTHORS
        elif self.author_number_journal == 7 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL FINAL

        elif self.author_number_journal == 8 and not self.no_month_true_journal and not self.no_day_true_journal\
        and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()} {self.i_date_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO DAY FINAL

        elif self.author_number_journal == 8 and self.no_day_true_journal and not self.no_month_true_journal\
        and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal_filipino.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH FINAL

        elif self.author_number_journal == 8 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)


        #NORMAL NO DAY FINAL

        elif self.author_number_journal == 8 and self.no_day_true_journal and not self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}, {self.i_month_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO MONTH FINAL

        elif self.author_number_journal == 8 and self.no_month_true_journal and self.filipino_cite:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
({self.i_year_journal.get()}). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    def printed_journal_citation_nd(self):
        self.i_jn.delete(1.0, END)
        self.i_jn.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_jn.tag_config("title_italics", font="times 12 italic")

    # Corporate NO DATE
        if self.corporate_author_true_journal and self.author_number_journal == 1:
            self.output1 = \
f"{self.i_first_name_journal.get()}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # No Author NO DATE
        elif self.no_author_true_journal and self.author_number_journal == 1:
            self.output1 = \
f"{self.i_article_title_journal.get()}. \
(n.d.). "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 1 Normal Author NO DATE
        elif self.author_number_journal == 1:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 2 Normal Author NO DATE
        elif self.author_number_journal == 2:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 3 Normal Author NO DATE
        elif self.author_number_journal == 3:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 4 Normal Author NO DATE
        elif self.author_number_journal == 4:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 5 Normal Authors NO DATE
        elif self.author_number_journal == 5:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 6 Normal Authors NO DATE
        elif self.author_number_journal == 6:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 7 Normal Author NO DATE
        elif self.author_number_journal == 7:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    # 8+ Normal Author NO DATE
        elif self.author_number_journal == 8:
            if not self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. {str(self.i_middle_initial7_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            elif self.no_middle_true_journal:
                self.output1 = \
f"{str(self.i_last_name_journal.get()).capitalize()}, {str(self.i_first_name_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name2_journal.get()).capitalize()}, {str(self.i_first_name2_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name3_journal.get()).capitalize()}, {str(self.i_first_name3_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name4_journal.get()).capitalize()}, {str(self.i_first_name4_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name5_journal.get()).capitalize()}, {str(self.i_first_name5_journal.get()).capitalize()[:1]}., \
{str(self.i_last_name6_journal.get()).capitalize()}, {str(self.i_first_name6_journal.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_journal.get()).capitalize()}, {str(self.i_first_name7_journal.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_journal.get()}. "
            self.output2 = f"{self.i_periodical_title_journal.get()}, {self.i_volume_number_journal.get()}"
            self.output3 = f"({self.i_issue_number_journal.get()}), {self.i_page_number_journal.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    def filipino_activate_action(self):
        if not self.filipino_cite:
            self.filipino_cite = True
            self.journal_filipino_month_activate.configure(text="English Dates")
            self.i_month_journal.grid_forget()
            self.i_month_journal_filipino.grid(row=12, column=0)
        elif self.filipino_cite:
            self.filipino_cite = False
            self.journal_filipino_month_activate.configure(text="Filipino Dates")
            self.i_month_journal_filipino.grid_forget()
            self.i_month_journal.grid(row=12, column=0)

    def clearallentries_journal(self):
        self.i_year_journal.delete(0, END)
        self.i_article_title_journal.delete(0, END)
        self.i_periodical_title_journal.delete(0, END)
        self.i_volume_number_journal.delete(0, END)
        self.i_issue_number_journal.delete(0, END)
        self.i_page_number_journal.delete(0, END)
        self.i_doi_link_journal.delete(0, END)
        self.i_month_journal.delete(0, END)
        self.i_date_journal.delete(0, END)
        self.i_first_name_journal.delete(0, END)
        self.i_middle_initial_journal.delete(0, END)
        self.i_last_name_journal.delete(0, END)
        self.i_jn.delete(1.0, END)
        if self.author_number_journal >= 2:
            self.i_last_name2_journal.delete(0, END)
            self.i_first_name2_journal.delete(0, END)
            self.i_middle_initial2_journal.delete(0, END)
            if self.author_number_journal >= 3:
                self.i_last_name3_journal.delete(0, END)
                self.i_first_name3_journal.delete(0, END)
                self.i_middle_initial3_journal.delete(0, END)
                if self.author_number_journal >= 4:
                    self.i_last_name4_journal.delete(0, END)
                    self.i_first_name4_journal.delete(0, END)
                    self.i_middle_initial4_journal.delete(0, END)
                    if self.author_number_journal >= 5:
                        self.i_last_name5_journal.delete(0, END)
                        self.i_first_name5_journal.delete(0, END)
                        self.i_middle_initial5_journal.delete(0, END)
                        if self.author_number_journal >= 6:
                            self.i_last_name6_journal.delete(0, END)
                            self.i_first_name6_journal.delete(0, END)
                            self.i_middle_initial6_journal.delete(0, END)
                            if self.author_number_journal >= 7:
                                self.i_last_name7_journal.delete(0, END)
                                self.i_first_name7_journal.delete(0, END)
                                self.i_middle_initial7_journal.delete(0, END)

