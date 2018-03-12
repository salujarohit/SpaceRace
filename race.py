import pygame

pygame.init() #initiating pygame modules

display_width = 800
display_height = 600

black = (0,0,0) 
white = (255,255,255)


gameDisplay = pygame.display.set_mode((display_width,display_height)) #Initialize window or screen to run the game
pygame.display.set_caption('Race')
clock = pygame.time.Clock() #setting game clock to track time inside game

shipImg = pygame.image.load('ship.png')

def ship(x,y):
	gameDisplay.blit(shipImg,(x,y))


x = (display_width * 0.45)
y = (display_height * 0.8)



crashed = False

while not crashed:
	
	for event in pygame.event.get(): # any action during the game is recorded as a pygame event(eg. mouse clicks, keyboard strokes)
		if event.type == pygame.QUIT:
			crashed = True
	#print(event)
	
		
	gameDisplay.fill(white)
	ship(x,y)
	pygame.display.update()
	clock.tick(60) #updating the window at 60 fps


pygame.quit()
quit()







