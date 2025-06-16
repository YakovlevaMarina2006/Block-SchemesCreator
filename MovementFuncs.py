
from tkinter import *

control_panel_height = 30
flag = False
from_block = None
to_block = None

def get_window_size(window):
    data = window.geometry()
    return int(data.split("x")[0]), int(data.split("x")[1].split("+")[0])

def dnd_start(event, block):
    # widget = event.widget.master
    # print(widget == block.block)
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
    if y < control_panel_height:
        y = control_panel_height
    elif y > get_window_size(window)[1] - widget.winfo_height():
        y = get_window_size(window)[1] - widget.winfo_height()
    block.place(x=x, y=y)

    i = scheme.find_block(block)
    for j in range(scheme.get_size()):
        if scheme.arrows[i][j] != 0:
            redraw_line(canvas, scheme.get_arrows()[i][j], block, scheme.blocks[j])
        if scheme.arrows[j][i] != 0:
            redraw_line(canvas, scheme.get_arrows()[j][i], scheme.blocks[j], block)


def resize_motion(event, block):
    #widget = event.widget.master.master
    block.resize(x=-block.block.startX + event.x, y=-block.block.startY + event.y)


def draw_line(canvas, scheme, block):
    global flag
    global from_block
    global to_block
    if not flag:
        flag = True
        from_block = block
    else:
        to_block = block
        if scheme.get_arrow(from_block, to_block) != 0:
            canvas.delete(scheme.get_arrow(from_block, to_block))
        scheme.add_arrow(from_block, to_block, canvas.create_line(from_block.get_position()["x"], from_block.get_position()["y"], \
                         to_block.get_position()["x"], to_block.get_position()["y"], arrow="last"))
        flag = False


def redraw_line(canvas, line, from_block, to_block):

    canvas.coords(line, from_block.get_position()["x"], from_block.get_position()["y"], \
                                        to_block.get_position()["x"], to_block.get_position()["y"])


def delete_arrow(canvas, scheme, arrow):
    canvas.delete(arrow)
