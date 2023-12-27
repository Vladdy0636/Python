class Score:
    def __init__(self, canvas):
        self.canvas = canvas
        self.score = 0
        self.lost = 0
        self.text = ""
        self.show_text()

    def show_text(self):
        if self.text == "":
            self.text = self.canvas.create_text(350, 10, text=f"М'ячів відбито: 0", font=("Helvetica", 16))
        else:
            self.canvas.itemconfig(self.text, text=f"М'ячів відбито: {self.score}", font=("Helvetica", 16))

    def ball_jump(self):
        self.score += 1
        self.show_text()
        