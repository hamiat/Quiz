import pygame
from pygame import Rect

WIDTH = 1280
HEIGHT = 720
    
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz Game")
clock = pygame.time.Clock()

def layout():
    main_container = Rect(50, 40, 820, 240)
    timer_container = Rect(990, 40, 240, 240)
    answer1_container = Rect(50, 358, 495, 165)
    answer2_container = Rect(735, 358, 495, 165)
    answer3_container = Rect(50, 538, 495, 165)
    answer4_container = Rect(735, 538, 495, 165)

    return {
        'main': main_container,
        'timer': timer_container,
        'answers': [answer1_container, answer2_container, answer3_container, answer4_container]
    }

def draw():
    containers = layout()
    
    screen.fill("#8fD9FB")
    pygame.draw.rect(screen, "#F1ECE6", containers['main'])
    pygame.draw.rect(screen, "#E8B600", containers['timer'])

    for answer in containers['answers']:
        pygame.draw.rect(screen,  "#D98326", answer)

    pygame.display.flip()
    

def end_game():
    pass

def correct_answer():
    pass

def on_mouse_down(pos):
    pass

def update_time_left():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
