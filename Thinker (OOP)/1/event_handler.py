class event_handler:
    def __init__(self, tk_instance):
        self.tk = tk_instance
        self.is_active = True
        self.tk.bind_all('<Escape>', self.on_escape)

    def on_escape(self, event=None):
        self.is_active = False
        self.canvas.itemconfig(self.text, text=f"М'ячів відбито: {self.score}", font=("Helvetica", 16))
        self.tk.destroy()
        print("Гра завершена!")

