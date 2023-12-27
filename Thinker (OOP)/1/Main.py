from board import Board
from ball import Ball
from event_handler import event_handler
from Score import Score

from tkinter import *
import time
import random


tk = Tk()
tk.title("Гра Ball Jump")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0, background='blue')
canvas.pack()
tk.update()

score = Score(canvas)
board = Board(canvas, color='pink')
ball = Ball(canvas, board, score, color='green')




def on_escape(event=None):
    tk.destroy()
    print("Гра завершена!")

tk.bind_all('<Escape>', on_escape)
event_handler = event_handler(tk)

while True:
    if board.Start == True:
        if not event_handler.is_active:
            break
        if not ball.hit_bottom:
            ball.draw()
            board.draw() 
        else:
            tk.mainloop()
            
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


