import pygame
import cairo
import math
import random
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
TILE_SIZE = 40
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 150, 255)
GREEN = (100, 255, 100)
RED = (255, 100, 100)
YELLOW = (255, 255, 100)
GRAY = (180, 180, 180)

class ShapeDrawer:
    
    @staticmethod
    def draw_square(surface, x, y, size, color):
        ctx = cairo.Context(surface)
        ctx.set_source_rgba(color[0]/255, color[1]/255, color[2]/255, 0.8)
        ctx.rectangle(x, y, size, size)
        ctx.fill()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(2)
        ctx.rectangle(x, y, size, size)
        ctx.stroke()
    
    @staticmethod
    def draw_triangle(surface, x, y, size, color):
        ctx = cairo.Context(surface)
        ctx.set_source_rgba(color[0]/255, color[1]/255, color[2]/255, 0.8)
        ctx.move_to(x + size/2, y)
        ctx.line_to(x, y + size)
        ctx.line_to(x + size, y + size)
        ctx.close_path()
        ctx.fill()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(2)
        ctx.move_to(x + size/2, y)
        ctx.line_to(x, y + size)
        ctx.line_to(x + size, y + size)
        ctx.close_path()
        ctx.stroke()
    
    @staticmethod
    def draw_circle(surface, x, y, radius, color):
        ctx = cairo.Context(surface)
        ctx.set_source_rgba(color[0]/255, color[1]/255, color[2]/255, 0.8)
        ctx.arc(x + radius, y + radius, radius, 0, 2 * math.pi)
        ctx.fill()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(2)
        ctx.arc(x + radius, y + radius, radius, 0, 2 * math.pi)
        ctx.stroke()
    
    @staticmethod
    def draw_trapezoid(surface, x, y, size, color):
        ctx = cairo.Context(surface)
        ctx.set_source_rgba(color[0]/255, color[1]/255, color[2]/255, 0.8)
        ctx.move_to(x + size * 0.2, y)
        ctx.line_to(x + size * 0.8, y)
        ctx.line_to(x + size, y + size)
        ctx.line_to(x, y + size)
        ctx.close_path()
        ctx.fill()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(2)
        ctx.move_to(x + size * 0.2, y)
        ctx.line_to(x + size * 0.8, y)
        ctx.line_to(x + size, y + size)
        ctx.line_to(x, y + size)
        ctx.close_path()
        ctx.stroke()
    
    @staticmethod
    def draw_rectangle(surface, x, y, width, height, color):
        ctx = cairo.Context(surface)
        ctx.set_source_rgba(color[0]/255, color[1]/255, color[2]/255, 0.8)
        ctx.rectangle(x, y, width, height)
        ctx.fill()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(2)
        ctx.rectangle(x, y, width, height)
        ctx.stroke()
    
    @staticmethod
    def draw_pentagon(surface, x, y, size, color):
        ctx = cairo.Context(surface)
        ctx.set_source_rgba(color[0]/255, color[1]/255, color[2]/255, 0.8)
        center_x = x + size/2
        center_y = y + size/2
        radius = size/2
        for i in range(5):
            angle = (i * 2 * math.pi / 5) - math.pi/2
            px = center_x + radius * math.cos(angle)
            py = center_y + radius * math.sin(angle)
            if i == 0:
                ctx.move_to(px, py)
            else:
                ctx.line_to(px, py)
        ctx.close_path()
        ctx.fill()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(2)
        for i in range(5):
            angle = (i * 2 * math.pi / 5) - math.pi/2
            px = center_x + radius * math.cos(angle)
            py = center_y + radius * math.sin(angle)
            if i == 0:
                ctx.move_to(px, py)
            else:
                ctx.line_to(px, py)
        ctx.close_path()
        ctx.stroke()

class Question:
    def __init__(self):
        self.all_shapes = ['square', 'triangle', 'circle', 'trapezoid', 'rectangle', 'pentagon']
        
        self.question_bank = [
            {
                'shape1': 'square',
                'shape2': 'triangle',
                'answer': 'pentagon',
                'explanation': 'Persegi (4 sisi) + Segitiga (3 sisi) = Segilima (7 sisi)'
            },
            {
                'shape1': 'triangle',
                'shape2': 'triangle',
                'answer': 'square',
                'explanation': 'Segitiga + Segitiga = Persegi (2 segitiga dapat membentuk persegi)'
            },
            {
                'shape1': 'square',
                'shape2': 'square',
                'answer': 'rectangle',
                'explanation': 'Persegi + Persegi = Persegi Panjang (2 persegi membentuk persegi panjang)'
            },
            {
                'shape1': 'triangle',
                'shape2': 'square',
                'answer': 'pentagon',
                'explanation': 'Segitiga (3 sisi) + Persegi (4 sisi) = Segilima (7 sisi)'
            },
            {
                'shape1': 'rectangle',
                'shape2': 'triangle',
                'answer': 'pentagon',
                'explanation': 'Persegi Panjang (4 sisi) + Segitiga (3 sisi) = Segilima (7 sisi)'
            },
            {
                'shape1': 'trapezoid',
                'shape2': 'triangle',
                'answer': 'pentagon',
                'explanation': 'Trapesium (4 sisi) + Segitiga (3 sisi) = Segilima (7 sisi)'
            },
            {
                'shape1': 'triangle',
                'shape2': 'trapezoid',
                'answer': 'pentagon',
                'explanation': 'Segitiga (3 sisi) + Trapesium (4 sisi) = Segilima (7 sisi)'
            },
            {
                'shape1': 'rectangle',
                'shape2': 'square',
                'answer': 'pentagon',
                'explanation': 'Persegi Panjang (4 sisi) + Persegi (4 sisi) = Gabungan bentuk segi empat'
            }
        ]
        
        self.current_question = None
        self.used_questions = []
        self.generate_new_question()
    
    def generate_new_question(self):
        # Reset Soal
        if len(self.used_questions) >= len(self.question_bank):
            self.used_questions = []
        
        available_questions = [q for q in self.question_bank if q not in self.used_questions]
        selected_question = random.choice(available_questions)
        self.used_questions.append(selected_question)
        
        answer = selected_question['answer']
        options = [answer]
        
        wrong_options = [s for s in self.all_shapes if s != answer]
        random.shuffle(wrong_options)
        options.extend(wrong_options[:3])
        
        random.shuffle(options)
        
        self.current_question = {
            'shape1': selected_question['shape1'],
            'shape2': selected_question['shape2'],
            'answer': answer,
            'options': options,
            'explanation': selected_question['explanation']
        }
    
    def check_answer(self, answer):
        return answer == self.current_question['answer']

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 30
        self.speed = 3
        self.color = BLUE
    
    def move(self, dx, dy, maze):
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed
        
        if not self.check_collision(new_x, new_y, maze):
            self.x = new_x
            self.y = new_y
    
    def check_collision(self, x, y, maze):
        corners = [
            (x, y),
            (x + self.size, y),
            (x, y + self.size),
            (x + self.size, y + self.size)
        ]
        
        for corner_x, corner_y in corners:
            maze_x = int(corner_x // TILE_SIZE)
            maze_y = int(corner_y // TILE_SIZE)
            
            if maze_y >= len(maze) or maze_x >= len(maze[0]):
                return True
            
            if maze[maze_y][maze_x] == 1:
                return True
        
        return False
    
    def draw(self, screen):
        data = bytearray(int(self.size * self.size * 4))
        surface = cairo.ImageSurface.create_for_data(
            data, cairo.FORMAT_ARGB32, int(self.size), int(self.size)
        )
        
        ctx = cairo.Context(surface)
        ctx.set_source_rgb(self.color[0]/255, self.color[1]/255, self.color[2]/255)
        ctx.arc(self.size/2, self.size/2, self.size/2 - 2, 0, 2 * math.pi)
        ctx.fill()
        
        ctx.set_source_rgb(1, 1, 1)
        ctx.arc(self.size/3, self.size/3, 4, 0, 2 * math.pi)
        ctx.fill()
        ctx.arc(2*self.size/3, self.size/3, 4, 0, 2 * math.pi)
        ctx.fill()
        
        ctx.set_source_rgb(0, 0, 0)
        ctx.arc(self.size/3, self.size/3, 2, 0, 2 * math.pi)
        ctx.fill()
        ctx.arc(2*self.size/3, self.size/3, 2, 0, 2 * math.pi)
        ctx.fill()
        
        img = pygame.image.frombuffer(bytes(data), (int(self.size), int(self.size)), 'ARGB')
        screen.blit(img, (self.x, self.y))

class Door:
    def __init__(self, x, y):
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.is_open = False
        self.color = RED
    
    def draw(self, screen):
        if not self.is_open:
            pygame.draw.rect(screen, self.color, 
                           (self.x, self.y, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, BLACK, 
                           (self.x, self.y, TILE_SIZE, TILE_SIZE), 2)
    
    def check_collision(self, player):
        return (self.x < player.x + player.size and
                self.x + TILE_SIZE > player.x and
                self.y < player.y + player.size and
                self.y + TILE_SIZE > player.y)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Game Edukasi Labirin Bangun Datar")
        self.clock = pygame.time.Clock()
        
        # Maze layout (0 = jalan, 1 = dinding, 2 = pintu, 3 = finish)
        self.maze = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,1,1,1,1,1,1,1,1,1,0,1],
            [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
            [1,0,1,1,1,1,1,1,1,1,1,0,1,0,1],
            [1,0,0,0,0,0,2,0,0,0,0,0,1,0,1],
            [1,1,1,1,1,0,1,1,1,1,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
            [1,0,0,0,2,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,2,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,3,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
        
        self.player = Player(TILE_SIZE + 5, TILE_SIZE + 5)
        self.doors = []
        self.question = Question()
        self.showing_question = False
        self.current_door = None
        self.showing_explanation = False
        self.selected_answer = None
        
        # Temukan semua pintu
        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                if self.maze[y][x] == 2:
                    self.doors.append(Door(x, y))
        
        self.font = pygame.font.Font(None, 32)
        self.small_font = pygame.font.Font(None, 24)
        self.running = True
        self.game_won = False
    
    def draw_maze(self):
        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                
                if self.maze[y][x] == 1:  
                    pygame.draw.rect(self.screen, BLACK, rect)
                elif self.maze[y][x] == 3:  
                    pygame.draw.rect(self.screen, GREEN, rect)
                    text = self.font.render("F", True, BLACK)
                    self.screen.blit(text, (rect.x + 5, rect.y + 10))
                else:  # Jalan
                    pygame.draw.rect(self.screen, WHITE, rect)
                
                pygame.draw.rect(self.screen, GRAY, rect, 1)
    
    def draw_shape(self, shape_type, x, y, size):
        data = bytearray(int(size * size * 4))
        surface = cairo.ImageSurface.create_for_data(
            data, cairo.FORMAT_ARGB32, int(size), int(size)
        )
        
        color = (100, 150, 255)
        
        if shape_type == 'square':
            ShapeDrawer.draw_square(surface, 10, 10, size-20, color)
        elif shape_type == 'triangle':
            ShapeDrawer.draw_triangle(surface, 10, 10, size-20, color)
        elif shape_type == 'circle':
            ShapeDrawer.draw_circle(surface, 10, 10, (size-20)/2, color)
        elif shape_type == 'trapezoid':
            ShapeDrawer.draw_trapezoid(surface, 10, 10, size-20, color)
        elif shape_type == 'rectangle':
            ShapeDrawer.draw_rectangle(surface, 10, 10, size-20, (size-20)*0.6, color)
        elif shape_type == 'pentagon':
            ShapeDrawer.draw_pentagon(surface, 10, 10, size-20, color)
        
        img = pygame.image.frombuffer(bytes(data), (int(size), int(size)), 'ARGB')
        self.screen.blit(img, (x, y))
    
    def draw_question_popup(self):
        popup_width = 700
        popup_height = 500
        popup_x = (SCREEN_WIDTH - popup_width) // 2
        popup_y = (SCREEN_HEIGHT - popup_height) // 2
        
        pygame.draw.rect(self.screen, WHITE, 
                        (popup_x, popup_y, popup_width, popup_height))
        pygame.draw.rect(self.screen, BLACK, 
                        (popup_x, popup_y, popup_width, popup_height), 3)
        
        if self.showing_explanation:
            text = self.font.render("Jawaban Salah!", True, RED)
            self.screen.blit(text, (popup_x + 50, popup_y + 30))
            
            exp_lines = self.question.current_question['explanation'].split('\n')
            y_offset = 100
            for line in exp_lines:
                text = self.small_font.render(line, True, BLACK)
                self.screen.blit(text, (popup_x + 50, popup_y + y_offset))
                y_offset += 30
            
            text = self.small_font.render("Jawaban yang benar:", True, BLACK)
            self.screen.blit(text, (popup_x + 50, popup_y + 200))
            
            correct_answer = self.question.current_question['answer']
            self.draw_shape(correct_answer, popup_x + 280, popup_y + 180, 80)
            
            button_rect = pygame.Rect(popup_x + 250, popup_y + 400, 200, 50)
            pygame.draw.rect(self.screen, BLUE, button_rect)
            text = self.font.render("Coba Lagi", True, WHITE)
            text_rect = text.get_rect(center=button_rect.center)
            self.screen.blit(text, text_rect)
            
            return button_rect
        else:
            text = self.font.render("Jawab Soal untuk Membuka Pintu!", True, BLACK)
            self.screen.blit(text, (popup_x + 120, popup_y + 20))
            
            q = self.question.current_question
            self.draw_shape(q['shape1'], popup_x + 150, popup_y + 80, 80)
            
            plus_text = self.font.render("+", True, BLACK)
            self.screen.blit(plus_text, (popup_x + 250, popup_y + 100))
            
            self.draw_shape(q['shape2'], popup_x + 300, popup_y + 80, 80)
            
            equals_text = self.font.render("=", True, BLACK)
            self.screen.blit(equals_text, (popup_x + 400, popup_y + 100))
            
            question_mark = self.font.render("?", True, BLACK)
            self.screen.blit(question_mark, (popup_x + 470, popup_y + 100))
            
            option_rects = []
            options = q['options']
            for i, option in enumerate(options):
                row = i // 2
                col = i % 2
                x = popup_x + 100 + col * 300
                y = popup_y + 220 + row * 120
                
                rect = pygame.Rect(x, y, 120, 120)
                color = YELLOW if self.selected_answer == option else WHITE
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 2)
                
                self.draw_shape(option, x + 20, y + 20, 80)
                
                option_rects.append((rect, option))
            
            return option_rects
    
    def check_door_collision(self):
        for door in self.doors:
            if not door.is_open and door.check_collision(self.player):
                return door
        return None
    
    def check_finish(self):
        player_tile_x = int((self.player.x + self.player.size/2) // TILE_SIZE)
        player_tile_y = int((self.player.y + self.player.size/2) // TILE_SIZE)
        
        if (player_tile_y < len(self.maze) and 
            player_tile_x < len(self.maze[0]) and
            self.maze[player_tile_y][player_tile_x] == 3):
            return True
        return False
    
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                
                if event.type == MOUSEBUTTONDOWN and self.showing_question:
                    mouse_pos = pygame.mouse.get_pos()
                    
                    if self.showing_explanation:
                        if hasattr(self, 'back_button') and self.back_button.collidepoint(mouse_pos):
                            self.showing_explanation = False
                            self.selected_answer = None
                    else:
                        for rect, option in self.option_rects:
                            if rect.collidepoint(mouse_pos):
                                self.selected_answer = option
                                if self.question.check_answer(option):
                                    self.current_door.is_open = True
                                    self.showing_question = False
                                    self.question.generate_new_question()
                                    self.selected_answer = None
                                else:
                                    self.showing_explanation = True
            
            if not self.showing_question and not self.game_won:
                keys = pygame.key.get_pressed()
                dx = dy = 0
                if keys[K_LEFT] or keys[K_a]:
                    dx = -1
                if keys[K_RIGHT] or keys[K_d]:
                    dx = 1
                if keys[K_UP] or keys[K_w]:
                    dy = -1
                if keys[K_DOWN] or keys[K_s]:
                    dy = 1
                
                self.player.move(dx, dy, self.maze)
                
                door = self.check_door_collision()
                if door:
                    self.showing_question = True
                    self.current_door = door
                
                if self.check_finish():
                    self.game_won = True
            
            self.screen.fill(WHITE)
            self.draw_maze()
            
            for door in self.doors:
                door.draw(self.screen)
            
            self.player.draw(self.screen)
            
            if self.showing_question:
                result = self.draw_question_popup()
                if self.showing_explanation:
                    self.back_button = result
                else:
                    self.option_rects = result
            
            if self.game_won:
                win_text = self.font.render("Anjay Done", True, GREEN)
                text_rect = win_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
                pygame.draw.rect(self.screen, WHITE, 
                               (text_rect.x - 20, text_rect.y - 20, 
                                text_rect.width + 40, text_rect.height + 40))
                pygame.draw.rect(self.screen, BLACK, 
                               (text_rect.x - 20, text_rect.y - 20, 
                                text_rect.width + 40, text_rect.height + 40), 3)
                self.screen.blit(win_text, text_rect)
            
            pygame.display.flip()
        
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()