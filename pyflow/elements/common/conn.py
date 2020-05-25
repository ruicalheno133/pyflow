class Conn():

    def __init__(self, start, end):
        self._start = start 
        self._end = end 

    def __rshift__ (self, other):
        self.end >> other

        self.end = other
        return self 

    @property
    def start(self):
        return self._start 

    @start.setter 
    def start (self, start):
        self._start = start

    @property
    def end(self):
        return self._end 

    @end.setter 
    def end (self, end):
        self._end = end