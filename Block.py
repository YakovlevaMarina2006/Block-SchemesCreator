from tkinter import *
from tkinter.scrolledtext import ScrolledText
import MovementFuncs as MF


class Block:
    def __init__(self, window, canvas, scheme, width, height, color, panel_color, text="", min_size=50):
        # self.x = 0
        # self.y = 0
        self.scheme = scheme
        self.canvas = canvas
        self.width = width
        self.height = height
        self.color = color
        self.panel_color = panel_color
        self.min_size = min_size

        self.block = Frame(canvas, bg=self.color, width=self.width, height=self.height)
        self.panel = Frame(self.block, bg=self.panel_color, width=self.width, height=20)
        self.text_frame = Frame(self.block, bg="black", width=self.width, height=self.height - 20)
        self.text = ScrolledText(self.text_frame, bg=self.color, wrap="word")
        self.text.insert('1.0', text)
        self.panel2 = Frame(self.block, bg=self.panel_color, width=self.width, height=20)

        self.del_button = Button(self.panel, text="X", command=lambda: self.scheme.delete_block(self.canvas, self))
        self.resize_button = Button(self.panel2, text="⬊")
        self.make_lower_button = Button(self.panel, text="▽", command=lambda: self.make_lower())
        self.connect_button = Button(self.panel, text=".")

        self.make_dragable(window, canvas, scheme)
        self.make_resizable()
        self.make_connectable(canvas, scheme)

        for i in range(3): self.block.rowconfigure(index=i, weight=1)

        self.panel.grid(row=0, column=0, sticky="nsew")

        self.panel2.grid(row=2, column=0, sticky="nsew")

        self.del_button.pack(side="right", anchor="e")
        self.make_lower_button.pack(side="right")
        self.connect_button.pack(side="left")

        self.resize_button.pack(anchor="e")

        self.text_frame.grid(row=1, column=0, sticky="nsew")
        self.text_frame.columnconfigure(0, weight=10)
        self.text_frame.rowconfigure(0, weight=10)
        self.text_frame.grid_propagate(False)

        self.text.grid(sticky="nsew")

    def place(self, x, y):
        self.block.place(x=x, y=y)

    def make_dragable(self, window, canvas, scheme):
        self.panel.bind('<Button-1>', lambda event: MF.dnd_start(event, self))
        self.panel.bind('<B1-Motion>', lambda event: MF.dnd_motion(event, scheme, self, window, canvas))
        self.panel2.bind('<Button-1>', lambda event: MF.dnd_start(event, self))
        self.panel2.bind('<B1-Motion>', lambda event: MF.dnd_motion(event, scheme, self, window, canvas))

    def make_resizable(self):
        self.resize_button.bind('<Button-1>', lambda event: MF.dnd_start(event, self))
        self.resize_button.bind('<B1-Motion>', lambda event: MF.resize_motion(event, self))

    def make_connectable(self, canvas, scheme):
        self.connect_button.config(command=lambda : scheme.add_arrow(canvas, self))

    def destroy(self):
        self.block.destroy()

    def resize(self, x, y):
        self.width += x
        self.width = max(self.width, self.min_size)
        self.height += y
        self.height = max(self.height, self.min_size)
        self.text_frame.config(width=self.width)
        self.text_frame.config(height=self.height)

    def get_position(self):
        return {"x": self.block.winfo_x(), "y": self.block.winfo_y()}

    def get_size(self):
        return {"width": self.width, "height": self.height}

    def color_info(self):
        return {"color": self.color, "panel color": self.panel_color}

    def get_text(self):
        return self.text.get("1.0",'end-1c')

    def make_lower(self):
        self.block.lower()
