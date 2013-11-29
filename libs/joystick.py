import pygame
from shuttle import *


"""
This file contains classes for 'encoding' joystick input
on the control station and then later 'decoding' them on the 
device. The control station will use gamepy to read joysticks. Different versions
of gamepy and possibly other factors seem to map joysticks differently.
It will be up to the 'encoder' on the control station to wrap up 'convert' these
differences and make sure that the control device is recieving a standard control mapping.
"""

class BnoJoystick:
  def __init__(self):
    self.id = None
    self.name = None
    self.buttons = None
    self.axes = None
    self.hats = None

  def construct(self, obj):
    self.id = obj['id']
    self.name = obj['name']
    self.buttons = obj['buttons']
    self.axes = obj['axes']
    self.hats = obj['hats']

  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'buttons': self.buttons,
      'axes': self.axes,
      'hats': self.hats,
    }

  def __str__(self):
    return str(self.serialize())

"""
OSX with pygame 1.9.2pre
hats are shown as buttons [0..4]
"""
class BnoJoystickReader(BnoJoystick):
  def __init__(self, pg_joystick):
    BnoJoystick.__init__(self)

    self.pg_joystick = pg_joystick
    self.pg_joystick.init()

    self.id = self.pg_joystick.get_id()
    self.name = self.pg_joystick.get_name()

    self.num_axis = self.pg_joystick.get_numaxes()
    self.num_buttons = self.pg_joystick.get_numbuttons()
    self.num_hats = self.pg_joystick.get_numhats()

  def read(self):
    self.axes = self.dump_axes()
    self.buttons = self.dump_buttons()
    self.hats = self.dump_hats()

  def axis(self, index):
    return self.pg_joystick.get_axis(index)

  def button(self, index):
    return self.pg_joystick.get_button(index)

  def hat(self, index):
    return self.pg_joystick.get_hat(index)

  def dump_axes(self):
    return [self.axis(i) for i in range(self.num_axis)]

  def dump_buttons(self):
    return [self.button(i) for i in range(self.num_buttons)]

  def dump_hats(self):
    return [self.hat(i) for i in range(self.num_hats)]


class Buttons:
  X = 0
  Y = 1
  A = 2
  B = 3
  LEFT = 4
  RIGHT = 5
  UP = 6
  DOWN = 7
  LEFT_PADDLE = 8
  RIGHT_PADDLE = 9
  BACK = 10
  START = 11
  XBOX_CENTER = 12
  LEFT_DPAD_UP = 13
  LEFT_DPAD_DOWN = 14
  LEFT_DPAD_LEFT = 15
  LEFT_DPAD_RIGHT = 16

class Axis:
  X = 0
  Y = 1
  LEFT = 2
  RIGHT = 3
  LEFT_X = 4
  RIGHT_X = 5
  LEFT_Y = 6
  RIGHT_Y = 7

class XBoxController(BnoJoystick):
  """
  these are the mappings that the controller will expect for an
  xbox controller. It is up to the control station to make sure
  that these mappings are correct. See above class
  """
  BUTTON_MAP = {
    Buttons.LEFT_DPAD_UP: 0,
    Buttons.LEFT_DPAD_DOWN: 1,
    Buttons.LEFT_DPAD_LEFT: 2,
    Buttons.LEFT_DPAD_RIGHT: 3,
    Buttons.START: 4,
    Buttons.BACK: 5,
    Buttons.RIGHT_PADDLE: 9,
    Buttons.LEFT_PADDLE: 8,
    Buttons.XBOX_CENTER: 10,
    Buttons.A: 11,
    Buttons.B: 12,
    Buttons.X: 13,
    Buttons.Y: 14,
  }

  def __init__(self):
    BnoJoystick.__init__(self)

  def get_left_js(self):
    x = self.axes[0]
    y = self.axes[1]
    return x, y

  def get_right_js(self):
    x = self.axes[2]
    y = self.axes[3]
    return x, y

  def get_trigger(self):
    x = self.axes[4]
    y = self.axes[5]
    return x, y

  def get_button(self, button):
    if button in self.BUTTON_MAP:
      return bool(self.buttons[self.BUTTON_MAP[button]])
    else:
      return None

  def __str__(self):
    s = ''
    s += 'left js: %s' % str(self.get_left_js())
    s += '\n'
    s += 'right js: %s' % str(self.get_right_js())
    s += '\n'
    s += 'trigger: %s' % str(self.get_trigger())
    s += '\n'
    s += str(self.buttons)
    s += '\n'
    s += str(self.get_button(Buttons.A))
    s += '\n'
    s += str(self.id)
    return s

if __name__ == '__main__':
  clock = pygame.time.Clock()
  pygame.init()
  pygame.joystick.init()

  joystick_count = pygame.joystick.get_count()

  print "Number of joysticks: %s" % (joystick_count,)

  joysticks = [BnoJoystickReader(pygame.joystick.Joystick(i)) for i in range(joystick_count)]

  request_js = joysticks[0]
  request_shuttle = RequestShuttle()
  request_shuttle.set_joystick_a(request_js)

  recieve_js = XBoxController()
  recieve_shuttle = RequestShuttle()
  recieve_shuttle.set_joystick_a(recieve_js)

  done = False
  while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
    
    request_shuttle.read_joysticks()
    obj = request_shuttle.serialize()

    recieve_shuttle.construct(obj)
    print recieve_shuttle.joystick_a




