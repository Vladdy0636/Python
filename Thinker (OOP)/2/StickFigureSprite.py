import time
from tkinter import PhotoImage

from CollisionCheck import CollisionCheck


from Coords import Coords
from Sprite import Sprite


class StickFigureSprite(Sprite):
    def __init__(self, game, door):
        self.canvas = game.canvas
        self.door = door
        super().__init__(game)

        self.images_left = [PhotoImage(file="C:\\games\\game_tkinter\\img\\figure-L1.png"),
                            PhotoImage(file="C:\\games\\game_tkinter\\img\\figure-L2.png"),
                            PhotoImage(file="C:\\games\\game_tkinter\\img\\figure-L3.png")]

        self.images_right = [PhotoImage(file="C:\\games\\game_tkinter\\img\\figure-R1.png"),
                             PhotoImage(file="C:\\games\\game_tkinter\\img\\figure-R2.png"),
                             PhotoImage(file="C:\\games\\game_tkinter\\img\\figure-R3.png")]



        self.image = game.canvas.create_image(200, 370, image=self.images_left[0], anchor='nw')
        self.x = -2
        self.y = 2
        self.current_image = 0
        self.current_image_add = 1
        self.jump_count = 0
        self.last_time = time.time()
        self.coordinates = Coords()

        self.setup_key_bindings()

    def setup_key_bindings(self):
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyRelease-Right>', self.stop)
        self.canvas.bind_all('<KeyRelease-Left>', self.stop)
        self.canvas.bind_all('<KeyPress-space>', self.jump)
        self.canvas.bind_all('<Escape>', self.on_escape)

    def on_escape(self, event=None):
        self.canvas.destroy()
        self.game.game_over = True
        self.game.stop()
        print("Гра завершена!")

    def turn_left(self, event):
        self.x = -2

    def turn_right(self, event):
        self.x = 2

    def jump(self, event):
        if self.y == 0:
            self.y = -4
            self.jump_count = 0

    def animate(self):
        if self.x != 0 and self.y == 0:
            if time.time() - self.last_time > 0.1:
                self.last_time = time.time()
                self.current_image += self.current_image_add
                if self.current_image >= 2:
                    self.current_image_add = -1
                if self.current_image <= 0:
                    self.current_image_add = 1

        if self.x < 0:
            self.update_image(self.images_left)
        elif self.x > 0:
            self.update_image(self.images_right)
       
    def update_image(self, image_list):
        if self.y != 0:
            self.canvas.itemconfig(self.image, image=image_list[2])
        else:
            self.canvas.itemconfig(self.image, image=image_list[self.current_image])

    def stop(self, event):
        self.x = 0

    def coords(self):
        xy = self.canvas.coords(self.image)

        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30

        return self.coordinates

    def move(self):
        self.animate()

        if self.y < 0:
            self.jump_count += 1
            if self.jump_count > 20:
                self.y = 4

        if self.y > 0:
            self.jump_count -= 1

        co = self.coords()

        left = True
        right = True
        top = True
        bottom = True
        falling = True

        if self.y > 0 and co.y2 >= self.game.canvas_height:
            self.y = 0
            bottom = False

        elif self.y < 0 and co.y1 <= 0:
            self.y = 0
            top = False

        if self.x > 0 and co.x2 >= self.game.canvas_width:
            self.x = 0
            right = False

        elif self.x < 0 and co.x1 < 0:
            self.x = 0
            left = False

        for sp in self.game.sprites:
            platform_co = sp.coords()

            if top and self.y == 0 and CollisionCheck.collided_top(co, platform_co):
                self.y = -self.y
                top = False

            if bottom and self.y > 0 and CollisionCheck.collided_bottom(self.y, co, platform_co):
                print("on a platform")
                self.y = 0
                bottom = False
                top = True
                falling = False

            if bottom and falling and self.y == 0 and co.y2 < self.game.canvas_height and CollisionCheck.collided_bottom(
                    1, co,
                    platform_co):
                falling = False

            if left and self.x < 0 and CollisionCheck.collided_left(co, platform_co):
                self.x = 0
                left = False

                if sp.endgame:
                    self.setEndGame()

            if right and self.x > 0 and CollisionCheck.collided_right(co, platform_co):
                self.x = 0
                right = False

                if sp.endgame:
                    self.setEndGame()

        if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
            self.y = -1

        self.game.canvas.move(self.image, self.x, self.y)

    def setEndGame(self):
        self.door.set_photo(photo_image="C:\\games\\game_tkinter\\img\\door2.png")
        time.sleep(1)
        self.door.set_photo(photo_image="C:\\games\\game_tkinter\\img\\door1.png")
        self.game.canvas.delete("timer")
        self.game.canvas.create_text(250, 250, text=f"Ви виграли, відчинив двері! \nЦе зайняло: {self.game.seconds} секунд.", font=('Arial', 25), fill='black')
        self.game.tk.update()
        self.game.game_over = True
