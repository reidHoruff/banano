
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

for x in range(8):
  GPIO.setup(x, GPIO.OUT)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print "server is running..."

while True:
  message = socket.recv()
  print "recieve %s" % message
  socket.send("request was recieved")




