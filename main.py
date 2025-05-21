
from tkinter import *
from Block import *

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
    widget.place(x = x, y = y)



if __name__ == '__main__':
    root = Tk()  # создаем корневой объект - окно
    root.title("Block-Schemes Creator")  # устанавливаем заголовок окна

    max_screen_size_width = root.wm_maxsize()[0]
    max_screen_size_height = root.wm_maxsize()[1]
    root.geometry(f"{max_screen_size_width//2}x{max_screen_size_height//2}+500+300")  # устанавливаем размеры окна
    # root.iconphoto(False, icon)
    root.update_idletasks()
    canvas = Canvas(bg="white", width=get_window_size(root)[0] - 100, height=get_window_size(root)[1] - 100)
    canvas.pack(fill=BOTH, anchor=CENTER, expand=1)

    block1 = Block(canvas, 300, 300, "pink", "red")
    block1.create(canvas)
    block1.bind('<Button-1>', dnd_start)
    block1.bind('<B1-Motion>', dnd_motion)

    block2 = Block(canvas, 100, 100, "light blue", "purple")
    block2.create(canvas)
    block2.bind('<Button-1>', dnd_start)
    block2.bind('<B1-Motion>', dnd_motion)
    #block2.delete()


    root.mainloop()
