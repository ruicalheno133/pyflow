from pyflow.elements.common.node import Node

class Task (Node):
    
    # TODO: add suitable constructors
    def __init__(self, name, diagram):
        super().__init__(name, diagram)
        self._isForCompensation = False 
        self._startQuantity = 1 
        self._completionQuantity = 1 
        self._default = None 

    @property
    def isForCompensation(self):
        return self._isForCompensation 

    @isForCompensation.setter 
    def isForCompensation (self, isForCompensation):
        self._isForCompensation = isForCompensation

    @property
    def startQuantity(self):
        return self._startQuantity 

    @startQuantity.setter 
    def startQuantity (self, startQuantity):
        self._startQuantity = startQuantity

    @property
    def completionQuantity(self):
        return self._completionQuantity 

    @completionQuantity.setter 
    def completionQuantity (self, completionQuantity):
        self._completionQuantity = completionQuantity

    @property
    def default(self):
        return self._default 

    @default.setter 
    def default (self, default):
        self._default = default

    def __repr__(self):
        return self._id