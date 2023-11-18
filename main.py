import pygame
import sys

pygame.init()

WIDTH, HEIGHT, FPS_CAP = 1280, 720, 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Space Shooter")

background = pygame.image.load("GFX/background.png")
spaceship = pygame.image.load("GFX/spaceship.png")

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 40

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))
        screen.blit(spaceship, (WIDTH/2 - SPACESHIP_HEIGHT/2, HEIGHT/2 - SPACESHIP_WIDTH/2))

        pygame.display.flip()

        clock.tick(FPS_CAP)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
