class Camera:
    def __init__(self, sw, sh, maze_width_tiles, maze_height_tiles, tile_size):
        self.sw = sw
        self.sh = sh
        self.tile_size = tile_size
        
        self.maze_width = maze_width_tiles * tile_size
        self.maze_height = maze_height_tiles * tile_size
        
        self.x = 0
        self.y = 0

    def update(self, player):
        target_x = player.x + player.target_width // 2 - self.sw // 2
        target_y = player.y + player.target_height // 2 - self.sh // 2

        self.x = max(0, min(target_x, self.maze_width - self.sw))
        self.y = max(0, min(target_y, self.maze_height - self.sh))