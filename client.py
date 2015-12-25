from socketIO_client import SocketIO, BaseNamespace

class TestNamespace(BaseNamespace):
    def on_response(*args):
        print('on_response', args)


socket = SocketIO('10.0.0.7', 5000)
socket.emit('my event', {'data': 'I\'m connected.'})

##from socketIO_client import SocketIO, BaseNamespace
##
##class Namespace(BaseNamespace):
##
##    def on_connect(self):
##        print '[Connected]'
##
##socketIO = SocketIO('localhost', 8000, Namespace)
##socketIO.wait(seconds=1)
