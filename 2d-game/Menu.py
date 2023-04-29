from pyglet import shapes, text


class Menu:
    def __init__(self, win_w, win_h):
        self.background = shapes.Rectangle(x=0, y=0, width=win_w, height=win_h, color=(156, 0, 75))
        self.welcome = text.Label('WELCOME!', font_size=40, x=win_w/2, y=win_h - 200, anchor_x='center', anchor_y='center')
        self.game_over = text.Label('GAME OVER!', font_size=40, x=win_w/2, y=win_h - 200, anchor_x='center', anchor_y='center')

        self.instructions_start = text.Label('Start: SPACE', x=win_w/2, y=win_h / 1.8, anchor_x='center', anchor_y='center')
        self.instructions_exit = text.Label('Exit: Q', x=win_w/2, y=win_h / 1.8 - 30, anchor_x='center', anchor_y='center')

        self.instructions_controls_tilt = text.Label('Tilt the phone to steer your car.', x=win_w/2, y=win_h/5, anchor_x='center', anchor_y='center')
        self.instructions_controls_pull = text.Label('Pull the phone towards you to slow down.', x=win_w/2, y=win_h/6, anchor_x='center', anchor_y='center')

    def draw(self, welcome):
        self.background.draw()
        if welcome:
            self.welcome.draw()
        else:
            self.game_over.draw()
        self.instructions_start.draw()
        self.instructions_exit.draw()
        self.instructions_controls_tilt.draw()
        self.instructions_controls_pull.draw()
