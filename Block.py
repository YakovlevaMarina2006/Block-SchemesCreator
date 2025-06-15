from tkinter import *
from tkinter.scrolledtext import ScrolledText
import MovementFuncs as MF
#from main import get_window_size

class Block:
    def __init__(self, master, width, height, color, panel_color, min_size=50):
        self.x = 0
        self.y = 0
        self.master = master
        self.width = width
        self.height = height
        self.color = color
        self.panel_color = panel_color
        self.min_size = min_size
        self.block = Frame(master, bg=self.color, width=self.width, height=self.height)
        self.panel = Frame(self.block, bg=self.panel_color, width=self.width, height=20)
        self.text_frame = Frame(self.block, bg="black", width=self.width, height=self.height - 20)
        self.text = ScrolledText(self.text_frame, bg=self.color, wrap="word")
        self.panel2 = Frame(self.block, bg=self.panel_color, width=self.width, height=20)
        self.del_button = Button(self.panel, text="X", command=lambda: self.delete())
        self.resize_button = Button(self.panel2, text="⬊")

    def put(self, master, x=0, y=0):
        self.x = x
        self.y = y
        # global root
        # a = get_window_size(master)
        self.block.place(x=self.x, y=self.y)
        for i in range(3): self.block.rowconfigure(index=i, weight=1)

        self.panel.grid(row=0, column=0, sticky="nsew")

        self.panel2.grid(row=2, column=0, sticky="nsew")

        self.del_button.pack(anchor="e")

        self.resize_button.pack(anchor="e")

        self.text_frame.grid(row=1, column=0, sticky="nsew")
        self.text_frame.columnconfigure(0, weight=10)
        self.text_frame.rowconfigure(0, weight=10)
        self.text_frame.grid_propagate(False)

        self.text.grid(sticky="nsew")

    def place(self, x, y):
        self.x = x
        self.y = y
        self.block.place(x=self.x, y=self.y)

    def make_dragable(self, window, scheme, canvas):
        self.panel.bind('<Button-1>', lambda event: MF.dnd_start(event, self))
        self.panel.bind('<B1-Motion>', lambda event: MF.dnd_motion(event, scheme, self, window, canvas))
        self.panel2.bind('<Button-1>', lambda event: MF.dnd_start(event, self))
        self.panel2.bind('<B1-Motion>', lambda event: MF.dnd_motion(event, scheme, self, window, canvas))

    def make_resizable(self):
        self.resize_button.bind('<Button-1>', lambda event: MF.dnd_start(event, self))
        self.resize_button.bind('<B1-Motion>', lambda event: MF.resize_motion(event, self))

    def delete(self):
        #self.tk_obj.pack_forget()
        self.block.destroy()

    def resize(self, x, y):
        # widget = event.widget.master
        self.width += x
        self.width = max(self.width, self.min_size)
        self.height += y
        self.height = max(self.height, self.min_size)
        self.text_frame.config(width=self.width)
        self.text_frame.config(height=self.height)

    def move_to(self, x, y):
        self.x = x
        self.y = y
        self.block.place(x=self.x, y=self.y)

    def get_position(self):
        return {"x": self.x, "y": self.y}

    def make_lower(self):
        self.block.lower()
