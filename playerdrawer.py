import cairo
import os

ASSETS_PATH = r"E:\Semester 3\Grafkom\Projek_Grafkom\assets"
os.makedirs(ASSETS_PATH, exist_ok=True)

def create_player_asset(size=500):
    path = os.path.join(ASSETS_PATH, "player.png")
    data = bytearray(size * size * 4)
    surf = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32, size, size)
    ctx = cairo.Context(surf)

    # Kepala
    ctx.set_source_rgb(0.8, 0.9, 1.0)
    ctx.arc(size//2, size*0.3, size*0.18, 0, 2*3.14159)
    ctx.fill()

    # Mata
    ctx.set_source_rgb(1, 1, 1)
    ctx.arc(size//2 - 40, size*0.28, 35, 0, 2*3.14159)
    ctx.arc(size//2 + 40, size*0.28, 35, 0, 2*3.14159)
    ctx.fill()
    ctx.set_source_rgb(0, 0, 0)
    ctx.arc(size//2 - 40, size*0.28, 20, 0, 2*3.14159)
    ctx.arc(size//2 + 40, size*0.28, 20, 0, 2*3.14159)
    ctx.fill()

    # Baju pink
    ctx.set_source_rgb(1.0, 0.4, 0.7)
    ctx.rectangle(size*0.3, size*0.45, size*0.4, size*0.25)
    ctx.fill()

    # Celana biru
    ctx.set_source_rgb(0.1, 0.3, 0.8)
    ctx.rectangle(size*0.33, size*0.68, size*0.15, size*0.25)
    ctx.rectangle(size*0.52, size*0.68, size*0.15, size*0.25)
    ctx.fill()

    # Sepatu hitam
    ctx.set_source_rgb(0.1, 0.1, 0.1)
    ctx.rectangle(size*0.3, size*0.92, size*0.18, 30)
    ctx.rectangle(size*0.52, size*0.92, size*0.18, 30)
    ctx.fill()

    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(25)
    ctx.rectangle(0, 0, size, size)
    ctx.stroke()

    surf.write_to_png(path)
    print(f"Player asset saved: {path}")

if __name__ == "__main__":
    create_player_asset()