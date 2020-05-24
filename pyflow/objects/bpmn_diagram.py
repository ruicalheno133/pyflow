import networkx as nx
from .sequence_flow import SequenceFlow
from .task import Task

class BPMNDiagram ():

    def add_sequence_flow(self, sf: SequenceFlow):
        self.graph.add_edge(sf.sourceRef, sf.targetRef)

    def add_task(self, task: Task):
        self.graph.add_node(task._name)
        self.tasks.append(task)

    def add_gateway(self, gateway):
        self.graph.add_node(gateway.name)

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