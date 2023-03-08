import pygame
from pygame.locals import *

def game_over_func(screen, score, width, height):
    game_over_screen = True
    pygame.init()

    pygame.font.init()

    # set up fonts
    font = pygame.font.SysFont(None, 40)
    main_menu_text = font.render('Main Menu', True, (255, 255, 255))
    main_menu_rect = main_menu_text.get_rect(center=(width/2, height/2 + 100))

    while game_over_screen:

        game_over_text = "Game Over! Your Score: {}".format(score)
        game_over_font = pygame.font.Font(None, 80)
        game_over_text_surface = game_over_font.render(game_over_text, True, (255, 0, 0))
        game_over_rect = game_over_text_surface.get_rect(center=(width/2, height/2))

        screen.fill((0, 0, 0))
        screen.blit(game_over_text_surface, game_over_rect)
        screen.blit(main_menu_text, main_menu_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if main_menu_rect.collidepoint(mouse_pos):
                    game_over_screen = False
                    break

    return True