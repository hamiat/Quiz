from pygame import Rect
import pygame
from color_palette import Palette
      
class Game:
    def __init__(self, palette: Palette):
        self.running = True
        self.palette = palette
        self.containers = self.create_layout()

    def create_layout(self):
        main_container = Rect(50, 40, 820, 240)
        timer_container = Rect(900, 40, 240, 240)

        answer_container = [
            Rect(50, 358, 495, 165),
            Rect(735, 358, 495, 165),
            Rect(50, 538, 495, 165),
            Rect(735, 538, 495, 165)
        ]

        return {
            'main': main_container,
            'timer': timer_container,
            'answers': answer_container
        }
    
    def draw(self, screen):
        screen.fill(self.palette.BACKGROUND)
        pygame.draw.rect(screen, self.palette.PRIMARY, self.containers['main'])
        pygame.draw.rect(screen, self.palette.TIMER, self.containers['timer'])

        for answer in self.containers['answers']:
            pygame.draw.rect(screen, self.palette.SECONDARY, answer)
        
        pygame.display.flip()
