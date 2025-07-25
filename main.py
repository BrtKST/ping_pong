import pygame
import random
import settings as st

pygame.init()

#window settings
WIDTH = st.WIDTH
HEIGHT = st.HEIGHT
font = pygame.font.SysFont('arial', 50)

#import settings test
print(WIDTH, HEIGHT)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#speed variables
VEL = st.VEL
BALL_VEL = st.BALL_VEL


def draw(player_1,player_2,score_1,score_2,ball):
    WIN.fill(st.GREEN)
    pygame.draw.rect(WIN,st.BLUE,player_1)
    pygame.draw.rect(WIN,st.RED,player_2)

    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    run_game = True

    #creating, resp sprites
    player_1 = pygame.Rect(45, HEIGHT/2 - st.player_height/2, st.player_width, st.player_height)
    player_2 = pygame.Rect(WIDTH-45, HEIGHT/2 - st.player_height/2, st.player_width, st.player_height)
    ball = pygame.Rect(WIDTH//2, HEIGHT//2, st.BALL_RADIUS, st.BALL_RADIUS)
    ball_dx, ball_dy = random.choice([-1, 1]) * BALL_VEL, random.choice([-1, 1]) * BALL_VEL

    score_1 = 0
    score_2 = 0

    while run_game:
        clock.tick(st.FPS)
        keys = pygame.key.get_pressed()

        draw(player_1, player_2, score_1, score_2, ball)
        #print('test')
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run_game = False
            if event.type == pygame.QUIT:
                run_game = False

        ball.x += ball_dx
        ball.y += ball_dy
        
        #Players movement
        if keys[pygame.K_w] and player_1.top > 0:
            player_1.y -= VEL
        if keys[pygame.K_s] and player_1.bottom < HEIGHT:
            player_1.y += VEL 

        if keys[pygame.K_UP] and player_2.top > 0:
            player_2.y -= VEL
        if keys[pygame.K_DOWN] and player_2.bottom < HEIGHT:
            player_2.y += VEL 

    pygame.quit()
            

if __name__ == "__main__":
    main()