import pygame
from .config import *

"""docstring for Player"""
class Player(pygame.sprite.Sprite):

	def __init__(self, left, bottom): # Posicion en Izquierda(left), y Abajo(bottom)
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface( (40, 40) )
		self.image.fill(BLUE)

		# Posicion de nuestro player
		self.rect = self.image.get_rect()
		self.rect.left = left # Modif de su posicion izquierda
		self.rect.bottom = bottom # Modif de su posicion abajo

		self.pos_y = self.rect.bottom
		self.vel_y = 0 # velocidad q cae en y

		self.can_jump = False # Para ver si puede saltar nuestro jugador

		self.playing = True # Para saber si el jugador esta jugando

	def collide_with(self, sprites): # Para validar si colisiona con un obtaculos
	 	# Verificamos si choca con algun objeto de nuestro Sprite
		objects = pygame.sprite.spritecollide(self, sprites, False)

		if objects: # Comprobamos si esta la colision
			return objects[0] # Retornamos el objeto

	def collide_bottom(self, wall): # Para validar si colisiona con un obtaculos en la parte de abajo
		return self.rect.colliderect(wall.rect_top) # Rectornamos el objeto de la colision

	def skid(self, wall): # Para patinar o surferar ensima de un obtaculos
		self.pos_y = wall.rect.top # Posicionamos en nuestra posicion en y  
		self.vel_y = 0 # Indicamos su velocida en y
		self.can_jump = True # Y activamos el salto

	def validate_platform(self, platfom): # Para valida si colisiona con un plataforma
		result = pygame.sprite.collide_rect( (self), platfom ) # para una colision

		if result: # validamos si existe la colision
			self.vel_y = 0 
			self.pos_y = platfom.rect.top # Modifica ahora para la posicion de la platform
			self.can_jump = True

	def jump(self): # Para hacer un salto
		if self.can_jump: # Compruebo si puedo saltar
			self.vel_y = -23 # Cambio su posicion velocidad q cae en y
			self.can_jump = False # Ahora no puede saltar

	def update_pos(self): # para actualizar la posicion
		self.vel_y += PLAYER_GRAV # incrementa segun la gravedad
		self.pos_y += self.vel_y + 0.5 * PLAYER_GRAV # incrementa

	def update(self): # para actualizar
		if self.playing:
			self.update_pos()

			self.rect.bottom = self.pos_y # Modifica la parte de abajo segun la self.pos_y

	def stop(self): # Para Detener a el jugador
		self.playing = False
