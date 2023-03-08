import pygame
import random
from sys import exit
from game_over import game_over_func


def play_clickball():
    
    #this is the window
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('ClickBall')
    
    #fps of the game
    clock = pygame.time.Clock()

    #the background image
    background = pygame.image.load('pictures/background.jpg').convert_alpha()
    background_true = pygame.transform.scale(background, (800,600))

    #the position of the ball at starting
    ball_x = 400
    ball_y = 300

    

    #load image 
    ball_image = pygame.image.load('pictures/ball_new.png').convert_alpha()

    #ball radius
    ball_radius = min(ball_image.get_width(), ball_image.get_height()) // 2

    #makes a recangle
    ball_rect = ball_image.get_rect(center=(ball_x, ball_y))
    
    #the surface the ball image will be placed on
    ball_surface = pygame.Surface((200, 200), pygame.SRCALPHA)

    
    #score board is its own surface 
    SCOREBOARD_WIDTH = 800
    SCOREBOARD_HEIGHT = 200
    SCOREBOARD_COLOR = (0, 0, 25, 128)
    scoreboard_surface = pygame.Surface((SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT), pygame.SRCALPHA)
    #this draws the scoreboard since its not an image
    pygame.draw.rect(scoreboard_surface, SCOREBOARD_COLOR, (0, 0, SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT))


    font = pygame.font.Font(None, 50)

    #this takes positional arguments in the {} relative to the order of the arguments provided in format()
    score_text = "Score: {} Time: {}".format(0, 10)
    text = font.render(score_text, True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCOREBOARD_WIDTH/2, SCOREBOARD_HEIGHT/2))

    score = 0
    start_ticks = 0
    countdown = 10
    time_remaining = countdown

    ball_clicked = False

    

    while True:

        #events are in an array and you need to itterate through them to access them
        for event in pygame.event.get():

            #exits the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #if the event is a mouse button down 
            if event.type == pygame.MOUSEBUTTONDOWN:

                #makes a rect for the ball, hit detection
                ball_rect = ball_surface.get_rect(center=(ball_x, ball_y))

                 #checks to see if the distance between the center of the ball and the click is less than
                 #the radius of the ball ^2
                 #if it is, then a click has been detected
                if ((event.pos[0] - ball_x) ** 2 + (event.pos[1] - ball_y) ** 2) < ball_radius ** 2:

                    ball_x = random.randint(15, 785)
                    ball_y = random.randint(75, 550)

                    score += 1

                    # ball_surface.fill((0, 255, 0))
                    ball_rect = ball_image.get_rect(center=(ball_x, ball_y))

                    #places ball image on the ball rect
                    ball_surface.blit(ball_image, ball_rect) #

                    #countdown logic
                    if score <= 1:
                        ball_clicked = True
                        start_ticks = pygame.time.get_ticks() 

                    score_text = "Score: {} Time: {}".format(score, time_remaining)
                    text = font.render(score_text, True, (255,255,255))
                    text_rect = text.get_rect(center=(SCOREBOARD_WIDTH/2, SCOREBOARD_HEIGHT/2))
                else:
                    if game_over_func(screen, score, WINDOW_WIDTH , WINDOW_HEIGHT):
                        return


                
        if time_remaining == 0:
              if game_over_func(screen, score, WINDOW_WIDTH , WINDOW_HEIGHT):
                  return
               
              
                    

        if ball_clicked:
            time_remaining = max(0, countdown - int((pygame.time.get_ticks() - start_ticks) / 1000))
            score_text = "Score: {} Time: {}".format(score, time_remaining)
            text = font.render(score_text, True, (255, 255, 255))
            text_rect = text.get_rect(center=(SCOREBOARD_WIDTH/2, SCOREBOARD_HEIGHT/2))

        
        screen.blit(background_true, (0,0))
        screen.blit(scoreboard_surface, (0, 0))
        screen.blit(ball_image, ball_rect) #places the image of the ball on the rect
        
        
        
        
        scoreboard_surface.fill((0,0,25, 128))
        scoreboard_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)

    

