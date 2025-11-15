import cairo
import os
import math

ASSETS_PATH = r"E:\Semester 3\Grafkom\Projek_Grafkom\assets"
os.makedirs(ASSETS_PATH, exist_ok=True)

def create_door_closed(size=500):
    path = os.path.join(ASSETS_PATH, "door_closed.png")
    data = bytearray(size * size * 4)
    surf = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32, size, size)
    ctx = cairo.Context(surf)

    # Pintu merah
    ctx.set_source_rgb(1.0, 0.1, 0.1)
    ctx.rectangle(0, 0, size, size)
    ctx.fill()

    # Panel
    ctx.set_source_rgb(0.8, 0.0, 0.0)
    ctx.rectangle(40, 40, size-80, size//2 - 60)
    ctx.rectangle(40, size//2 + 20, size-80, size//2 - 60)
    ctx.fill()

    # Handle kuning
    ctx.set_source_rgb(1, 0.9, 0.2)
    ctx.arc(size - 80, size//2, 45, 0, 2*math.pi)
    ctx.fill()

    # Gembok hitam
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(30)
    ctx.arc(size//2, size//2 - 30, 70, 0, 2*math.pi)
    ctx.stroke()
    ctx.rectangle(size//2 - 55, size//2 - 30, 110, 100)
    ctx.fill()

    # Outline putih
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(35)
    ctx.rectangle(0, 0, size, size)
    ctx.stroke()

    surf.write_to_png(path)
    print(f"Door closed saved: {path}")

def create_door_open(size=500):
    path = os.path.join(ASSETS_PATH, "door_open.png")
    data = bytearray(size * size * 4)
    surf = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32, size, size)
    ctx = cairo.Context(surf)

    # Pintu terbuka
    ctx.set_source_rgb(1.0, 0.1, 0.1)
    ctx.move_to(0, 0)
    ctx.line_to(size*0.55, size*0.15)
    ctx.line_to(size*0.55, size*0.85)
    ctx.line_to(0, size)
    ctx.close_path()
    ctx.fill()

    # Centang putih
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(50)
    ctx.move_to(size//2 - 80, size//2 + 30)
    ctx.line_to(size//2 - 20, size//2 + 90)
    ctx.line_to(size//2 + 100, size//2 - 90)
    ctx.stroke()

    # Outline putih
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(35)
    ctx.rectangle(0, 0, size, size)
    ctx.stroke()

    surf.write_to_png(path)
    print(f"Door open saved: {path}")

if __name__ == "__main__":
    create_door_closed()
    create_door_open()