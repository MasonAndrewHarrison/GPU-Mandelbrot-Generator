import taichi as ti
import taichi.math as tm
from PIL import Image 
import numpy as np

ti.init(arch=ti.gpu)

resolution = (1920, 1080)
pixels = ti.field(dtype=float, shape=resolution)

@ti.func
def mandelbrot(c: tm.vec2, max_iter: int = 100) -> float:
    z = tm.vec2(0.0, 0.0)
    result = float(max_iter)
    for n in range(max_iter):

        z = tm.cpow(z, 2) + c

        if tm.length(z) > 2.0:
            result = float(n) / float(max_iter)
            break
        
    return result

@ti.kernel
def paint(t: float, x_offset: float, y_offset: float, zoom: float):
    width, height = pixels.shape
    aspect = float(width) / float(height)

    for i, j in pixels:

        x = (float(i + x_offset) / float(width) - 0.5) * aspect
        y = (float(j + y_offset) / float(height) - 0.5)
        
        x = (x / (zoom*0.5)) + x_offset - 0.50
        y = (y / (zoom*0.5)) + y_offset

        c = tm.vec2(x, y)
        pixels[i, j] = mandelbrot(c, max_iter = 250)


gui = ti.GUI("Demo", res=resolution)

i = 0
x_offset: float = 0.0
y_offset: float = 0.0
zoom: float = 1.0
changed: bool = True

while gui.running:

    while gui.get_event():
        pass

    if gui.is_pressed('a'):
        x_offset -= 0.05 / zoom
        changed = True
    elif gui.is_pressed('d'):
        x_offset += 0.05 / zoom
        changed = True
    if gui.is_pressed('w'):
        y_offset += 0.05 / zoom
        changed = True
    elif gui.is_pressed('s'):
        y_offset -= 0.05 / zoom
        changed = True
    if gui.is_pressed('q'):
        zoom *= 1.05
        changed = True
    elif gui.is_pressed('e'):
        zoom /= 1.05
        changed = True
    if gui.is_pressed('p'):
        ti.tools.image.imwrite(pixels, 'screenshot.png')
    
    if changed:
        paint(i, x_offset, y_offset, zoom)
        changed = False

    gui.set_image(pixels)
    gui.show()
    
    i += 1