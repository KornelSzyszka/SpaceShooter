import random

# image size
WIDTH, HEIGHT = 36, 36
# screen size
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720


class Asteroid:
    def __init__(self, asteroid_img):
        self.image = asteroid_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.randint(1, 5)

    def update(self, asteroids):
        self.rect.y += self.speed_y
        if self.rect.y > SCREEN_HEIGHT:
            asteroids.remove(self)
