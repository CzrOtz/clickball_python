import pygame
from pygame.locals import *
from game2 import play_clickball


#How does data flow though this 



pygame.init()

# set up the display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('ClickBall')

# define colors
WHITE = (255, 255, 255)
BUTTON_COLOR = (34, 128, 34)  # use a variable for button color

# set up fonts
font = pygame.font.SysFont(None, 40)

# this is the text inside the play button
play_text = font.render('Play', True, WHITE)

#this is the rectangle that holds the play button 
play_rect = play_text.get_rect(center=(WINDOW_WIDTH//2-125, WINDOW_HEIGHT//2))

#this is the text for the stats 
stats_text = font.render('Stats', True, WHITE)

#this is the rectangle that 
stats_rect = stats_text.get_rect(center=(WINDOW_WIDTH//2+125, WINDOW_HEIGHT//2))

main_background = pygame.image.load('pictures/welcomebackground.jpg').convert_alpha()
main_background_true = pygame.transform.scale(main_background, (800,600))





banner_width = 800
banner_height = 100
banner_surface = pygame.Surface((banner_width, banner_height))
banner_surface.fill((5, 2, 23, 50))
banner_text = font.render('ClickBall', True, (255, 255, 255))
text_rect = banner_text.get_rect(center=(banner_width//2, banner_height//2))
banner_surface.blit(banner_text, text_rect)

# set up buttons
button_width = 100
button_height = 50
button_margin = 200  # increase the button margin
play_button = pygame.Rect((WINDOW_WIDTH-button_width-button_margin)//2, WINDOW_HEIGHT//2, button_width, button_height)
stats_button = pygame.Rect((WINDOW_WIDTH+button_margin)//2, WINDOW_HEIGHT//2, button_width, button_height)

# draw the screen
# screen.fill(BLACK)
screen.blit(banner_surface, (0, 0))
pygame.draw.rect(screen, BUTTON_COLOR, play_button)
pygame.draw.rect(screen, BUTTON_COLOR, stats_button)
# set the center of the text rect to match the center of the button rect
play_text_rect = play_text.get_rect(center=play_button.center)
stats_text_rect = stats_text.get_rect(center=stats_button.center)
screen.blit(play_text, play_text_rect)
screen.blit(stats_text, stats_text_rect)
pygame.display.flip()

# main loop
while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            import sys
            sys.exit()
            
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_pos):
                play_clickball()
                
            elif stats_button.collidepoint(mouse_pos):
                print('Stats button clicked')
                
    
    # Draw the banner and buttons
    screen.blit(main_background_true, (0,0))
    screen.blit(banner_surface, (0, 0))
    pygame.draw.rect(screen, BUTTON_COLOR, play_button)
    pygame.draw.rect(screen, BUTTON_COLOR, stats_button)
    play_text_rect = play_text.get_rect(center=play_button.center)
    stats_text_rect = stats_text.get_rect(center=stats_button.center)
    screen.blit(play_text, play_text_rect)
    screen.blit(stats_text, stats_text_rect)
    pygame.display.update()