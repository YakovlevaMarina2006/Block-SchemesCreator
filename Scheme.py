

class Scheme:
    def __init__(self):
        self.blocks = []
        self.arrows = []
        self.size = 0

    def add_block(self, block):
        self.blocks.append(block)
        self.size += 1
        for string in self.arrows:
            string.append(0)
        self.arrows.append([0 for i in range(self.size)])

    def add_arrow(self, from_block, to_block, line):
        self.arrows[self.find_block(from_block)][self.find_block(to_block)] = line

    def find_block(self, block):
        return self.blocks.index(block)

    def get_arrow(self, from_block, to_block):
        return self.arrows[self.find_block(from_block)][self.find_block(to_block)]

    def get_size(self):
        return self.size

    def get_arrows(self):
        return self.arrows
