
#from tkinter import *
from Block import *
from Scheme import *
from SaveOpen import *
from tkinter.messagebox import showinfo
#from MovementFuncs import draw_line,


CONTROL_PANEL_HEIGHT = 30


def OK_btn_func(window, entry):
    global scheme
    scheme = Scheme(entry.get())
    window.destroy()


def create_scheme(canvas):
    global scheme
    scheme.clear(canvas)
    window = Tk()
    window.title("Enter the name")
    entry = Entry(window, width=40)
    entry.pack(side=LEFT)
    OK_btn = Button(window, text="OK", command=lambda: OK_btn_func(window, entry))
    OK_btn.pack(side=RIGHT)
    window.resizable(False, False)


def show_instruction():
    instruction_text = ""
    with open("instruction3.txt", "r") as file:
        instruction_text = file.read()
    window = Tk()
    window.title("instruction")
    label = Label(window, text=instruction_text, font=("Arial", 14), justify=LEFT)
    label.pack()


def open_scheme_start(canvas, window):
    global scheme
    scheme.clear(canvas)
    scheme = open_scheme(canvas, window)

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

    scheme = Scheme("")

    control_panel = Frame(canvas, bg="black", height=CONTROL_PANEL_HEIGHT)
    control_panel.pack(fill=X, side=TOP, anchor="n", expand=1)

    add_block_btn = Button(control_panel, text="add block", command=lambda : scheme.add_block(root, canvas))
    add_block_btn.pack(side=LEFT)


    instruction_btn = Button(control_panel, text="instruction", command=show_instruction)
    instruction_btn.pack(side=RIGHT)

    save_btn = Button(control_panel, text="save", command=lambda: save_scheme(scheme))
    save_btn.pack(side=RIGHT)

    open_btn = Button(control_panel, text="open", command=lambda : open_scheme_start(canvas, root))
    open_btn.pack(side=RIGHT)

    create_btn = Button(control_panel, text="create", command=lambda: create_scheme(canvas))
    create_btn.pack(side=RIGHT)


    root.update_idletasks()

    root.mainloop()
