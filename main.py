import pygame
import sys
import random
import asteroid as ast

pygame.init()

WIDTH, HEIGHT, FPS_CAP = 1280, 720, 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Space Shooter")

background_image = pygame.image.load("GFX/background.png")
spaceship_image = pygame.image.load("GFX/spaceship.png")
asteroid_image = pygame.image.load("GFX/asteroid.png")

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 40
SPACE_SHIP_SPEED = 5

asteroid_image = pygame.transform.scale(asteroid_image, (ast.WIDTH, ast.HEIGHT))
asteroids = []


def main():
    running = True
    spaceship_pos_x, spaceship_pos_y = (WIDTH - SPACESHIP_WIDTH) // 2, (HEIGHT - SPACESHIP_HEIGHT) // 2

    # Main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, (0, 0))
        # Spaceship movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and spaceship_pos_x > 0:
            spaceship_pos_x -= SPACE_SHIP_SPEED
        if keys[pygame.K_RIGHT] and spaceship_pos_x < WIDTH - SPACESHIP_WIDTH:
            spaceship_pos_x += SPACE_SHIP_SPEED
        if keys[pygame.K_UP] and spaceship_pos_y > 0:
            spaceship_pos_y -= SPACE_SHIP_SPEED
        if keys[pygame.K_DOWN] and spaceship_pos_y < HEIGHT - SPACESHIP_HEIGHT:
            spaceship_pos_y += SPACE_SHIP_SPEED

        spaceship_rect_surface = pygame.Surface((SPACESHIP_WIDTH, SPACESHIP_HEIGHT), pygame.SRCALPHA)
        spaceship_rect_surface.blit(spaceship_image, (0, 0))
        screen.blit(spaceship_rect_surface, (spaceship_pos_x, spaceship_pos_y))

        # Asteroid drawing and position update
        for asteroid in asteroids:
            asteroid.update(asteroids)
            screen.blit(asteroid.image, asteroid.rect)

        # Generating asteroids
        if random.randint(0, 100) < 3:  # generation chance
            new_asteroid = ast.Asteroid(asteroid_image)
            asteroids.append(new_asteroid)

        pygame.display.flip()

        clock.tick(FPS_CAP)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
