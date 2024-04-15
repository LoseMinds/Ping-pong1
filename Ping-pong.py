from pygame import *

window = display.set_mode((700,500))
display.set_caption('Пинг-понг')

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, weight, height):
        super().__init__()
        self.w = weight
        self.h = height
        self.image = transform.scale(image.load(img),(self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def rendering(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def __init__(self, img, x, y, weight, height, speed_x, speed_y):
        super().__init__(img, x, y, weight, height)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        pass


class Rocket(GameSprite):
    def __init__(self, img, x, y, weight, height, speed):
        super().__init__(img, x, y, weight, height)
        self.speed = speed

    def move(self):
        pass

background = transform.scale(
    image.load('fon.png'),
    (700,500)
)
rocket1 = Rocket('rocket.png', 20, 200, 20, 100, 2)
rocket2 = Rocket('rocket.png', 680, 200, 20, 100, 2)
ball = Ball('ball.png',350, 250, 20, 20, 2, 2)


clock = time.Clock()

game = True

while game:
    window.blit(background, (0,0))
    rocket1.rendering()
    rocket2.rendering()
    ball.rendering()
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(60)
    display.update()



