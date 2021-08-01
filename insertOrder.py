from tkinter import *
from tkinter import ttk
from order import Order

class OrderFrame():
    # Maybe get a parent field and send the order back through that
    def __init__(self, n: str):
        self.root = Tk()
        self.root.title("Order Input")
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.item_name = StringVar()
        self.name_entry = ttk.Entry(self.mainframe, width=10, textvariable=self.item_name)
        self.name_entry.grid(column = 2, row = 2, sticky=(W,E))

        self.item_price = StringVar()
        self.price_entry = ttk.Entry(self.mainframe, width = 10, textvariable=self.item_price)
        self.price_entry.grid(column = 4, row = 2, sticky=(W, E))

        self.customer_name = StringVar()
        self.customer_name.set(n)
        ttk.Label(self.mainframe, textvariable = self.customer_name).grid( column = 2, row = 1, sticky = W)

        ttk.Label(self.mainframe, text="Customer").grid( column = 1, row = 1, sticky = E)
        ttk.Label(self.mainframe, text = "Item").grid(column = 1, row = 2, sticky = E)
        ttk.Label(self.mainframe, text = "Price").grid(column = 3, row = 2, sticky = E)

        ttk.Button(self.mainframe, text = "Add", command = self.add).grid(column = 4, row = 3, sticky = (W, E))

        for child in self.mainframe.winfo_children():
            child.grid(padx=5, pady=5)

        self.name_entry.focus()
        self.root.bind("<Return>", self.add)
        self.root.mainloop()

    def add(self):
        # Should send the value to the main frame
        try:
            self.price = float(self.item_price.get())
            self.description = str(self.item_name.get())
            self.root.quit()
        except ValueError:
            pass