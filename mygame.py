from pygame import *
from pygame.sprite import *
from random import *

DELAY = 1000;

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load("flag.bmp")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Almond(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("almond.bmp").convert_alpha()
        self.rect = self.image.get_rect()

    def move(self):
        randX = randint(0, 800)
        randY = randint(0, 800)
        self.rect.center = (randX, randY)

class Obama(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("obama.bmp").convert()
        self.rect = self.image.get_rect()

    def eat(self, target):
        return self.rect.colliderect(target)

    def update(self):
        self.rect.center = mouse.get_pos()

init()

maxHeight = 800
maxWidth = 800
screen = display.set_mode((maxWidth, maxHeight))
display.set_caption('The Snack-uation Room')
bgcolor = image.load("flag.bmp").convert_alpha()

mouse.set_visible(False)

f = font.Font(None, 65)

almond = Almond()
obama = Obama()
sprites = RenderPlain(almond, obama)

snacks = 0
time.set_timer(USEREVENT + 1, DELAY)

while True:
    e = event.poll()
    if e.type == QUIT:
        quit()
        break

    elif e.type == MOUSEBUTTONDOWN:
        if obama.eat(almond):
            mixer.Sound("cha-ching.wav").play()
            almond.move()
            hits += 1

            time.set_timer(USEREVENT + 1, DELAY)

    elif e.type == USEREVENT + 1:
        almond.move()
#how to upload background image??
    screen.image.load("flag.bmp").convert_alpha()
    t = f.render("Jackpot = " + str(snacks), False, (0,0,0))
    screen.blit(t, (320,0))

    sprites.update()
    sprites.draw(screen)
    display.update()
    
            