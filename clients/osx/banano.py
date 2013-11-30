import pygame
import time
import zmq
from ...libs.joystick import *
from ...libs.shuttle import *

if __name__ == '__main__':
  print "Banano for OSX"
  context = zmq.Context() 
  socket = context.socket(zmq.REQ)
  #socket.connect("tcp://192.168.2.8:5555")
  socket.connect("tcp://localhost:5555")

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

    print "sending..."
    socket.send(request_shuttle.serialize_json())
    response = socket.recv()
    print "response:", response

    time.sleep(1.0/30.0)
