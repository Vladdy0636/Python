import random

class Ball:
    def __init__(self, canvas, board, score, color):
        self.canvas = canvas
        self.board = board
        self.score_instance = score

        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)

        self.x = starts[0]
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False


    def hit_paddle(self, pos):
        board_position = self.canvas.coords(self.board.id)

        if pos[2] >= board_position[0] and pos[0] <= board_position[2]:
            if board_position[1] <= pos[3] <= board_position[3]:
                self.y = -2
                self.score_instance.ball_jump()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 1

        if pos[3] >= self.canvas_height:
            self.text = self.canvas.create_text(250, 100, text="ВИ ПРОГРАЛИ", font=("Helvetica", 30), state='normal', fill='red')
            self.hit_bottom = True

        if self.hit_paddle(pos):
            if self.board.get_board_speed() > 0:
                self.y = -1 - self.board.get_board_speed()
            else:
                self.y = -1 + self.board.get_board_speed()
            #self.y = -1

        if pos[0] <= 0:
            self.x = 3

        if pos[2] >= self.canvas_width:
            self.x = -3