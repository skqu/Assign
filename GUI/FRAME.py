from .GUI import GUI

class FRAME(GUI):
    def __init__(self, name, frame = None):
        super().__init__()
        self.name = name
        if frame:
            self.master = frame.obj
        self.construct()
