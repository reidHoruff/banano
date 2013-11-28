import zmq

class GPIOClient:
  def __init__(self):
    print "connecting to GPIO server..."
    context = zmq.Context() 
    self.socket = context.socket(zmq.REQ)
    self.socket.connect("tcp://192.168.2.8:5555")

  def request(self, port, value):
    data = "%s:%s" % (int(port), int(value))
    self.socket.send(data)
    response = self.socket.recv()

if __name__ == '__main__':
  value = True
  c = GPIOClient()
  while True:
    c.request(4, value)
    value = not value
