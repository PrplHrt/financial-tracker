from tkinter import *
from tkinter import ttk

class Order():
    # Maybe get a parent field and send the order back through that
    def __init__(self, root, custName: str):
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.itemName = StringVar()
        self.name_entry = ttk.Entry(self.mainframe, width=10, textvariable=self.itemName)
        self.name_entry.grid(column = 2, row = 2, sticky=(W,E))

        self.itemPrice = StringVar()
        self.price_entry = ttk.Entry(self.mainframe, width = 10, textvariable=self.itemPrice)
        self.price_entry.grid(column = 4, row = 2, sticky=(W, E))

        self.customerName = StringVar()
        self.customerName.set(custName)
        ttk.Label(self.mainframe, textvariable = self.customerName).grid( column = 2, row = 1, sticky = W)

        ttk.Label(self.mainframe, text="Customer").grid( column = 1, row = 1, sticky = E)
        ttk.Label(self.mainframe, text = "Item").grid(column = 1, row = 2, sticky = E)
        ttk.Label(self.mainframe, text = "Price").grid(column = 3, row = 2, sticky = E)

        ttk.Button(self.mainframe, text = "Add", command = self.add).grid(column = 4, row = 3, sticky = (W, E))

        for child in self.mainframe.winfor_children():
            child.grid(padx=5, pady=5)

        self.name_entry.focus()
        root.bind("<Return>", self.add)

    def add(self):
        # Should send the value to the main frame
        try:
            self.price = float(self.itemPrice.get())
            self.description = str(self.itemName.get())
            self.destroy()
        except ValueError:
            pass