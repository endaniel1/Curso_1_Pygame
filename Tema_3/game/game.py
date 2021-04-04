import pygame
import sys

from .config import * # Donde vamos a tener las config Globales
from .platform import Platform
from .player import Player

clock = pygame.time.Clock()

"""docstring for Game"""
class Game:
	def __init__(self):
		pygame.init() 

		self.surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
		pygame.display.set_caption(TITLE)

		self.running = True # Para ver si esta en inicio el juego o no

	def start(self): # Funcion para empezar el Juego
		self.new()

	def new(self): # Funcion para nuevo juego
		self.generate_elements()
		self.run()

	def generate_elements(self): # Funcion q genera los elementos
		self.platform = Platform()
		self.player = Player(100, self.platform.rect.top - 200)

		self.sprites = pygame.sprite.Group() # para tener los sprite en Grupos

		self.sprites.add(self.platform) # Añadimos la plataforma a los sprites
		self.sprites.add(self.player) # Añadimos el player a los sprites

	def run(self): # Funcion para arrancar el juego
		while self.running:
			self.events()
			self.draw()
			self.update()

	def events(self): # Funcion q hace los eventos
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False # detenemos self.running
				pygame.quit() # detenemos pygame
				sys.exit() # detenemos el script

	def draw(self): # Funcion q pinta las surface
		self.surface.fill(BLACK) # ccolor a nuestra surface

		self.sprites.draw(self.surface) # pintamos nuestra surface en nuestro sprites

	def update(self): # Funcion q va actualizando 
		pygame.display.flip() # Esta es igual q el metodo pygame.display.update()

		self.sprites.update() # Controla los cambios de los Sprites

		self.player.validate_platform(self.platform) # para validar si choca en la plataforma

	def stop(self):
		pass
