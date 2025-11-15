import cairo
import math

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