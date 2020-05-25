class Conn():

    def __init__(self, n1, n2):
        self.n1 = n1 
        self.n2 = n2 

    def __rshift__ (self, other):
        self.n2 >> other

        self.n2 = other
        return self 