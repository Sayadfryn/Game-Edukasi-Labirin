import pygame
import os

ASSETS_PATH = r"E:\Semester 3\Grafkom\Projek_Grafkom\assets"

class Player:
    def __init__(self, x, y, tile_size):
        self.x = x
        self.y = y
        self.target_width = 120
        self.target_height = 120
        self.speed = 8
        self.tile_size = tile_size

        sprite_path = os.path.join(ASSETS_PATH, "player.png")
        self.sprite = self.load_and_scale(sprite_path, self.target_width, self.target_height)

    def load_and_scale(self, path, w, h):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Gambar tidak ditemukan: {path}")
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.smoothscale(img, (w, h))

    def move(self, dx, dy, maze):
        if dx == dy == 0:
            return
        nx = self.x + dx * self.speed
        ny = self.y + dy * self.speed
        if not self.check_collision(nx, ny, maze):
            self.x, self.y = nx, ny

    def check_collision(self, x, y, maze):
        margin = 10
        points = [
            (x + margin, y + margin),
            (x + self.target_width - margin, y + margin),
            (x + margin, y + self.target_height - margin),
            (x + self.target_width - margin, y + self.target_height - margin),
        ]
        for px, py in points:
            mx, my = int(px // self.tile_size), int(py // self.tile_size)
            if not (0 <= my < len(maze) and 0 <= mx < len(maze[0])) or maze[my][mx] == 1:
                return True
        return False

    def draw(self, screen, cam_x, cam_y):
        screen.blit(self.sprite, (self.x - cam_x, self.y - cam_y))