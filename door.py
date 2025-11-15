import pygame
import os

ASSETS_PATH = r"E:\Semester 3\Grafkom\Projek_Grafkom\assets"

class Door:
    def __init__(self, grid_x, grid_y, tile_size):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.x = grid_x * tile_size
        self.y = grid_y * tile_size
        self.tile_size = tile_size
        self.is_open = False

        closed_path = os.path.join(ASSETS_PATH, "door_closed.png")
        open_path = os.path.join(ASSETS_PATH, "door_open.png")

        self.closed = self.load_and_scale(closed_path, tile_size, tile_size)
        self.opened = self.load_and_scale(open_path, tile_size, tile_size)

    def load_and_scale(self, path, w, h):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Gambar pintu tidak ditemukan: {path}")
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.smoothscale(img, (w, h))

    def check_collision(self, player):
        return (self.x < player.x + player.target_width and
                self.x + self.tile_size > player.x and
                self.y < player.y + player.target_height and
                self.y + self.tile_size > player.y)

    def draw(self, screen, cam_x, cam_y):
        sprite = self.opened if self.is_open else self.closed
        screen.blit(sprite, (self.x - cam_x, self.y - cam_y))