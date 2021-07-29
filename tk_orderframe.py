from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def add(*args):
    try:
        price = float(itemPrice.get())
        item = str(itemName.get())
        msg = str(customerName.get()) + " ordered " + item + " for $" + str(price)
        messagebox.showinfo("Order", msg)
    except ValueError:
        pass
        

root = Tk()
root.title("Order Input")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

itemName = StringVar()
name_entry = ttk.Entry(mainframe, width = 10, textvariable=itemName)
name_entry.grid(column = 2, row = 2, sticky= (W, E))

itemPrice = StringVar()
price_entry = ttk.Entry(mainframe, width = 10, textvariable=itemPrice)
price_entry.grid(column = 4, row = 2, sticky=(W, E))

customerName = StringVar()
customerName.set("Izzy")
ttk.Label(mainframe, textvariable = customerName).grid( column = 2, row = 1, sticky = W)

ttk.Label(mainframe, text="Customer").grid( column = 1, row = 1, sticky = E)
ttk.Label(mainframe, text = "Item").grid(column = 1, row = 2, sticky = E)
ttk.Label(mainframe, text = "Price").grid(column = 3, row = 2, sticky = E)

ttk.Button(mainframe, text = "Add", command = add).grid(column = 4, row = 3, sticky = (W, E))

for child in mainframe.winfo_children():
    child.grid(padx=5, pady=5)

name_entry.focus()
root.bind("<Return>", add)

root.mainloop()
