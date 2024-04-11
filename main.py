import tkinter as tk
import re
from tkinter import END

#datasource_from_google_sheets
#import pygsheets
#path = '' #get json file from google cloud
#gc = pygsheets.authorize(service_account_file = path)
#sh = gc.open('my_sheet')
#wk1 = sh[0]
#my_list = wk1.get_col(2, include_tailing_empty = false)
#my_list = wk1.get_values('B1','B14')
#print(my_list)

#datasource_from_database
#from sqlalchemy import create_engine
#my_conn = create_engine("")
#q = "select query"
#my_cursor = my_conn.execute(q)
#result = my_cursor.fetchall()
#print(result)
#my_list(r for r, in result)
#print(my_list)

my_w = tk.Tk()
my_w.geometry("450x400")
my_w.title("Autocomplete-DeskTop-App")
font1 = ('Times',24,'bold')

my_list = [(1, 'John Duo', 'Four', 75, 'Female'),
           (2, 'Max Ruin', 'Three', 85, 'Male'),
           (3, 'Arnold', 'Three', 55, 'Male'),
           (4, 'Krish Star', 'Four', 60, 'Female')]

l0 = tk.Label(text='Autocomplete', font=font1)
l0.grid(row = 0, column = 0, columnspan = 4)
def my_upd(my_widget):
    my_w = my_widget.widget
    index = (my_w.curselection()[0])
    value = my_w.get(index)
    for row in my_list:
        if (row[1] == value):
            #print(row[1], row[3], row[4])
            l3.config(text = str(row[3]))
            l4.config(text = row[4])
            break
    e1_str.set(value)
    l1.delete(0, END)

def my_down(my_widget):
    l1.focus()
    l1.selection_set(0)

e1_str = tk.StringVar()
e1 = tk.Entry(my_w ,font = font1 ,textvariable = e1_str, width = 15)
e1.grid(row = 1 ,column = 0 ,padx = 5 ,pady = 10, sticky = 'w')

l3 = tk.Label(my_w, text = 'Mark', font = font1, bg = 'yellow')
l3.grid(row = 1, column = 1, padx = 5, sticky = 'w')

l4 = tk.Label(my_w, text = 'class', font = font1, bg = 'lightgreen')
l4.grid(row = 1, column = 1, padx = 90, sticky = 'w')

l1 = tk.Listbox(my_w ,height = 6 ,font = font1 ,relief = 'flat', width = 10,
                bg = 'SystemButtonFace', highlightcolor = 'SystemButtonFace')
l1.grid(row = 2 ,column = 0, padx = 5, sticky = 'w')

def get_data(*args):
    search_str = e1.get() #user entered String
    l1.delete(0, END)
    for element in my_list:
        if(re.match(search_str ,element[1] ,re.IGNORECASE)):
            l1.insert(tk.END,element[1])

#l1.bind("<<ListboxSelect>>", my_upd)
e1.bind("<Down>", my_down)

l1.bind("<Right>", my_upd)

l1.bind("<Return>", my_upd)

e1_str.trace('w', get_data)

#print(my_w['bg'])
my_w.mainloop() #keep the window open




