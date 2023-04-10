from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class APAFilmCitation:
    def __init__(self, filmtab):
        self.producer_number_film = 1
        self.director_number_film = 1
        self.filipino_cite = False

        self.producer = Label(filmtab, text="Name of Producer", font=("arial", 14, "bold"), background='#5ACAEC')
        self.producer.grid(row=0, column=2)

        self.last_name_film_producer = Label(filmtab, text="Last Name/Surname:", background='#5ACAEC')
        self.last_name_film_producer.grid(row=1, column=1)
        self.i_last_name_film_producer = Entry(filmtab)
        self.i_last_name_film_producer.grid(row=2, column=1, padx=5)

        self.first_name_film_producer = Label(filmtab, text="First Name:", background='#5ACAEC')
        self.first_name_film_producer.grid(row=1, column=2, padx=5)
        self.i_first_name_film_producer = Entry(filmtab)
        self.i_first_name_film_producer.grid(row=2, column=2, padx=5)

        self.middle_initial_film_producer = Label(filmtab, text="Middle Initial/Name:", background='#5ACAEC')
        self.middle_initial_film_producer.grid(row=1, column=3, padx=5)
        self.i_middle_initial_film_producer = Entry(filmtab)
        self.i_middle_initial_film_producer.grid(row=2, column=3, padx=5)

        self.reset_producer_film = Button(filmtab, text="Reset Producer", command=self.reset_producer_film)
        self.reset_producer_film.grid(row=3, column=2, pady=5)

        # NAME OF DIRECTOR

        self.producer = Label(filmtab, text="Name of Director", font=("arial", 14, "bold"), background='#5ACAEC')
        self.producer.grid(row=4, column=2)

        self.last_name_film_director = Label(filmtab, text="Last Name/Surname:", background='#5ACAEC')
        self.last_name_film_director.grid(row=5, column=1)
        self.i_last_name_film_director = Entry(filmtab)
        self.i_last_name_film_director.grid(row=6, column=1, padx=5)

        self.first_name_film_director = Label(filmtab, text="First Name:", background='#5ACAEC')
        self.first_name_film_director.grid(row=5, column=2, padx=5)
        self.i_first_name_film_director = Entry(filmtab)
        self.i_first_name_film_director.grid(row=6, column=2, padx=5)

        self.middle_initial_film_director = Label(filmtab, text="Middle Initial/Name:", background='#5ACAEC')
        self.middle_initial_film_director.grid(row=5, column=3, padx=5)
        self.i_middle_initial_film_director = Entry(filmtab)
        self.i_middle_initial_film_director.grid(row=6, column=3, padx=5)

        self.reset_director_film = Button(filmtab, text="Reset Director", command=self.reset_director_film)
        self.reset_director_film.grid(row=7, column=2, pady=5)

        # NOTE REGARDING PRODUCERS AND DIRECTORS

        self.note_regarding_producersanddirectors = Label(filmtab, text="NOTE: A film must always have a producer and director.",
                                                          font=("arial", 10, "italic"), background='#5ACAEC')
        self.note_regarding_producersanddirectors.grid(row=8, column=2, pady=5)

        # DATE OF PUBLICATION

        self.dateofpublication = Label(filmtab, text="Date of Publication", font=("arial", 14, "bold"), background='#5ACAEC')
        self.dateofpublication.grid(row=9, column=2, pady=5, padx=190)

        self.date_month_film = Label(filmtab, text="Month:", background='#5ACAEC')
        self.date_month_film.grid(row=11, column=1)
        self.i_date_month_film = ttk.Combobox(filmtab,
                                                     values=["January", "February", "March", "April", "May", "June"
                                                         , "July", "August", "September", "October", "November",
                                                             "December"])
        self.i_date_month_film.grid(row=12, column=1, pady=5)

        self.i_date_month_filipino_film = ttk.Combobox(filmtab,
                                                 values=["Enero", "Pebrero", "Marso", "Abril", "Mayo", "Hunyo"
                                                     , "Hulyo", "Agosto", "Setyembre", "Oktubre", "Nobyembre",
                                                         "Disyembre"])

        self.date_day_film = Label(filmtab, text="Day (Numerical Form):", background='#5ACAEC')
        self.date_day_film.grid(row=11, column=2)
        self.i_date_day_film = ttk.Combobox(filmtab,
                                                 values=["1", "2", "3", "4", "5", "6"
                                                     , "7", "8", "9", "10", "11",
                                                         "12", "13", "14", "15", "16",
                                                         "17", "18", "19", "20", "21",
                                                         "22", "23", "24", "25", "26", "27",
                                                         "28", "29", "30", "31"])
        self.i_date_day_film.grid(row=12, column=2, pady=5)

        self.date_year_film = Label(filmtab, text="Year:", background='#5ACAEC')
        self.date_year_film.grid(row=11, column=3)
        self.i_date_year_film = Entry(filmtab)
        self.i_date_year_film.grid(row=12, column=3, pady=5)

        self.filipino_activate_button = Button(filmtab, text="Filipino Dates" , command=self.filipino_activate_action)
        self.filipino_activate_button.grid(row=13, column=2, pady=5)

        self.note_regarding_dates = Label(filmtab, text="NOTE: A film must always have a date of publication", font=("arial", 10, "italic"), background='#5ACAEC')
        self.note_regarding_dates.grid(row=14, column=2, pady=5)

        # TITLE / COUNTRY OF ORIGIN / STUDIO OR DISTRIBUTOR

        self.title_film = Label(filmtab, text="Title of Film:", background='#5ACAEC')
        self.title_film.grid(row=15, column=1)
        self.i_title_film = Entry(filmtab)
        self.i_title_film.grid(row=16, column=1)

        self.country_of_origin_film = Label(filmtab, text="Country of Origin:", background='#5ACAEC')
        self.country_of_origin_film.grid(row=15, column=2)
        self.i_country_of_origin = Entry(filmtab)
        self.i_country_of_origin.grid(row=16, column=2)

        self.studio_or_distributor_film = Label(filmtab, text="Studio/Distributor:", background='#5ACAEC')
        self.studio_or_distributor_film.grid(row=15, column=3)
        self.i_studio_or_distributor = Entry(filmtab)
        self.i_studio_or_distributor.grid(row=16, column=3)

        self.display_output_film = Button(filmtab, text="English Cite!", command=self.film_citation)
        self.display_output_film.grid(row=18, column=1, pady=5)
        self.display_output_film_filipino = Button(filmtab, text = "Filipino Cite!", command=self.film_citation_Filipino)
        self.display_output_film_filipino.grid(row=18, column=3, pady=5)

        self.display_output_film_filipino.configure(state=DISABLED)

        self.film_citation = Label(filmtab, text="Citation:", background='#5ACAEC')
        self.film_citation.grid(row=19, column=2)
        self.i_film_citation = Text(filmtab, height=5, width=50, font="times 12")
        self.i_film_citation.grid(row=20, column=2, pady=5)

        # CLEAR ALL ENTRIES BUTTON

        self.clearallentries = Button(filmtab, text="Clear all entries", command=self.clearallentries_film)
        self.clearallentries.grid (row=21, column=2, pady=5)

    def reset_producer_film(self):
        self.producer_number_film = 1
        self.i_last_name_film_producer.delete(0, END)
        self.i_first_name_film_producer.delete(0, END)
        self.i_middle_initial_film_producer.delete(0, END)

    def reset_director_film(self):
        self.director_number_film_number_film = 1
        self.i_last_name_film_director.delete(0, END)
        self.i_first_name_film_director.delete(0, END)
        self.i_middle_initial_film_director.delete(0, END)

    def filipino_activate_action(self):
        if not self.filipino_cite:
            self.filipino_cite = True
            self.filipino_activate_button.configure(text="English Dates")
            self.i_date_month_film.grid_forget()
            self.i_date_month_filipino_film.grid(row=12, column=1, pady=5)
            self.display_output_film.configure(state=DISABLED)
            self.display_output_film_filipino.configure(state=NORMAL)
        elif self.filipino_cite:
            self.display_output_film.configure(state=NORMAL)
            self.display_output_film_filipino.configure(state=DISABLED)
            self.filipino_cite = False
            self.filipino_activate_button.configure(text="Filipino Dates")
            self.i_date_month_filipino_film.grid_forget()
            self.i_date_month_film.grid(row=12, column=1, pady=5)

    def film_citation(self):
        self.nodate = "n.d."
        self.i_film_citation.delete(1.0, END)
        self.i_film_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_film_citation.tag_config("title_italics", font="times 12 italic")

        if self.producer_number_film == 1 and self.director_number_film == 1:
            self.output1 = \
                f"{str(self.i_last_name_film_producer.get()).capitalize()}, {str(self.i_first_name_film_producer.get()).capitalize()[:1]}.{str(self.i_middle_initial_film_producer.get()).capitalize()[:1]}. (Producer), \
{str(self.i_last_name_film_director.get()).capitalize()}, {str(self.i_first_name_film_director.get()).capitalize()[:1]}.{str(self.i_middle_initial_film_director.get()).capitalize()[:1]}. (Director)," \
                f"({self.i_date_year_film.get()}, {str(self.i_date_month_film.get()).capitalize()} {self.i_date_day_film.get()})."
            self.output2 = \
                f"{self.i_title_film.get()}"
            self.output3 = \
                f" [Motion Picture]. {self.i_country_of_origin.get()}: {self.i_studio_or_distributor.get()}"
            self.i_film_citation.insert(INSERT, self.output1)
            self.i_film_citation.insert(INSERT, self.output2, "title_italics")
            self.i_film_citation.insert(INSERT, self.output3)

    def film_citation_Filipino(self):
        self.nodate = "n.d."
        self.i_film_citation.delete(1.0, END)
        self.i_film_citation.tag_add("title_italics", "1.0", "1.0 lineend")
        self.i_film_citation.tag_config("title_italics", font="times 12 italic")

        # NORMAL CITATIONS

        if self.producer_number_film == 1 and self.director_number_film == 1:
            self.output1 = \
                f"{str(self.i_last_name_film_producer.get()).capitalize()}, {str(self.i_first_name_film_producer.get()).capitalize()[:1]}.{str(self.i_middle_initial_film_producer.get()).capitalize()[:1]}. (Prodyuser), \
{str(self.i_last_name_film_director.get()).capitalize()}, {str(self.i_first_name_film_director.get()).capitalize()[:1]}.{str(self.i_middle_initial_film_director.get()).capitalize()[:1]}. (Direktor)," \
                f"({self.i_date_year_film.get()}, {str(self.i_date_month_filipino_film.get()).capitalize()} {self.i_date_day_film.get()})."
            self.output2 = \
                f"{self.i_title_film.get()} [Pelikula]. "
            self.output3 = \
                f"{self.i_country_of_origin.get()}: {self.i_studio_or_distributor.get()}"
            self.i_film_citation.insert(INSERT, self.output1)
            self.i_film_citation.insert(INSERT, self.output2, "title_italics")
            self.i_film_citation.insert(INSERT, self.output3)

    def clearallentries_film(self):
        self.i_first_name_film_producer.delete(0, END)
        self.i_first_name_film_director.delete(0, END)
        self.i_middle_initial_film_producer.delete(0, END)
        self.i_middle_initial_film_director.delete(0, END)
        self.i_last_name_film_producer.delete(0, END)
        self.i_last_name_film_director.delete(0, END)
        self.i_date_year_film.delete(0, END)
        self.i_date_month_film.delete(0, END)
        self.i_date_day_film.delete(0, END)
        self.i_date_month_filipino_film.delete(0, END)
        self.i_title_film.delete(0, END)
        self.i_country_of_origin.delete(0, END)
        self.i_studio_or_distributor.delete(1.0, END)













