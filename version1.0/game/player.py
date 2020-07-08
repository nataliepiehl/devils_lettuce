import math
from pyglet.window import key
from . import resources, physicalobject

class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.player_image, *args, **kwargs)
        self.keys = dict(left=False, right=False, up=False, down=False)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = True
        elif symbol == key.DOWN:
            self.keys['down'] = True
        elif symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.DOWN:
            self.keys['down'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False

    def update(self, dt):
        super(Player, self).update(dt)

        # 200 thrust in x direction
        if self.keys['left']:
            self.velocity_x = -200
        elif self.keys['right']:
            self.velocity_x = 200
        else:
            self.velocity_x = 0

        # 150 thrust in y direction
        if self.keys['up']:
            self.velocity_y = 150
        elif self.keys['down']:
            self.velocity_y = -150
        else:
            self.velocity_y = 0

        super(Player, self).check_bounds()
