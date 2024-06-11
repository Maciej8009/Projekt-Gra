import base64
from msilib import Table
from tkinter import *
import DataBaseConnect
from PIL import ImageTk, Image
import io
import ShopMenu


def shopPage2(userId: int):
    def buy(productID: int):
        print(productID, userId)
        buyOrNotBuy, message = DataBaseConnect.alreadyBought(productID, userId)
        if buyOrNotBuy:
            DataBaseConnect.buy(productID, userId)
            Shop.tk.call('grid', Label(Shop, text=message, fg="red"))
        else:
            Shop.tk.call('grid', Label(Shop, text=message, fg="red"))


    Shop = Tk()
    Shop.title("Sklep")
    Shop.geometry('900x800')
    shopItems = DataBaseConnect.shopList()
    total_rows = len(shopItems)
    total_columns = len(shopItems[0])
    colFrame = 0
    rowFrame = 0
    for i in range(total_rows):
        frame = Frame(Shop, width=400, height=200)
        row = 0
        for j in range(total_columns):
            if (type(shopItems[i][j]) == int) & (j != 6):
                if shopItems[i][j] != 0:
                    row = row + 1
                    if j == 1:
                        labelPriceType = Label(frame, text="Money", font=("Helvetica", 10), padx=5, pady=5)
                        labelPriceType.grid(row=row, column=0)
                    elif j == 2:
                        labelPriceType = Label(frame, text="Wood", font=("Helvetica", 10), padx=5, pady=5)
                        labelPriceType.grid(row=row, column=0)
                    elif j == 3:
                        labelPriceType = Label(frame, text="Stone", font=("Helvetica", 10), padx=5, pady=5)
                        labelPriceType.grid(row=row, column=0)
                    elif j == 4:
                        labelPriceType = Label(frame, text="Iron", font=("Helvetica", 10), padx=5, pady=5)
                        labelPriceType.grid(row=row, column=0)
                    elif j == 5:
                        labelPriceType = Label(frame, text="Diamonds", font=("Helvetica", 10), padx=5, pady=5)
                        labelPriceType.grid(row=row, column=0)
                    label = Label(frame, text=shopItems[i][j])
                    label.grid(row=row, column=1)  # DZIAŁAAAAA
            elif j != 6:
                labelName = Label(frame, text=shopItems[i][j], font=("Arial", 25), bg="grey", width=16, height=1)
                labelName.grid(row=row, column=0, columnspan=2)
                labelInfoWaluta = Label(frame, text="Waluta", font=("Arial",15), bg="lightgrey", width=13, height=1)
                labelInfoWartosc = Label(frame, text="Wartosc", font=("Arial",15), bg="lightgrey", width=13, height=1)
                labelInfoWaluta.grid(row=row+1, column=0)
                labelInfoWartosc.grid(row=row+1, column=1)
                row += 1
            # else:
            #     # button = Button(frame, text="Buy", command=lambda: buy(shopItems[i][j]))
            #     # button.grid(row=row + 1, column=0, columnspan=2)
        if colFrame == 0:
            frame.grid(row=rowFrame, column=colFrame, sticky='n')
            colFrame += 1
        else:
            frame.grid(row=rowFrame, column=colFrame, sticky='n')
            colFrame -= 1
            rowFrame += 1

    buttonBuyAxe = Button(Shop, text="Buy Axe", command=lambda: buy(0, ), width=30, height=2, padx=10, pady=10)
    buttonBuyPickaxe = Button(Shop, text="Buy Pickaxe", command=lambda: buy(1, ), width=30, height=2, padx=10, pady=10)
    buttonBuyBetterPickAxe = Button(Shop, text="Buy Better Pickaxe", command=lambda: buy(2, ), width=30, height=2, padx=10, pady=10)
    buttonBuyDrill = Button(Shop, text="Buy Drill", command=lambda: buy(3, ), width=30, height=2, padx=10, pady=10)
    buttonBuyAxe.grid(row=rowFrame, column=0, columnspan=2)
    rowFrame += 1
    buttonBuyPickaxe.grid(row=rowFrame, column=0, columnspan=2)
    rowFrame += 1
    buttonBuyBetterPickAxe.grid(row=rowFrame, column=0, columnspan=2)
    rowFrame += 1
    buttonBuyDrill.grid(row=rowFrame, column=0, columnspan=2)
    Shop.mainloop()
