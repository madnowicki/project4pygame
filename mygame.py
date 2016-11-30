from pygame import *
from pygame.sprite import *
from random import *

DELAY = 1000;
maxHeight = 600
maxWidth = 800
screen = display.set_mode((maxWidth, maxHeight))
display.set_caption('The Snack-uation Room')
bgimage = pygame.image.load("flag.bmp").convert_alpha()
bgimage = pygame.transform.scale(bgimage, (maxWidth, maxHeight))
screen.blit(bgimage, (0,0))

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
'''
class Star(Sprite):
    def __init__(self, x, y):
        super(Star, self).__init__()
        self.image = pygame.Surface((2, 2))
        pygame.draw.circle(self.image,
                           (128, 128, 200),
                           (0, 0),
                           2,
                           0)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 1
        self.size = 1
        self.colour = 128

    def accelerate(self):
        self.image = pygame.Surface((1, self.size))

        if self.size < 200:
            self.size += 4
            self.colour += 20
            if self.colour >= 200:
                self.colour = random.randint(180, 200)
        else:
            self.colour -= 30
            if self.colour <= 20:
                self.colour = random.randrange(20)

        pygame.draw.line(self.image, (self.colour, self.colour, self.colour),
                         (0, 0), (0, self.size))

        if self.velocity < Y_MAX / 3:
            self.velocity += 1

        # x, y = self.rect.center
        # self.rect.center = random.randrange(X_MAX), y
        def update(self):
        x, y = self.rect.center
        if self.rect.center[1] > Y_MAX:
            self.rect.center = (x, 0)
        else:
            self.rect.center = (x, y + self.velocity)
'''
init()



#stars = create_starfield(everything)


mouse.set_visible(False)

f = font.Font(None, 65)

almond = Almond()
obama = Obama()
sprites = RenderPlain(almond, obama)

snacks = 0
time.set_timer(USEREVENT + 1, DELAY)

while True:
    for event in event.get():
        if event.type == QUIT
        done = True

    pos = mouse.get_pos()
    
        
#how to upload background image??
    #screen.image.load("flag.bmp").convert_alpha()
    t = f.render("Snackpot = " + str(snacks), False, (0,0,0))
    screen.blit(t, (320,0))
    screen.blit(bgimage, (0,0))

    sprites.update()
    sprites.draw(screen)
    display.update()
    
            