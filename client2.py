from socketIO_client import SocketIO, LoggingNamespace

def on_bbb_response(*args):
    print('on_bbb_response', args)

with SocketIO('localhost', 5000, LoggingNamespace) as socketIO:
    socketIO.emit('my event', {'data': 'yyy'}, on_bbb_response)
    socketIO.wait_for_callbacks(seconds=1)
