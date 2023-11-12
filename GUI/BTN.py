from .GUI import GUI
from .DISPLAY import DISPLAY
from calc import calc 

class BTN(GUI):

    def __init__(self, text, col, row, frm) -> None:
        super().__init__()
        self.config["text"] = text
        self.config["width"] = 20
        self.config["height"] = 3
        self.config["font"] =  20
        self.dpl = DISPLAY()
        self.master = frm
        self.config["command"] = self.clb
        self.construct()
        self.placement(row, col)
        self.grid()

    def clb(self):
        if self.get() == " c ":
            self.dpl.set("")
        elif self.get() == " = ":
            content = self.dpl.get()
            calculator = calc.CALC()
            result = calculator.calculate(content)
            self.dpl.append(" = " + str(result))
            #data = DATA.DATA()
            #data.write(content)
        else:
            self.dpl.append(self.get())

    def get(self):
        return self.config["text"]

    def grid(self):
        self.padding(padd=5)
        self.build()
        