import taichi as ti

ti.init(arch=ti.gpu)

n = 640
pixels = ti.field(dtype=float, shape=(n * 2, n))


@ti.kernel
def paint(t: float):

    width, height = pixels.shape
    mid_x = width / 2
    mid_y = height / 2

    for i, j in pixels:

        x_dist = i - mid_x
        y_dist = j - mid_y
        y_dist *=2
        dist = ti.sqrt(x_dist**2 + y_dist**2)
        
        pixels[i, j] = 1 if dist > 200 else 0


gui = ti.GUI("Demo", res=(n * 2, n))

i = 0
while gui.running:
    paint(i)
    gui.set_image(pixels)
    gui.show()
    i += 1