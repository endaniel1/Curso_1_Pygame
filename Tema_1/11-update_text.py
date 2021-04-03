#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Actualizando Texto!!") # Damos un titulo a nuestra ventana

# RGB
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(20, 255, 20)
blue = pygame.Color(59, 87, 181)

# Obtenemos la fuente
font = pygame.font.Font("../roboto/Last-Dream.ttf", 48)


# Aqui estamos a la espera de los diferentes evento q puedan estar susitarte en la ventana
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Si es ventento es de tipo Quit
			pygame.quit() # Aqui finalizamos la ventana
			sys.exit() # Aqui finalizamos el Script


	surface.fill(white)

	seconds = pygame.time.get_ticks() // 1000 # Obtenemos los el time

	# Creamos un texto le pasamos seconds en formato string, True, color
	text = font.render(str(seconds), True, green) 
	# obtemos y cambios para q este en la posicion del centro
	rect = text.get_rect()
	rect.center = (width // 2, heigth // 2)
	# Pintamos la superfice con el texto y la posicion
	surface.blit(text, rect)

	pygame.display.update()