import tkinter as tk

def init_grid(widget, numRow, numCol):

    rows = 0
    while rows < numRow:
        widget.rowconfigure(rows, weight=1)
        rows += 1

    columns = 0
    while columns < numCol:
        widget.columnconfigure(columns, weight=1)
        columns += 1