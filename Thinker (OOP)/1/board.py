class Board:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 350)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.Start = False
        self.left_pressed = False
        self.right_pressed = False

        canvas.bind('<Button-1>', self.game_start)
        canvas.bind_all('<KeyPress-a>', self.press_left)
        canvas.bind_all('<KeyRelease-a>', self.release_left)
        canvas.bind_all('<KeyPress-d>', self.press_right)
        canvas.bind_all('<KeyRelease-d>', self.release_right)

    def game_start(self, event):
        self.Start = True

    def press_left(self, event):
        self.left_pressed = True

    def release_left(self, event):
        self.left_pressed = False

    def press_right(self, event):
        self.right_pressed = True

    def release_right(self, event):
        self.right_pressed = False

    def turn_left(self):
        if self.left_pressed and self.canvas.coords(self.id)[0] > 0:
            self.x = -5
            self.board_speed = -5

    def turn_right(self):
        if self.right_pressed and self.canvas.coords(self.id)[2] < self.canvas_width:
            self.x = 5
            self.board_speed = 5

    def draw(self):
        self.turn_left()
        self.turn_right()

        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
            
    def get_board_speed(self):
        return self.x
