import pygame
from .config import *

"""docstring for Wall"""
class Wall(pygame.sprite.Sprite):

	def __init__(self, left, bottom):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface((40, 80))
		self.image.fill(RED)

		# Posicion de nuestro obtaculo o pared
		self.rect = self.image.get_rect() # Para Obtener el rectangulo
		self.rect.left = left
		self.rect.bottom = bottom

		self.vel_x = SPEED # Velocidad a la q se va a mover

		# Para crear posiciona el rectangulo en la parte de arriba de nuestra obtaculo o pared
		self.rect_top = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 1)

	def update(self):
		self.rect.left -= self.vel_x # Para mover nuestra pared a la Izquierda

		# Para mover nuestro rectangulo
		self.rect_top.x = self.rect.x

	def stop(self): # Detenemos nuestro obtaculos
		self.vel_x = 0