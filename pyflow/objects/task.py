class Task ():
    
    # TODO: add suitable constructors
    def __init__(self, name, diagram):
        self._id = name
        self._name = name
        self._diagram = diagram
        self._isForCompensation = False 
        self._startQuantity = 1 
        self._completionQuantity = 1 
        self._default = None 
        self._incoming = [] 
        self._outgoing = []

    def add_incoming(self, task):
        self._incoming.append(task)

    def add_outgoing(self, task):
        self._outgoing.append(task) 

    def __repr__(self):
        return self._name

    def __rshift__ (self, other):
        if isinstance(other, list):
            pass #TODO: support for parallel gateways
        elif isinstance(other, tuple):
            self._diagram.connect_exclusive_diverge(self, other)
        else:
            self._diagram.connect(self, other)

        return other

    def __lshift__ (self, other):
        if isinstance(other, list):
            pass #TODO: support for parallel gateways
        elif isinstance(other, tuple):
            self._diagram.connect_exclusive_converge(self, other)
        else:
            pass 

        return other

    def __rrshift__(self, other):
        self.__lshift__(other)

        return self

    def __rlshift__(self, other):
        self.__rshift__(other)

        return self