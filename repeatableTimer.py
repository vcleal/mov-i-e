from threading import Timer

class RepeatableTimer(object):
    def __init__(self, interval, function, args=[], kwargs={}):
        self._interval = interval
        self._function = function
        self._args = args
        self._kwargs = kwargs
        self.t = None
    def start(self):
        self.t = Timer(self._interval, self._function, *self._args, **self._kwargs)
        self.t.start()
    def cancel(self):
        if self.t is not None:
            self.t.cancel()