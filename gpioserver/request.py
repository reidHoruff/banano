import zmq

class GPIOClient:
  def __init__(self):
    print "connecting to GPIO server..."
    context = zmq.Context() 
    self.socket = context.socket(zmq.REQ)
    self.socket.connect("tcp://localhost:5555")

  def request(self):
    print "requesting to gpio server"
    self.socket.send("hello from GPIO Client")
    response = self.socket.recv()
    print "response from gpio server: %s" % response


if __name__ == '__main__':
  c = GPIOClient()
  for x in range(10):
    c.request()
