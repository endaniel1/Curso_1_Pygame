#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Objectos!!") # Damos un titulo a nuestra ventana

# RGB
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(20, 255, 20)
blue = pygame.Color(59, 87, 181)

# circle
circle = (200, 300) # Cordenas en X, Y
radio = 100 # Radio de nuestro circulo

# line
p1 = (100, 100) # Cordenas en X, Y en el punto 1
p2 = (200, 200) # Cordenas en X, Y en el punto 2
size = 2 # EL Grosor de nuesta linea

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
	pygame.draw.rect(surface, red, (100, 100, 80, 40))

	pygame.draw.circle(surface, green, circle, radio)

	pygame.draw.line(surface, blue, p1, p2, size)

	pygame.display.update()