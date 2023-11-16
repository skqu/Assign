from .GUI import GUI
from data import data
from calc import calc 

class BTN(GUI):

    def __init__(self, text, col, row, frm) -> None:
        super().__init__()
        self.config["text"] = text
        self.config["width"] = 20
        self.config["height"] = 3
        self.config["font"] =  20
        self.data = data.DATA()
        self.master = frm
        self.config["command"] = self.clb
        self.construct()
        self.placement(row, col)
        self.grid()

    def clb(self):
        if self.get() == " c ":
            self.data.wrtie("")
        elif self.get() == " = ":
            content = self.data.read()
            calculator = calc.CALC()
            result = calculator.calculate(content)
            self.data.write(" = " + str(result))
            self.data.Save()
        else:
            self.data.write(self.get())

    def get(self):
        return self.config["text"]

    def grid(self):
        self.padding(padd=5)
        self.build()
        