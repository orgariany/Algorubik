from pprint import pprint
from copy import deepcopy as dc

UPPER_SIDE = 0
LEFT_SIDE = 1
RIGHT_SIDE = 2
FRONT_SIDE = 3
BACK_SIDE = 4
BOTTOM_SIDE = 5


class RubiksCube(object):
    def __init__(self):
        self.size = 3
        self.generate_cube()

    def scramble(self):
        pass

    def generate_cube(self):
        self.grid = [None] * 6
        self.grid[UPPER_SIDE] = [['yellow'] * self.size] * self.size
        self.grid[BOTTOM_SIDE] = [['white'] * self.size] * self.size
        self.grid[LEFT_SIDE] = [['green'] * self.size] * self.size
        self.grid[RIGHT_SIDE] = [['blue'] * self.size] * self.size
        self.grid[FRONT_SIDE] = [['red'] * self.size] * self.size
        self.grid[BACK_SIDE] = [['orange'] * self.size] * self.size

    def turn_front(self):
        original_state = dc(self.grid)
        # self.rotate_side_clockwise(FRONT_SIDE)
        self.grid[UPPER_SIDE][2][0] = original_state[LEFT_SIDE][2][2]
        self.grid[UPPER_SIDE][2][1] = original_state[LEFT_SIDE][1][2]
        self.grid[UPPER_SIDE][2][2] = original_state[LEFT_SIDE][0][2]

        # self.grid[RIGHT_SIDE][0][0] = original_state[UPPER_SIDE][2][0]
        # self.grid[RIGHT_SIDE][1][0] = original_state[UPPER_SIDE][2][1]
        # self.grid[RIGHT_SIDE][2][0] = original_state[UPPER_SIDE][2][2]

        # self.grid[BOTTOM_SIDE][0][0] = original_state[RIGHT_SIDE][0][0]
        # self.grid[BOTTOM_SIDE][0][1] = original_state[RIGHT_SIDE][1][0]
        # self.grid[BOTTOM_SIDE][0][2] = original_state[RIGHT_SIDE][2][0]

        # self.grid[RIGHT_SIDE][0][2] = original_state[BOTTOM_SIDE][0][0]
        # self.grid[RIGHT_SIDE][1][2] = original_state[BOTTOM_SIDE][0][1]
        # self.grid[RIGHT_SIDE][2][2] = original_state[BOTTOM_SIDE][0][2]

    def turn_back(self):
        self.rotate_side_clockwise(BACK_SIDE)

    def turn_right(self):
        self.rotate_side_clockwise(RIGHT_SIDE)

    def turn_left(self):
        self.rotate_side_clockwise(LEFT_SIDE)

    def turn_up(self):
        self.rotate_side_clockwise(UPPER_SIDE)

    def turn_bottom(self):
        self.rotate_side_clockwise(BOTTOM_SIDE)

    def rotate_side_clockwise(self, side):
        original_state = dc(self.grid)
        self.grid[side][0][0] = original_state[1][0]
        self.grid[side][0][1] = original_state[0][0]
        self.grid[side][0][2] = original_state[0][1]
        self.grid[side][1][0] = original_state[2][0]
        self.grid[side][1][2] = original_state[0][2]
        self.grid[side][2][0] = original_state[2][1]
        self.grid[side][2][1] = original_state[2][2]
        self.grid[side][2][2] = original_state[1][2]


r = RubiksCube()
r.turn_front()
pprint(r.grid)