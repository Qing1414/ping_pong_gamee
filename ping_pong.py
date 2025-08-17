from pygame import * 

init()
win_width,win_height = 800,500
window.display.set_mode((win_width,win_height))
display.set_caption("Ping pong")
clock = time.Clock()

FPS = 60

#colours
BLUE = (200,255,255)
GREEN = (16,120,16) #court
GREY1 = (240,240,240) #lines + UI
GREY2 = (240,240,240) #paddle
GREY3 = (240,240,240) #ball