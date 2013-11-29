"""
This file contains classes for constructing objects
through which the controller and controll station will
communicate.

An object will be constructed. Serialized via json,
sent to the partner divce where it can reconstruct it
self.
"""

import json
import joystick 

class RequestShuttle:

  def __init__(self):
    self.joystick_a = None
    self.joystick_b = None
    self.message = None

  def set_joystick_a(self, js):
    self.joystick_a = js

  def set_joystick_b(self, js):
    self.joystick_b = js

  def read_joysticks(self):
    if self.joystick_a:
      self.joystick_a.read()
    if self.joystick_b:
      self.joystick_b.read()

  def set_message(self, message):
    self.message = message

  def serialize(self):
    obj = [None, None, None]
    
    if self.joystick_a:
      obj[0] = self.joystick_a.serialize()
    if self.joystick_b:
      obj[1] = self.joystick_b.serialize()
    obj[2] = self.message
    return obj

  def construct(self, obj):
    if self.joystick_a:
      self.joystick_a.construct(obj[0])
    if self.joystick_b:
      self.joystick_b.construct(obj[1])
    self.message = obj[2]

  def __str__(self):
    return str(self.serialize())

class ResponseShuttle:
  
  def __init__(self):
    self.console = list()
    pass

  def serialize(self):
    obj = [
        self.console,
    ]
    return obj

  def construct(self, obj):
    self.console = obj[0]

  def __str__(self):
    return str(self.serialize())
