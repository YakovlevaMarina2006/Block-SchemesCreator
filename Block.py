from tkinter import *
from tkinter.scrolledtext import ScrolledText
# import MovementFuncs as MF

class Block:
    def __init__(self, master, width, height, color, panel_color):
        self.master = master
        self.width = width
        self.height = height
        self.color = color
        self.panel_color = panel_color
        self.block = Frame(master, bg=self.color, width=self.width, height=self.height)
        self.panel = Frame(self.block, bg=self.panel_color, width=self.width, height=20)
        self.text_frame = Frame(self.block, bg="black", width=self.width, height=self.height - 20)
        self.text = ScrolledText(self.text_frame, bg=self.color, wrap="word")
        self.panel2 = Frame(self.block, bg=self.panel_color, width=self.width, height=20)
        self.del_button = Button(self.panel, text="X", command=lambda: self.delete())
        self.resize_button = Button(self.panel2, text="X")

    def put(self, master):

        self.block.place(x=0, y=0)
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


    # def make_draggable(self):
    #     self.panel.bind('<Button-1>', MF.dnd_start)
    #     self.panel.bind('<B1-Motion>', MF.dnd_motion)
    #     self.panel2.bind('<Button-1>', MF.dnd_start)
    #     self.panel2.bind('<B1-Motion>', MF.dnd_motion)
    #
    # def make_resizable(self):
    #     self.resize_button.bind('<Button-1>', MF.dnd_start)
    #     self.resize_button.bind('<B1-Motion>', MF.resize_motion)

    def delete(self):
        #self.tk_obj.pack_forget()
        self.block.destroy()

    def resize(self, event):
        widget = event.widget.master
        self.width += -widget.startX + event.x
        self.height += -widget.startY + event.y
        self.text_frame.config(width=self.width)
        self.text_frame.config(height=self.height)
