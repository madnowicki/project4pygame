from pygame import *
from pygame.sprite import *
from random import *
init()

#DELAY = 1000;
maxHeight = 600
maxWidth = 800
screen = display.set_mode((maxWidth, maxHeight))
display.set_caption('The Snack-uation Room')

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

def intro():
	bgimage = pygame.image.load("const.bmp").convert_alpha()
	bgimage = pygame.transform.scale(bgimage, (maxWidth, maxHeight))
	screen.blit(bgimage, (0,0))
	f = font.Font(None, 30)
	t = f.render("Intro screen and instructions", False, (0,0,0))
	screen.blit(t, (320,0))	

	while True:
		for e in event.get():
			if e.type == KEYDOWN:
				if e.key == K_SPACE:
					return
		screen.blit(bgimage, (0,0))
		screen.blit(t, (320,0))
		display.flip()
	pygame.quit()

intro()

def main():
	bgimage = pygame.image.load("flag.bmp").convert()
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
	        if obama.eat(almond):
	            mixer.Sound("bite.wav").play()
	            almond.move()
	            snacks += 1

	            # reset timer
	            
	    elif e.type == USEREVENT + 1: # TIME has passed
	        almond.move()

	    # refill background color so that we can paint sprites in new locations
	    #screen.fill(bgcolor)
	    screen.blit(bgimage, (0,0))
	    t = f.render("Snackpot = " + str(snacks), False, (0,0,0))
	    screen.blit(t, (320, 0))        # draw text to screen.  Can you move it?

	    # update and redraw sprites
	    sprites.update()
	    sprites.draw(screen)
	    display.update()
	#snacks = 0

main()
