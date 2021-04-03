#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Evento del Teclado!") # Damos un titulo a nuestra ventana

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

		""" Para la manipulacion de eventos del teclado
		Se trabaja con la variable event y con su metodo type event.type
		"""
		# Para comparar si es presionada una tecla pygame.KEYDOWN
		if event.type == pygame.KEYDOWN:
			# Comparamos si la tecla es Izquierda o es A
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				message = "Izquierda"			
			# Comparamos si la tecla es Derecha o es D
			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				message = "Derecha"
			# Comparamos si la tecla es Abajo o es S
			if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				message = "Abajo"
			# Comparamos si la tecla es Arriba o es W
			if event.key == pygame.K_UP or event.key == pygame.K_w:
				message = "Arriba"

			print("{} !!".format(message)) # Imprimimos el mensaje

		#Para cuando es soltada una tecla
		if event.type == pygame.KEYUP:
			#print("Tecla Liberado!!")
			pass

	pygame.display.update()