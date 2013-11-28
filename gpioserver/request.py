import zmq

class GPIOClient:
  def __init__(self):
    print "connecting to GPIO server..."
    context = zmq.Context() 
    self.socket = context.socket(zmq.REQ)
    self.socket.connect("tcp://192.168.2.8:5555")

  def request(self, port, value):
    data = "%s:%s" % (int(port), int(value))
    print "making request..."
    self.socket.send(data)
    response = self.socket.recv()
    print "recieved response %s" % response

if __name__ == '__main__':
  foo = 0
  value = True
  c = GPIOClient()
  while True:
    raw_input()
    print foo
    c.request(4, value)
    value = not value
    foo += 1
