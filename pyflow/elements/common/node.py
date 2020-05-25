from pyflow.elements.common.conn import Conn

class Node ():

    def __init__(self, id, diagram):
        self._id = id
        self._incoming = []
        self._outgoing = []
        self._diagram = diagram

    @property
    def id(self):
        return self._id 

    @id.setter 
    def id (self, id):
        self._id = id

    @property
    def incoming(self):
        return self._incoming 

    @incoming.setter 
    def incoming (self, incoming):
        self._incoming = incoming

    @property
    def outgoing(self):
        return self._outgoing 

    @outgoing.setter 
    def outgoing (self, outgoing):
        self._outgoing = outgoing

    @property
    def diagram(self):
        return self._diagram 

    @diagram.setter 
    def diagram (self, diagram):
        self._diagram = diagram

    def add_incoming(self, incoming):
        self._incoming.append(incoming) 

    def add_outgoing(self, outgoing):
        self._outgoing.append(outgoing)

    def __rshift__ (self, other):
        if isinstance(other, list):
            self._diagram.connect_multiple(self, other)
        else:
            self._diagram.connect(self, other)

        return Conn(self, other)

    def __lshift__ (self, other):
        if isinstance(other, list):
            self._diagram.connect_multiple(self, other, diverge=False)
        else:
            pass 

        return Conn(other, self)

    def __rrshift__(self, other):
        self.__lshift__(other)

        return self

    def __rlshift__(self, other):
        self.__rshift__(other)

        return self
    