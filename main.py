
#from tkinter import *
from Block import *
from Scheme import *
#from MovementFuncs import draw_line,


CONTROL_PANEL_HEIGHT = 30


if __name__ == '__main__':
    root = Tk()  # создаем корневой объект - окно
    root.title("Block-Schemes Creator")  # устанавливаем заголовок окна
    max_screen_size_width = root.wm_maxsize()[0]
    max_screen_size_height = root.wm_maxsize()[1]
    root.geometry(f"{max_screen_size_width // 2}x{max_screen_size_height // 2}+500+300")  # устанавливаем размеры окна
    #icon = PhotoImage(file="cat_icon.png")
    #root.iconphoto(False, icon)
    root.update_idletasks()


    canvas = Canvas()
    canvas.config(highlightthickness=0)
    canvas.pack(fill=BOTH, side=TOP, expand=1)

    control_panel = Frame(canvas, bg="black", height=CONTROL_PANEL_HEIGHT)
    control_panel.pack(fill=X, side=TOP, anchor="n", expand=1)

    add_block_btn = Button(control_panel, text="add block", command=lambda : scheme.add_block(canvas, root))
    add_block_btn.pack(side=LEFT)

    scheme = Scheme()

    root.update_idletasks()

    root.mainloop()
