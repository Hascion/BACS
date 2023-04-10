from tkinter import *
from tkinter import messagebox, ttk

class APAThesisCitation:
    def __init__(self, thesistab):
        self.author_number_thesis = 1
        self.corporate_author_true_thesis = False
        self.no_author_true_thesis = False
        self.no_true_thesis = False
        self.online_true_thesis = False
        self.no_middle_true_thesis = False

        self.last_name_thesis = Label(thesistab, text="Last Name/Surname:", background='#888EF1')
        self.last_name_thesis.grid(row=0, column=0)
        self.i_last_name_thesis = Entry(thesistab)
        self.i_last_name_thesis.grid(row=1, column=0)

        self.first_name_thesis = Label(thesistab, text="First Name:", background='#888EF1')
        self.first_name_thesis.grid(row=0, column=1)
        self.i_first_name_thesis = Entry(thesistab)
        self.i_first_name_thesis.grid(row=1, column=1, padx=10)

        self.middle_initial_thesis = Label(thesistab, text="Middle Initial/Name:", background='#888EF1')
        self.middle_initial_thesis.grid(row=0, column=2)
        self.i_middle_initial_thesis = Entry(thesistab)
        self.i_middle_initial_thesis.grid(row=1, column=2)

        self.no_middle_button_thesis = Button(thesistab, text="No Middle Initial/Name", command=self.no_middle_thesis)
        self.no_middle_button_thesis.grid(row=9, column=2, pady=5)

        self.add_author_button_thesis = Button(thesistab, text="Add Author", command=self.add_author_thesis)
        self.add_author_button_thesis.grid(row=8, column=1, pady=10, padx=5)

        self.corporate_author_button_thesis = Button(thesistab, text="Corporate Author", command=self.corporate_author_thesis)
        self.corporate_author_button_thesis.grid(row=8, column=0, pady=5)

        self.no_author_button_thesis = Button(thesistab, text="Unknown Author", command=self.no_author_thesis)
        self.no_author_button_thesis.grid(row=8, column=2, pady=5)

        self.reset_button_thesis = Button(thesistab, text="Reset Authors", command=self.reset_authors_thesis)
        self.reset_button_thesis.grid(row=9, column=1)

        self.year_thesis = Label(thesistab, text="Year of Publication:", background='#888EF1')
        self.year_thesis.grid(row=10, column=1, pady=5)
        self.i_year_thesis = Entry(thesistab)
        self.i_year_thesis.grid(row=11, column=1, pady=5)

        self.no_button_thesis = Button(thesistab, text="No Year", command=self.no_year_thesis)
        self.no_button_thesis.grid(row=12, column=1, pady=5)

        self.levelof_title_thesis = Label(thesistab, text="Level of Thesis/Dissertation:", background='#888EF1')
        self.levelof_title_thesis.grid(row=13, column=1)
        self.i_levelof_title_thesis = ttk.Combobox(thesistab,
                                           values=["Undergraduate thesis", "Master's thesis", "Doctoral thesis"])
        self.i_levelof_title_thesis.grid(row=14, column=1, pady=5)

        self.research_title_thesis = Label(thesistab, text="Title of Thesis/Dissertation", background='#888EF1')
        self.research_title_thesis.grid(row=15, column=1)
        self.i_research_title_thesis = Entry(thesistab)
        self.i_research_title_thesis.grid(row=16, column=1, pady=5, padx=210)

        self.nameof_school_thesis = Label(thesistab, text="Name of School:", background='#888EF1')
        self.nameof_school_thesis.grid(row=17, column=0)
        self.i_nameof_school_thesis = Entry(thesistab)
        self.i_nameof_school_thesis.grid(row=18, column=0, pady=5)

        self.location_of_thesis = Label(thesistab, text="Location (City, Country):", background='#888EF1')
        self.location_of_thesis.grid(row=17, column=2)
        self.i_location_of_thesis = Entry(thesistab)
        self.i_location_of_thesis.grid(row=18, column=2, pady=5)

        self.i_middle_initial7_thesis = Entry(thesistab)
        self.i_first_name7_thesis = Entry(thesistab)
        self.i_last_name7_thesis = Entry(thesistab)
        self.i_middle_initial6_thesis = Entry(thesistab)
        self.i_first_name6_thesis = Entry(thesistab)
        self.i_last_name6_thesis = Entry(thesistab)
        self.i_middle_initial5_thesis = Entry(thesistab)
        self.i_first_name5_thesis = Entry(thesistab)
        self.i_last_name5_thesis = Entry(thesistab)
        self.i_middle_initial4_thesis = Entry(thesistab)
        self.i_first_name4_thesis = Entry(thesistab)
        self.i_last_name4_thesis = Entry(thesistab)
        self.i_middle_initial3_thesis = Entry(thesistab)
        self.i_first_name3_thesis = Entry(thesistab)
        self.i_last_name3_thesis = Entry(thesistab)
        self.i_middle_initial2_thesis = Entry(thesistab)
        self.i_first_name2_thesis = Entry(thesistab)
        self.i_last_name2_thesis = Entry(thesistab)

        self.display_output_thesis = Button(thesistab, text="English Citation", command=self.printed_thesis_citation)
        self.display_output_thesis.grid(row=23, column=0, pady=5)
        self.display_output_thesis_filipino = Button(thesistab, text = " Filipino Citation", command=self.printed_thesis_citation_Filipino)
        self.display_output_thesis_filipino.grid(row=23, column=2 ,pady=5)

        self.online_button_thesis = Button(thesistab, text="Thesis in Database", command=self.online_thesis)
        self.online_button_thesis.grid(row=19, column=1, pady=10)

        self.database_name_thesis = Label(thesistab, text="Name of Database:", background='#888EF1')
        self.i_database_name_thesis = Entry(thesistab)

        self.accession_number_thesis = Label(thesistab, text="Accession / Order Number:", background='#888EF1')
        self.i_accession_number_thesis = Entry(thesistab)

        self.jn = Label(thesistab, text="Citation:", background='#888EF1')
        self.jn.grid(row=24, column=1)
        self.i_thesis_citation = Text(thesistab, height=5, width=50, font="times 12")
        self.i_thesis_citation.grid(row=25, column=1, pady=5)

        self.clear = Button(thesistab, text="Clear All Entries", command=self.clearallentries_thesis)
        self.clear.grid(row=26, column=1, pady=10)

    def add_author_thesis(self):
        self.corporate_author_button_thesis.configure(state=DISABLED)
        self.no_author_button_thesis.configure(state=DISABLED)
        if self.author_number_thesis == 1:
            self.i_last_name2_thesis.grid(row=2, column=0, pady=10)
            self.i_first_name2_thesis.grid(row=2, column=1, pady=10)
            self.i_middle_initial2_thesis.grid(row=2, column=2, pady=10)
            self.author_number_thesis += 1
            return

        elif self.author_number_thesis == 2:
            self.i_last_name3_thesis.grid(row=3, column=0)
            self.i_first_name3_thesis.grid(row=3, column=1)
            self.i_middle_initial3_thesis.grid(row=3, column=2)
            self.author_number_thesis += 1
            return

        elif self.author_number_thesis == 3:
            self.i_last_name4_thesis.grid(row=4, column=0, pady=10)
            self.i_first_name4_thesis.grid(row=4, column=1, pady=10)
            self.i_middle_initial4_thesis.grid(row=4, column=2, pady=10)
            self.author_number_thesis += 1
            return

        elif self.author_number_thesis == 4:
            self.i_last_name5_thesis.grid(row=5, column=0)
            self.i_first_name5_thesis.grid(row=5, column=1)
            self.i_middle_initial5_thesis.grid(row=5, column=2)
            self.author_number_thesis += 1
            return

        elif self.author_number_thesis == 5:
            self.i_last_name6_thesis.grid(row=6, column=0, pady=10)
            self.i_first_name6_thesis.grid(row=6, column=1, pady=10)
            self.i_middle_initial6_thesis.grid(row=6, column=2, pady=10)
            self.author_number_thesis += 1
            return

        elif self.author_number_thesis == 6:
            self.i_last_name7_thesis.grid(row=7, column=0)
            self.i_first_name7_thesis.grid(row=7, column=1)
            self.i_middle_initial7_thesis.grid(row=7, column=2)
            self.author_number_thesis += 1
            return

        elif self.author_number_thesis == 7:
            self.response = messagebox.askquestion("Too many names!", '''
            The limit of names to be placed in a citation is 7.

            For works with more than 7 names please input the
            last author's name into the last set of boxes.

            Continue inputting citation for more than 7 authors?''')
            if self.response == "yes":
                self.author_number_thesis += 1
            elif self.response == "no":
                self.author_number_thesis -= 1
            self.add_author_button_thesis.configure(state=DISABLED)

    def corporate_author_thesis(self):
        if not self.corporate_author_true_thesis:
            self.last_name_thesis.grid_forget()
            self.i_last_name_thesis.grid_forget()
            self.middle_initial_thesis.grid_forget()
            self.i_middle_initial_thesis.grid_forget()
            self.first_name_thesis.configure(text="Corporate Author Name:")
            self.corporate_author_button_thesis.configure(text="Normal Author/s")
            self.add_author_button_thesis.configure(state=DISABLED)
            self.no_author_button_thesis.configure(state=DISABLED)
            self.corporate_author_true_thesis = True
        elif self.corporate_author_true_thesis:
            self.last_name_thesis.grid(row=0, column=0)
            self.i_last_name_thesis.grid(row=1, column=0)
            self.middle_initial_thesis.grid(row=0, column=2)
            self.i_middle_initial_thesis.grid(row=1, column=2)
            self.first_name_thesis.configure(text="First Name:")
            self.corporate_author_button_thesis.configure(text="Corporate Author")
            self.add_author_button_thesis.configure(state=NORMAL)
            self.no_author_button_thesis.configure(state=NORMAL)
            self.corporate_author_true_thesis = False

    def no_author_thesis(self):
        if not self.no_author_true_thesis:
            self.last_name_thesis.grid_forget()
            self.i_last_name_thesis.grid_forget()
            self.first_name_thesis.grid_forget()
            self.i_first_name_thesis.grid_forget()
            self.middle_initial_thesis.grid_forget()
            self.i_middle_initial_thesis.grid_forget()
            self.no_author_button_thesis.configure(text="With Author/s")
            self.add_author_button_thesis.configure(state=DISABLED)
            self.corporate_author_button_thesis.configure(state=DISABLED)
            self.no_author_true_thesis = True
        elif self.no_author_true_thesis:
            self.last_name_thesis.grid(row=0, column=0)
            self.i_last_name_thesis.grid(row=1, column=0)
            self.first_name_thesis.grid(row=0, column=1)
            self.i_first_name_thesis.grid(row=1, column=1, padx=10)
            self.middle_initial_thesis.grid(row=0, column=2)
            self.i_middle_initial_thesis.grid(row=1, column=2)
            self.no_author_button_thesis.configure(text="Unknown Author")
            self.add_author_button_thesis.configure(state=NORMAL)
            self.corporate_author_button_thesis.configure(state=NORMAL)
            self.no_author_true_thesis = False

    def reset_authors_thesis(self):
        self.first_name_thesis.configure(text="First Name:")
        self.add_author_button_thesis.configure(state=NORMAL)
        self.corporate_author_button_thesis.configure(state=NORMAL)
        self.no_author_button_thesis.configure(state=NORMAL)
        self.corporate_author_button_thesis.configure(text="Corporate Author")
        self.no_author_button_thesis.configure(text="Unknown Author")
        self.author_number_thesis = 1
        self.corporate_author_true_thesis = False
        self.no_author_true_thesis = False
        self.last_name_thesis.grid(row=0, column=0)
        self.i_last_name_thesis.grid(row=1, column=0)
        self.first_name_thesis.grid(row=0, column=1)
        self.i_first_name_thesis.grid(row=1, column=1, padx=10)
        self.middle_initial_thesis.grid(row=0, column=2)
        self.i_middle_initial_thesis.grid(row=1, column=2)
        self.i_last_name2_thesis.grid_forget()
        self.i_first_name2_thesis.grid_forget()
        self.i_middle_initial2_thesis.grid_forget()
        self.i_last_name3_thesis.grid_forget()
        self.i_first_name3_thesis.grid_forget()
        self.i_middle_initial3_thesis.grid_forget()
        self.i_last_name4_thesis.grid_forget()
        self.i_first_name4_thesis.grid_forget()
        self.i_middle_initial4_thesis.grid_forget()
        self.i_last_name5_thesis.grid_forget()
        self.i_first_name5_thesis.grid_forget()
        self.i_middle_initial5_thesis.grid_forget()
        self.i_last_name6_thesis.grid_forget()
        self.i_first_name6_thesis.grid_forget()
        self.i_middle_initial6_thesis.grid_forget()
        self.i_last_name7_thesis.grid_forget()
        self.i_first_name7_thesis.grid_forget()
        self.i_middle_initial7_thesis.grid_forget()

    def online_thesis(self):
        if not self.online_true_thesis:
            self.database_name_thesis.grid(row=21, column=0)
            self.i_database_name_thesis.grid(row=22, column=0, pady=5)
            self.accession_number_thesis.grid(row=21, column=2)
            self.i_accession_number_thesis.grid(row=22, column=2, pady=5)
            self.online_button_thesis.configure(text="Thesis not in Database")
            self.online_true_thesis = True
            if self.no_true_thesis and self.no_middle_true_thesis:
                self.display_output_thesis.configure(command=self.online_thesis_citation_nd_nomiddlename)
                self.display_output_thesis_filipino.configure(command=self.online_thesis_citation_nd_nomiddlename_Filipino)
            elif self.no_middle_true_thesis:
                self.display_output_thesis.configure(command=self.online_thesis_citation_nomiddlename)
                self.display_output_thesis_filipino.configure(command=self.online_thesis_citation_nomiddlename_Filipino)
            elif self.no_true_thesis:
                self.display_output_thesis.configure(command=self.online_thesis_citation_nd)
            elif not self.no_true_thesis:
                self.display_output_thesis.configure(command=self.online_thesis_citation)
                self.display_output_thesis_filipino.configure(command=self.online_thesis_citation_Filipino)

        elif self.online_true_thesis:
            self.database_name_thesis.grid_forget()
            self.i_database_name_thesis.grid_forget()
            self.accession_number_thesis.grid_forget()
            self.i_accession_number_thesis.grid_forget()
            self.online_button_thesis.configure(text="Thesis in Database")
            self.online_true_thesis = False
            if self.no_true_thesis:
                self.display_output_thesis.configure(command=self.printed_thesis_citation_nd)
            elif not self.no_true_thesis:
                self.display_output_thesis.configure(command=self.printed_thesis_citation)
                self.display_output_thesis_filipino.configure(command=self.printed_thesis_citation_Filipino)

    def no_middle_thesis(self):
        if not self.no_middle_true_thesis:
            self.i_middle_initial_thesis.configure(state=DISABLED)
            self.i_middle_initial2_thesis.configure(state=DISABLED)
            self.i_middle_initial4_thesis.configure(state=DISABLED)
            self.i_middle_initial3_thesis.configure(state=DISABLED)
            self.i_middle_initial5_thesis.configure(state=DISABLED)
            self.i_middle_initial6_thesis.configure(state=DISABLED)
            self.i_middle_initial7_thesis.configure(state=DISABLED)
            self.no_middle_button_thesis.configure(text="With Middle Initial/Name")
            self.no_middle_true_thesis = True
            if self.online_true_thesis:
                self.display_output_thesis.configure(command=self.online_thesis_citation_nomiddlename)
                self.display_output_thesis_filipino.configure(command=self.online_thesis_citation_nomiddlename_Filipino)
            elif not self.online_true_thesis:
                self.display_output_thesis.configure(command=self.printed_thesis_citation_nomiddlename)
                self.display_output_thesis_filipino.configure(command=self.printed_thesis_citation_nomiddlename_Filipino)
        elif self.no_middle_true_thesis:
            self.i_middle_initial_thesis.configure(state=NORMAL)
            self.i_middle_initial2_thesis.configure(state=NORMAL)
            self.i_middle_initial4_thesis.configure(state=NORMAL)
            self.i_middle_initial3_thesis.configure(state=NORMAL)
            self.i_middle_initial5_thesis.configure(state=NORMAL)
            self.i_middle_initial6_thesis.configure(state=NORMAL)
            self.i_middle_initial7_thesis.configure(state=NORMAL)
            self.no_middle_button_thesis.configure(text="No Middle Initial/Name")
            self.no_middle_true_thesis = False
            if self.online_true_thesis:
                self.display_output_thesis.configure(command=self.online_thesis_citation)
            elif not self.online_true_thesis:
                self.display_output_thesis.configure(command=self.printed_thesis_citation)

    def no_year_thesis(self):
        if not self.no_true_thesis:
            self.year_thesis.grid_forget()
            self.i_year_thesis.grid_forget()
            self.no_button_thesis.configure(text="With Year")
            self.no_true_thesis = True
            if self.online_true_thesis:
                self.display_output_thesis.configure(command=self.online_thesis_citation_nd)
                self.display_output_thesis_filipino.configure(command=self.online_thesis_citation_Filipino)
            elif not self.online_true_thesis and self.no_middle_true_thesis:
                self.display_output_thesis.configure(command=self.printed_thesis_citation_nd_nomiddlename)
                self.display_output_thesis_filipino.configure(command=self.printed_thesis_citation_nomiddlename_Filipino)
            elif self.online_true_thesis:
                self.display_output_thesis.configure(command=self.printed_thesis_citation_nd)
                self.display_output_thesis_filipino.configure(command=self.printed_thesis_citation_Filipino)
        elif self.no_true_thesis:
            self.year_thesis.grid(row=10, column=1, pady=5)
            self.i_year_thesis.grid(row=11, column=1, pady=5)
            self.no_button_thesis.configure(text="No Year")
            self.no_true_thesis = False
            if self.online_true_thesis:
                self.display_output_thesis.configure(command=self.online_thesis_citation)
            elif not self.online_true_thesis:
                self.display_output_thesis.configure(command=self.printed_thesis_citation)

# ONLINE THESIS CITATION

    def online_thesis_citation(self):
        self.i_thesis_citation.delete(1.0, END)
        self.i_thesis_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_thesis_citation.tag_config("title_italics", font="times 12 italic")

        if self.corporate_author_true_thesis and self.author_number_thesis == 1:
            self.output1 = \
f"{self.i_first_name_thesis.get()}. \
({self.i_year_thesis.get()}). "

# beyond this line, pare-parehas na lang nung code for each condition

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.no_author_true_thesis and self.author_number_thesis == 1:
            self.output1 = \
f"{self.i_research_title_thesis.get()}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 1:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 2:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 3:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 4:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 5:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 6:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 7:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial7_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 8:

            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial7_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# ONLINE THESIS CITATION WITH NO MIDDLE INITIAL

    def online_thesis_citation_nomiddlename(self):
        self.i_thesis_citation.delete(1.0, END)
        self.i_thesis_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_thesis_citation.tag_config("title_italics", font="times 12 italic")

        if self.author_number_thesis == 1 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 2 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}.\
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 3 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 4 and self.no_middle_true_thesis :
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 5 and self.no_middle_true_thesis :
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 6 and self.no_middle_true_thesis :
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 7 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 8 and self.no_middle_true_thesis:

            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# ONLINE THESIS CITATION WITH NO DATE

    def online_thesis_citation_nd(self):
        self.i_thesis_citation.delete(1.0, END)
        self.i_thesis_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_thesis_citation.tag_config("title_italics", font="times 12 italic")

        if self.corporate_author_true_thesis and self.author_number_thesis == 1:
            self.output1 = f"{self.i_first_name_thesis.get()}. (n.d.)."
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.no_author_true_thesis and self.author_number_thesis == 1:
            self.output1 = f"{self.i_research_title_thesis.get()}. (n.d.). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 1:
            self.output1 = \
                f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. " \
                f"{str(self.i_middle_initial_thesis.get()).capitalize()[:1]}. (n.d.). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 2:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}. \
(n.d.) "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 3:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 4:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 5:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 6:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 7:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial7_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 8:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial7_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# ONLINE THESIS CITATION WITH NO DATE AND NO MIDDLE INITIAL

    def online_thesis_citation_nd_nomiddlename (self):
        self.i_thesis_citation.delete(1.0, END)
        self.i_thesis_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_thesis_citation.tag_config("title_italics", font="times 12 italic")

        if self.author_number_thesis and self.no_middle_true_thesis == 1:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. (n.d.). "

            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis and self.no_middle_true_thesis == 2:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. (n.d.) "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis and self.no_middle_true_thesis == 3:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis and self.no_middle_true_thesis == 4:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis and self.no_middle_true_thesis == 5:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis and self.no_middle_true_thesis == 6:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis and self.no_middle_true_thesis == 7:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis and self.no_middle_true_thesis == 8:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# PRINTED CITATION

    def printed_thesis_citation(self):
        self.i_thesis_citation.delete(1.0, END)
        self.i_thesis_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_thesis_citation.tag_config("title_italics", font="times 12 italic")

        if self.corporate_author_true_thesis and self.author_number_thesis == 1:
            self.output1 = \
f"{self.i_first_name_thesis.get()}. \
({self.i_year_thesis.get()}). "

# under this lines, pare-parehas na lang nung code; therefore madali na lang mag-edit

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.no_author_true_thesis and self.author_number_thesis == 1:

            self.output1 = \
f"{self.i_research_title_thesis.get()}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()}"

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 1 author

        elif self.author_number_thesis == 1:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 2 authors

        elif self.author_number_thesis == 2:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 3 authors

        elif self.author_number_thesis == 3:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()})."

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 4 authors

        elif self.author_number_thesis == 4:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()})."

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 5 authors

        elif self.author_number_thesis == 5:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()})."

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 6 authors

        elif self.author_number_thesis == 6:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()})."

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 7 authors

        elif self.author_number_thesis == 7:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial7_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 8 authors

        elif self.author_number_thesis == 8:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial7_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
            {self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# PRINTED CITATION WITH NO MIDDLE NAME

    def printed_thesis_citation_nomiddlename(self):
        self.i_thesis_citation.delete(1.0, END)
        self.i_thesis_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_thesis_citation.tag_config("title_italics", font="times 12 italic")

        if self.author_number_thesis == 1 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 2 authors

        elif self.author_number_thesis == 2 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 3 authors

        elif self.author_number_thesis == 3 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}.\
({self.i_year_thesis.get()})."

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 4 authors

        elif self.author_number_thesis == 4 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}.\
({self.i_year_thesis.get()})."

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 5 authors

        elif self.author_number_thesis == 5 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()})."

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 6 authors

        elif self.author_number_thesis == 6 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()})."

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 7 authors

        elif self.author_number_thesis == 7 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
{self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# 8 authors

        elif self.author_number_thesis == 8 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. \
({self.i_year_thesis.get()}). "

            self.output2 = f"{self.i_research_title_thesis.get()} "

            self.output3 = f"(Unpublished {str(self.i_levelof_title_thesis.get()).lower()}). \
            {self.i_nameof_school_thesis.get()}, ({self.i_location_of_thesis.get()})."

            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# PRINTED CITATION NO DATE

    def printed_thesis_citation_nd(self):
        self.i_thesis_citation.delete(1.0, END)
        self.i_thesis_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_thesis_citation.tag_config("title_italics", font="times 12 italic")

        if self.corporate_author_true_thesis and self.author_number_thesis == 1:
            self.output1 = \
f"{self.i_first_name_thesis.get()}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.no_author_true_thesis and self.author_number_thesis == 1:
            self.output1 = \
f"{self.i_research_title_thesis.get()}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 1:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 2:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 3:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 4:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 5:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 6:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 7:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}, & \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial7_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 8:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}, \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}, ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial7_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# PRINTED CITATION WITH NO DATE AND NO MIDDLE INITIAL

    def printed_thesis_citation_nd_nomiddlename(self):

        self.i_thesis_citation.delete(1.0, END)
        self.i_thesis_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_thesis_citation.tag_config("title_italics", font="times 12 italic")

        if self.author_number_thesis == 1 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 2 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 3 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 4 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 5 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 6 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 7 and self.no_middle_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        elif self.author_number_thesis == 8 and self.no_middle_true_thesis == 8:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. \
(n.d.). "
            self.output2 = f"{self.i_research_title_thesis.get()}. "

            self.output3 = f"({self.i_levelof_title_thesis.get()}). Retrieved from " \
                           f"{self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})"
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

# FILIPINO PRINTED THESIS CITATIONS

    def printed_thesis_citation_Filipino(self):
        self.nodate = "n.d."
        self.i_thesis_citation.delete(1.0, END)
        self.i_thesis_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_thesis_citation.tag_config("title_italics", font="times 12 italic")

        # NORMAL CITATIONS YEAR ONLY 1 - 7

        if self.author_number_thesis == 1 and not self.no_author_true_thesis \
                and not self.corporate_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 2 and not self.no_author_true_thesis \
                and not self.corporate_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 3 and not self.no_true_thesis and not self.no_author_true_thesis \
                and not self.corporate_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 4 and not self.no_true_thesis and not self.no_author_true_thesis \
                and not self.corporate_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 5 and not self.no_true_thesis and not self.no_author_true_thesis \
                and not self.corporate_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 6 and not self.no_true_thesis and not self.no_author_true_thesis \
                and not self.corporate_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}., ... ({self.i_year_thesis.get()}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 7 and not self.no_true_thesis and not self.no_author_true_thesis \
                and not self.corporate_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        # NORMAL AUTHORS NO DATE 1 - 7

        if self.author_number_thesis == 1 and self.no_true_thesis and not self.corporate_author_true_thesis and not self.no_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 2 and self.no_true_thesis and not self.corporate_author_true_thesis and not self.no_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 3 and self.no_true_thesis and not self.corporate_author_true_thesis and not self.no_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 4 and self.no_true_thesis and not self.corporate_author_true_thesis and not self.no_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 5 and self.no_true_thesis and not self.corporate_author_true_thesis and not self.no_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 6 and self.no_true_thesis and not self.corporate_author_true_thesis and not self.no_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}. ... ({self.nodate}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 7 and self.no_true_thesis and not self.corporate_author_true_thesis and not self.no_author_true_thesis:
            self.output1 = \
                f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial7_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

    def printed_thesis_citation_nomiddlename_Filipino(self):
        self.nodate = "n.d."
        self.i_thesis_citation.delete(1.0, END)
        self.i_thesis_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_thesis_citation.tag_config("title_italics", font="times 12 italic")
        # NO MIDDLE INITIAL

        if self.author_number_thesis == 1 and self.no_middle_true_thesis:
                self.output1 = \
                    f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 2 and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 3 and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 4 and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 5 and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 6 and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., ... ({self.i_year_thesis.get()}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 7 and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

    def printed_thesis_citation_nd_nomiddlename_Filipino(self):
        self.nodate = "n.d."
        self.i_thesis_citation.delete(1.0, END)
        self.i_thesis_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_thesis_citation.tag_config("title_italics", font="times 12 italic")

        # NO MIDDLE INITIAL AND YEAR

        if self.author_number_thesis == 1 and self.no_true_thesis and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 2 and self.no_true_thesis and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., &\
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 3 and self.no_true_thesis and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 4 and self.no_true_thesis and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 5 and self.no_true_thesis and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 6 and self.no_true_thesis and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., ... ({self.nodate}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 7 and self.no_true_thesis and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"(Hindi nalathalang {str(self.i_levelof_title_thesis.get().lower())}). {self.i_nameof_school_thesis.get()}. ({self.i_location_of_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)
# FILIPINO ONLINE THESIS CITATIONS

    def online_thesis_citation_Filipino(self):
        self.nodate = "n.d."
        self.i_thesis_citation.delete(1.0, END)
        self.i_thesis_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_thesis_citation.tag_config("title_italics", font="times 12 italic")

        # NORMAL CITATIONS YEAR ONLY 1 - 7

        if self.author_number_thesis == 1 and not self.no_author_true_thesis \
                and not self.corporate_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 2 and not self.no_author_true_thesis \
                and not self.corporate_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 3 and not self.no_true_thesis and not self.no_author_true_thesis \
                and not self.corporate_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 4 and not self.no_true_thesis and not self.no_author_true_thesis \
                and not self.corporate_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 5 and not self.no_true_thesis and not self.no_author_true_thesis \
                and not self.corporate_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 6 and not self.no_true_thesis and not self.no_author_true_thesis \
                and not self.corporate_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}., ... ({self.i_year_thesis.get()}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 7 and not self.no_true_thesis and not self.no_author_true_thesis \
                and not self.corporate_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        # NORMAL AUTHORS NO DATE 1 - 7

        if self.author_number_thesis == 1 and self.no_true_thesis and not self.corporate_author_true_thesis and not self.no_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 2 and self.no_true_thesis and not self.corporate_author_true_thesis and not self.no_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 3 and self.no_true_thesis and not self.corporate_author_true_thesis and not self.no_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 4 and self.no_true_thesis and not self.corporate_author_true_thesis and not self.no_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 5 and self.no_true_thesis and not self.corporate_author_true_thesis and not self.no_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 6 and self.no_true_thesis and not self.corporate_author_true_thesis and not self.no_author_true_thesis:
            self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}. ... ({self.nodate}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 7 and self.no_true_thesis and not self.corporate_author_true_thesis and not self.no_author_true_thesis:
            self.output1 = \
                f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial6_thesis.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. {str(self.i_middle_initial7_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
            self.output2 = f" {self.i_research_title_thesis.get()}. "
            self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
            self.i_thesis_citation.insert(INSERT, self.output1)
            self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
            self.i_thesis_citation.insert(INSERT, self.output3)

    def online_thesis_citation_nomiddlename_Filipino(self):
        self.nodate = "n.d."
        self.i_thesis_citation.delete(1.0, END)
        self.i_thesis_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_thesis_citation.tag_config("title_italics", font="times 12 italic")
        # NO MIDDLE INITIAL

        if self.author_number_thesis == 1 and self.no_middle_true_thesis:
                self.output1 = \
                    f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 2 and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 3 and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 4 and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 5 and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 6 and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., ... ({self.i_year_thesis.get()}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 7 and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. ({self.i_year_thesis.get()}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

    def online_thesis_citation_nd_nomiddlename_Filipino(self):
        self.nodate = "n.d."
        self.i_thesis_citation.delete(1.0, END)
        self.i_thesis_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_thesis_citation.tag_config("title_italics", font="times 12 italic")

        # NO MIDDLE INITIAL AND YEAR

        if self.author_number_thesis == 1 and self.no_true_thesis and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 2 and self.no_true_thesis and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 3 and self.no_true_thesis and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 4 and self.no_true_thesis and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 5 and self.no_true_thesis and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., & \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 6 and self.no_true_thesis and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., ... ({self.nodate}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)

        if self.author_number_thesis == 7 and self.no_true_thesis and self.no_middle_true_thesis:
                self.output1 = \
f"{str(self.i_last_name_thesis.get()).capitalize()}, {str(self.i_first_name_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name2_thesis.get()).capitalize()}, {str(self.i_first_name2_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name3_thesis.get()).capitalize()}, {str(self.i_first_name3_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name4_thesis.get()).capitalize()}, {str(self.i_first_name4_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name5_thesis.get()).capitalize()}, {str(self.i_first_name5_thesis.get()).capitalize()[:1]}., \
{str(self.i_last_name6_thesis.get()).capitalize()}, {str(self.i_first_name6_thesis.get()).capitalize()[:1]}., ... \
{str(self.i_last_name7_thesis.get()).capitalize()}, {str(self.i_first_name7_thesis.get()).capitalize()[:1]}. ({self.nodate}). "
                self.output2 = f" {self.i_research_title_thesis.get()}. "
                self.output3 = f"({self.i_levelof_title_thesis.get()}). Kinuha mula sa {self.i_database_name_thesis.get()}. ({self.i_accession_number_thesis.get()})."
                self.i_thesis_citation.insert(INSERT, self.output1)
                self.i_thesis_citation.insert(INSERT, self.output2, "title_italics")
                self.i_thesis_citation.insert(INSERT, self.output3)


# CLEAR ALL ENTRIES

    def clearallentries_thesis(self):
        self.i_year_thesis.delete(0, END)
        self.i_levelof_title_thesis.delete(0, END)
        self.i_research_title_thesis.delete(0, END)
        self.i_nameof_school_thesis.delete(0, END)
        self.i_location_of_thesis.delete(0, END)
        self.i_database_name_thesis.delete(0, END)
        self.i_first_name_thesis.delete(0, END)
        self.i_middle_initial_thesis.delete(0, END)
        self.i_last_name_thesis.delete(0, END)
        self.i_thesis_citation.delete(1.0, END)
        if self.author_number_thesis >= 2:
            self.i_last_name2_thesis.delete(0, END)
            self.i_first_name2_thesis.delete(0, END)
            self.i_middle_initial2_thesis.delete(0, END)
            if self.author_number_thesis >= 3:
                self.i_last_name3_thesis.delete(0, END)
                self.i_first_name3_thesis.delete(0, END)
                self.i_middle_initial3_thesis.delete(0, END)
                if self.author_number_thesis >= 4:
                    self.i_last_name4_thesis.delete(0, END)
                    self.i_first_name4_thesis.delete(0, END)
                    self.i_middle_initial4_thesis.delete(0, END)
                    if self.author_number_thesis >= 5:
                        self.i_last_name5_thesis.delete(0, END)
                        self.i_first_name5_thesis.delete(0, END)
                        self.i_middle_initial5_thesis.delete(0, END)
                        if self.author_number_thesis >= 6:
                            self.i_last_name6_thesis.delete(0, END)
                            self.i_first_name6_thesis.delete(0, END)
                            self.i_middle_initial6_thesis.delete(0, END)
                            if self.author_number_thesis >= 7:
                                self.i_last_name7_thesis.delete(0, END)
                                self.i_first_name7_thesis.delete(0, END)
                                self.i_middle_initial7_thesis.delete(0, END)

