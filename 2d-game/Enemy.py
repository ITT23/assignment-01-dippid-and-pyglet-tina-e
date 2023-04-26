from pyglet import shapes
import random


def get_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


class Enemy:
    def __init__(self, win_w, win_h):
        self.win_w = win_w
        self.win_h = win_h
        self.width = 50
        self.height = 75
        self.min_v = 0.1
        self.random_v = 6
        self.random_y = 3500

        self.cars = []
        x_lane_middle = win_w / 2 - self.width / 2
        x_lane_left = win_w / 6 + win_w / 12
        x_lane_right = win_w - win_w / 3
        self.cars.append((shapes.Rectangle(x=x_lane_left, y=random.randint(self.win_h, self.random_y), width=self.width, height=self.height, color=get_random_color()), random.randint(0, self.random_v)))
        self.cars.append((shapes.Rectangle(x=x_lane_middle, y=random.randint(self.win_h, self.random_y), width=self.width, height=self.height, color=get_random_color()), random.randint(0, self.random_v)))
        self.cars.append((shapes.Rectangle(x=x_lane_right, y=random.randint(self.win_h, self.random_y), width=self.width, height=self.height, color=get_random_color()), random.randint(0, self.random_v)))

        self.num_enemies_reached_bottom = 0

    def update(self, v):
        '''
        move oncoming cars with their specific velocity
        :param v: velocity of the player based on sensor dat
        '''
        for i, car_v_tuple in enumerate(self.cars):
            car = car_v_tuple[0]
            specific_v = car_v_tuple[1]
            if car.y + car.height <= 0:
                self.reset_car(car, i)
                self.num_enemies_reached_bottom += 1
            else:
                # avoid backwards
                if v <= self.min_v:
                    v = self.min_v + (specific_v / 2)
                car.y -= v * 10 + (specific_v / 2)

    def draw(self):
        for car, specific_v in self.cars:
            car.draw()

    def reset(self):
        for i, car_v_tuple in enumerate(self.cars):
            self.reset_car(car_v_tuple[0], i)

    def reset_car(self, car, i):
        '''
        reset a car's position, color and velocity to bring up "new" cars spawning at the top
        :param car: car that collided with bottom
        :param i: index of car in self.cars (left, middle, right)
        '''
        car.color = get_random_color()
        car.y = random.randint(self.win_h, self.random_y)
        self.cars[i] = (car, random.randint(0, self.random_v))

