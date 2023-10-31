import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mbox
from turtle_race import display_msg

app = tk.Tk()
# Add a Title
app.title("Python GUI App")
# Label
ttk.Label(app, text="Messsage Box Application").grid(column=0, row=0, padx=20, pady=30)
# Create a Menu Bar
menuBar = Menu(app)
app.config(menu=menuBar)


# Display a Message Box
def _msgBox():
    mbox.showinfo('Python Message Box', {display_msg})
    # Create Message Menu
    infoMenu = Menu(menuBar, tearoff=0)
    infoMenu.add_command(label="Info", command=_msgBox)
    menuBar.add_cascade(label="Message", menu=infoMenu)
    # Calling Main()
    app.mainloop()

_msgBox()