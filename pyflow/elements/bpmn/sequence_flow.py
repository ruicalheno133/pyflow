class SequenceFlow ():
    _gen_id = 0

    @classmethod
    def generate_id(cls):
        gen_id = "gt_converge_{}".format(cls._gen_id)
        cls._gen_id += 1 
        return gen_id

    def __init__(self, source, target, id=None):
        self.id = id if id else SequenceFlow.generate_id()
        self.sourceRef = source._id 
        self.targetRef = target._id

    @property
    def id(self):
        return self._id 

    @id.setter 
    def id (self, id):
        self._id = id

    @property
    def sourceRef(self):
        return self._sourceRef 

    @sourceRef.setter 
    def sourceRef (self, sourceRef):
        self._sourceRef = sourceRef

    @property
    def targetRef(self):
        return self._targetRef 

    @targetRef.setter 
    def targetRef (self, targetRef):
        self._targetRef = targetRef