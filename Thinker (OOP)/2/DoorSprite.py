from tkinter import PhotoImage
from Sprite import Sprite
from Coords import Coords



class DoorSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        super().__init__(game)
        self.x = x
        self.y = y
        self.photo_image = photo_image

        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')

        self.coordinates = Coords(x, y, x + (width / 2), y + height)
        self.endgame = True

    def set_photo(self, photo_image):
        self.photo_image = PhotoImage(file=photo_image)
        self.image = self.game.canvas.create_image(self.x, self.y, image=self.photo_image, anchor='nw')
        self.game.tk.update()
