#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Mover Imagen!") # Damos un titulo a nuestra ventana

# RGB
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(20, 255, 20)
blue = pygame.Color(59, 87, 181)

# Obtenemos nuestra imagen
image = pygame.image.load("../images/fulbot.png")
rect = image.get_rect()
rect.center = (width // 2, heigth // 2)

# Aqui estamos a la espera de los diferentes evento q puedan estar susitarte en la ventana
while True:
	pygame.time.delay(2) #milisegundos
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Si es ventento es de tipo Quit
			pygame.quit() # Aqui finalizamos la ventana
			sys.exit() # Aqui finalizamos el Script

	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_w]:
		rect.y -= 5

	if pressed[pygame.K_a]:
		rect.x -= 5

	if pressed[pygame.K_s]:
		rect.y += 5

	if pressed[pygame.K_d]:
		rect.x += 5

	# Validacion 
	if rect.left < 0:
		rect.left = 0

	if rect.right > width:
		rect.right = width

	if rect.top < 0:
		rect.top = 0

	if rect.bottom > heigth:
		rect.bottom = heigth

	surface.fill(white) # Colocamos nuestro color a nuestra superfice

	surface.blit(image, rect)

	pygame.display.update()