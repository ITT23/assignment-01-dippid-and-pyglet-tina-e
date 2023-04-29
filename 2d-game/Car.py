from pyglet import shapes


class Car:
    def __init__(self, win_w, win_h):
        self.win_w = win_w
        self.width = 50
        self.height = 75
        self.body = shapes.BorderedRectangle(x=win_w / 2, y=win_h / 5, width=self.width, height=self.height, color=(156, 0, 75), border=3, border_color=(0, 0, 0))

    def update(self, movement):
        """
        move the player's car; *(-10) to adjust sensitivity
        :param movement: movement (x) of the player based on sensor dat
        """
        self.body.x += movement * (-10)

    def draw(self):
        self.body.draw()

    def reset(self):
        self.body.x = self.win_w / 2
