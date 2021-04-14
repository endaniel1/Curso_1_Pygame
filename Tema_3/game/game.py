import pygame
import sys
import random
import os

from .config import * # Donde vamos a tener las config Globales
from .platform import Platform
from .player import Player
from .wall import Wall
from .coin import Coin

"""docstring for Game"""
class Game:
	def __init__(self):
		pygame.init() 

		self.surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
		pygame.display.set_caption(TITLE)

		self.running = True # Para ver si esta en inicio el juego o no

		self.playing = True # Para saber si el jugador esta jugando

		self.clock = pygame.time.Clock() # Para q el juego vaya a la velocida por cuadros por segundo

		self.font = pygame.font.match_font(FONT) # Para Crear una fuente

		self.dir = os.path.dirname(__file__) # Obtenemos la direccion asoluta
		self.dir_sounds = os.path.join(self.dir, 'sources\sounds') # Con eso creamos la ruta de nuestros sonidos



	def start(self): # Funcion para empezar el Juego
		self.new()

	def new(self): # Funcion para nuevo juego
		self.score = 0
		self.level = 0
		self.generate_elements()
		self.run()

	def generate_elements(self): # Funcion q genera los elementos
		self.platform = Platform()
		self.player = Player(100, self.platform.rect.top - 200)


		self.sprites = pygame.sprite.Group() # para tener los sprite en Grupos
		self.walls = pygame.sprite.Group()
		self.coins = pygame.sprite.Group()

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

			self.level += 1 # Para q se aumente el nivel

			self.generate_coins() # Y generamos mas coin

	def generate_coins(self):
		last_position = WIDTH + 100

		if not len(self.coins) > 0: # Verificamos si no ay monedas
			for c in range(0, MAX_COINS):
				pos_x = random.randrange(last_position + 180, last_position + 300)

				coin = Coin(pos_x, 150)

				last_position = coin.rect.right

				self.sprites.add(coin)
				self.coins.add(coin)

	def run(self): # Funcion para arrancar el juego
		while self.running:
			self.clock.tick(FPS)
			self.events()
			self.draw()
			self.update()

	def events(self): # Funcion q hace los eventos
		pygame.init()
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

		self.draw_text() # Para pintar el texto

		self.sprites.draw(self.surface) # pintamos nuestra surface en nuestro sprites

	def score_format(self): # Para dar formato al texto del score
		return "Score: {}".format(self.score)

	def level_format(self): # Para dar formato al texto del level
		return "Level: {}".format(self.level)

	def draw_text(self): # Para pintar una superfice con un texto dato
		self.display_text(self.score_format(), 36, WHITE, WIDTH // 2, TEXT_POSY)
		self.display_text(self.level_format(), 36, WHITE, 60, TEXT_POSY)

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

			coin = self.player.collide_with(self.coins) # Para saber si ay un colision
			if coin: # Ay un a colision con los coin
				self.score += 1 # Aumentamos los puntos
				coin.kill() # Borramos los coin

				#sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, 'coin-drop.wav'))
				#sound.play()
				# Cargamos un audio y lo reproducimos
				pygame.mixer.music.load(os.path.join(self.dir_sounds, 'coin-drop.wav'))
				pygame.mixer.music.play()

			self.sprites.update() # Controla los cambios de los Sprites

			self.player.validate_platform(self.platform) # para validar si choca en la plataforma

			self.update_elements(self.walls) # Para actualizar elementos			
			self.update_elements(self.coins) # Para actualizar elementos

			self.generate_walls() # Para Generar obtaculos o paredes
			self.generate_coins() # Para Generar obtaculos o paredes

	def update_elements(self, elements): # Funcion para actualizar elementos
		for element in elements: # Recorremos nuestro elementos
			if not element.rect.right > 0: # comprobamos si no estan la pantalla
				element.kill() # Destruimos o Eliminamod el elemento

	def stop(self): # Fuhncion para detener 
		print("Existe una colision")
		# Cargamos un audio y lo reproducimos
		pygame.mixer.music.load(os.path.join(self.dir_sounds, 'lose.mp3'))
		pygame.mixer.music.play()

		self.player.stop()
		self.stop_elements(self.walls)

		self.playing = False

	def stop_elements(self, elements): # Funcion para detener elementos
		for element in elements: #Recorremos nuestro elementos
			element.stop()

	def display_text(self, text, size, color, pos_x, pos_y): # Para crear una superfice con un texto
		font = pygame.font.Font(self.font, size)

		text = font.render(text, True, color)
		rect = text.get_rect()

		rect.midtop = (pos_x, pos_y)

		self.surface.blit(text, rect)