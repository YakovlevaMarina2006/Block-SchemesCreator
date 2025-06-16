
from tkinter import *
from Block import *
from Scheme import *
from MovementFuncs import draw_line, control_panel_height


# def get_window_size(window):
#     data = window.geometry()
#     return int(data.split("x")[0]), int(data.split("x")[1].split("+")[0])
#
# def dnd_start(event):
#     widget = event.widget.master
#     widget.startX = event.x
#     widget.startY = event.y
#
# def dnd_motion(event):
#     widget = event.widget.master
#     x = widget.winfo_x() - widget.startX + event.x
#     if x < 0:
#         x = 0
#     elif x > get_window_size(root)[0] - widget.winfo_width():
#         x = get_window_size(root)[0] - widget.winfo_width()
#
#     y = widget.winfo_y() - widget.startY + event.y
#     if y < 0:
#         y = 0
#     elif y > get_window_size(root)[1] - widget.winfo_height():
#         y = get_window_size(root)[1] - widget.winfo_height()
#     widget.place(x=x, y=y)
#     canvas.coords(line1, x, y, block2.get_position()["x"],
#                   block2.get_position()["y"])
#
# def resize_motion(event):
#     widget = event.widget.master
#     block2.resize(x=-widget.startX + event.x, y=-widget.startY + event.y)
#
# def make_dragable(block):
#     block.panel.bind('<Button-1>', dnd_start)
#     block.panel.bind('<B1-Motion>', dnd_motion)
#     block.panel2.bind('<Button-1>', dnd_start)
#     block.panel2.bind('<B1-Motion>', dnd_motion)
#
# def make_resizable(block):
#     block.resize_button.bind('<Button-1>', dnd_start)
#     block.resize_button.bind('<B1-Motion>', block.resize)

def add_block(root, scheme, canvas):
    new_block = Block(canvas, scheme, 100, 100, "pink", "red")
    new_block.put(root, 100, 100)
    new_block.make_dragable(root, scheme, canvas)
    new_block.make_resizable()
    new_block.make_connectable(canvas, scheme)
    scheme.add_block(new_block)




if __name__ == '__main__':
    root = Tk()  # создаем корневой объект - окно
    root.title("Block-Schemes Creator")  # устанавливаем заголовок окна
    max_screen_size_width = root.wm_maxsize()[0]
    max_screen_size_height = root.wm_maxsize()[1]
    root.geometry(f"{max_screen_size_width // 2}x{max_screen_size_height // 2}+500+300")  # устанавливаем размеры окна
    icon = PhotoImage(file="cat_icon.png")
    root.iconphoto(False, icon)
    root.update_idletasks()

    # f = Frame(root, bg="red")
    # f.pack(fill=BOTH, expand=1)

    # control_panel = Frame(f, bg="black", height=100)
    # control_panel.pack(fill=X, side=TOP, anchor="n", expand=1)

    # control_panel2 = Frame(f, bg="pink")
    # control_panel2.pack(fill=BOTH, side=TOP, expand=1)

    canvas = Canvas()
    canvas.config(highlightthickness=0)
    canvas.pack(fill=BOTH, side=TOP, expand=1)

    control_panel = Frame(canvas, bg="black", height=control_panel_height)
    control_panel.pack(fill=X, side=TOP, anchor="n", expand=1)

    add_block_btn = Button(control_panel, text="add block", command=lambda : add_block(root, scheme, canvas))
    add_block_btn.pack(side=LEFT)

    scheme = Scheme()

    # block1 = Block(canvas, 300, 300, "pink", "red")
    # block1.put(root, 300, 300)
    # block1.make_dragable(root, scheme, canvas)
    # block1.make_resizable()
    # scheme.add_block(block1)
    #
    # block2 = Block(canvas, 200, 100, "light blue", "purple")
    # block2.put(root, 100, 100)
    # block2.make_dragable(root, scheme, canvas)
    # block2.make_resizable()
    # scheme.add_block(block2)
    #
    # block1.make_lower()
    # block2.make_lower()

    # draw_line(canvas, scheme, block2, block1)
    #draw_line(canvas, scheme, block1, block2)

    # line1 = canvas.create_line(0, 0, 100, 100, 100, 200)
    # canvas.coords(line1, 300, 0, 100, 100, 100, 200)
    # print(line1)

    root.update_idletasks()

    root.mainloop()
