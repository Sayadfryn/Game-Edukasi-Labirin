import pygame
import os
import cairo
from pygame.locals import *
from shapedrawer import ShapeDrawer
from question import Question
from player import Player
from door import Door
from camera import Camera
from minimap import Minimap
from maze import maze

ASSETS_PATH = r"E:\Semester 3\Grafkom\Projek_Grafkom\assets"
os.makedirs(ASSETS_PATH, exist_ok=True)
pygame.init()
info = pygame.display.Info()
SW, SH = info.current_w, info.current_h
TILE_SIZE = 180  
FPS = 60

FLOOR_COLOR = (70, 70, 90)
WALL_COLOR = (20, 20, 40)
GRID_COLOR = (100, 100, 130)
SKY_COLOR = (50, 50, 70)
GOAL_COLOR = (0, 200, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


if not os.path.exists(os.path.join(ASSETS_PATH, "player.png")):
    print("Membuat karakter...")
    import playerdrawer
    playerdrawer.create_player_asset()

if not os.path.exists(os.path.join(ASSETS_PATH, "door_closed.png")):
    print("Membuat pintu...")
    import doordrawer
    doordrawer.create_door_closed()
    doordrawer.create_door_open()
    
if not os.path.exists(os.path.join(ASSETS_PATH, "floor.png")):
    print("Membuat texture lantai, tembok, dan goal...")
    import texturedrawer
    texturedrawer.create_floor()
    texturedrawer.create_wall()
    texturedrawer.create_goal()

if not os.path.exists(os.path.join(ASSETS_PATH, "player.png")):
    print("Membuat karakter...")
    import playerdrawer
    playerdrawer.create_player_asset()

if not os.path.exists(os.path.join(ASSETS_PATH, "door_closed.png")):
    print("Membuat pintu...")
    import doordrawer
    doordrawer.create_door_closed()
    doordrawer.create_door_open()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SW, SH), FULLSCREEN)
        pygame.display.set_caption("LABIRIN BANGUN DATAR")
        self.clock = pygame.time.Clock()

        
        self.floor_img = pygame.image.load(os.path.join(ASSETS_PATH, "floor.png")).convert_alpha()
        self.wall_img = pygame.image.load(os.path.join(ASSETS_PATH, "wall.png")).convert_alpha()
        self.goal_img = pygame.image.load(os.path.join(ASSETS_PATH, "goal.png")).convert_alpha()

        self.floor_img = pygame.transform.smoothscale(self.floor_img, (TILE_SIZE, TILE_SIZE))
        self.wall_img = pygame.transform.smoothscale(self.wall_img, (TILE_SIZE, TILE_SIZE))
        self.goal_img = pygame.transform.smoothscale(self.goal_img, (TILE_SIZE, TILE_SIZE))
        
        self.maze = maze
        # Di __init__ → HANYA BUAT OBJEK
        self.player = Player(TILE_SIZE + 30, TILE_SIZE + 30, TILE_SIZE)
        self.doors = [Door(x, y, TILE_SIZE) for y, row in enumerate(maze) for x, cell in enumerate(row) if cell == 2]
        self.question = Question()
        self.camera = Camera(SW, SH, len(maze[0]), len(maze), TILE_SIZE)
        self.minimap = Minimap(maze, SW, SH, TILE_SIZE)

        self.font = pygame.font.Font(None, 50)
        self.small = pygame.font.Font(None, 36)
        self.show_q = self.show_exp = False
        self.current_door = None
        self.selected = None
        self.running = True
        self.won = False
        self.back_btn = None
        self.opts = []

    def draw_maze(self):
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                rx = x * TILE_SIZE - self.camera.x
                ry = y * TILE_SIZE - self.camera.y
                rect = pygame.Rect(rx, ry, TILE_SIZE, TILE_SIZE)
                if not (rect.right >= 0 and rect.left <= SW and rect.bottom >= 0 and rect.top <= SH):
                    continue

                cell = self.maze[y][x]
                if cell == 1:
                    self.screen.blit(self.wall_img, (rx, ry))
                elif cell == 3:
                    self.screen.blit(self.goal_img, (rx, ry))
                else:
                    self.screen.blit(self.floor_img, (rx, ry))


    def draw_shape(self, typ, x, y, sz):
        data = bytearray(sz * sz * 4)
        surf = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32, sz, sz)
        col = (70, 130, 255)

        if typ == 'circle':
            ShapeDrawer.draw_circle(surf, 10, 10, (sz-20)//2, col)
        elif typ == 'triangle':
            ShapeDrawer.draw_triangle(surf, 10, 10, sz-20, col)
        elif typ == 'square':
            ShapeDrawer.draw_square(surf, 10, 10, sz-20, col)
        elif typ == 'rectangle':
            ShapeDrawer.draw_rectangle(surf, 10, 10, sz-20, sz//2 - 10, col)
        elif typ == 'trapezoid':
            ShapeDrawer.draw_trapezoid(surf, 10, 10, sz-20, col)
        elif typ == 'pentagon':
            ShapeDrawer.draw_pentagon(surf, 10, 10, sz-20, col)
        elif typ == 'hexagon':
            ShapeDrawer.draw_hexagon(surf, 10, 10, sz-20, col) 

        img = pygame.image.frombuffer(bytes(data), (sz, sz), 'ARGB')
        self.screen.blit(img, (x, y))

    def draw_popup(self):
        w, h = 900, 650
        px, py = (SW - w)//2, (SH - h)//2
        overlay = pygame.Surface((SW, SH)); overlay.set_alpha(220); overlay.fill(BLACK)
        self.screen.blit(overlay, (0,0))
        pygame.draw.rect(self.screen, WHITE, (px, py, w, h))
        pygame.draw.rect(self.screen, BLACK, (px, py, w, h), 5)

        if self.show_exp:
            self.screen.blit(self.font.render("SALAH!", True, (200,0,0)), (px+50, py+40))
            for i, line in enumerate(self.question.current_question['explanation'].split('\n')):
                self.screen.blit(self.small.render(line, True, BLACK), (px+50, py+120 + i*40))
            self.screen.blit(self.small.render("Jawaban benar:", True, BLACK), (px+50, py+300))
            self.draw_shape(self.question.current_question['answer'], px+380, py+280, 110)
            btn = pygame.Rect(px+330, py+520, 240, 70)
            pygame.draw.rect(self.screen, (0,100,200), btn)
            self.screen.blit(self.font.render("Coba Lagi", True, WHITE), 
                           self.font.render("Coba Lagi", True, WHITE).get_rect(center=btn.center))
            return btn
        else:
            q = self.question.current_question
            self.screen.blit(self.font.render("BUKA PINTU DENGAN JAWAB SOAL!", True, BLACK), (px+100, py+30))
            self.draw_shape(q['shape1'], px+200, py+120, 110)
            self.screen.blit(self.font.render("+", True, BLACK), (px+340, py+150))
            self.draw_shape(q['shape2'], px+400, py+120, 110)
            self.screen.blit(self.font.render("=", True, BLACK), (px+540, py+150))
            self.screen.blit(self.font.render("?", True, (200,0,0)), (px+620, py+140))

            opts = []
            for i, opt in enumerate(q['options']):
                r, c = i//2, i%2
                bx = px + 120 + c*380
                by = py + 320 + r*160
                rect = pygame.Rect(bx, by, 150, 150)
                col = (255,255,100) if self.selected == opt else WHITE
                pygame.draw.rect(self.screen, col, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 4)
                self.draw_shape(opt, bx+25, by+25, 100)
                opts.append((rect, opt))
            return opts


    def run(self):  
        while self.running:
            self.clock.tick(FPS)
            for e in pygame.event.get():
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    self.running = False
                if e.type == MOUSEBUTTONDOWN and self.show_q:
                    pos = pygame.mouse.get_pos()
                    if self.show_exp:
                        if self.back_btn and self.back_btn.collidepoint(pos):
                            self.show_exp = False
                            self.selected = None
                    else:
                        for r, opt in self.opts:
                            if r.collidepoint(pos):
                                self.selected = opt
                                if self.question.check_answer(opt):
                                    self.current_door.is_open = True
                                    self.show_q = False
                                    self.question.generate_new_question()
                                else:
                                    self.show_exp = True

            if not self.won:
                k = pygame.key.get_pressed()
                dx = dy = 0
                if k[K_a] or k[K_LEFT]: dx = -1
                if k[K_d] or k[K_RIGHT]: dx = 1
                if k[K_w] or k[K_UP]: dy = -1
                if k[K_s] or k[K_DOWN]: dy = 1

                if not self.show_q:
                    self.player.move(dx, dy, self.maze)

                self.camera.update(self.player)

                if not self.show_q:
                    door = next((d for d in self.doors if not d.is_open and d.check_collision(self.player)), None)
                    if door:
                        self.show_q = True
                        self.current_door = door

                px = int((self.player.x + self.player.target_width // 2) // TILE_SIZE)
                py = int((self.player.y + self.player.target_height // 2) // TILE_SIZE)
                if 0 <= py < len(self.maze) and 0 <= px < len(self.maze[0]) and self.maze[py][px] == 3:
                    self.won = True

            self.screen.fill(SKY_COLOR)
            self.draw_maze()
            for d in self.doors:
                d.draw(self.screen, self.camera.x, self.camera.y)
            self.player.draw(self.screen, self.camera.x, self.camera.y)
            self.minimap.draw(self.screen, self.player, self.doors)

            if self.show_q:
                res = self.draw_popup()
                if self.show_exp:
                    self.back_btn = res
                else:
                    self.opts = res

            if self.won:
                overlay = pygame.Surface((SW, SH))
                overlay.set_alpha(200)
                overlay.fill(BLACK)
                self.screen.blit(overlay, (0, 0))
                win = self.font.render("SELAMAT! KAMU MENANG!", True, (0, 255, 0))
                self.screen.blit(win, win.get_rect(center=(SW//2, SH//2)))
                self.screen.blit(self.small.render("Tekan ESC untuk keluar", True, WHITE),
                               self.small.render("Tekan ESC untuk keluar", True, WHITE).get_rect(center=(SW//2, SH//2 + 80)))

            pygame.display.flip()

        pygame.quit()  

if __name__ == "__main__":
    Game().run()