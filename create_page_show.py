import tkinter as tk
import ttk
from init_grid import *
from print_sql import *

def create_page_show(show_page, window_height, window_width):

    init_grid(show_page, window_width, window_height)

    show_pageTitle = tk.Label(show_page,
                            text="Gerenciamento de materiais",
                            font="Times 24 bold", 
                            padx=5, pady=5, 
                            bg="#005696", 
                            fg="white").grid(row=0,columnspan=window_width, sticky='NESW')

    print_sql_table(show_page, 2, 0, window_height, window_width)
