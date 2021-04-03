#Esctututa Base 
import pygame # Importamos pygamne
import sys # Importamos sys

pygame.init() # iniciamos pygame

# Definimos el ancho y alto
width = 400 
heigth = 500

# Creamos una ventana
surface = pygame.display.set_mode( (width, heigth) ) #surface
pygame.display.set_caption("Colision Por Mascaras!") # Damos un titulo a nuestra ventana

# RGB
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(20, 255, 20)
blue = pygame.Color(59, 87, 181)

# Obtenemos nuestra imagen
image = pygame.image.load("../images/mi_image_trans1.png")
rect1 = image.get_rect()
rect1.center = (width // 2, heigth // 2)
mask_image_rect1 = pygame.mask.from_surface(image)# Creamos una mascara 

image2 = pygame.image.load("images/mi_image_trans2.png")
rect2 = image2.get_rect() # Rectangulo 2
mask_image_rect2 = pygame.mask.from_surface(image2) # Creamos una mascara 

# Font
font = pygame.font.Font("../roboto/Last-Dream.ttf", 32)

# Aqui estamos a la espera de los diferentes evento q puedan estar susitarte en la ventana
while True:
	pygame.time.delay(2) #milisegundos
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Si es ventento es de tipo Quit
			pygame.quit() # Aqui finalizamos la ventana
			sys.exit() # Aqui finalizamos el Script

	surface.fill(white) # Colocamos nuestro color a nuestra superfice

	rect2.center = pygame.mouse.get_pos()

	surface.blit(image, rect1)
	surface.blit(image2, rect2)

	message = ""

	offset = (rect2.x - rect1.x, rect2.y - rect1.y) # cordenadas en x, y
	# Comprobamos si existe o no una colision de mascaras
	if mask_image_rect1.overlap(mask_image_rect2, offset):
		message = "Existe Colision !!"

	text = font.render(message, True, blue) # Creamos nuestro texto
	rect4 = text.get_rect() # Obtenemos su posicion
	rect4.midtop = (width // 2, 50) # Lo ponemos en la parte de arriba

	surface.blit(text, rect4) # Pintamos nuestro texto

	pygame.display.update()