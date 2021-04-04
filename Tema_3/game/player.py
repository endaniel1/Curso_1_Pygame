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
		self.vel_y = 0 

	def validate_platform(self, platfom): # Para valida si colisiona con un plataforma
		result = pygame.sprite.collide_rect( (self), platfom ) # para una colision

		if result: # validamos si existe la colision
			self.vel_y = 0 
			self.pos_y = platfom.rect.top # Modifica ahora para la posicion de la platform

	def update_pos(self): # para actualizar la posicion
		self.vel_y += PLAYER_GRAV # incrementa segun la gravedad
		self.pos_y += self.vel_y + 0.5 * PLAYER_GRAV # incrementa

	def update(self): # para actualizar
		self.update_pos()

		self.rect.bottom = self.pos_y # Modifica la parte de abajo segun la self.pos_y
