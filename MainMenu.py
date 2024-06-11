from tkinter import *
from tkinter.ttk import Separator
from typing import Any

import DataBaseConnect
import ShopMenu
import LoginMenu

class MainMenu:
    def __init__(self, UserID: int, UserName: str):
        print("JD")
        self.UserID = UserID
        self.UserName = UserName


    def MenuPage(self):
        def userScore():
            scores = DataBaseConnect.getUserScores()
            total_rows = len(scores)
            total_columns = len(scores[0])
            for i in range(total_rows):
                frame = Frame(root, width=400, height=200)
                for j in range(total_columns):
                    scoreLabel = Label(frame, text=scores[i][j], font=("Arial", 10), padx=30, pady=2, width=10, height=1, bg='grey')
                    scoreLabel .grid(row=i, column=j)
                frame.pack()

        def userEQ():
            eq = DataBaseConnect.getUserEQ(self.UserID)
            total_columns = len(eq)
            frame = Frame(root, width=400, height=200)
            labelItem = Label(frame, text='Money', font=("Arial", 15), padx=10, pady=2, width=10, height=1, bg='grey')
            labelItem.grid(row=0, column=0)
            labelItem = Label(frame, text='Wood', font=("Arial", 15), padx=10, pady=2, width=10, height=1, bg='grey')
            labelItem.grid(row=0, column=1)
            labelItem = Label(frame, text='Stone', font=("Arial", 15), padx=10, pady=2, width=10, height=1, bg='grey')
            labelItem.grid(row=0, column=2)
            labelItem = Label(frame, text='Iron', font=("Arial", 15), padx=10, pady=2, width=10, height=1, bg='grey')
            labelItem.grid(row=0, column=3)
            labelItem = Label(frame, text='Diamond', font=("Arial", 15), padx=10, pady=2, width=10, height=1, bg='grey')
            labelItem.grid(row=0, column=4)

            for i in range(total_columns):
                eqLabel = Label(frame, text=eq[i], font=("Arial", 10), padx=10, pady=2, width=10, height=1, bg='grey')
                eqLabel.grid(row=1, column=i)
            frame.pack()

        def getToShop():
            ShopMenu.shopPage2(self.UserID)

        def getToGame1():
            print("game1")

        def getToGame2():
            print("game2")

        def getToGame3():
            print("game3")

        def getToGame4():
            print("game4")

        def logout():
            root.destroy()
            LoginMenu.floginMenu()

        root = Tk()
        root.title("Gra - ProjektGra")
        root.geometry('800x800')
        label = Label(root, text="Witaj "+self.UserName+"!", font="Ariel", fg="blue", bg="white")
        label.pack()
        label2 = Label(root, text="Top 5 Graczy:", font="Ariel", fg="red", width=30, padx=5, pady=5)
        label2.pack()
        userScore()
        separator = Separator(root, orient='horizontal')
        separator.pack(fill='x')
        label3 = Label(root, text="Twój ekwipunek", font="Ariel", fg="red", width=30, padx=5, pady=5)
        label3.pack()
        userEQ()
        separator = Separator(root, orient='horizontal')
        separator.pack(fill='x')
        ShopButton = Button(root, text="Sklep", font="Ariel", fg="blue", width=30, height=1, padx=5, pady=5, command=getToShop)
        ShopButton.pack()
        MiniGameButton1 = Button(root, text="Zacznij Gre Timberman!", font="Ariel", fg="blue", width=30, height=1, padx=5, pady=5, command=getToGame1)
        MiniGameButton1.pack()
        MiniGameButton2 = Button(root, text="Zacznij Gre!", font="Ariel", fg="blue", width=30, height=1, padx=5, pady=5, command=getToGame2)
        MiniGameButton2.pack()
        MiniGameButton3 = Button(root, text="Zacznij Gre!", font="Ariel", fg="blue", width=30, height=1, padx=5, pady=5, command=getToGame3)
        MiniGameButton3.pack()
        MiniGameButton4 = Button(root, text="Zacznij Gre!", font="Ariel", fg="blue", width=30, height=1, padx=5, pady=5, command=getToGame4)
        MiniGameButton4.pack()

        logOutButton = Button(root, text="Wyloguj się", font="Ariel", fg="blue", width=30, height=1, padx=5, pady=5, command=logout)
        logOutButton.pack()

        root.mainloop()


