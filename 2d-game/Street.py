from pyglet import shapes


class Street:
    def __init__(self, win_w, win_h):
        self.win_h = win_h
        self.x = win_w / 6
        self.width = win_w - (1 / 3 * win_w)
        self.min_v = 0.1

        self.street = shapes.Rectangle(x=self.x, y=0, width=self.width, height=win_h, color=(120, 120, 120))
        self.border_l_outer = shapes.Line(x=self.x, y=0, x2=self.x, y2=win_h, width=2, color=(255, 225, 0))
        self.border_l_inner = shapes.Line(x=self.x + 5, y=0, x2=self.x + 5, y2=win_h, width=2, color=(255, 225, 0))
        self.border_r_outer = shapes.Line(x=self.x + self.width, y=0, x2=self.x + self.width, y2=win_h, width=2, color=(255, 225, 0))
        self.border_r_inner = shapes.Line(x=self.x + self.width - 5, y=0, x2=self.x + self.width - 5, y2=win_h, width=2, color=(255, 225, 0))

        self.lanes = []
        space = win_h / 10
        lane_h = (win_h - 4 * space) / 5
        for i in range(5):
            self.lanes.append(shapes.Rectangle(x=self.x + self.width / 3, y=i*lane_h + i*space, width=7, height=lane_h, color=(255, 255, 255)))
            self.lanes.append(shapes.Rectangle(x=self.x + 2 / 3 * self.width, y=i*lane_h + i*space, width=7, height=lane_h, color=(255, 255, 255)))

    def update(self, v):
        '''
        move lanes to create a movement illusion
        :param v: velocity of the player based on sensor data
        '''
        for lane in self.lanes:
            if lane.y + lane.height <= 0:
                lane.y = self.win_h
            else:
                # avoid backwards
                if v <= self.min_v:
                    v = self.min_v
                lane.y -= v * 10

    def draw(self):
        self.street.draw()
        self.border_l_outer.draw()
        self.border_l_inner.draw()
        self.border_r_outer.draw()
        self.border_r_inner.draw()
        for lane in self.lanes:
            lane.draw()
