import pygame
import time
import random

pygame.init()

display_width = 800 # exercise
display_height = 600 # exercise

black = (0, 0, 0) # exercise
white = (255, 255, 255) # exercise
red = (255, 0, 0) # exercise

pipe_color = (53, 115, 255) # exercise

bird_size = 5

pipe_gap = 100


game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

class Pipe:

	def __init__(self, x, y, height, width):
		self.x = x
		self.top_y = y
		self.height = height
		self.bottom_y = self.top_y + self.height + pipe_gap
		self.width = width
		self.color = pipe_color


def show_score(score):
	# Displays score at the top left of screen
	font = pygame.font.SysFont(None, 25)
	text = font.render("Score " + str(score), True, black)
	game_display.blit(text, (0, 0))



def draw_pipe(pipe):
	# Draws pipe at coordniate(x, y) with given height, weight, and color
	pygame.draw.rect(game_display, pipe.color, [pipe.x, pipe.top_y, pipe.width, pipe.height])
	pygame.draw.rect(game_display, pipe.color, [pipe.x, pipe.bottom_y, pipe.width, pipe.height])


def draw_bird(x, y):
	# Draws the bird at coordinate (x, y)
	pygame.draw.circle(game_display, black, (x, y), 5)


def display_message(text):
	# Displays a message in the middle of the screen
	font = pygame.font.Font('freesansbold.ttf', 115)
	text_surface = font.render(text, True, black)
	text_rectangle = text_surface.get_rect()
	text_rectangle.center = ((display_width / 2), (display_height / 2))
	game_display.blit(text_surface, text_rectangle)
	pygame.display.update()


def start_game():
	x = int(display_width * 0.3)
	y = int(display_height * 0.5)

	y_change = 0

	gravity = 3

	pipe_x = 1200
	pipe_y = display_height * -0.3
	pipe_speed = 4
	pipe_width = 100
	pipe_height = 400

	pipe = Pipe(pipe_x, pipe_y, pipe_height, pipe_width)

	score = 0

	game_over = False


	while not game_over:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					y_change = -12
					in_key_press = True

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					y_change = 0
					in_key_press = False


		y = y + y_change + gravity

		game_display.fill(white)

		draw_pipe(pipe)
		pipe.x -= pipe_speed
		draw_bird(x, y)
		show_score(score)

		# establishes boundaries of our game
		if y < 0 or y > display_height - bird_size:
			display_message("Game Over")
			game_over = True
			time.sleep(5)

		# once pipe goes off screen
		if pipe.x < 0:
			pipe.x = display_width + pipe_width
			pipe.top_y = random.randrange(-0.5 * display_height, 0.2 * display_height)
			pipe.bottom_y = pipe.top_y + pipe_height + pipe_gap
			score += 1

		# check for collisions between bird and pipe
		if x > pipe.x and x < pipe.x + pipe.width:
			top_pipe_collision = y > pipe.top_y and y < pipe.top_y + pipe_height or y + bird_size > pipe.top_y and y + bird_size < pipe.top_y + bird_size
			bottom_pipe_collision = y > pipe.bottom_y and y < pipe.bottom_y + pipe_height or y + bird_size > pipe.bottom_y and y + bird_size < pipe.bottom_y + bird_size
			if top_pipe_collision or bottom_pipe_collision:
				display_message("Game Over")
				game_over = True
				time.sleep(5)


		pygame.display.update()
		clock.tick(60)


if __name__ == '__main__':
	start_game()
	pygame.quit()
	quit()
