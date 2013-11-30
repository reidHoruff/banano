from ..libs.joystick import *
from ..libs.shuttle import *
import zmq

if __name__ == '__main__':
  print "code server is running..."

  #setup connection
  context = zmq.Context()
  socket = context.socket(zmq.REP)
  socket.bind("tcp://*:5555")

  #cerste shuttle and controller
  recieve_shuttle = RequestShuttle()
  recieve_js = XBoxController()
  recieve_shuttle.set_joystick_a(recieve_js)

  while True:
    message = socket.recv()
    recieve_shuttle.construct_from_json(message)
    print recieve_shuttle.joystick_a.get_button(Buttons.A)
    socket.send("");
