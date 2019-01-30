from create_page_show import *
from create_page_user import *
from create_page_insert import *

def create_pages(window, nb, window_width, window_height, login):

    window.geometry(str(window_width*10) + 'x' + str(window_height*10))
    nb.grid(row=0, column=0, rowspan=window_height, columnspan=window_width ,sticky="NESW")

    user_page = tk.Frame(nb)
    nb.add(user_page, text="USUÁRIO")
    create_page_user(user_page, window_width, window_height, login)

    show_page = tk.Frame(nb)
    nb.add(show_page, text="VER")
    create_page_show(show_page, window_width, window_height)

    insert_page = tk.Frame(nb)
    nb.add(insert_page, text="QUERY")
    create_page_insert(insert_page, window_width, window_height)

    # remove_page = tk.Frame(nb)
    # nb.add(remove_page, text="REMOVER")