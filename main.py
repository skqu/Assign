from calc import calc
from GUI import BTN
from GUI import DISPLAY
from GUI import FRAME
from GUI import GUI



btns_name = [
    [" ( ", " ) ", " ^ ", " c "], 
    [" 7 ", " 8 ", " 9 ", " / "], 
    [" 4 ", " 5 ", " 6 ", " * "], 
    [" 1 ", " 2 ", " 3 ", " - "], 
    [" 0 ", " . ", " = ", " + "]]
btns = []

frame_right = FRAME.FRAME("right")
frame_right.placement(0,1)
frame_right.padding(0)
frame_right.build()

frame_display = FRAME.FRAME(name="display", frame = frame_right)
frame_display.placement(0,0)
frame_display.padding(2)
frame_display.build()
display = DISPLAY.DISPLAY()
display._init_disp(frame_display)

frm = FRAME.FRAME("btn", frame = frame_right)
frm.placement(1,0)
frm.padding(10)
frm.build()


for row in range(len(btns_name)):
    for col in range(len(btns_name[row])):
        btn = BTN.BTN(btns_name[row][col], col, row, frm.obj)
        btns.append(btn)

GUI.GUI.start()