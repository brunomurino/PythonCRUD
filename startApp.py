import tkinter as tk
import ttk
from init_grid import *
from authenticate_user import *
from create_pages import *

def enterApp(window, nb, authenticationPage, varLogin, varPwrd):

    login = varLogin

    validUser = authenticate_user(varLogin, varPwrd)
    if validUser:
        print("Valid user!")
        authenticationPage.destroy()
        window.unbind("<Return>")

        window_width = 100
        window_height = 100
        create_pages(window, nb, window_width, window_height, login)

def startApp():

    login_width = 60
    login_height = 20 

    window = tk.Tk()
    window.title("Gerenciamento")
    init_grid(window, 4, 2)
    window.geometry(str(login_width*10) + 'x' + str(login_height*10))

    nb = ttk.Notebook(window)
    nb.grid(row=1, column=0, rowspan=login_height-1, columnspan=login_width ,sticky="NESW")

    authenticationPage = tk.Frame(window)
    nb.add(authenticationPage, text="LOGIN")
    authenticationPage.configure(width=login_width/5, height=login_height/5, bg="white")

    init_grid(authenticationPage, 4, 2)

    tk.Label(authenticationPage, text="Gerenciamento de materiais", font="Times 24 bold").grid(row=0, column=0, columnspan=int(login_width/10))

    textLogin = tk.Label(authenticationPage, text="Usuário").grid(row=1, column=0)
    textPwrd = tk.Label(authenticationPage, text="Senha").grid(row=2, column=0)

    log = tk.StringVar(value='johndoe')
    pwrd = tk.StringVar(value='senha')

    entryLogin = tk.Entry(authenticationPage, textvariable=log)
    entryLogin.grid(row=1, column=1)
    entryLogin.focus()
    entryPwrd = tk.Entry(authenticationPage, textvariable=pwrd, show="*").grid(row=2, column=1)

    sendButton = tk.Button(authenticationPage, text="Login", command=lambda: enterApp(window, nb, authenticationPage, log.get(), pwrd.get())).grid(row=3, column=0, columnspan=int(login_width/10))
       
    window.bind('<Return>', lambda event: enterApp(window, nb, authenticationPage, log.get(), pwrd.get()))

    return window

print("Bem vindo!")

einstein_color = (0,86,150) # RGB code of #005696

window = startApp()

window.mainloop()
