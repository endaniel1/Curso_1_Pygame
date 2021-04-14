#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Sonido - Musica de Fondo!!") # Damos un titulo a nuestra ventana

# RGB
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(20, 255, 20)
blue = pygame.Color(59, 87, 181)

pygame.mixer.music.load("../sounds/lose.mp3") # Cargamos el archivo de musica
pygame.mixer.music.set_volume(1.0) # Para el volumen maximo, Float 0.0 - 1.0
# Despues ejecutamos la funcion play
pygame.mixer.music.play(-1, 0.0) # cantida de veces q la cacion se va a repoducir, y en q momento se va reproducir

# Diferentes metodos para la manipulacion de la cancion
# pygame.mixer.music.rewind() # Se puede reiniciar la cnmcion
# pygame.mixer.music.pause() # Se puede pausar la cancion
# pygame.mixer.music.stop() # Se puede detener la cancion
# pygame.mixer.music.fadeout(5000) # Se puede detener la cancion poco a poco


# Aqui estamos a la espera de los diferentes evento q puedan estar susitarte en la ventana
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Si es ventento es de tipo Quit
			pygame.quit() # Aqui finalizamos la ventana
			sys.exit() # Aqui finalizamos el Script


	pygame.display.update()