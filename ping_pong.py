from pygame import * 

init()
win_width,win_height = 800,500
window = display.set_mode((win_width,win_height))
display.set_caption("Ping pong")
clock = time.Clock()

FPS = 60

#colours
BLUE = (200,255,255)
GREEN = (16,120,16) #court
GREY1 = (240,240,240) #lines + UI
GREY2 = (240,240,240) #paddle
GREY3 = (240,240,240) #ball

# Geometry
PAD_W, PAD_H = 14, 120   # thinner paddles
BALL_R = 10              # round ball radius
PAD_GAP = 30             # gap from side wall
BASE_SPEED_PADDLE = 6
BALL_SPEED_X = 4
BALL_SPEED_Y = 3

WIN_SCORE = 6
winner = None
paused = False
score1,score2 = 0, 0
racket1 = None
racket2 = None
ball = None

#UI
font.init()
score_font = font.Font(None, 56)
hint_font  = font.Font(None, 28)

#court

def draw_court():
    window.fill(GREEN)
    draw.rect(window,GREY1,Rect(8,8,win_width - 16,win_height - 16,),width=4)

    dash_h = 18
    gap_h = 14
    x = win_width // 2
    y = 8
    
    while y < win_width - 8:
        draw.line(window,GREY1,(x,y),(x, min(y + dash_h,win_height - 8)),width=4)
        y += dash_h + gap_h
        
def UI():
    score_text = score_font.render(f"{score1}   :   {score2}",True,GREY2)
    window.blit(score_text,(win_width//2 -score_text.get_width()//2,16))
    
    if winner is not None:
        win_text = hint_font.render(f"Player {winner} has won,press 'R' to reset.",True,GREY2)
        window.blit(win_text,(win_width//2 -score_text.get_width()//2,60))

#game loop

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False
                
            if e.key == K_p:
                paused = not paused
        
            if e.key == K_r:
                score1 = score2 = 0
                winner = None
                racket1.rect.centery = win_height // 2
                racket2.rect.centery = win_height // 2
                ball.center_serve(direction=1)
                
                
       
        draw_court()
        UI()
        display.update()
        clock.tick(FPS)
      
    

                
    
                
                
    