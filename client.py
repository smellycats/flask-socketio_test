from socketIO_client import SocketIO, BaseNamespace

def on_response(*args):
    print('on_response', args)

print 'test'
socket = SocketIO('localhost', 5000)
chat = socket.define(BaseNamespace, '/test')
print 'test1'
chat.emit('my event')
chat.on('my response', on_response)

##from socketIO_client import SocketIO, BaseNamespace
##
##class Namespace(BaseNamespace):
##
##    def on_connect(self):
##        print '[Connected]'
##
##socketIO = SocketIO('localhost', 8000, Namespace)
##socketIO.wait(seconds=1)
