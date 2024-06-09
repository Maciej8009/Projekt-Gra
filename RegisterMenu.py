from tkinter import *
import DataBaseConnect
import MainMenu
import time

def registerMenu():
    def registerMenuFunction(nick: str, email: str, password: str):
        print("JD", nick, email, password)
        addOrNotAddThatIsTheQuestion, message = DataBaseConnect.addUser(nick, email, password)
        if addOrNotAddThatIsTheQuestion:
            messageLabel = Label(root, text="Użytkownik dodany!")
            messageLabel.pack()
            root.destroy()
        else:
            messageLabel = Label(root, text=message)
            messageLabel.pack()
            return

    root = Tk()
    root.title("Register")
    root.geometry('600x800')
    nameLabel = Label(root, text="Podaj Nazwę")
    nameLabel.pack()
    nickEntry = Entry(root, font="Ariel", bg="#666")
    nickEntry.pack()
    emailLabel = Label(root, text="Podaj email")
    emailLabel.pack()
    emailEntry = Entry(root, font="Ariel", bg="#666")
    emailEntry.pack()
    passwordLabel = Label(root, text="Podaj hasło")
    passwordLabel.pack()
    passwordEntry = Entry(root, font="Ariel", bg="#666", show="*")
    passwordEntry.pack()
    passwordInfoLabel = Label(root, text="Hasło musi zawierać przynajmniej: Jedną dużą i małą literę, znak specjalny(@,#,$,%), ")
    passwordInfoLabel2 = Label(root, text="mieć długość przynajmniej 8 znaków i nie być dłuższe niż 20 znaków")
    passwordInfoLabel.pack()
    passwordInfoLabel2.pack()
    button = Button(root, text="Register", command=lambda: registerMenuFunction(nickEntry.get(), emailEntry.get(), passwordEntry.get()))
    button.pack()
    root.mainloop()


