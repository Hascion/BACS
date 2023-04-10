from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from PIL import Image

class APASupportCitation:
    def __init__(self, supporttab):
        self.canvas=Canvas(supporttab, width=705, height=655)
        self.image=ImageTk.PhotoImage(Image.open ("Support Tab.png"))
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        self.canvas.pack()

