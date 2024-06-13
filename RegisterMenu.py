from tkinter import *
import DataBaseConnect
import LoginMenu
import MainMenu
import time


def registerMenu():
    def registerMenuFunction(nick: str, email: str, password: str):
        print("JD", nick, email, password)
        addOrNotAddThatIsTheQuestion, message = DataBaseConnect.addUser(nick, email, password)
        if addOrNotAddThatIsTheQuestion:
            messageLabel = Label(RegisterMenu, text="Użytkownik dodany!")
            messageLabel.pack()
            RegisterMenu.destroy()
            LoginMenu.floginMenu()
        else:
            messageLabel = Label(RegisterMenu, text=message)
            messageLabel.pack()
            return

    def close():
        RegisterMenu.destroy()
        LoginMenu.floginMenu()

    RegisterMenu = Tk()
    RegisterMenu.title("Register")
    RegisterMenu.geometry('600x800')
    nameLabel = Label(RegisterMenu, text="Podaj Nazwę")
    nameLabel.pack()
    nickEntry = Entry(RegisterMenu, font="Ariel", bg="#666")
    nickEntry.pack()
    emailLabel = Label(RegisterMenu, text="Podaj email")
    emailLabel.pack()
    emailEntry = Entry(RegisterMenu, font="Ariel", bg="#666")
    emailEntry.pack()
    passwordLabel = Label(RegisterMenu, text="Podaj hasło")
    passwordLabel.pack()
    passwordEntry = Entry(RegisterMenu, font="Ariel", bg="#666", show="*")
    passwordEntry.pack()
    passwordInfoLabel = Label(RegisterMenu, text="Hasło musi zawierać przynajmniej: Jedną dużą i małą literę, znak specjalny(@,#,$,%), ")
    passwordInfoLabel2 = Label(RegisterMenu, text="mieć długość przynajmniej 8 znaków i nie być dłuższe niż 20 znaków")
    passwordInfoLabel.pack()
    passwordInfoLabel2.pack()
    button = Button(RegisterMenu, text="Register", command=lambda: registerMenuFunction(nickEntry.get(), emailEntry.get(), passwordEntry.get()))
    button.pack()
    buttonExit = Button(RegisterMenu, text="Wyjście", width=10, height=2, command=close)
    buttonExit.pack(side=BOTTOM)
    RegisterMenu.mainloop()


