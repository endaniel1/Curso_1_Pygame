#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Superficies") # Damos un titulo a nuestra ventana

# RGB
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(20, 255, 20)
blue = pygame.Color(59, 87, 181)

#Creamos nuestra surface2
surface2 = pygame.Surface((200, 200))
surface2.fill(green)

#Obtemos la cordenada en donde esta con surface2.get_rect()
rect = surface2.get_rect()
rect.center = (width // 2, heigth // 2)

# Aqui estamos a la espera de los diferentes evento q puedan estar susitarte en la ventana
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Si es ventento es de tipo Quit
			pygame.quit() # Aqui finalizamos la ventana
			sys.exit() # Aqui finalizamos el Script

	surface.fill(white)

	# surface.blit() Pintar una supercie en otra
	"""
	 1.- superfice
	 2.- Cordenadas o lugar a donde va a a estar X, Y
	"""
	surface.blit(surface2, rect )

	# pintamos o DIBUJAMOS UN RECTANGULO A NUESTRA surface2 (su posicion es relativa a la surface en donde esta) 
	pygame.draw.rect(surface2, red, (100, 50, 80, 40))

	pygame.display.update()