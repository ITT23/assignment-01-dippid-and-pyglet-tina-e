import sys

import pyglet
from DIPPID import SensorUDP
from Game import Game

PORT = 5700
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 780
sensor = SensorUDP(PORT)

window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
pyglet.gl.glClearColor(0.1, 0.6, 0.2, 0)
game = Game(sensor, WINDOW_WIDTH, WINDOW_HEIGHT)


@window.event
def on_draw():
    window.clear()
    game.update()
    game.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        game.game_state = 1
        game.enemy.num_enemies_reached_bottom = 0
    elif symbol == pyglet.window.key.Q:
        sensor.disconnect()
        sys.exit(0)


pyglet.app.run()

