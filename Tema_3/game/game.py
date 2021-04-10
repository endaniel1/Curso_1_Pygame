import pygame
import sys
import random

from .config import * # Donde vamos a tener las config Globales
from .platform import Platform
from .player import Player
from .wall import Wall

"""docstring for Game"""
class Game:
	def __init__(self):
		pygame.init() 

		self.surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
		pygame.display.set_caption(TITLE)

		self.running = True # Para ver si esta en inicio el juego o no

		self.playing = True # Para saber si el jugador esta jugando

		self.clock = pygame.time.Clock() # Para q el juego vaya a la velocida por cuadros por segundo

	def start(self): # Funcion para empezar el Juego
		self.new()

	def new(self): # Funcion para nuevo juego
		self.generate_elements()
		self.run()

	def generate_elements(self): # Funcion q genera los elementos
		self.platform = Platform()
		self.player = Player(100, self.platform.rect.top - 200)


		self.sprites = pygame.sprite.Group() # para tener los sprite en Grupos
		self.walls = pygame.sprite.Group()

		self.sprites.add(self.platform) # Añadimos la plataforma a los sprites
		self.sprites.add(self.player) # Añadimos el player a los sprites

		self.generate_walls()

	def generate_walls(self): # Funcion para genera obtaculos o paredes
		last_position = WIDTH + 100 # para obtener o general la ultima posicion

		if not len(self.walls) > 0: # Verificamos si no ay obtaculos

			for w in range(0, MAX_WALLS): # Creamos una cantida X del mismo

				# Generamos la posicion o margen X a la izquierda para crear el elemento  
				left = random.randrange(last_position + 200, last_position + 400)

				# Creamos nuestra Obtaculo pasandole la posicion LEFT y la posicion de nuestra platafoma
				wall = Wall(left, self.platform.rect.top)
				# Cambiamos para q tenga la posicion a la derecha de nuestra platafoma creada
				last_position = wall.rect.right

				self.sprites.add(wall) # Añadimos a nuestro sprites
				self.walls.add(wall) # Añadimos a nuestra walls



	def run(self): # Funcion para arrancar el juego
		while self.running:
			self.clock.tick(FPS)
			self.events()
			self.draw()
			self.update()

	def events(self): # Funcion q hace los eventos

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False # detenemos self.running
				pygame.quit() # detenemos pygame
				sys.exit() # detenemos el script

		key = pygame.key.get_pressed() # para saber si preciono un recla

		if key[pygame.K_SPACE]:
			self.player.jump()

	def draw(self): # Funcion q pinta las surface
		self.surface.fill(BLACK) # ccolor a nuestra surface

		self.sprites.draw(self.surface) # pintamos nuestra surface en nuestro sprites

	def update(self): # Funcion q va actualizando 
		if self.playing:
			pygame.display.flip() # Esta es igual q el metodo pygame.display.update()

			wall = self.player.collide_with(self.walls) # Para saber si ay un colision
			if wall: # Ay un a colision 
				# Comprobamos si la colision en la parte de abajo de nuestro personaje
				if self.player.collide_bottom(wall):
					self.player.skid(wall)
				else:
					self.stop() # Detenemos todo

			self.sprites.update() # Controla los cambios de los Sprites

			self.player.validate_platform(self.platform) # para validar si choca en la plataforma

			self.update_elements(self.walls) # Para actualizar elementos
			self.generate_walls() # Para Generar obtaculos o paredes

	def update_elements(self, elements): # Funcion para actualizar elementos
		for element in elements: # Recorremos nuestro elementos
			if not element.rect.right > 0: # comprobamos si no estan la pantalla
				element.kill() # Destruimos o Eliminamod el elemento

	def stop(self): # Fuhncion para detener 
		print("Existe una colision")
		self.player.stop()
		self.stop_elements(self.walls)

		self.playing = False

	def stop_elements(self, elements): # Funcion para detener elementos
		for element in elements: #Recorremos nuestro elementos
			element.stop()
