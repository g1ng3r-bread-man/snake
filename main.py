import pygame
import random
from constants import *

def main():
    pygame.init
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    dt = 0
    print("Starting Snake!")
    print(f"""Screen width: 1280\nScreen height: 720""")
    screen = pygame.display.set_mode((1280, 720))

    #game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        pygame.display.flip()
        frame = pygame.time.Clock().tick(60)
        dt = frame / 1000




if __name__ == "__main__":
    main()