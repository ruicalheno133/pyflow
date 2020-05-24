import networkx as nx
from .sequence_flow import SequenceFlow
from .exclusive_gateway import ExclusiveGateway
from .task import Task

class BPMNDiagram ():

    def add_sequence_flow(self, sf: SequenceFlow):
        self.graph.add_edge(sf.sourceRef, sf.targetRef)

    def add_task(self, task: Task):
        if task._id not in self.graph.nodes:
            self.graph.add_node(task._id)
            self.tasks.append(task)

    def add_gateway(self, gateway):
        self.graph.add_node(gateway._id)

    def connect_exclusive_converge(self, task2: Task, task_list: list):
        gt = ExclusiveGateway(diverge=False)
        sf = SequenceFlow(gt, task2)
        self.add_task(task2)
        self.add_gateway(gt) 

        task2.add_incoming(gt)

        self.add_sequence_flow(sf)

        for task in task_list:
            sf = SequenceFlow(task, gt)

            self.add_task(task)

            task.add_outgoing(gt)

            self.add_sequence_flow(sf)

    def connect_exclusive_diverge(self, task1: Task, task_list: list):
        gt = ExclusiveGateway()
        sf = SequenceFlow(task1, gt)

        self.add_task(task1)
        self.add_gateway(gt) 

        task1.add_outgoing(gt)

        self.add_sequence_flow(sf)

        for task in task_list:
            sf = SequenceFlow(gt, task)

            self.add_task(task)

            task.add_incoming(gt)

            self.add_sequence_flow(sf)

    def connect(self, task1: Task, task2: Task):
        sf = SequenceFlow(task1, task2)

        self.add_task(task1)
        self.add_task(task2) 

        task1.add_outgoing(task2) 
        task2.add_incoming(task1)
        
        self.add_sequence_flow(sf)

    def __init__(self, name: str):
        self.name = name 
        self.graph = nx.DiGraph()
        self.tasks = []