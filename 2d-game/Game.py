import sys

import pyglet
from pyglet import text, media, resource
from DIPPID import SensorUDP
from Car import Car
from Street import Street
from Menu import Menu
from Enemy import Enemy

PORT = 5700
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 780
sensor = SensorUDP(PORT)


class Game:
    def __init__(self):
        self.street = Street(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.car = Car(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.enemy = Enemy(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.menu = Menu(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.game_state = -1
        self.score = text.Label("Score: 0", x=WINDOW_WIDTH-50, y=WINDOW_HEIGHT-20, anchor_x='center', anchor_y='center')

        # soundtrack from: https://pixabay.com/music/synthwave-digital-love-127441/
        # game over sound from: https://pixabay.com/sound-effects/game-over-arcade-6435/
        self.player = media.Player()
        self.game_over_sound = resource.media('assets/game_over.mp3')
        self.player.queue(resource.media('assets/soundtrack.mp3'))
        self.player.play()

    def draw(self):
        # running
        if self.game_state == 1:
            self.street.draw()
            self.car.draw()
            self.enemy.draw()
        # welcome state
        elif self.game_state == 0:
            self.menu.draw(welcome=False)
        # game over state
        elif self.game_state == -1:
            self.menu.draw(welcome=True)
        self.score.draw()

    def update(self):
        if self.game_state == 1:
            # check if car still on the street
            if self.car.body.x < self.street.street.x or (self.car.body.x + self.car.body.width) > (self.street.street.x + self.street.street.width):
                self.reset_on_game_over()
                return
            # check collision with oncoming cars
            for c, _ in self.enemy.cars:
                if c.x < self.car.body.x + self.car.body.width and c.x + c.width > self.car.body.x and c.y < self.car.body.y + self.car.body.height and c.height + c.y > self.car.body.y:
                    self.reset_on_game_over()
                    return
            # move car and handle speed;
            # player's car is steered by tilting (acc x) and slowed down by pulling (acc z)
            if sensor.has_capability('accelerometer'):
                acc_x = float(sensor.get_value('accelerometer')['x'])
                acc_z = float(sensor.get_value('accelerometer')['z'])
                self.car.update(acc_x)
                self.street.update(acc_z)
                self.enemy.update(acc_z)
        self.score.text = f"Score: {self.enemy.num_enemies_reached_bottom}"

    def reset_on_game_over(self):
        self.player.delete()
        self.player = media.Player()
        self.player.queue(self.game_over_sound)
        self.player.queue(resource.media('assets/soundtrack.mp3'))
        self.player.play()

        self.game_state = 0
        self.car.reset()
        self.enemy.reset()


window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
pyglet.gl.glClearColor(0.1, 0.6, 0.2, 0)
game = Game()


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

