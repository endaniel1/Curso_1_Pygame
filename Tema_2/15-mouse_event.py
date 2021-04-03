#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Evento del Mouse!") # Damos un titulo a nuestra ventana

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

		""" Para la manipulacion de eventos del mouse
		Se trabaja con la variable event y con su metodo type event.type
		"""
		# Para comparar si es presionada un click pygame.MOUSEBUTTONDOWN
		if event.type == pygame.MOUSEBUTTONDOWN:

			print(event.pos) # Con pos obtemos las cordenadas en X, Y, Donde fue el click

			if event.button == 1: # Aqui vemos si presiono el click Izquierdo
				message = "Click Izquierdo"

			if event.button == 2: # Aqui vemos si presiono el Scroll
				message = "Click Centor"
				
			if event.button == 3: # Aqui vemos si presiono el click Derecho
				message = "Click Derecho"

			if event.button == 4: # Aqui vemos si hizo Scroll hacia Arriba
				message = "Scroll Hacia Arriba"

			if event.button == 5: # Aqui vemos si hizo Scroll hacia Abajo
				message = "Scroll Hacia Abajo"
				
			print(message) #imprimos el message 

		#Para cuando es soltada un click
		if event.type == pygame.MOUSEBUTTONUP:
			#print("Boton Liberado !!")
			pass

	pygame.display.update()