import tkinter as tk
from init_grid import *
from print_sql import *

def create_page_user(user_page, window_height, window_width, login):

    init_grid(user_page, window_width, window_height)

    user_pageTitle = tk.Label(user_page,
                            text="Usuário",
                            font="Times 24 bold", 
                            padx=5, pady=5, 
                            bg="#005696", 
                            fg="white").grid(row=0,columnspan=window_width, sticky='NEWS')

    print_sql_record(user_page, login, 2, 0, window_height, window_width)

