from pyglet import text, media, resource
from Car import Car
from Street import Street
from Menu import Menu
from Enemy import Enemy


class Game:
    def __init__(self, sensor, window_width, window_height):
        self.sensor = sensor
        self.street = Street(window_width, window_height)
        self.car = Car(window_width, window_height)
        self.enemy = Enemy(window_width, window_height)
        self.menu = Menu(window_width, window_height)
        self.score = text.Label("Score: 0", x=window_width-50, y=window_height-20, anchor_x='center', anchor_y='center')
        self.game_state = -1
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
            if self.sensor.has_capability('accelerometer'):
                acc_x = float(self.sensor.get_value('accelerometer')['x'])
                acc_z = float(self.sensor.get_value('accelerometer')['z'])
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
