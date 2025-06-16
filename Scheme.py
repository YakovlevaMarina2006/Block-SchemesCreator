

import Block as Block
import DrawingFuncs as DF

connection_started_flag = False
from_block = None
to_block = None

class Scheme:
    def __init__(self, name):
        self.name = name
        self.blocks = []
        self.arrows = []
        self.size = 0

    def add_block(self, window, canvas, x=100, y=100, width=100, height=100, color="light blue", panel_color="purple", text=""):
        new_block = Block.Block(window, canvas, self, width, height, color, panel_color, text)
        new_block.place(x, y)
        self.blocks.append(new_block)
        self.size += 1
        for string in self.arrows:
            string.append(0)
        self.arrows.append([0 for i in range(self.size)])
        print(self.blocks)



    def add_arrow(self, canvas, block):
        global connection_started_flag
        global from_block
        global to_block
        if not connection_started_flag:
            connection_started_flag = True
            from_block = block
        else:
            to_block = block
            if self.get_arrow(from_block, to_block) != 0:
                DF.delete_arrow(canvas, self.get_arrow(from_block, to_block))
            self.arrows[self.find_block(from_block)][self.find_block(to_block)] = DF.draw_line(canvas, from_block, to_block)
            connection_started_flag = False

            DF.redraw_line(canvas, self.arrows[self.find_block(from_block)][self.find_block(to_block)], from_block, to_block)
        print(self.arrows)


    def find_block(self, block):
        return self.blocks.index(block)

    def get_arrow(self, from_block, to_block):
        return self.arrows[self.find_block(from_block)][self.find_block(to_block)]

    def get_size(self):
        return self.size

    def get_arrows(self):
        return self.arrows

    def get_blocks(self):
        return self.blocks

    def delete_arrow(self, from_block, to_block):
        self.arrows[self.find_block(from_block)][self.find_block(to_block)] = 0

    def delete_block(self, canvas, block):
        block_index = self.find_block(block)
        for i in range(self.size):
            DF.delete_arrow(canvas, self.arrows[i][block_index])
            DF.delete_arrow(canvas, self.arrows[block_index][i])

        self.arrows.pop(block_index)
        for string in self.arrows:
            string.pop(block_index)
        self.blocks.remove(block)
        block.destroy()
        self.size -= 1

    def clear(self, canvas):
        blocks = self.blocks.copy()
        for block in blocks:
            self.delete_block(canvas, block)
        print(self.blocks)
        canvas.delete("all")