from .GUI import GUI
from data import data
from calc import calc 

class BTN(GUI):

    def __init__(self, text, col, row, frm, clb = None, height = 3, bd=3, highlightthickness=3) -> None:
        super().__init__()
        self.config["text"] = text
        self.config["width"] = 20
        self.config["height"] = height
        self.config["font"] =  20
        self.config["bd"] = bd
        self.config[ "highlightthickness"] = highlightthickness
        self.data = data.DATA()
        self.master = frm
        if clb == None:
            self.config["command"] = self.clb
        else:
            self.config["command"] = self.hClb
        self.construct()
        self.placement(row, col)
        self.grid()

    def clb(self):
        if self.get() == " c ":
            self.data.write("")
        elif self.get() == " = ":
            content = self.data.read()
            if content.count("=") > 0:
                content = content[content.find("=") + 1:]
                print(content)
            calculator = calc.CALC()
            result = calculator.calculate(content)
            self.data.write(content + " = " + str(result))
            self.data.Save()
        else:
            data = self.data.read() + self.get()
            self.data.write(data)

    def hClb(self):
        data = self.config["text"][2:]
        self.data.write(data)


    def get(self):
        return self.config["text"]

    def grid(self):
        self.padding(padd=5)
        self.build()
        