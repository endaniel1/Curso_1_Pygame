#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Colores!!") # Damos un titulo a nuestra ventana

# RGB VALORES Q SOPORTA VALIDOS 0 - 255
red = pygame.Color(255, 0, 0) # Utilizamos de la clase Color para general lo de los colores
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

my_color = (200, 90, 130) # Tambien se puede trabajar mediante tuplas, pero siempre tendra 3 valores

# Aqui estamos a la espera de los diferentes evento q puedan estar susitarte en la ventana
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Si es ventento es de tipo Quit
			pygame.quit() # Aqui finalizamos la ventana
			sys.exit() # Aqui finalizamos el Script

	surface.fill(my_color)

	pygame.display.update()