import pygame
import time
import random 

pygame.init() #initiating pygame modules

display_width = 800
display_height = 600

black = (0,0,0) 
white = (255,255,255)
red = (170,0,0)
green = (0,170,0)

bright_red = (255,0,0)
bright_green = (0,255,00)

obs_color = (53,115,255)

ship_width = 99

pause = False



gameDisplay = pygame.display.set_mode((display_width,display_height)) #Initialize window or screen to run the game
pygame.display.set_caption('Space Race')
clock = pygame.time.Clock() #setting game clock to track time inside game

shipImg = pygame.image.load('ship.png')

def score(count):
	 font = pygame.font.SysFont(None , 25)
	 text = font.render(("Score: " + str(count )) , True , white  )
	 gameDisplay.blit(text , (0,0) )
	 


def obstacles(obsx , obsy , obswidth , obsheight , obscolor):

	pygame.draw.rect(gameDisplay, obscolor , [obsx, obsy, obswidth, obsheight])

		




def ship(x,y):
	gameDisplay.blit(shipImg,(x,y))

def text_objects(text , font):
	textSurface = font.render(text , True , white )
	return(textSurface , textSurface.get_rect()) 




def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',50 )
	textSurf, textRect = text_objects(text , largeText)
	textRect.center = ((display_width/2) , (display_height)/2)
	gameDisplay.blit(textSurf , textRect)
	pygame.display.update()

		
def pause_text():
	message_display('Paused')

def intro_text():
	message_display('Space Race')

def crash_text():
	message_display('You Crashed')

def crash():

	crash_text()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		#gameDisplay.fill(black)
		

		button('Go Again',150,450,100,50,green,bright_green, game_loop)
		button('Quit',550,450,100,50,red,bright_red, quitgame)

		pygame.display.update()
		clock.tick(15)

	


def button(msg,x,y,w,h,ic,ac, action = None):

	mouse = pygame.mouse.get_pos()
		#print(mouse)

	click = pygame.mouse.get_pressed()
	#print(click)



	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
		if click[0] == 1 and action != None:
			action()


	else:
		pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

	smallText = pygame.font.Font("freesansbold.ttf",20)
	textSurf,textRect =text_objects(msg ,smallText)
	textRect.center = ( (x+(w/2)), (y+ (h/2)) )
	gameDisplay.blit(textSurf,textRect)

def unpause():
	global pause
	pause = False


def paused():

	

	global pause
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(black)


		pause_text()	

		button('Continue',150,450,100,50,green,bright_green, unpause)
		button('Quit',550,450,100,50,red,bright_red, quitgame)

		pygame.display.update()
		clock.tick(15)


def quitgame():
	pygame.quit()
	quit()

def game_intro():

	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(black)
		intro_text()

		button('GO',150,450,100,50,green,bright_green, game_loop)
		button('Quit',550,450,100,50,red,bright_red, quitgame)

		pygame.display.update()
		clock.tick(15)






def game_loop():

	global pause

	x = (display_width * 0.45)
	y = (display_height * 0.8)

	x_change = 0

	obs_startx = random.randrange(2 , display_width -102 )
	obs_starty = -600
	obs_speed = 4 
	obs_width = 100
	obs_height = 100

	dodged = 0

	gameExit = False


	ship_speed = 0 

	


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
					quit()
		

		#print(event)

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change += -5 - ship_speed
				elif event.key == pygame.K_RIGHT:
					x_change += 5 + ship_speed
				elif event.key == pygame.K_p:
					pause = True
					paused()




			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					x_change = 0
				if event.key == pygame.K_RIGHT:
					x_change = 0

		x = x +  x_change
		
			
		gameDisplay.fill(black)


		

		obstacles(obs_startx, obs_starty, obs_width, obs_height, obs_color )
			
		obs_starty += obs_speed



		ship(x,y)
		score(dodged)


		if x > display_width - ship_width  or x < 0:
			crash() 

		if obs_starty > display_height:
			obs_starty = -100
			obs_startx = random.randrange(2 , display_width -102 )

			dodged+= 1
			obs_speed+= 0.5
			ship_speed+= 0.5
			obs_width+=4
			


		
		if y < obs_starty + obs_height:
			#print("y crossover")

			if x > obs_startx and x < obs_startx + obs_width or x + ship_width > obs_startx and x + ship_width < obs_startx + obs_width:
				crash()

		
		pygame.display.update()
		clock.tick(60) #updating the window at 60 fps


game_intro()
game_loop( )

pygame.quit()
quit()







