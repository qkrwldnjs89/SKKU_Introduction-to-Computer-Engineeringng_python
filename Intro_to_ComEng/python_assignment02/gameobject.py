from math import atan, sqrt

import pygame
import pygame.sprite
import pygame.transform
from pygame.locals import *

from util import *


class Sprite():
    def __init__(self, image, size=None, update_ms=-1):
        self.size = size
        if size is not None:
            self.image = self.sheet = pygame.transform.scale(pygame.image.load(image), size)
        else:
            # use default size
            self.image = self.sheet = pygame.image.load(image)
        self.frame = 0
        self.update_ms = update_ms
        self.last_tick = 0
        self.clear()

    def clear(self):
        self.update = 0
        self.update_calculated = False

    def get_elapsed_tick(self, tick):
        if self.update_calculated:
            return self.update
        self.update_calculated = True
        self.last_tick += tick
        while self.last_tick >= self.update_ms:
            self.last_tick -= self.update_ms
            self.update += 1
        return self.update

    def sprite_update(self, *args, **kwargs):
        pass


class GameObject(Sprite):
    @staticmethod
    def dist_sq(this, other):
        # 피타고라스 정의
        return sqrt((this.pos[0] - other.pos[0]) ** 2 + (this.pos[1] - other.pos[1]) ** 2)

    @staticmethod
    def collide(this, other, r=None):
        # 두점 사이의 거리 비교
        dist = this.radius + other.radius
        if dist > GameObject.dist_sq(this, other):
            return True
        return False
        # Return True when this and other collide. Otherwise, return False

    def __init__(self, image, size,
                 update_ms=-1, pos=(0, 0), velocity=(0, 0), acceleration=(0, 0)):
        super().__init__(image, size, update_ms)
        self.pos = list(pos)
        self.velocity = list(velocity)
        self.acceleration = list(acceleration)

        if size is not None:
            self.radius = sqrt(size[0] * size[0] + size[1] * size[1]) // 2
        else:
            self.radius = 50

        self._last_angle = 0

    def get_angle(self):
        self._last_angle = -(180 * atan(self.velocity[1] / (1e-10 + self.velocity[0]))) / PI
        flip = False

        if self.velocity[0] < 0:
            flip = True

        return self._last_angle, flip

    def get_pos(self):
        if self.size is not None:
            return [int(x) - (y // 2) for (x, y) in zip(self.pos, self.size)]

    def _sprite_update(self, *args, **kwargs):
        angle, flip = self.get_angle()
        if flip:
            self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.rotate(self.image, self._last_angle)

    def location_update(self, *args, **kwargs):
        self.pos[0] += self.velocity[0] * 10
        self.pos[1] += self.velocity[1] * 10
        if self.pos[0] >= int(WIDTH):
            self.pos[0] = int(WIDTH)
        if self.pos[0] <= 0:
            self.pos[0] = 0

        if self.pos[1] >= int(HEIGHT):
            self.pos[1] = int(HEIGHT)
        if self.pos[1] <= 0:
            self.pos[1] = 0


class Marisa(GameObject):
    def __init__(self, image, size, update_ms, pos=(0, 0), velocity=(0.5, 0), acceleration=(0, 0)):
        super().__init__(image, size, update_ms, pos, velocity, acceleration)
        self.size = [125, 70]
        self.normal_sprite = [pygame.Rect(8 + x * 125, 320, 125, 70) for x in range(6)]
        self.kurkuru_sprite = [pygame.Rect(8 + x * 125, 190, 125, 70) for x in range(8)]

        self.sprite_len = 6
        self.sprite_update(first=True)
        self._fever_timer = 0

    def keyEventHandle(self, keyEvents, elapsed_ms):
        update = self.get_elapsed_tick(elapsed_ms)

        # Modify this appropriately.
        if update > 0:
            if keyEvents.up is True:
                # self.velocity = angular_tranform(ANGLE_UPDATE,  self.velocity)
                pass
            if keyEvents.down is True:
                # self.velocity = angular_tranform(ANGLE_UPDATE,  self.velocity)
                pass
            if keyEvents.left is True:
                self.velocity = angular_tranform(ANGLE_UPDATE * -1,  self.velocity)
            if keyEvents.right is True:
                self.velocity = angular_tranform(ANGLE_UPDATE,  self.velocity)

        if self._fever_timer > 0:
            self._fever_timer -= elapsed_ms
            if self._fever_timer < 0:
                self.fever_down()
                self._fever_timer = 0

    def get_apple(self):
        self.velocity = [x * 1.1 for x in self.velocity]
        self.fever_on()

    def fever_on(self):
        if self._fever_timer == 0:
            self.velocity = [x * FEVER_ for x in self.velocity]
        self._fever_timer = FEVER_TIMER

    def fever_down(self):
        self.velocity = [(x / FEVER_) for x in self.velocity]

    def sprite_update(self, *args, **kwargs):

        if kwargs.get('first', False):
            self.sheet.set_clip(self.normal_sprite[0])
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            return

        update = self.get_elapsed_tick(kwargs.get('elapsed_ms', 0))


        for x in range(update):
            self.frame += 1
            if self._fever_timer > 0:
                self.frame %= 8
                self.sheet.set_clip(self.kurkuru_sprite[self.frame])
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self._sprite_update(*args, **kwargs)
            else:
                self.frame %= 6
                self.sheet.set_clip(self.normal_sprite[self.frame])
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self._sprite_update(*args, **kwargs)
