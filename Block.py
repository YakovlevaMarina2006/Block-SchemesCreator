from tkinter import *
from tkinter.scrolledtext import ScrolledText

class Block:
    def __init__(self, master, width, height, color, panel_color):
        self.master = master
        self.width = width
        self.height = height
        self.color = color
        self.panel_color = panel_color
        self.tk_obj = 0
        self.panel = 0

    def create(self, master):
        block = Frame(master, bg=self.color, width=self.width, height=self.height)
        self.tk_obj = block
        block.place(x=0, y=0)
        panel = Frame(block, bg=self.panel_color, width=self.width, height=self.height//5)
        panel.place(x=0, y=0)

        btn = Button(panel, text="X", command=lambda: self.delete())
        btn.place(x=self.width-20, y=0)
        self.panel = panel
        text = ScrolledText(block, bg=self.color, wrap="word")
        text.place(x=0, y=20, width=self.width, height=self.height-20)
        #text.pack(fill=BOTH, anchor=CENTER, expand=1)
        #text_frame.place(x=0, y=30)

    def bind(self, *args):
        self.panel.bind(*args)

    def delete(self):
        #self.tk_obj.pack_forget()
        self.tk_obj.destroy()