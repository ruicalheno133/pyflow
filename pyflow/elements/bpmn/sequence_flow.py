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