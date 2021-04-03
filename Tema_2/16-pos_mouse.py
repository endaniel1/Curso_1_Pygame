#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Evento del Mouse - Posicion Mouse!") # Damos un titulo a nuestra ventana

# RGB
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(20, 255, 20)
blue = pygame.Color(59, 87, 181)

# Creamos una fuente
font = pygame.font.Font("freesansbold.ttf", 32)

# Aqui estamos a la espera de los diferentes evento q puedan estar susitarte en la ventana
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Si es ventento es de tipo Quit
			pygame.quit() # Aqui finalizamos la ventana
			sys.exit() # Aqui finalizamos el Script

	# Obtenemos la Posicion de nuestro mouse con pygame.mouse.get_pos()
	pos_x, pos_y = pygame.mouse.get_pos() # Tupla X, Y

	message = "pos x: {} pos y: {}".format(pos_x, pos_y)

	# print(message) # Mostramos aqui un mesaje si quieremos

	# Creamos nuestro mensaje con nuestra fuente
	text = font.render(message, True, red)
	# Obtenemos la posicion
	rect = text.get_rect()
	# Modificamos para q este al centro
	rect.center = (width // 2, heigth // 2)

	surface.fill(white) # Colocamos nuestro color a nuestra superfice

	surface.blit(text, rect) # Pintamos nuestro texto 

	pygame.display.update()