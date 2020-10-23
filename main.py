#!/usr/bin/env python

import tkinter as tk
from tkinter import ttk
import re

window = tk.Tk()

#region STYLES
ttk.Style().configure('black/black.TLabel', foreground='black', background='black')
ttk.Style().configure('black/black.TButton', foreground='black', background='black')
#end STYLES

#region FUNCTIONS
def setup_window_position():
    w = window.winfo_reqwidth()
    h = window.winfo_reqheight()
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('+%d+%d' % (x, y))

def show_branch_name():
    branchPrefix = taskPrefixEntry.get().upper() + "/"
    branchName = return_replaced_empty_space_by_custom_char()

    window.clipboard_clear()
    window.clipboard_append("git checkout -b " + branchPrefix.replace('\n', '').replace('\r', '') + branchName.replace('\n', '').replace('\r', ''))
    window.update


def return_replaced_empty_space_by_custom_char():
    customChar = replaceEmptyByEntry.get()

    lowerCasedTaskName = return_lower_cased_string()
    lowerCasedTaskName = re.sub("[^A-Za-z\\s]+", "", lowerCasedTaskName)
    lowerCasedTaskName = lowerCasedTaskName.replace(" ", customChar)

    return lowerCasedTaskName


def return_lower_cased_string():
    entryString = taskNameEntry.get()
    return entryString.lower()



#end FUNCTIONS

#region SETUP UI
tk.Label(window, text="Replace spaces", anchor="w").grid(row=0)
tk.Label(window, text="Task prefix", anchor="w").grid(row=1)
tk.Label(window, text="Task name", anchor="w").grid(row=2)

replaceEmptyByEntry = tk.Entry(window)
taskPrefixEntry = tk.Entry(window)
taskNameEntry = tk.Entry(window)

replaceEmptyByEntry.grid(row=0, column=2, columnspan=3, sticky='ew')
taskPrefixEntry.grid(row=1, column=2, columnspan=3, sticky='ew')
taskNameEntry.grid(row=2, column=2, columnspan=3, sticky='ew')

ttk.Button(window,text='Copy command and branch name to clipboard', style='black/black.TButton', command=show_branch_name).grid(row=3, columnspan=4, rowspan=2, sticky='ew')
#end SETUP UI

#region SETUP WINDOW
window.title('Branch Name Helper')
window.resizable(0,0)
setup_window_position()
#end SETUP WINDOW

tk.mainloop()