from pygame import *
from pygame.sprite import *
from random import *
import random
init()

maxHeight = 600
maxWidth = 800
screen = display.set_mode((maxWidth, maxHeight))
display.set_caption('The Snack-uation Room')

class Almond(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("almondicon.bmp").convert_alpha()
        self.rect = self.image.get_rect()

    def move(self):
        randX = randint(0, 400)
        randY = randint(0, 400)
        self.rect.center = (randX, randY)

class AlmondDrop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(AlmondDrop, self).__init__()
        self.image = image.load("almondicon.bmp").convert_alpha()
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

        if self.velocity < maxHeight / 3:
            self.velocity += 1

    def update(self):
        x, y = self.rect.center
        if self.rect.center[1] > maxHeight:
            self.rect.center = (x, 0)
        else:
            self.rect.center = (x, y + self.velocity)

class Obama(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("icon.bmp").convert_alpha()
        self.rect = self.image.get_rect()

    def eat(self, target):
        return self.rect.colliderect(target)

    def update(self):
        self.rect.center = mouse.get_pos()

def create_pileofalmonds(group):
    pile = []
    for i in range(100):
        x, y = random.randrange(maxWidth), random.randrange(maxHeight)
        s = AlmondDrop(320,0)
        s.add(group)
        pile.append(s)
    return pile

def intro():
	bgimage = pygame.image.load("ovalofficedesk.bmp").convert_alpha()
	bgimage = pygame.transform.scale(bgimage, (maxWidth, maxHeight))
	screen.blit(bgimage, (0,0))
	f = font.Font(None, 45)
	t1 = f.render("Oh no! We have a snack-uation on our hands.", False, (255,255,255))
	t2 = f.render("The nation needs your help.",False,(255,255,255))
	t3 = f.render("Can you feed President Obama his 7 nightly almonds?",False,(255,255,255))
	t4 = f.render("Press the space bar if you accept this challenge.", False, (255,255,255))
	screen.blit(t1, (0,0))	
	screen.blit(t2, (0,25))	
	screen.blit(t3, (0,45))	
	screen.blit(t4, (0,65))	

	mixer.init()
	mixer.Sound("anthem.wav").play()

	while True:
		for e in event.get():
			if e.type == KEYDOWN:
				if e.key == K_SPACE:
					return
		screen.blit(bgimage, (0,0))
		screen.blit(t1, (0,0))
		screen.blit(t2, (0,35))	
		screen.blit(t3, (0,65))
		screen.blit(t4, (0,85))
		display.flip()
	pygame.quit()

intro()

def ends():
	bgimage = pygame.image.load("ovalofficedesk.bmp").convert_alpha()
	bgimage = pygame.transform.scale(bgimage, (maxWidth, maxHeight))
	screen.blit(bgimage, (0,0))
	f = font.Font(None, 40)
	t = f.render("You hit the Snackpot! Obama can relax now!", False, (255,255,255))
	screen.blit(t, (0,0))	

	#call pile of almonds function here
	everything = pygame.sprite.Group()
	piles = create_pileofalmonds(everything)
	for i in piles: 
		i.accelerate()
	everything.update()

	screen.blit(bgimage, (0,0))
	screen.blit(t, (50,300))
	display.flip()
	display.update()
	pygame.time.delay(3000)
	pygame.quit()

def main():
	font.init()
	mixer.init()
	bgimage = pygame.image.load("wh.bmp").convert()
	bgimage = pygame.transform.scale(bgimage, (maxWidth, maxHeight))
	screen.blit(bgimage, (0,0))

	mouse.set_visible(False)
	f = font.Font(None, 65)

	almond = Almond()
	obama = Obama()
	sprites = RenderPlain(almond, obama)

	snacks = 0

	while True:
	    e = event.poll()
	    if e.type == QUIT:
	    	quit()
	    	break

	    elif e.type == MOUSEBUTTONDOWN:
	    	if snacks < 7:
	    		if obama.eat(almond):
	    			mixer.Sound("bite.wav").play()
	    			almond.move()
	    			snacks += 1
	    	else:
	    		mixer.Sound("cha-ching.wav").play()
	    		ends()
	    		break
	            
	    elif e.type == USEREVENT + 1: # TIME has passed
	        almond.move()

	    screen.blit(bgimage, (0,0))
	    t = f.render("Snackpot = " + str(snacks), False, (0,0,0))
	    screen.blit(t, (0, 0))        

	    sprites.update()
	    sprites.draw(screen)
	    display.update()

main()
