#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Rectangulos 1!!") # Damos un titulo a nuestra ventana

# RGB
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)

# Position X, Y de nuestro rectangulo argument 1 y 2
# Dimention Ancho(width), Alto(heigth) de nuestro rectangulo argument 1 y 2
rect = pygame.Rect(100, 150, 120, 60)
rect.center = (width // 2, heigth // 2) # resive X , Y

#Mostramos los valores de nuestro rect en las cordenas X y/o Y
print(rect.x)
print(rect.y)

# Aqui estamos a la espera de los diferentes evento q puedan estar susitarte en la ventana
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Si es ventento es de tipo Quit
			pygame.quit() # Aqui finalizamos la ventana
			sys.exit() # Aqui finalizamos el Script


	surface.fill(white)

	""" pygame.draw.rect() PARA PINTAR UN RECTANGULO
	# 1.- argument Donde se pintara la figura
	# 2.- argument de q color sera la figura
	# 3.- argument el rectangulo a utilizar
	"""
	pygame.draw.rect(surface, red, rect)

	pygame.display.update()