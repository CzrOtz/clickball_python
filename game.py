import pygame
import random
from sys import exit
pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('ClickBall')
clock = pygame.time.Clock()

BALL_RADIUS = 50
BALL_COLOR = (223, 8, 8)
ball_x = 500
ball_y = 500
ball_surface = pygame.Surface((BALL_RADIUS*2, BALL_RADIUS*2), pygame.SRCALPHA)
pygame.draw.circle(ball_surface, BALL_COLOR, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)

SCOREBOARD_WIDTH = 1000
SCOREBOARD_HEIGHT = 200
SCOREBOARD_COLOR = (0, 0, 255)
scoreboard_surface = pygame.Surface((SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT), pygame.SRCALPHA)
pygame.draw.rect(scoreboard_surface, SCOREBOARD_COLOR, (0, 0, SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT))


font = pygame.font.Font(None, 50)
score_text = "Score: {} Time: {}".format(0, 20)
text = font.render(score_text, True, (255, 255, 255))
text_rect = text.get_rect(center=(SCOREBOARD_WIDTH/2, SCOREBOARD_HEIGHT/2))

score = 0
start_ticks = 0
countdown = 20
time_remaining = countdown

ball_clicked = False

game_over_surface = pygame.Surface((1000,1000), pygame.SRCALPHA)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball_rect = ball_surface.get_rect(center=(ball_x, ball_y))
            if ball_rect.collidepoint(event.pos): 
                ball_x = random.randint(BALL_RADIUS, WINDOW_WIDTH - BALL_RADIUS)
                ball_y = random.randint(BALL_RADIUS, WINDOW_HEIGHT - BALL_RADIUS)
                score += 1
                if score <= 1:
                    ball_clicked = True
                    start_ticks = pygame.time.get_ticks() 
                score_text = "Score: {} Time: {}".format(score, time_remaining)
                text = font.render(score_text, True, (255,255,255))
                text_rect = text.get_rect(center=(SCOREBOARD_WIDTH/2, SCOREBOARD_HEIGHT/2))
            else:
                ball_clicked = False #stop countdown out of bounds click
                game_over_text = "Game Over! Your Score: {}".format(score)
                game_over_font = pygame.font.Font(None, 80)
                game_over_text_surface = game_over_font.render(game_over_text, True, (255, 0, 0))
                game_over_rect = game_over_text_surface.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
                screen.fill((0, 0, 0))
                screen.blit(game_over_text_surface, game_over_rect)
                pygame.display.flip()
                pygame.time.delay(5000)
                pygame.quit()


            
    if time_remaining == 0:
            game_over_text = "Game Over! Your Score: {}".format(score)
            game_over_font = pygame.font.Font(None, 80)
            game_over_text_surface = game_over_font.render(game_over_text, True, (255, 0, 0))
            game_over_rect = game_over_text_surface.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
            screen.fill((0, 0, 0))
            screen.blit(game_over_text_surface, game_over_rect)
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.quit()
                

    if ball_clicked:
        time_remaining = max(0, countdown - int((pygame.time.get_ticks() - start_ticks) / 1000))
        score_text = "Score: {} Time: {}".format(score, time_remaining)
        text = font.render(score_text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCOREBOARD_WIDTH/2, SCOREBOARD_HEIGHT/2))

    
    screen.fill((255, 255, 255))
    screen.blit(scoreboard_surface, (0, 0))
    screen.blit(ball_surface, (ball_x - BALL_RADIUS, ball_y - BALL_RADIUS))
    
    
    scoreboard_surface.fill((0,0,255))
    scoreboard_surface.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

