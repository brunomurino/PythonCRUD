import tkinter as tk
import ttk
from database_connect import runQuery

def print_sql_query(widget, query, rowstart, colstart, window_height, window_width):
    
    rs, col_names = runQuery(query)

    num_rows = len(rs)
    num_cols = len(rs[0])
    step = int((window_width/num_cols))

    listBox = ttk.Treeview(widget, columns=col_names, show='headings')

    for col in col_names:
        listBox.heading(col, text=col)    
        listBox.column(column=col, stretch=True)
    listBox.grid(row=rowstart, column=colstart, columnspan=window_width) 

    for row in rs:
        print(row)
        listBox.insert("", "end", values=row)


def print_sql_table(widget, rowstart, colstart, window_height, window_width):
    fields = ['ID', 'USERNAME', 'FIRST_NAME', 'LAST_NAME', 'EMAIL', 'PHONE_NUMBER']
    query = "SELECT "
    for field in fields:
        query += field + ", "
    query = query[:-2]
    query += " FROM USERS"
    rs, col_names = runQuery(query)

    fieldLength = {}
    for field in fields:
        queryLength = "SELECT LENGTH({}) FROM USERS ORDER BY LENGTH({}) DESC LIMIT 1".format(field, field)
        res, _ = runQuery(queryLength)
        fieldLength[field] = res[0][0]

    num_rows = len(rs)
    num_cols = len(rs[0])
    step = int((window_width/num_cols))

    listBox = ttk.Treeview(widget, columns=col_names, show='headings')

    for col in col_names:
        listBox.heading(col, text=col)    
        listBox.column(column=col,width=11*fieldLength[col], stretch=True)
    listBox.grid(row=rowstart, column=colstart, columnspan=window_width) 

    for ID, USERNAME, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER in rs:
        listBox.insert("", "end", values=(ID, USERNAME, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER))

def print_sql_record(widget, login, rowstart, colstart, window_height, window_width):
    fields = ['ID', 'USERNAME', 'FIRST_NAME', 'LAST_NAME', 'EMAIL', 'PHONE_NUMBER']
    query = "SELECT "
    for field in fields:
        query += field + ", "
    query = query[:-2]
    query += " FROM USERS WHERE USERNAME = '{}'".format(login)
    rs, col_names = runQuery(query)

    step = int((window_width/2))

    tableHeader = {}
    queryResult = {}

    for i, (col_name, col_val) in enumerate(zip(col_names, rs[0])):
        tableHeader[i] = tk.Label(widget, text=col_name, font="Times 24 bold")
        tableHeader[i].grid(column=0+colstart,row=i+rowstart, columnspan=step)
        queryResult[i] = tk.Label(widget, text=col_val, font="Times 16")
        queryResult[i].grid(column=step+colstart,row=i+rowstart, columnspan=step)
