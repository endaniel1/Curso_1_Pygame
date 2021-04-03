#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

import math

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Mover Imagen!") # Damos un titulo a nuestra ventana

# RGB
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(20, 255, 20)
blue = pygame.Color(59, 87, 181)

# Obtenemos nuestra imagen
image = pygame.image.load("../images/fulbot.png")
rect1 = image.get_rect()
rect1.center = (width // 2, heigth // 2)


surface2 = pygame.Surface( (rect1.width, rect1.height), pygame.SRCALPHA )
surface2.fill((0, 0, 0, 50))
rect2 = surface2.get_rect()
rect2.center = rect1.center

rect3 = pygame.Rect(0, 0, 80, 80) # Rectangulo 3

# Font
font = pygame.font.Font("../roboto/Last-Dream.ttf", 32)

# Aqui estamos a la espera de los diferentes evento q puedan estar susitarte en la ventana
while True:
	pygame.time.delay(2) #milisegundos
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Si es ventento es de tipo Quit
			pygame.quit() # Aqui finalizamos la ventana
			sys.exit() # Aqui finalizamos el Script


	surface.fill(white) # Colocamos nuestro color a nuestra superfice

	rect3.center = pygame.mouse.get_pos()

	surface.blit(image, rect1)
	surface2.blit(surface2, rect2)

	# Pintamos los rectangulos
	pygame.draw.rect(surface, red, rect3)

	message = ""

	# dist = raiz cuadrada de = x * x + y * y 
	# x = x1 - x2 # Rect x1 image 1, x2 image 2
	# y = y1 - y2 # Rect y1 image 1, y2 image 2
	dist = math.hypot(rect1.x - rect3.x, rect1.y - rect3.y)
	
	pygame.draw.line(surface, blue, rect1.center, rect3.center, 2)
	message = "{}".format(str(int(dist)))
	if dist < ( 50 + 50):
		message = "Existe Colision !!"

	#if rect1.colliderect(rect3): # Comprobamos si existe o no una colision de un rectangolo a otro
	#	message = "Existe Colision !!"

	text = font.render(message, True, blue) # Creamos nuestro texto
	rect4 = text.get_rect() # Obtenemos su posicion
	rect4.midtop = (width // 2, 50) # Lo ponemos en la parte de arriba

	surface.blit(text, rect4) # Pintamos nuestro texto


	pygame.display.update()