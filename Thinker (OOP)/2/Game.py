from tkinter import Tk, Canvas, PhotoImage
import time

class Game:
    def __init__(self):
        self.initialize_window()
        self.initialize_game_variables()
        self.start_time = time.time()
        self.timer_id = None

    def initialize_window(self):
        self.tk = Tk()
        self.tk.title("The man run to the exit")
        self.tk.resizable(False, False)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
        self.canvas.pack()
        self.canvas_height = 500
        self.canvas_width = 500

        self.bg = PhotoImage(file=f"C:\\games\\game_tkinter\\img\\background.png")
        self.canvas.create_image(0, 0, image=self.bg, anchor='nw')

    def initialize_game_variables(self):
        self.platforms = None
        self.sprites = []
        self.running = True
        self.game_over = False
        self.seconds = 0
        self.timer_text = self.canvas.create_text(450, 30, text="0", font=('Arial', 30), fill='black', tags="timer")

    def set_platforms(self, platforms):
        self.platforms = platforms

    def stop(self):
        self.running = False

    #def move_platforms(self):
        #for platform in self.platforms:
            #if platform.isAsWidth:
                #platform.moveRight(2)
            #else:
                #platform.moveLeft(2)

            #if platform.x <= 0:
                #platform.isAsWidth = True
            #elif platform.x >= 400:
                #platform.isAsWidth = False

            #newX = platform.x
            #newY = platform.y
            #platform.setPosition(newX, newY)

    def run_sprites(self):
        if not self.game_over:
            for sprite in self.sprites:
                sprite.move()

    def update_canvas(self):
        if self.game_over:
            return
        self.tk.update_idletasks()
        self.tk.update()

    def update_timer(self):
        current_time = time.time()
        elapsed_time = int(current_time - self.start_time)
        self.canvas.itemconfig(self.timer_text, text=str(elapsed_time))

    def update_timer_continuously(self):
        self.update_timer()
        if not self.game_over:
            self.timer_id = self.tk.after(1000, self.update_timer_continuously)

    def mainloop(self):
        self.update_timer_continuously()
        while self.running:
            #for platform in self.platforms:
                #platform.move()
            self.run_sprites()
            self.update_canvas()
            time.sleep(0.01)
        

    def setPlatforms(self, platforms):
        pass
    
    