from tkinter import *
from tkinter import ttk 

class GUI: 
    _root = Tk()
    def __init__(self):
        self.obj = None
        self.master = None
        self.config = {}
    
    def construct(self):
        name = self.__class__.__name__
        if name == "BTN": 
            self.obj = Button(self.master, cnf = self.config)
        elif name == "DISPLAY":
            self.obj = Label(master=self.master,cnf = self.config)
        elif name == "FRAME":
            if self.master != None:
                frame = self.master
            else:
                frame = __class__._root
            self.obj = ttk.Frame(frame)
    

    def placement(self, row, col):
        self.row = row
        self.col = col

    def padding(self, padd):
        self.padx = padd
        self.pady = padd

    def build(self):
        self.obj.grid(column=self.col, row=self.row, padx=self.padx, pady=self.pady)

    def get(self):
        pass
    
    def set(self, content):
        pass

    @staticmethod
    def start():
        __class__._root.mainloop()