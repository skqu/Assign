from .GUI import GUI

class DISPLAY(GUI):

    def __init__(self, frame, name, width = 80, height = 3):
        super().__init__()
        self.master = frame.obj
        self.config["text"] = ""
        self.config["relief"] = "solid"
        self.config["width"] = width
        self.config["height"] = height
        self.config["font"] = 20
        self.child = []
        self.construct()
        self.placement(0, 0)
        self.padding(10)
        self.build()


    def append(self, content):
        content = self.get() + content
        self.set(content=content)

    def SetChild(self, child):
        self.child.append(child)

    def getChild(self):
        return self.child

    def build(self):
        self.obj.config(text=self.config["text"])
        self.obj.grid(column=self.col,  row=self.row, padx=self.padx, pady=self.pady)
        
    def get(self) -> str:
        return self.config["text"]
    
    def set(self, content):
        self.config["text"] = content
        self.build()

