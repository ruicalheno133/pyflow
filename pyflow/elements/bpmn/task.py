from pyflow.elements.common.node import Node

class Task (Node):
    
    # TODO: add suitable constructors
    def __init__(self, name, diagram):
        super().__init__(name, diagram)
        self._isForCompensation = False 
        self._startQuantity = 1 
        self._completionQuantity = 1 
        self._default = None 

    def __repr__(self):
        return self._id