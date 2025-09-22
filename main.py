import pygame
from color_palette import LIGHT_PALETTE
from game_layout import Game

def main():

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    FPS = 60
        
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Quiz Game")
    clock = pygame.time.Clock()

    game = Game(LIGHT_PALETTE)

    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
        
        game.draw(screen)
        clock.tick(FPS)

    pygame.quit()


def end_game():
    pass

def correct_answer():
    pass

def on_mouse_down(pos):
    pass

def update_time_left():
    pass

if __name__ == "__main__":
    main()
