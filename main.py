
from tkinter import *
from Block import *

#root = Tk()

def get_window_size(window):
    data = window.geometry()
    return int(data.split("x")[0]), int(data.split("x")[1].split("+")[0])

def dnd_start(event):
    widget = event.widget.master
    widget.startX = event.x
    widget.startY = event.y

def dnd_motion(event):
    widget = event.widget.master
    x = widget.winfo_x() - widget.startX + event.x
    if x < 0:
        x = 0
    elif x > get_window_size(root)[0] - widget.winfo_width():
        x = get_window_size(root)[0] - widget.winfo_width()

    y = widget.winfo_y() - widget.startY + event.y
    if y < 0:
        y = 0
    elif y > get_window_size(root)[1] - widget.winfo_height():
        y = get_window_size(root)[1] - widget.winfo_height()
    widget.place(x=x, y=y)

def resize_motion(event):
    widget = event.widget.master
    block2.resize(x=-widget.startX + event.x, y=-widget.startY + event.y)

def make_dragable(block):
    block.panel.bind('<Button-1>', dnd_start)
    block.panel.bind('<B1-Motion>', dnd_motion)
    block.panel2.bind('<Button-1>', dnd_start)
    block.panel2.bind('<B1-Motion>', dnd_motion)

def make_resizable(block):
    block.resize_button.bind('<Button-1>', dnd_start)
    block.resize_button.bind('<B1-Motion>', block.resize)

if __name__ == '__main__':
    root = Tk()  # создаем корневой объект - окно
    root.title("Block-Schemes Creator")  # устанавливаем заголовок окна
    max_screen_size_width = root.wm_maxsize()[0]
    max_screen_size_height = root.wm_maxsize()[1]
    root.geometry(f"{max_screen_size_width // 2}x{max_screen_size_height // 2}+500+300")  # устанавливаем размеры окна

    # root.iconphoto(False, icon)
    root.update_idletasks()
    canvas = Canvas(bg="white")
    canvas.pack(fill=BOTH, anchor=CENTER, expand=1)

    block1 = Block(canvas, 300, 300, "pink", "red")
    block1.put(canvas)
    make_dragable(block1)
    make_resizable(block1)
    #block1.make_draggable()
    #block1.make_draggable()

    block2 = Block(canvas, 200, 100, "light blue", "purple")
    block2.put(canvas)
    make_dragable(block2)
    make_resizable(block2)
    #block2.make_draggable()
    #block2.resize(x=100,y=100)
    # block2.panel.bind('<Button-1>', dnd_start)
    # block2.panel.bind('<B1-Motion>', dnd_motion)
    # block2.resize_button.bind('<Button-1>', dnd_start)
    # block2.resize_button.bind('<B1-Motion>', block2.resize)
    #block2.make_resizable()
    #block2.make_resizable()
    #block2.delete()
    root.mainloop()
