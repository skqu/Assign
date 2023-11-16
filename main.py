from calc import calc
from GUI import BTN
from GUI import DISPLAY
from GUI import FRAME
from GUI import GUI
from data import data


cl_data = data.DATA()
cl_data._DataInit()
config = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database": "calculator",
    "file": "data.csv"
}
cl_data.Config(config)
cl_data.connect()


btns_name = [
    [" ( ", " ) ", " ^ ", " c "], 
    ["7", "8", "9", " / "], 
    ["4", "5", "6", " * "], 
    ["1", "2", "3", " - "], 
    ["0", " . ", " = ", " + "]]

frame_left = FRAME.FRAME("left")
frame_left.placement(0,0)
frame_left.padding(0)
frame_left.build()

h_display = DISPLAY.DISPLAY(frame_left, "History", width=30, height=30)


frame_right = FRAME.FRAME("right")
frame_right.placement(0,1)
frame_right.padding(0)
frame_right.build()

frame_display = FRAME.FRAME(name="display", frame = frame_right)
frame_display.placement(0,0)
frame_display.padding(2)
frame_display.build()
display = DISPLAY.DISPLAY(frame_display, "Result")

frm = FRAME.FRAME("btn", frame = frame_right)
frm.placement(1,0)
frm.padding(10)
frm.build()

cl_data.SetDisplay(h_display, "History")
cl_data.SetDisplay(display, "Result")


for i in range(10):
    btn = BTN.BTN("", 0, i, h_display.obj, clb="history", height=1, bd=0, highlightthickness=0)
    h_display.SetChild(btn)


for row in range(len(btns_name)):
    for col in range(len(btns_name[row])):
        btn = BTN.BTN(btns_name[row][col], col, row, frm.obj)


cl_data.Load()
GUI.GUI.start()