from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class APAMagazineCitation:
    def __init__(self, magazinetab):
        self.author_number_magazine = 1
        self.corporate_author_true_magazine = False
        self.no_author_true_magazine = False
        self.no_date_true_magazine = False
        self.online_true_magazine = False
        self.no_month_true_magazine = False
        self.no_day_true_magazine = False
        self.normal_author = True
        self.filipino_cite = False

        self.last_name_magazine = Label(magazinetab, text="Last Name/Surname:" ,background='#AC7CEB')
        self.last_name_magazine.grid(row=0, column=0)
        self.i_last_name_magazine = Entry(magazinetab)
        self.i_last_name_magazine.grid(row=1, column=0)

        self.first_name_magazine = Label(magazinetab, text="First Name:" ,background='#AC7CEB')
        self.first_name_magazine.grid(row=0, column=1)
        self.i_first_name_magazine = Entry(magazinetab)
        self.i_first_name_magazine.grid(row=1, column=1, padx=10)

        self.middle_initial_magazine = Label(magazinetab, text="Middle Initial/Name:" ,background='#AC7CEB')
        self.middle_initial_magazine.grid(row=0, column=2)
        self.i_middle_initial_magazine = Entry(magazinetab)
        self.i_middle_initial_magazine.grid(row=1, column=2)

        self.add_author_button_magazine = Button(magazinetab, text="Add Author", command=self.add_author_magazine)
        self.add_author_button_magazine.grid(row=8, column=1, pady=10, padx=5)

        self.corporate_author_button_magazine = Button(magazinetab, text="Corporate Author", command=self.corporate_author_magazine)
        self.corporate_author_button_magazine.grid(row=8, column=0, pady=5)

        self.no_author_button_magazine = Button(magazinetab, text="Unknown Author", command=self.no_author_magazine)
        self.no_author_button_magazine.grid(row=8, column=2, pady=5)

        self.reset_button_magazine = Button(magazinetab, text="Reset Authors", command=self.reset_authors_magazine)
        self.reset_button_magazine.grid(row=9, column=1)

        self.month_magazine = Label(magazinetab, text="Month:" ,background='#AC7CEB')
        self.month_magazine.grid(row=10, column=0)
        self.i_month_magazine = ttk.Combobox(magazinetab, values =["January", "February", "March", "April", "May", "June"
                     ,"July", "August", "September", "October", "November", "December"])

        self.i_month_magazine_filipino = ttk.Combobox(magazinetab,
                                                 values=["Enero", "Pebrero", "Marso", "Abril", "Mayo", "Hunyo"
                                                     , "Hulyo", "Agosto", "Setyembre", "Oktubre", "Nobyembre",
                                                         "Disyembre"])
        self.i_month_magazine.current(1)
        self.i_month_magazine.grid(row=11, column=0, pady=5)

        self.magazine_filipino_month_activate = Button(magazinetab, text="Filipino Months", command=self.filipino_activate_action)
        self.magazine_filipino_month_activate.grid(row=13, column=0, pady=5)

        self.i_no_month_button_magazine = Button(magazinetab, text="Year Only", command=self.no_month_magazine)
        self.i_no_month_button_magazine.grid(row=12, column=0, pady=5)

        self.date_magazine = Label(magazinetab, text="Day: (Numerical form)" ,background='#AC7CEB')
        self.date_magazine.grid(row=10, column=1)
        self.i_date_magazine = ttk.Combobox(magazinetab,
                                                 values=["1", "2", "3", "4", "5", "6"
                                                     , "7", "8", "9", "10", "11",
                                                         "12", "13", "14", "15", "16",
                                                         "17", "18", "19", "20", "21",
                                                         "22", "23", "24", "25", "26", "27",
                                                         "28", "29", "30", "31"])
        self.i_date_magazine.grid(row=11, column=1, pady=5)

        self.year_magazine = Label(magazinetab, text="Year of Publication:" ,background='#AC7CEB')
        self.year_magazine.grid(row=10, column=2, pady=5)
        self.i_year_magazine = Entry(magazinetab)
        self.i_year_magazine.grid(row=11, column=2, pady=5)

        self.i_no_day_magazine_button = Button(magazinetab, text="No Day", command=self.no_day_magazine)
        self.i_no_day_magazine_button.grid(row=12, column=2, pady=5)

        self.no_date_button_magazine = Button(magazinetab, text="No Date", command=self.no_date_magazine)
        self.no_date_button_magazine.grid(row=12, column=1, pady=5)

        self.article_title_magazine = Label(magazinetab, text="Title of Magazine Article:" ,background='#AC7CEB')
        self.article_title_magazine.grid(row=13, column=1)
        self.i_article_title_magazine = Entry(magazinetab)
        self.i_article_title_magazine.grid(row=14, column=1, pady=5, padx=220)

        self.periodical_title_magazine = Label(magazinetab, text="Title of Magazine:" ,background='#AC7CEB')
        self.periodical_title_magazine.grid(row=15, column=1)
        self.i_periodical_title_magazine = Entry(magazinetab)
        self.i_periodical_title_magazine.grid(row=16, column=1, pady=5)

        self.volume_number_magazine = Label(magazinetab, text="Volume Number:" ,background='#AC7CEB')
        self.volume_number_magazine.grid(row=17, column=0)
        self.i_volume_number_magazine = Entry(magazinetab)
        self.i_volume_number_magazine.grid(row=18, column=0, pady=5)

        self.issue_number_magazine = Label(magazinetab, text="Issue Number:" ,background='#AC7CEB')
        self.issue_number_magazine.grid(row=17, column=1)
        self.i_issue_number_magazine = Entry(magazinetab)
        self.i_issue_number_magazine.grid(row=18, column=1, pady=5)

        self.page_number_magazine = Label(magazinetab, text='''Page Number/s:''' ,background='#AC7CEB')
        self.page_number_magazine.grid(row=17, column=2)
        self.i_page_number_magazine = Entry(magazinetab)
        self.i_page_number_magazine.grid(row=18, column=2, pady=5)

        self.i_middle_initial7_magazine = Entry(magazinetab)
        self.i_first_name7_magazine = Entry(magazinetab)
        self.i_last_name7_magazine = Entry(magazinetab)
        self.i_middle_initial6_magazine = Entry(magazinetab)
        self.i_first_name6_magazine = Entry(magazinetab)
        self.i_last_name6_magazine = Entry(magazinetab)
        self.i_middle_initial5_magazine = Entry(magazinetab)
        self.i_first_name5_magazine = Entry(magazinetab)
        self.i_last_name5_magazine = Entry(magazinetab)
        self.i_middle_initial4_magazine = Entry(magazinetab)
        self.i_first_name4_magazine = Entry(magazinetab)
        self.i_last_name4_magazine = Entry(magazinetab)
        self.i_middle_initial3_magazine = Entry(magazinetab)
        self.i_first_name3_magazine = Entry(magazinetab)
        self.i_last_name3_magazine = Entry(magazinetab)
        self.i_middle_initial2_magazine = Entry(magazinetab)
        self.i_first_name2_magazine = Entry(magazinetab)
        self.i_last_name2_magazine = Entry(magazinetab)

        self.display_output_magazine = Button(magazinetab, text="Cite!", command=self.printed_magazine_citation)
        self.display_output_magazine.grid(row=23, column=1, pady=5)

        self.online_button_magazine = Button(magazinetab, text="Online magazine", command=self.online_magazine)
        self.online_button_magazine.grid(row=19, column=1, pady=10)

        self.doi_link_magazine = Label(magazinetab, text="D.O.I./Link:" ,background='#AC7CEB')
        self.i_doi_link_magazine = Entry(magazinetab)

        self.jn = Label(magazinetab, text="Citation:" ,background='#AC7CEB')
        self.jn.grid(row=24, column=1)
        self.i_jn = Text(magazinetab, height=5, width=50, font="times 12")
        self.i_jn.grid(row=25, column=1, pady=5)

        self.clear = Button(magazinetab, text="Clear All Entries", command=self.clearallentries_magazine)
        self.clear.grid(row=26, column=1, pady=10)

    def add_author_magazine(self):
        self.corporate_author_button_magazine.configure(state=DISABLED)
        self.no_author_button_magazine.configure(state=DISABLED)
        if self.author_number_magazine == 1:
            self.i_last_name2_magazine.grid(row=2, column=0, pady=10)
            self.i_first_name2_magazine.grid(row=2, column=1, pady=10)
            self.i_middle_initial2_magazine.grid(row=2, column=2, pady=10)
            self.author_number_magazine += 1
            return

        elif self.author_number_magazine == 2:
            self.i_last_name3_magazine.grid(row=3, column=0)
            self.i_first_name3_magazine.grid(row=3, column=1)
            self.i_middle_initial3_magazine.grid(row=3, column=2)
            self.author_number_magazine += 1
            return

        elif self.author_number_magazine == 3:
            self.i_last_name4_magazine.grid(row=4, column=0, pady=10)
            self.i_first_name4_magazine.grid(row=4, column=1, pady=10)
            self.i_middle_initial4_magazine.grid(row=4, column=2, pady=10)
            self.author_number_magazine += 1
            return

        elif self.author_number_magazine == 4:
            self.i_last_name5_magazine.grid(row=5, column=0)
            self.i_first_name5_magazine.grid(row=5, column=1)
            self.i_middle_initial5_magazine.grid(row=5, column=2)
            self.author_number_magazine += 1
            return

        elif self.author_number_magazine == 5:
            self.i_last_name6_magazine.grid(row=6, column=0, pady=10)
            self.i_first_name6_magazine.grid(row=6, column=1, pady=10)
            self.i_middle_initial6_magazine.grid(row=6, column=2, pady=10)
            self.author_number_magazine += 1
            return

        elif self.author_number_magazine == 6:
            self.i_last_name7_magazine.grid(row=7, column=0)
            self.i_first_name7_magazine.grid(row=7, column=1)
            self.i_middle_initial7_magazine.grid(row=7, column=2)
            self.author_number_magazine += 1
            return

        elif self.author_number_magazine == 7:
            self.response = messagebox.askquestion("Too many names!", '''
            The limit of names to be placed in a citation is 7.

            For works with more than 7 names please input the
            last author's name into the last set of boxes.

            Continue inputting citation for more than 7 authors?''')
            if self.response == "yes":
                self.author_number_magazine += 1
            elif self.response == "no":
                self.author_number_magazine -= 1
            self.add_author_button_magazine.configure(state=DISABLED)

    def corporate_author_magazine(self):
        if not self.corporate_author_true_magazine:
            self.last_name_magazine.grid_forget()
            self.i_last_name_magazine.grid_forget()
            self.middle_initial_magazine.grid_forget()
            self.i_middle_initial_magazine.grid_forget()
            self.first_name_magazine.configure(text="Corporate Author Name:")
            self.corporate_author_button_magazine.configure(text="Normal Author/s")
            self.add_author_button_magazine.configure(state=DISABLED)
            self.no_author_button_magazine.configure(state=DISABLED)
            self.corporate_author_true_magazine = True
            self.normal_author = False
        elif self.corporate_author_true_magazine:
            self.last_name_magazine.grid(row=0, column=0)
            self.i_last_name_magazine.grid(row=1, column=0)
            self.middle_initial_magazine.grid(row=0, column=2)
            self.i_middle_initial_magazine.grid(row=1, column=2)
            self.first_name_magazine.configure(text="First Name:")
            self.corporate_author_button_magazine.configure(text="Corporate Author")
            self.add_author_button_magazine.configure(state=NORMAL)
            self.no_author_button_magazine.configure(state=NORMAL)
            self.corporate_author_true_magazine = False
            self.normal_author = True

    def no_author_magazine(self):
        if not self.no_author_true_magazine:
            self.last_name_magazine.grid_forget()
            self.i_last_name_magazine.grid_forget()
            self.first_name_magazine.grid_forget()
            self.i_first_name_magazine.grid_forget()
            self.middle_initial_magazine.grid_forget()
            self.i_middle_initial_magazine.grid_forget()
            self.no_author_button_magazine.configure(text="With Author/s")
            self.add_author_button_magazine.configure(state=DISABLED)
            self.corporate_author_button_magazine.configure(state=DISABLED)
            self.no_author_true_magazine = True
            self.normal_author = False
        elif self.no_author_true_magazine:
            self.last_name_magazine.grid(row=0, column=0)
            self.i_last_name_magazine.grid(row=1, column=0)
            self.first_name_magazine.grid(row=0, column=1)
            self.i_first_name_magazine.grid(row=1, column=1, padx=10)
            self.middle_initial_magazine.grid(row=0, column=2)
            self.i_middle_initial_magazine.grid(row=1, column=2)
            self.no_author_button_magazine.configure(text="Unknown Author")
            self.add_author_button_magazine.configure(state=NORMAL)
            self.corporate_author_button_magazine.configure(state=NORMAL)
            self.no_author_true_magazine = False
            self.normal_author = True

    def no_month_magazine(self):
        if not self.no_month_true_magazine:
            self.i_month_magazine.grid_forget()
            self.i_date_magazine.grid_forget()
            self.month_magazine.grid_forget()
            self.date_magazine.grid_forget()
            self.i_no_month_button_magazine.configure(text="With Month")
            self.i_no_day_magazine_button.configure(text="With Day")
            self.i_no_day_magazine_button.configure(state=DISABLED)
            self.no_month_true_magazine = True
            self.no_day_true_magazine = True
            if self.filipino_cite:
                self.i_month_magazine_filipino.grid_forget()
        elif self.no_month_true_magazine:
            self.i_month_magazine.grid(row=11, column=0, pady=5)
            self.i_date_magazine.grid(row=11, column=1, pady=5)
            self.month_magazine.grid(row=10, column=0)
            self.date_magazine.grid(row=10, column=1)
            self.i_no_day_magazine_button.configure(state=NORMAL)
            self.i_no_month_button_magazine.configure(text="Year Only")
            self.i_no_day_magazine_button.configure(text="No Day")
            self.no_month_true_magazine = False
            self.no_day_true_magazine = False
            if self.filipino_cite:
                self.i_month_magazine_filipino.grid(row=11, column=0)

    def no_day_magazine(self):
        if not self.no_day_true_magazine:
            self.no_day_true_magazine = True
            self.i_date_magazine.grid_forget()
            self.date_magazine.grid_forget()
            self.i_no_day_magazine_button.configure(text="With Day")


        elif self.no_day_true_magazine:
            self.no_day_true_magazine = False
            self.i_date_magazine.grid(row=11, column=1, pady=5)
            self.date_magazine.grid(row=10, column=1)
            self.i_no_day_magazine_button.configure(text="No Day")

    def reset_authors_magazine(self):
        self.first_name_magazine.configure(text="First Name:")
        self.add_author_button_magazine.configure(state=NORMAL)
        self.corporate_author_button_magazine.configure(state=NORMAL)
        self.no_author_button_magazine.configure(state=NORMAL)
        self.corporate_author_button_magazine.configure(text="Corporate Author")
        self.no_author_button_magazine.configure(text="Unknown Author")
        self.author_number_magazine = 1
        self.corporate_author_true_magazine = False
        self.no_author_true_magazine = False
        self.last_name_magazine.grid(row=0, column=0)
        self.i_last_name_magazine.grid(row=1, column=0)
        self.first_name_magazine.grid(row=0, column=1)
        self.i_first_name_magazine.grid(row=1, column=1, padx=10)
        self.middle_initial_magazine.grid(row=0, column=2)
        self.i_middle_initial_magazine.grid(row=1, column=2)
        self.i_last_name2_magazine.grid_forget()
        self.i_first_name2_magazine.grid_forget()
        self.i_middle_initial2_magazine.grid_forget()
        self.i_last_name3_magazine.grid_forget()
        self.i_first_name3_magazine.grid_forget()
        self.i_middle_initial3_magazine.grid_forget()
        self.i_last_name4_magazine.grid_forget()
        self.i_first_name4_magazine.grid_forget()
        self.i_middle_initial4_magazine.grid_forget()
        self.i_last_name5_magazine.grid_forget()
        self.i_first_name5_magazine.grid_forget()
        self.i_middle_initial5_magazine.grid_forget()
        self.i_last_name6_magazine.grid_forget()
        self.i_first_name6_magazine.grid_forget()
        self.i_middle_initial6_magazine.grid_forget()
        self.i_last_name7_magazine.grid_forget()
        self.i_first_name7_magazine.grid_forget()
        self.i_middle_initial7_magazine.grid_forget()

    def no_date_magazine(self):
        if not self.no_date_true_magazine:
            self.year_magazine.grid_forget()
            self.i_year_magazine.grid_forget()
            self.month_magazine.grid_forget()
            self.i_month_magazine.grid_forget()
            self.date_magazine.grid_forget()
            self.i_date_magazine.grid_forget()
            self.no_date_button_magazine.configure(text="With Date")
            self.no_date_true_magazine = True
            self.i_no_day_magazine_button.configure(state=DISABLED)
            self.i_no_month_button_magazine.configure(state=DISABLED)
            if self.filipino_cite:
                self.i_month_magazine_filipino.grid_forget()
            if self.online_true_magazine:
                self.display_output_magazine.configure(command=self.online_magazine_citation_nd)
            elif not self.online_true_magazine:
                self.display_output_magazine.configure(command=self.printed_magazine_citation_nd)
        elif self.no_date_true_magazine:
            self.year_magazine.grid(row=10, column=2, pady=5)
            self.i_year_magazine.grid(row=11, column=2, pady=5)
            self.month_magazine.grid(row=10, column=0)
            self.i_month_magazine.grid(row=11, column=0, pady=5)
            self.date_magazine.grid(row=10, column=1)
            self.i_date_magazine.grid(row=11, column=1, pady=5)
            self.no_date_button_magazine.configure(text="No Date")
            self.i_no_day_magazine_button.configure(state=NORMAL)
            self.i_no_month_button_magazine.configure(state=NORMAL)
            self.no_date_true_magazine = False
            self.no_month_true_magazine = False
            self.no_day_true_magazine = False
            if self.filipino_cite:
                self.i_month_magazine_filipino.grid(row=11, column=0)
                self.i_month_magazine.grid_forget()
            if self.online_true_magazine:
                self.display_output_magazine.configure(command=self.online_magazine_citation)
            elif not self.online_true_magazine:
                self.display_output_magazine.configure(command=self.printed_magazine_citation)

    def online_magazine(self):
        if not self.online_true_magazine:
            self.doi_link_magazine.grid(row=21, column=1)
            self.i_doi_link_magazine.grid(row=22, column=1, pady=5)
            self.online_button_magazine.configure(text="Printed magazine")
            self.online_true_magazine = True
            if self.no_date_true_magazine:
                self.display_output_magazine.configure(command=self.online_magazine_citation_nd)
            elif not self.no_date_true_magazine:
                self.display_output_magazine.configure(command=self.online_magazine_citation)
        elif self.online_true_magazine:
            self.doi_link_magazine.grid_forget()
            self.i_doi_link_magazine.grid_forget()
            self.online_button_magazine.configure(text="Online magazine")
            self.online_true_magazine = False
            if self.no_date_true_magazine:
                self.display_output_magazine.configure(command=self.printed_magazine_citation_nd)
            elif not self.no_date_true_magazine:
                self.display_output_magazine.configure(command=self.printed_magazine_citation)

    def online_magazine_citation(self):
        self.i_jn.delete(1.0, END)
        self.i_jn.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_jn.tag_config("title_italics", font="times 12 italic")

    #CORPORATE
        if self.corporate_author_true_magazine and self.author_number_magazine == 1 and not self.no_day_true_magazine and not self.no_month_true_magazine and not self.no_author_true_magazine \
                and not self.normal_author and not self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #CORPORATE NO DAY

        elif self.corporate_author_true_magazine and self.author_number_magazine == 1 and not self.no_month_true_magazine and self.no_day_true_magazine and not self.no_author_true_magazine\
                and not self.normal_author and not self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #CORPORATE NO MONTH

        elif self.corporate_author_true_magazine and self.author_number_magazine == 1 and self.no_month_true_magazine and not self.no_author_true_magazine and not self.normal_author\
                and not self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_magazine.get()}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #UNKNOWN

        if self.no_author_true_magazine and self.author_number_magazine == 1 and not self.no_month_true_magazine and not self.no_day_true_magazine\
                and not self.corporate_author_true_magazine and not self.normal_author and not self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #UNKNOWN NO DAY

        elif self.author_number_magazine and not self.no_month_true_magazine and self.no_day_true_magazine and self.author_number_magazine == 1 and not self.corporate_author_true_magazine\
                and not self.no_author_true_magazine and not self.normal_author and not self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #UNKNOWN NO MONTH

        elif self.no_author_true_magazine == 1 and self.no_month_true_magazine and not self.corporate_author_true_magazine and not self.no_author_true_magazine and not self.normal_author \
                and not self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_magazine.get()}. \
({self.i_year_magazine.get()}). "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE 1 AUTHOR

        if self.author_number_magazine == 1 and not self.no_month_true_magazine and not self.no_day_true_magazine and not self.corporate_author_true_magazine\
                and not self.no_author_true_magazine and self.normal_author and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY 1 AUTHOR

        elif self.author_number_magazine == 1 and not self.no_month_true_magazine and self.no_day_true_magazine and self.normal_author and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH 1 AUTHOR

        elif self.author_number_magazine == 1 and self.no_month_true_magazine and self.normal_author and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE 2 AUTHORS

        if self.author_number_magazine == 2 and not self.corporate_author_true_magazine and not self.no_author_true_magazine and not self.no_month_true_magazine \
                and not self.no_day_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY 2 AUTHORS

        elif self.author_number_magazine == 2 and self.no_day_true_magazine and not self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH 2 AUTHORS

        elif self.author_number_magazine == 2 and self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE 3 AUTHORS

        if self.author_number_magazine == 3 and not self.no_author_true_magazine and not self.corporate_author_true_magazine\
                and not self.no_month_true_magazine and not self.no_day_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY 3 AUTHORS

        elif self.author_number_magazine == 3 and self.no_day_true_magazine and not self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH 3 AUTHORS

        elif self.author_number_magazine == 3 and self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE 4 AUTHORS

        if self.author_number_magazine == 4 and not self.no_author_true_magazine and not self.corporate_author_true_magazine\
                and not self.no_day_true_magazine and not self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY 4 AUTHORS

        elif self.author_number_magazine == 4 and self.no_day_true_magazine and not self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH 4 AUTHORS

        elif self.author_number_magazine == 4 and self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE 5 AUTHORS

        if self.author_number_magazine == 5 and not self.no_author_true_magazine and not self.corporate_author_true_magazine\
                and not self.no_day_true_magazine and not self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY 5 AUTHORS

        elif self.author_number_magazine == 5 and self.no_day_true_magazine and not self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH 5 AUTHORS

        elif self.author_number_magazine == 5 and self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)


    #NORMAL ONLINE 6 AUTHORS

        if self.author_number_magazine == 6 and not self.corporate_author_true_magazine and not self.no_author_true_magazine\
                and not self.no_month_true_magazine and not self.no_day_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY 6 AUTHORS

        elif self.author_number_magazine == 6 and self.no_day_true_magazine and not self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH 6 AUTHORS

        elif self.author_number_magazine == 6 and self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        #NORMAL ONLINE 7 AUTHORS

        if self.author_number_magazine == 7 and not self.corporate_author_true_magazine and not self.no_author_true_magazine\
                and not self.no_month_true_magazine and not self.no_day_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY 7 DAY

        elif self.author_number_magazine == 7 and self.no_day_true_magazine and not self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH 7 AUTHORS

        elif self.author_number_magazine == 7 and self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        #NORMAL ONLINE FINAL AUTHORS

        if self.author_number_magazine == 8 and not self.corporate_author_true_magazine and not self.no_author_true_magazine\
                and not self.no_month_true_magazine and not self.no_day_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO DAY FINAL AUTHORS

        elif self.author_number_magazine == 8 and not self.no_month_true_magazine and self.no_day_true_magazine and not \
                self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL ONLINE NO MONTH FINAL AUTHORS

        elif self.author_number_magazine == 8 and self.no_month_true_magazine:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
      # FILIPINO CITE!!!!
      # CORPORATE
        if self.corporate_author_true_magazine and self.author_number_magazine == 1 and not self.no_day_true_magazine and not self.no_month_true_magazine and not self.no_author_true_magazine \
                and not self.normal_author and self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # CORPORATE NO DAY

        elif self.corporate_author_true_magazine and self.author_number_magazine == 1 and not self.no_month_true_magazine and self.no_day_true_magazine and not self.no_author_true_magazine \
                and not self.normal_author and self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # CORPORATE NO MONTH

        elif self.corporate_author_true_magazine and self.author_number_magazine == 1 and self.no_month_true_magazine and not self.no_author_true_magazine and not self.normal_author \
                and self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_magazine.get()}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # UNKNOWN

        if self.no_author_true_magazine and self.author_number_magazine == 1 and not self.no_month_true_magazine and not self.no_day_true_magazine \
                and not self.corporate_author_true_magazine and not self.normal_author and self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # UNKNOWN NO DAY

        elif self.author_number_magazine and not self.no_month_true_magazine and self.no_day_true_magazine and self.author_number_magazine == 1 and not self.corporate_author_true_magazine \
                and not self.no_author_true_magazine and not self.normal_author and self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # UNKNOWN NO MONTH

        elif self.no_author_true_magazine == 1 and self.no_month_true_magazine and not self.corporate_author_true_magazine and not self.no_author_true_magazine and not self.normal_author \
                and self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_magazine.get()}. \
({self.i_year_magazine.get()}). "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE 1 AUTHOR

        if self.author_number_magazine == 1 and not self.no_month_true_magazine and not self.no_day_true_magazine and not self.corporate_author_true_magazine \
                and not self.no_author_true_magazine and self.normal_author and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY 1 AUTHOR

        elif self.author_number_magazine == 1 and not self.no_month_true_magazine and self.no_day_true_magazine and self.normal_author \
                and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH 1 AUTHOR

        elif self.author_number_magazine == 1 and self.no_month_true_magazine and self.normal_author and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE 2 AUTHORS

        if self.author_number_magazine == 2 and not self.corporate_author_true_magazine and not self.no_author_true_magazine and not self.no_month_true_magazine \
                and not self.no_day_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY 2 AUTHORS

        elif self.author_number_magazine == 2 and self.no_day_true_magazine and not self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH 2 AUTHORS

        elif self.author_number_magazine == 2 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE 3 AUTHORS

        if self.author_number_magazine == 3 and not self.no_author_true_magazine and not self.corporate_author_true_magazine \
                and not self.no_month_true_magazine and not self.no_day_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY 3 AUTHORS

        elif self.author_number_magazine == 3 and self.no_day_true_magazine and not self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH 3 AUTHORS

        elif self.author_number_magazine == 3 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE 4 AUTHORS

        if self.author_number_magazine == 4 and not self.no_author_true_magazine and not self.corporate_author_true_magazine \
                and not self.no_day_true_magazine and not self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY 4 AUTHORS

        elif self.author_number_magazine == 4 and self.no_day_true_magazine and not self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH 4 AUTHORS

        elif self.author_number_magazine == 4 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE 5 AUTHORS

        if self.author_number_magazine == 5 and not self.no_author_true_magazine and not self.corporate_author_true_magazine \
                and not self.no_day_true_magazine and not self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY 5 AUTHORS

        elif self.author_number_magazine == 5 and self.no_day_true_magazine and not self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH 5 AUTHORS

        elif self.author_number_magazine == 5 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE 6 AUTHORS

        if self.author_number_magazine == 6 and not self.corporate_author_true_magazine and not self.no_author_true_magazine \
                and not self.no_month_true_magazine and not self.no_day_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY 6 AUTHORS

        elif self.author_number_magazine == 6 and self.no_day_true_magazine and not self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH 6 AUTHORS

        elif self.author_number_magazine == 6 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE 7 AUTHORS

        if self.author_number_magazine == 7 and not self.corporate_author_true_magazine and not self.no_author_true_magazine \
                and not self.no_month_true_magazine and not self.no_day_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY 7 DAY

        elif self.author_number_magazine == 7 and self.no_day_true_magazine and not self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH 7 AUTHORS

        elif self.author_number_magazine == 7 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE FINAL AUTHORS

        if self.author_number_magazine == 8 and not self.corporate_author_true_magazine and not self.no_author_true_magazine \
                and not self.no_month_true_magazine and not self.no_day_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO DAY FINAL AUTHORS

        elif self.author_number_magazine == 8 and not self.no_month_true_magazine and self.no_day_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        # NORMAL ONLINE NO MONTH FINAL AUTHORS

        elif self.author_number_magazine == 8 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    def online_magazine_citation_nd(self):
        self.i_jn.delete(1.0, END)
        self.i_jn.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_jn.tag_config("title_italics", font="times 12 italic")
        if self.corporate_author_true_magazine and self.author_number_magazine == 1:
            self.output1 = \
f"{self.i_first_name_magazine.get()}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.no_author_true_magazine and self.author_number_magazine == 1:
            self.output1 = \
f"{self.i_article_title_magazine.get()}. \
(n.d.). "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 1:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 2:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 3:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 4:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 5:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 6:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 7:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 8:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. {self.i_doi_link_magazine.get()}"
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    def printed_magazine_citation(self):
        self.i_jn.delete(1.0, END)
        self.i_jn.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_jn.tag_config("title_italics", font="times 12 italic")
        if self.corporate_author_true_magazine and self.author_number_magazine == 1 and not self.no_day_true_magazine\
                and not self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #Corporate NO DAY

        elif self.corporate_author_true_magazine and self.author_number_magazine == 1 and self.no_day_true_magazine\
            and not self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #Corporate NO MONTH

        elif self.corporate_author_true_magazine and self.author_number_magazine == 1 and self.no_month_true_magazine\
                and not self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_magazine.get()}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #Unknown Author

        elif self.no_author_true_magazine and self.author_number_magazine == 1 and not self.no_month_true_magazine\
                and not self.no_day_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #Unknown Author NO DAY

        elif self.no_author_true_magazine and self.author_number_magazine == 1 and not self.no_month_true_magazine \
                 and self.no_day_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #Unknown Author NO MONTH

        elif self.no_author_true_magazine and self.author_number_magazine == 1 and self.no_month_true_magazine\
                and not self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_magazine.get()}. \
({self.i_year_magazine.get()}). "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL CITATIONS

        if self.author_number_magazine == 1 and not self.corporate_author_true_magazine and not self.no_day_true_magazine and not self.no_author_true_magazine\
                and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NOMRAL NO DAY 1 AUTHOR

        elif self.author_number_magazine == 1 and not self.corporate_author_true_magazine and not self.no_author_true_magazine\
            and not self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO MONTH 1 AUTHOR

        elif self.author_number_magazine == 1 and not self.corporate_author_true_magazine and not self.no_author_true_magazine\
            and self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL 2 AUTHORS

        elif self.author_number_magazine == 2 and not self.no_month_true_magazine and not self.no_day_true_magazine\
                and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO DAY 2 AUTHORS

        elif self.author_number_magazine == 2 and self.no_day_true_magazine and not self.no_month_true_magazine\
                and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO MONTH 2 AUTHORS

        elif self.author_number_magazine == 2 and self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL 3 AUTHORS

        elif self.author_number_magazine == 3 and not self.no_month_true_magazine and not self.no_day_true_magazine\
                and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO DAY 3 AUTHORS

        elif self.author_number_magazine == 3 and not self.no_month_true_magazine and self.no_day_true_magazine\
                and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO MONTH 3 AUTHORS

        elif self.author_number_magazine == 3 and self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). {self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL 4 AUTHORS

        elif self.author_number_magazine == 4 and not self.no_month_true_magazine and not self.no_day_true_magazine\
                and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO DAY 4 AUTHORS

        elif self.author_number_magazine == 4 and not self.no_month_true_magazine and self.no_day_true_magazine\
                and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)


    #NORMAL NO MONTH 4 AUTHORS

        elif self.author_number_magazine == 4 and self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL 5 AUTHORS

        elif self.author_number_magazine == 5 and not self.no_month_true_magazine and not self.no_day_true_magazine\
                and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO DAY 5 AUTHORS

        elif self.author_number_magazine == 5 and self.no_day_true_magazine and not self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO MONTH 5 AUTHORS

        elif self.author_number_magazine == 5 and self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL 6 AUTHORS


        elif self.author_number_magazine == 6 and not self.no_month_true_magazine and not self.no_day_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)


    #NORMAL NO DAY 6 AUTHORS

        elif self.author_number_magazine == 6 and not self.no_month_true_magazine and self.no_day_true_magazine\
                and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO MONTH 6 AUTHORS

        elif self.author_number_magazine == 6 and self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)


    #NORMAL 7 AUTHORS

        elif self.author_number_magazine == 7 and not self.no_month_true_magazine and not self.no_day_true_magazine\
                and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO DAY 7 AUTHORS

        elif self.author_number_magazine == 7 and not self.no_month_true_magazine and self.no_day_true_magazine\
                and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO MONTH 7 AUTHORS
        elif self.author_number_magazine == 7 and self.no_month_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL FINAL

        elif self.author_number_magazine == 8 and not self.no_month_true_magazine and not self.no_day_true_magazine and not self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

        #FILIPINO CITE

        if self.corporate_author_true_magazine and self.author_number_magazine == 1 and not self.no_day_true_magazine \
                and not self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # Corporate NO DAY

        elif self.corporate_author_true_magazine and self.author_number_magazine == 1 and self.no_day_true_magazine \
                and not self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # Corporate NO MONTH

        elif self.corporate_author_true_magazine and self.author_number_magazine == 1 and self.no_month_true_magazine\
                and self.filipino_cite:
            self.output1 = \
f"{self.i_first_name_magazine.get()}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # Unknown Author

        elif self.no_author_true_magazine and self.author_number_magazine == 1 and not self.no_month_true_magazine \
                and not self.no_day_true_magazine and self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # Unknown Author NO DAY

        elif self.no_author_true_magazine and self.author_number_magazine == 1 and not self.no_month_true_magazine \
                and self.no_day_true_magazine and self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_magazine.get()}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # Unknown Author NO MONTH

        elif self.no_author_true_magazine and self.author_number_magazine == 1 and self.no_month_true_magazine\
                and self.filipino_cite:
            self.output1 = \
f"{self.i_article_title_magazine.get()}. \
({self.i_year_magazine.get()}). "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL CITATIONS

        if self.author_number_magazine == 1 and not self.corporate_author_true_magazine and not self.no_day_true_magazine and not self.no_author_true_magazine\
                and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NOMRAL NO DAY 1 AUTHOR

        elif self.author_number_magazine == 1 and not self.corporate_author_true_magazine and not self.no_author_true_magazine \
                and not self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH 1 AUTHOR

        elif self.author_number_magazine == 1 and not self.corporate_author_true_magazine and not self.no_author_true_magazine \
                and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL 2 AUTHORS

        elif self.author_number_magazine == 2 and not self.no_month_true_magazine and not self.no_day_true_magazine\
                and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO DAY 2 AUTHORS

        elif self.author_number_magazine == 2 and self.no_day_true_magazine and not self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH 2 AUTHORS

        elif self.author_number_magazine == 2 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL 3 AUTHORS

        elif self.author_number_magazine == 3 and not self.no_month_true_magazine and not self.no_day_true_magazine\
                and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO DAY 3 AUTHORS

        elif self.author_number_magazine == 3 and not self.no_month_true_magazine and self.no_day_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH 3 AUTHORS

        elif self.author_number_magazine == 3 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). {self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL 4 AUTHORS

        elif self.author_number_magazine == 4 and not self.no_month_true_magazine and not self.no_day_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO DAY 4 AUTHORS

        elif self.author_number_magazine == 4 and not self.no_month_true_magazine and self.no_day_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH 4 AUTHORS

        elif self.author_number_magazine == 4 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL 5 AUTHORS

        elif self.author_number_magazine == 5 and not self.no_month_true_magazine and not self.no_day_true_magazine\
                and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO DAY 5 AUTHORS

        elif self.author_number_magazine == 5 and self.no_day_true_magazine and not self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH 5 AUTHORS

        elif self.author_number_magazine == 5 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL 6 AUTHORS


        elif self.author_number_magazine == 6 and not self.no_month_true_magazine and not self.no_day_true_magazine\
                and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO DAY 6 AUTHORS

        elif self.author_number_magazine == 6 and not self.no_month_true_magazine and self.no_day_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH 6 AUTHORS

        elif self.author_number_magazine == 6 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL 7 AUTHORS

        elif self.author_number_magazine == 7 and not self.no_month_true_magazine and not self.no_day_true_magazine\
                and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO DAY 7 AUTHORS

        elif self.author_number_magazine == 7 and not self.no_month_true_magazine and self.no_day_true_magazine\
                and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH 7 AUTHORS
        elif self.author_number_magazine == 7 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL FINAL

        elif self.author_number_magazine == 8 and not self.no_month_true_magazine and not self.no_day_true_magazine\
                and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()} {self.i_date_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO DAY FINAL

        elif self.author_number_magazine == 8 and self.no_day_true_magazine and not self.no_month_true_magazine\
                and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine_filipino.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

            # NORMAL NO MONTH FINAL

        elif self.author_number_magazine == 8 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)


        #NORMAL NO DAY FINAL

        elif self.author_number_magazine == 8 and self.no_day_true_magazine and not self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}, {self.i_month_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    #NORMAL NO MONTH FINAL

        elif self.author_number_magazine == 8 and self.no_month_true_magazine and self.filipino_cite:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
({self.i_year_magazine.get()}). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    def printed_magazine_citation_nd(self):
        self.i_jn.delete(1.0, END)
        self.i_jn.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_jn.tag_config("title_italics", font="times 12 italic")
        if self.corporate_author_true_magazine and self.author_number_magazine == 1:
            self.output1 = \
f"{self.i_first_name_magazine.get()}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.no_author_true_magazine and self.author_number_magazine == 1:
            self.output1 = \
f"{self.i_article_title_magazine.get()}. \
(n.d.). "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 1:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 2:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 3:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 4:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 5:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 6:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 7:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)
        elif self.author_number_magazine == 8:
            self.output1 = \
f"{str(self.i_last_name_magazine.get()).capitalize()}, {str(self.i_first_name_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name2_magazine.get()).capitalize()}, {str(self.i_first_name2_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial2_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name3_magazine.get()).capitalize()}, {str(self.i_first_name3_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial3_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name4_magazine.get()).capitalize()}, {str(self.i_first_name4_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial4_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name5_magazine.get()).capitalize()}, {str(self.i_first_name5_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial5_magazine.get()).capitalize()[:1]}, \
{str(self.i_last_name6_magazine.get()).capitalize()}, {str(self.i_first_name6_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial6_magazine.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_magazine.get()).capitalize()}, {str(self.i_first_name7_magazine.get()).capitalize()[:1]}. {str(self.i_middle_initial7_magazine.get()).capitalize()[:1]}. \
(n.d.). \
{self.i_article_title_magazine.get()}. "
            self.output2 = f"{self.i_periodical_title_magazine.get()}, {self.i_volume_number_magazine.get()}"
            self.output3 = f"({self.i_issue_number_magazine.get()}), {self.i_page_number_magazine.get()}. "
            self.i_jn.insert(INSERT, self.output1)
            self.i_jn.insert(INSERT, self.output2, "title_italics")
            self.i_jn.insert(INSERT, self.output3)

    def filipino_activate_action(self):
        if not self.filipino_cite:
            self.filipino_cite = True
            self.magazine_filipino_month_activate.configure(text="English Dates")
            self.i_month_magazine.grid_forget()
            self.i_month_magazine_filipino.grid(row=11, column=0)
        elif self.filipino_cite:
            self.filipino_cite = False
            self.magazine_filipino_month_activate.configure(text="Filipino Dates")
            self.i_month_magazine_filipino.grid_forget()
            self.i_month_magazine.grid(row=11, column=0)

    def clearallentries_magazine(self):
        self.i_year_magazine.delete(0, END)
        self.i_article_title_magazine.delete(0, END)
        self.i_periodical_title_magazine.delete(0, END)
        self.i_volume_number_magazine.delete(0, END)
        self.i_issue_number_magazine.delete(0, END)
        self.i_page_number_magazine.delete(0, END)
        self.i_doi_link_magazine.delete(0, END)
        self.i_month_magazine.delete(0, END)
        self.i_date_magazine.delete(0, END)
        self.i_first_name_magazine.delete(0, END)
        self.i_middle_initial_magazine.delete(0, END)
        self.i_last_name_magazine.delete(0, END)
        self.i_jn.delete(1.0, END)
        if self.author_number_magazine >= 2:
            self.i_last_name2_magazine.delete(0, END)
            self.i_first_name2_magazine.delete(0, END)
            self.i_middle_initial2_magazine.delete(0, END)
            if self.author_number_magazine >= 3:
                self.i_last_name3_magazine.delete(0, END)
                self.i_first_name3_magazine.delete(0, END)
                self.i_middle_initial3_magazine.delete(0, END)
                if self.author_number_magazine >= 4:
                    self.i_last_name4_magazine.delete(0, END)
                    self.i_first_name4_magazine.delete(0, END)
                    self.i_middle_initial4_magazine.delete(0, END)
                    if self.author_number_magazine >= 5:
                        self.i_last_name5_magazine.delete(0, END)
                        self.i_first_name5_magazine.delete(0, END)
                        self.i_middle_initial5_magazine.delete(0, END)
                        if self.author_number_magazine >= 6:
                            self.i_last_name6_magazine.delete(0, END)
                            self.i_first_name6_magazine.delete(0, END)
                            self.i_middle_initial6_magazine.delete(0, END)
                            if self.author_number_magazine >= 7:
                                self.i_last_name7_magazine.delete(0, END)
                                self.i_first_name7_magazine.delete(0, END)
                                self.i_middle_initial7_magazine.delete(0, END)