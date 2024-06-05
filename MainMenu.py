from tkinter import *
from typing import Any


class MainMenu:
    def __init__(self):
        print("JD")


    def MenuPage(self):
        root = Tk()
        root.title("Gra - ProjektGra")
        root.geometry('600x800')
        label = Label(root, text="ZALOGOWANY!!!!!", font="Ariel", fg="blue", bg="white")
        label.pack()
        root.mainloop()
