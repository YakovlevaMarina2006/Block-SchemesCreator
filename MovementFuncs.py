
from main import CONTROL_PANEL_HEIGHT
from DrawingFuncs import redraw_line

def get_window_size(window):
    data = window.geometry()
    return int(data.split("x")[0]), int(data.split("x")[1].split("+")[0])

def dnd_start(event, block):
    block.block.startX = event.x
    block.block.startY = event.y

def dnd_motion(event, scheme, block, window, canvas):
    widget = block.block
    x = widget.winfo_x() - widget.startX + event.x
    if x < 0:
        x = 0
    elif x > get_window_size(window)[0] - widget.winfo_width():
        x = get_window_size(window)[0] - widget.winfo_width()

    y = widget.winfo_y() - widget.startY + event.y
    if y < CONTROL_PANEL_HEIGHT:
        y = CONTROL_PANEL_HEIGHT
    elif y > get_window_size(window)[1] - widget.winfo_height():
        y = get_window_size(window)[1] - widget.winfo_height()
    block.place(x=x, y=y)

    i = scheme.find_block(block)
    for j in range(scheme.get_size()):
        if scheme.arrows[i][j] != 0:
            redraw_line(canvas, scheme.get_arrows()[i][j], block, scheme.get_blocks()[j])
        if scheme.arrows[j][i] != 0:
            redraw_line(canvas, scheme.get_arrows()[j][i], scheme.get_blocks()[j], block)


def resize_motion(event, block):
    block.resize(x=-block.block.startX + event.x, y=-block.block.startY + event.y)



