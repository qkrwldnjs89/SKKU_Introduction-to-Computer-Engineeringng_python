import os
import random
from math import cos, sin
from types import SimpleNamespace

GAMETITLE = "Marisachan Ganbatte!"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PI = 3.141592
WIDTH = 1024
HEIGHT = 768
NUM_APPLE = 3
NUM_MUSHROOM = 2
ANGLE_UPDATE = 15
FEVER_ = 2.0
FEVER_TIMER = 1500
RESOURCE_FOLDER = "resources"
BG_PATH = os.path.join(RESOURCE_FOLDER, "background.png")
MARISA_PATH = os.path.join(RESOURCE_FOLDER, "marisa.png")
APPLE_PATH = os.path.join(RESOURCE_FOLDER, "apple.png")
MUSHROOM_PATH = os.path.join(RESOURCE_FOLDER, "mushroom.png")
BGM_PATH = os.path.join(RESOURCE_FOLDER, "melody.wav")


def KeyEvents():
    return SimpleNamespace(up=False, down=False, left=False, right=False)


def angular_tranform(angle, arr):
    angle = PI * (angle / 180)
    return [cos(angle) * arr[0] - sin(angle) * arr[1], sin(angle) * arr[0] + cos(angle) * arr[1]]


def add2d(x, y):
    return [x[0] + y[0], x[1] + y[1]]


def get_rand_pos(sz, obj_size):
    x = random.randint(0, sz[0] - obj_size[0] + 1)
    y = random.randint(0, sz[1] - obj_size[1] + 1)
    return [x, y]
