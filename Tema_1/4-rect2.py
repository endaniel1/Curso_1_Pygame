#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Rectagulos 2!!") # Damos un titulo a nuestra ventana

# RGB
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(20, 255, 20)

# Rect
rect = pygame.Rect(100, 150, 120, 60)
rect.center = (width // 2, heigth // 2)

print(rect.x)
print(rect.y)

# Tambien si puede generar mendiante una tupla, pero siempre va a llevar 4 argumento y no tendra los atributos y metodos de pygame
rect2 = (100, 100, 80, 40)

# Aqui estamos a la espera de los diferentes evento q puedan estar susitarte en la ventana
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Si es ventento es de tipo Quit
			pygame.quit() # Aqui finalizamos la ventana
			sys.exit() # Aqui finalizamos el Script


	surface.fill(white)

	pygame.draw.rect(surface, red, rect)
	pygame.draw.rect(surface, green, rect2)

	pygame.display.update()