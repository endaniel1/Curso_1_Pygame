#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Colisiones!") # Damos un titulo a nuestra ventana

# RGB
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(20, 255, 20)
blue = pygame.Color(59, 87, 181)

rect1 = pygame.Rect(0, 0, 100, 80) # Rectangulo 1
rect1.center = (width // 2, heigth // 2)
rect2 = pygame.Rect(0, 0, 100, 80) # Rectangulo 2

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

	rect2.center = pygame.mouse.get_pos()

	# Pintamos los rectangulos
	pygame.draw.rect(surface, green, rect1)
	pygame.draw.rect(surface, red, rect2)

	message = ""

	if rect1.colliderect(rect2): # Comprobamos si existe o no una colision de un rectangolo a otro
		message = "Existe Colision !!"

	text = font.render(message, True, blue) # Creamos nuestro texto
	rect3 = text.get_rect() # Obtenemos su posicion
	rect3.midtop = (width // 2, 50) # Lo ponemos en la parte de arriba

	surface.blit(text, rect3) # Pintamos nuestro texto

	pygame.display.update()