from copy import deepcopy
from random import randint
from itertools import cycle

import pyglet
from pyglet.window import Window, key, mouse

window_width = 640
window_height = 480

cell_size = 2
cells_high = window_height // cell_size
cells_wide = window_width // cell_size

grid = [1 for cell in range(cells_high)]
grid = [grid[:] for cell in range(cells_wide)]
working_grid = grid[:]

born = {3}
survives = {2, 3, 8}

window = Window(window_width, window_height)
window.set_caption("Cellular Automaton")


@window.event
def on_draw():
    window.clear()
    color_cells()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.I:
        for x in range(cells_wide):
            for y in range(cells_high):
                grid[x][y] = 0
    elif symbol == key.O:
        for x in range(cells_wide):
            for y in range(cells_high):
                grid[x][y] = 1
    elif symbol == key.P:
        randomize_grid()
    elif symbol == key.RIGHT:
        update_grid()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        grid[x // cell_size][y // cell_size] = 1
    elif button == mouse.RIGHT:
        grid[x // cell_size][y // cell_size] = 0


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if 0 <= x / cell_size < cells_wide and 0 <= y / cell_size < cells_high:
        if buttons == mouse.LEFT:
            grid[x // cell_size][y // cell_size] = 1
        elif buttons == mouse.RIGHT:
            grid[x // cell_size][y // cell_size] = 0


def color_cells():
    batch = pyglet.graphics.Batch()
    cell_color = next(color_iterator)
    pyglet.gl.glColor3f(cell_color[0], cell_color[1], cell_color[2])
    for x in range(cells_wide):
        for y in range(cells_high):
            if grid[x][y]:
                x1 = x * cell_size
                y1 = y * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                batch.add(4, pyglet.gl.GL_QUADS, None, ('v2i', (x1, y1, x1, y2, x2, y2, x2, y1)))
    batch.draw()


def update(dt):
    global grid
    for x in range(cells_wide):
        for y in range(cells_high):
            n = get_neighbors(x, y)
            if not grid[x][y]:
                working_grid[x][y] = 1 if n in born else 0
            else:
                working_grid[x][y] = 1 if n in survives else 0
    grid = working_grid[:]


def get_neighbors(x, y):
    n = 0
    for i,j in ((-1,1), (1,-1), (1,1), (-1,-1), (1,0), (0,1), (-1,0), (0,-1)):
        if 0 <= x + i < cells_wide and 0 <= y + j < cells_high:
            n += grid[x + i][y + j]
    return n


def randomize_grid():
    for x in range(cells_wide):
        for y in range(cells_high):
            grid[x][y] = randint(0, 2)


def color_generator():
    color = [1.0, 0, 0]
    iterations = 50
    increment = 1.0 / iterations
    fill = True

    for i in cycle((1, 0, 2)):
        for n in range(iterations):
            if fill:
                color[i] += increment
            else:
                color[i] -= increment
            yield color
        fill = not fill


if __name__ == "__main__":
    randomize_grid()
    color_iterator = color_generator()
    pyglet.clock.schedule_interval(update, 1.0 / 60.0)
    pyglet.app.run()