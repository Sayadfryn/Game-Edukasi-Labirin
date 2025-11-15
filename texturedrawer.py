import cairo
import os
import math

ASSETS_PATH = r"E:\Semester 3\Grafkom\Projek_Grafkom\assets"

# Pastikan folder ada
os.makedirs(ASSETS_PATH, exist_ok=True)

def create_floor(size=180):
    path = os.path.join(ASSETS_PATH, "floor.png")
    data = bytearray(size * size * 4)
    surf = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32, size, size)
    ctx = cairo.Context(surf)

    ctx.set_source_rgb(0.27, 0.27, 0.35)
    ctx.rectangle(0, 0, size, size)
    ctx.fill()

    ctx.set_source_rgb(0.2, 0.2, 0.28)
    for i in range(0, size, 30):
        ctx.move_to(i, 0); ctx.line_to(i, size)
        ctx.move_to(0, i); ctx.line_to(size, i)
    ctx.set_line_width(1)
    ctx.stroke()

    surf.write_to_png(path)
    print(f"Floor saved: {path}")

def create_wall(size=180):
    path = os.path.join(ASSETS_PATH, "wall.png")
    data = bytearray(size * size * 4)
    surf = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32, size, size)
    ctx = cairo.Context(surf)

    ctx.set_source_rgb(0.12, 0.12, 0.18)
    ctx.rectangle(0, 0, size, size)
    ctx.fill()

    brick_h = 40
    for y in range(0, size, brick_h):
        offset = 20 if (y // brick_h) % 2 == 0 else 0
        for x in range(-60 + offset, size, 120):
            ctx.set_source_rgb(0.15, 0.15, 0.22)
            ctx.rectangle(x, y, 100, brick_h - 8)
            ctx.fill()
            ctx.set_source_rgb(0.08, 0.08, 0.12)
            ctx.rectangle(x, y, 100, brick_h - 8)
            ctx.stroke()

    ctx.set_source_rgba(0, 0, 0, 0.3)
    ctx.rectangle(0, size*0.7, size, size*0.3)
    ctx.fill()

    surf.write_to_png(path)
    print(f"Wall saved: {path}")

def create_goal(size=180):
    path = os.path.join(ASSETS_PATH, "goal.png")
    data = bytearray(size * size * 4)
    surf = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32, size, size)
    ctx = cairo.Context(surf)

    ctx.set_source_rgb(0.0, 0.7, 0.3)
    ctx.rectangle(0, 0, size, size)
    ctx.fill()

    for i in range(5):
        alpha = 0.15 * (5 - i)
        radius = size * 0.3 + i * 15
        ctx.set_source_rgba(0.0, 1.0, 0.4, alpha)
        ctx.arc(size//2, size//2, radius, 0, 2*math.pi)
        ctx.fill()

    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(60)
    ctx.set_source_rgb(1, 1, 0)
    text = "GOAL"
    xb, yb, w, h = ctx.text_extents(text)[:4]
    ctx.move_to(size//2 - w/2 - xb, size//2 + h/2 - yb)
    ctx.show_text(text)

    surf.write_to_png(path)
    print(f"Goal saved: {path}")

if __name__ == "__main__":
    create_floor()
    create_wall()
    create_goal()