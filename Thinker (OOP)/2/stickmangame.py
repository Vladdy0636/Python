from tkinter import PhotoImage



from DoorSprite import DoorSprite
from Game import Game
from PlatformSprite import PlatformSprite
from StickFigureSprite import StickFigureSprite

g = Game()
canvas = g.canvas
platforms = []
platform_positions = [
    (0, 460), (250, 400), (100, 340), (0, 280), (250, 220),
    (100, 160), (0, 100), (250, 40), (200, 280), (230, 100),
    (200, 460)
]

for index, position in enumerate(platform_positions, start=1):
    platform = PlatformSprite(g, PhotoImage(file=f"C:\\games\\game_tkinter\\img\\platform1.png"),
                          position[0], position[1], 100, 10)
    platforms.append(platform)
    g.sprites.append(platform)
    
print(platform)

door = DoorSprite(g, PhotoImage(file="C:\\games\\game_tkinter\\img\\door1.png"),
                  350, 95, 40, 35)

g.sprites.append(door)

sf = StickFigureSprite(g, door)
g.sprites.append(sf)

g.setPlatforms(platforms)

g.mainloop()
