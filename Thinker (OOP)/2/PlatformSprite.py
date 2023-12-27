from Coords import Coords
from Sprite import Sprite
import random


class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        super().__init__(game)
        self.height = height
        self.game = game
        self.width = width
        self.x = x
        self.x2 = self.x + height
        self.y = y
        self.direction = 1
        self.photo_image = photo_image
        self.image = self.game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.coordinates = Coords(self.x, self.y, self.x + width, self.y + height)
        self.speed = 3
        
    def move(self):
        self.game.canvas.move(self.image, self.speed, 0)
        x, y = self.game.canvas.coords(self.image)
        x2 = x + self.width
        print("x1: ", x, "x2: ", x2)
        
        if x + self.speed<= 0 or x2 + self.speed >= self.game.canvas_width:
            self.speed = -self.speed

            
        self.coordinates = Coords(x, y, x2, y)
    
