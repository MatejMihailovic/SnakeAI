import pygame
from GAagent import GAAgent
import numpy as np
from utils import save_animation
import keyboard
from Game import Game
from Food import Food
from Player import Player


def run_snake():
    pygame.init()
    pygame.font.init()
    game = Game(20, 20)

    snake_ga = Player(game, "red")
    game.player = snake_ga

    game.food.append(Food(game))

    ga_agent = GAAgent(population_name="standard_population", generation=100)
    snake_ga.set_agent(ga_agent)

    game.game_speed = 0  # parameter: game speed
    game.display_option = True  # parameter: show game
    record = True  # parameter: True if recording the game
    frames = []

    while not keyboard.is_pressed('s'):
        move = game.player.select_move(game)
        game.player.do_move(move, game)
        if game.player.crash:
            game.player.init_player(game)

        if game.display_option:
            game.display()
            pygame.time.wait(game.game_speed)
            if record:
                data = pygame.image.tostring(game.gameDisplay, 'RGBA')
                from PIL import Image
                img = Image.frombytes('RGBA', (game.game_width, game.game_height + 100), data)
                img = img.convert('RGB')
                frames.append(np.array(img))
    save_animation(frames, 'videos/snake.mp4', 25)


if __name__ == "__main__":
    run_snake()
