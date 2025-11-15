import pygame

class Minimap:
    def __init__(self, maze, sw, sh, tile_size):
        self.maze = maze
        self.size = 200
        self.ratio = self.size / max(len(maze[0]), len(maze))
        self.w = int(len(maze[0]) * self.ratio)
        self.h = int(len(maze) * self.ratio)
        self.x = 20
        self.y = 20
        self.tile_size = tile_size

    def draw(self, screen, player, doors):
        pygame.draw.rect(screen, (30, 30, 50), (self.x, self.y, self.w, self.h))
        pygame.draw.rect(screen, (200, 200, 200), (self.x, self.y, self.w, self.h), 3)

        # Gambar maze di minimap
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 1:
                    color = (60, 60, 80)
                elif cell == 3:
                    color = (0, 200, 100)
                elif cell == 2:
                    color = (200, 0, 0)
                else:
                    color = (100, 100, 120)
                rx = self.x + x * self.ratio
                ry = self.y + y * self.ratio
                pygame.draw.rect(screen, color, (rx, ry, self.ratio, self.ratio))

        # Gambar player (PAKAI target_width)
        px = self.x + (player.x + player.target_width // 2) / self.tile_size * self.ratio
        py = self.y + (player.y + player.target_height // 2) / self.tile_size * self.ratio
        pygame.draw.circle(screen, (255, 100, 200), (int(px), int(py)), 6)

        for d in doors:
            dx = self.x + d.grid_x * self.ratio
            dy = self.y + d.grid_y * self.ratio
            color = (0, 255, 0) if d.is_open else (255, 0, 0)
            pygame.draw.rect(screen, color, (dx, dy, self.ratio, self.ratio))