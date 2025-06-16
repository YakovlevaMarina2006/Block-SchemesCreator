from Scheme import *
from tkinter import filedialog
from DrawingFuncs import redraw_line
def save_scheme(scheme):
    filename = scheme.name
    with open(f"MySchemes/{filename}.txt", "w") as file:
        file.write(scheme.name)
        file.write("\n" + f"{scheme.get_size()}")

        for i in range(scheme.get_size()):      # save blocks info
            file.write(f"\n")
            block = scheme.get_blocks()[i]
            file.write(f"{block.get_position()['x']}*{block.get_position()['y']}*")
            file.write(f"{block.get_size()['width']}*{block.get_size()['height']}*{block.color_info()['color']}*{block.color_info()['panel color']}")
            file.write(f"\n")
            file.write(block.get_text())

        for i in range(scheme.get_size()):     # save arrows info
            file.write("\n")
            file.write(" ".join(map(str, scheme.get_arrows()[i])))
        file.write("\n")

def open_scheme(canvas, window):
    filepath = filedialog.askopenfilename()
    scheme = None
    with open(filepath, "r") as file:
        scheme = Scheme(file.readline()[:-1])
        size = int(file.readline()[:-1])
        for i in range(size):                    # add blocks
            x, y, width, height, color, panel_color = file.readline()[:-1].split("*")
            x = int(x)
            y = int(y)
            width = int(width)
            height = int(height)
            text = file.readline()[:-1]
            scheme.add_block(window, canvas, x, y, width, height, color, panel_color, text)


        for i in range(size):                  # add arrows
            string = list(map(int, file.readline()[:-1].split()))
            for j in range(size):
                if string[j] != 0:
                    print(string[j])
                    scheme.add_arrow(canvas, scheme.get_blocks()[i])
                    scheme.add_arrow(canvas, scheme.get_blocks()[j])


    for i in range(scheme.get_size()):  # add arrows
        for j in range(scheme.get_size()):
            if scheme.get_arrows()[i][j] != 0:
                redraw_line(canvas, scheme.get_arrows()[i][j], scheme.get_blocks()[i], scheme.get_blocks()[j])

    return scheme