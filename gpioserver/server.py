
"""
This is a zmq server that controlls the gpios via socket requests
"""

import time
import threading
import zmq

try:
  import RPi.GPIO as GPIO
except RuntimeError:
  print "error importing RPi.GPIO. Try running as root."


GPIO.setmode(GPIO.BCM)

for x in [4]:
  GPIO.setup(x, GPIO.OUT)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print "server is running..."

while True:
  message = socket.recv()
  data = message.split(':')
  port = int(data[0])
  value = bool(data[1])
  print "%s %s" % (port, value)

  socket.send("request was recieved")




