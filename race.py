import pygame
import time

pygame.init() #initiating pygame modules

display_width = 800
display_height = 600

black = (0,0,0) 
white = (255,255,255)

ship_width = 99


gameDisplay = pygame.display.set_mode((display_width,display_height)) #Initialize window or screen to run the game
pygame.display.set_caption('Race')
clock = pygame.time.Clock() #setting game clock to track time inside game

shipImg = pygame.image.load('ship.png')

def ship(x,y):
	gameDisplay.blit(shipImg,(x,y))

def text_objects(text , font):
	textSurface = font.render(text , True , black)
	return(textSurface , textSurface.get_rect()) 



def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',50 )
	textSurf, textRect = text_objects(text , largeText)
	textRect.center = ((display_width/2) , (display_height)/2)
	gameDisplay.blit(textSurf , textRect)
	pygame.display.update()

	time.sleep(2)
 
	



def crash():
	message_display('You Crashed')
	game_loop()


def game_loop():

	x = (display_width * 0.45)
	y = (display_height * 0.8)

	x_change = 0

	gameExit = False


	while not gameExit:
		
		#event handling loop
		for event in pygame.event.get(): # any action during the game is recorded as a pygame event(eg. mouse clicks, keyboard strokes)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


			#pressed = pygame.key.get_pressed()
			#if pressed[pygame.K_ESCAPE]: 
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
		

		#print(event)

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change += -5
				elif event.key == pygame.K_RIGHT:
					x_change += 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					x_change = 0
				if event.key == pygame.K_RIGHT:
					x_change = 0

		x = x +  x_change
		
			
		gameDisplay.fill(white)
		ship(x,y)

		if x > display_width - ship_width  or x < 0:
			crash() 
		
		pygame.display.update()
		clock.tick(60) #updating the window at 60 fps



game_loop( )

pygame.quit()
quit()







