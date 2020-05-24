class ExclusiveGateway ():
    _converge_id = 0
    _diverge_id = 0

    @classmethod
    def generate_diverge_id(cls):
        return "gt_diverge_{}".format(cls._diverge_id)

    @classmethod
    def generate_converge_id(cls):
        return "gt_converge_{}".format(cls._converge_id)

    @classmethod
    def generate_id(cls, diverge: bool):
        return cls.generate_diverge_id() if diverge else cls.generate_converge_id()

    def __init__(self, id=None, diverge=True):
        self._id = id if id else ExclusiveGateway.generate_id(diverge)
        self._name = "+"
        self._gatewayDirection = "Diverging" if diverge else "Converging"
        self._incoming = []
        self._outgoing = []