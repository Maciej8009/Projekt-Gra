import base64
from tkinter import *
import DataBaseConnect
from PIL import ImageTk, Image
import io

def shopPage():
    class Table:

        def __init__(self, root):

            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    # image = shopItems[i][0]
                    # binary_data = base64.b64decode(image)
                    # # Convert the bytes into a PIL image
                    # image = Image.open(io.BytesIO(binary_data))
                    # # Display the image
                    # image.show()
                    # print(image)
                    # image2 = base64.b64decode(image)
                    # self.pic = ImageTk.PhotoImage(open(image2, "rb"))
                    # self.label = Label(root, image=self.pic)
                    # self.label.grid(row=i, column=0)
                    self.e = Entry(root, width=10, fg='blue',
                                   font=('Arial', 16, 'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, shopItems[i][j])
                    self.button = Button(root, text='Buy')
                    self.button.grid(row=i, column=j + 1)

    root = Tk()
    root.title("Gra - ProjektGra")
    root.geometry('900x800')
    # label = Label(root, text="Witaj w sklepie!", font="Ariel", fg="blue", bg="white")
    # label.pack()
    shopItems = DataBaseConnect.shopList()
    total_rows = len(shopItems)
    total_columns = len(shopItems[0])
    t = Table(root)
    # for shopItem in shopItems:
    #     print(shopItem)
    root.mainloop()
    #a