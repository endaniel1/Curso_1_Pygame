#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Poligonos!!") # Damos un titulo a nuestra ventana

# RGB
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(20, 255, 20)
blue = pygame.Color(59, 87, 181)



# Aqui estamos a la espera de los diferentes evento q puedan estar susitarte en la ventana
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Si es ventento es de tipo Quit
			pygame.quit() # Aqui finalizamos la ventana
			sys.exit() # Aqui finalizamos el Script


	surface.fill(white)

	#draw
	# 1.- Donde se pintara la figura
	# 2.- De q color sera la figura
	#Triangulo
	pygame.draw.polygon(surface, green, ( 
		(0, 400), (100, 300), (200, 400) 
	))
	#Pentagono
	pygame.draw.polygon(surface, red, ( 
		(146, 0), (291, 106), (236, 277) , (56, 277),(0, 106)
	))


	pygame.display.update()