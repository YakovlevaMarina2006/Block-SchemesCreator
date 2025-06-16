


def draw_line(canvas, from_block, to_block):
    return canvas.create_line(from_block.get_position()["x"], from_block.get_position()["y"], \
                       to_block.get_position()["x"], to_block.get_position()["y"], arrow="last")


def redraw_line(canvas, line, from_block, to_block):
    canvas.coords(line, from_block.get_position()["x"], from_block.get_position()["y"], \
                                        to_block.get_position()["x"], to_block.get_position()["y"])


def delete_arrow(canvas, arrow):
    canvas.delete(arrow)