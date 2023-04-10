from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from ttkthemes import ThemedStyle
from PIL import ImageTk, Image

from book_citation_functions import APABookCitation
from journal_citation_functions import APAJournalCitation
from magazine_citation_functions import APAMagazineCitation
from thesis_citation_functions import APAThesisCitation
from website_citation_functions import APAWebsiteCitation
from film_citation_functions import APAFilmCitation
from help_citation_functions import APAHelpCitation

root = tk.ThemedTk()
root.title("Bilingual APA Citation Synthesizer")
root.configure(background='#FF6C60')
root.iconbitmap("images/logo.ico")
root.get_themes()
root.set_theme ("radiance")
img = PhotoImage(file="images/Background for Root.png")
img = img.subsample(1, 1)

background = Label(root, image=img, bd=0)
background.pack(fill='both', expand=True)
background.image = img
tabControl = ttk.Notebook(background)
background.rowconfigure(0, weight=100)
background.rowconfigure(3, weight=100)
background.columnconfigure(0, weight=100)
background.columnconfigure(3, weight=100)



def mousewheel1(event):
    shift = (event.state & 0x1) != 0
    scroll = -1 if event.delta > 0 else 1
    if shift:
        booktabcanvas.xview_scroll(scroll, "units")
        journaltabcanvas.xview_scroll(scroll, "units")
        websitetabcanvas.xview_scroll(scroll, "units")
        magazinetabcanvas.xview_scroll(scroll, "units")
        thesistabcanvas.xview_scroll(scroll, "units")
        filmtabcanvas.xview_scroll(scroll, "units")
    else:
        booktabcanvas.yview_scroll(scroll, "units")
        journaltabcanvas.yview_scroll(scroll, "units")
        websitetabcanvas.yview_scroll(scroll, "units")
        magazinetabcanvas.yview_scroll(scroll, "units")
        thesistabcanvas.yview_scroll(scroll, "units")
        filmtabcanvas.yview_scroll(scroll, "units")


def book_scroll_bar(event):
    booktabcanvas.configure(scrollregion=booktabcanvas.bbox("all"))
    journaltabcanvas.configure(scrollregion=journaltabcanvas.bbox("all"))
    websitetabcanvas.configure(scrollregion=websitetabcanvas.bbox("all"))
    magazinetabcanvas.configure(scrollregion=magazinetabcanvas.bbox("all"))
    thesistabcanvas.configure(scrollregion=thesistabcanvas.bbox("all"))
    filmtabcanvas.configure(scrollregion=thesistabcanvas.bbox("all"))



# Book Scroll
booktabcanvas = Canvas(tabControl)
booktab = Frame(booktabcanvas)
booktabcanvas.config(width=850, height=650)
booktabcanvas.create_window((7, 5), window=booktab, anchor="nw", tags="frame")
tabControl.add(booktabcanvas, text='Book')  # if nauna ito sa bookscroller, maboboblock
booktab.configure(background='#74E1CA')
booktabcanvas.configure(background='#74E1CA')


# Website Scroll
websitetabcanvas = Canvas(tabControl)
websitetabcanvas.config(width=850, height=650)
websitetab = Frame(websitetabcanvas)
websitetabcanvas.create_window((7, 5), window=websitetab, anchor="nw", tags="frame")
tabControl.add(websitetabcanvas, text='Website')
websitetab.configure(background='#58A7FA')
websitetabcanvas.configure(background='#58A7FA')

# Journal Scroll
journaltabcanvas = Canvas(tabControl)
journaltab = Frame(journaltabcanvas)
journaltabcanvas.config(width=850, height=650)
journaltabcanvas.create_window((7, 5), window=journaltab, anchor="nw", tags="frame")
tabControl.add(journaltabcanvas, text='Journal')  # if nauna ito sa bookscroller, maboboblock
journaltab.configure(background='#DC6ADB')
journaltabcanvas.configure(background='#DC6ADB')

# Thesis Scroll
thesistabcanvas = Canvas(tabControl)
thesistabcanvas.config(width=850, height=650)
thesistab = Frame(thesistabcanvas)
thesistabcanvas.create_window((7, 5), window=thesistab, anchor="nw", tags="frame")
tabControl.add(thesistabcanvas, text='Thesis')
thesistab.configure(background='#888EF1')
thesistabcanvas.configure(background='#888EF1')

# Film Scroll
filmtabcanvas = Canvas(tabControl)
filmtabcanvas.config(width=850, height=650)
filmtab = Frame(filmtabcanvas)
filmtabcanvas.create_window((7, 5), window=filmtab, anchor="nw", tags="frame")
tabControl.add(filmtabcanvas, text='Film')
filmtab.configure(background='#5ACAEC')
filmtabcanvas.configure(background='#5ACAEC')
filmtab.configure(background='#5ACAEC')

# Magazine Scroll
magazinetabcanvas = Canvas(tabControl)
magazinetabcanvas.config(width=850, height=650)
magazinetab = Frame(magazinetabcanvas)
magazinetabcanvas.create_window((7, 5), window=magazinetab, anchor="nw", tags="frame")
tabControl.add(magazinetabcanvas, text='Magazine')
magazinetabcanvas.configure(background='#AC7CEB')
magazinetab.configure(background='#AC7CEB')

#Help Scroll
helptabcanvas = Canvas(tabControl)
helptab = Frame(helptabcanvas)
helptabcanvas.config(width=850, height=650)
helptabcanvas.create_window((7, 5), window=helptab, anchor="nw", tags="frame")
tabControl.add(helptabcanvas, text='Help')
helptab.configure(background='#AC7CEB')
helptabcanvas.configure(background='#AC7CEB')

# Bind all to mouse wheel
booktabcanvas.bind_all("<MouseWheel>", mousewheel1)
journaltabcanvas.bind_all("<MouseWheel>", mousewheel1)
websitetabcanvas.bind_all("<MouseWheel>", mousewheel1)
filmtabcanvas.bind_all("<MouseWheel>", mousewheel1)
thesistabcanvas.bind_all("<MouseWheel>", mousewheel1)
magazinetabcanvas.bind_all("<MouseWheel>", mousewheel1)

# Bind to scroll bar
booktab.bind("<Configure>", book_scroll_bar)
journaltab.bind("<Configure>", book_scroll_bar)
websitetab.bind("<Configure>", book_scroll_bar)
filmtab.bind("<Configure>", book_scroll_bar)
thesistab.bind("<Configure>", book_scroll_bar)
magazinetab.bind("<Configure>", book_scroll_bar)

tabControl.pack()
root.title("Bilingual APA Citation Synthesizer (B.A.C.S.)")
root.geometry("1280x720+5+5")

# ALL CITATIONS SECTION

# Book Citation
book_citation = APABookCitation(booktab)

# Journal Citation
journal_citation = APAJournalCitation(journaltab)

# Magazine Citation
magazine_citation = APAMagazineCitation(magazinetab)

# Thesis Citation
thesis_citation = APAThesisCitation(thesistab)

# Website Citation
website_citation = APAWebsiteCitation(websitetab)

# Film Citation
film_citation = APAFilmCitation(filmtab)

#Help Tab
help_citation = APAHelpCitation(helptab)


root.mainloop()