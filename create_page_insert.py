import tkinter as tk
import ttk
from init_grid import *
from print_sql import *
from database_connect import runQuery

def sendQuery(insert_page,text, rowstart, colstart, window_height, window_width):

    query = text.get("1.0",'end')

    for widget in insert_page.winfo_children():
        widget.destroy()
    create_page_insert(insert_page, window_height, window_width)

    if len(query.strip()) > 0:
        print_sql_query(insert_page,query, 4, 0, window_height, window_width)
        
def create_page_insert(insert_page, window_height, window_width):

    init_grid(insert_page, window_width, window_height)

    insert_pageTitle = tk.Label(insert_page,
                            text="Gerenciamento de materiais",
                            font="Times 24 bold", 
                            padx=5, pady=5, 
                            bg="#005696", 
                            fg="white").grid(row=0,columnspan=window_width, sticky='NESW')

    text = tk.Text(insert_page, height=int(window_height/8), width=int(0.8*window_width), bg='white', foreground='black', bd=10, highlightbackground='red')
    text.focus()
    text.grid(row=2, column=0, columnspan=int(window_width))

    sendQueryBtn = tk.Button(insert_page, text='Run Query', command=lambda: sendQuery(insert_page,text, 4, 0, window_height, window_width))
    sendQueryBtn.grid(row=3, column=70)