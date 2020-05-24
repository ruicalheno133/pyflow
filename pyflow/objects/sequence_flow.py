class SequenceFlow ():

    def __init__(self, source, target, id=None):
        self.id = id if id else "ola"
        self.sourceRef = source._id 
        self.targetRef = target._id