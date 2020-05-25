import networkx as nx
from pyflow.elements.bpmn.sequence_flow import SequenceFlow
from pyflow.elements.bpmn.exclusive_gateway import ExclusiveGateway
from pyflow.elements.bpmn.parallel_gateway import ParallelGateway
from pyflow.elements.bpmn.task import Task
from pyflow.elements.common.node import Node
from pyflow.utils import bpmn as bpmn_utils

class BPMNDiagram ():

    def add_sequence_flow(self, sf: SequenceFlow):
        self.graph.add_edge(sf.sourceRef, sf.targetRef)

    def update_node_outgoing(self, node: Node, outgoing: Node):
        node.add_outgoing(outgoing)
        task_attr = bpmn_utils.dict_from_task(node)
        self.graph.nodes[node.id].update(task_attr)

    def update_node_incoming(self, node: Node, incoming: Node):
        node.add_incoming(incoming)
        task_attr = bpmn_utils.dict_from_task(node)
        self.graph.nodes[node.id].update(task_attr)

    def add_task(self, task: Task):
   
        if task._id not in self.graph.nodes:
            task_attr = bpmn_utils.dict_from_task(task)
            self.graph.add_node(task._id, **task_attr)
            self.tasks.append(task)

    def add_gateway(self, gateway):
        self.graph.add_node(gateway._id)

    def connect_multiple(self, node: ExclusiveGateway, node_list: list, diverge: bool =True):
        '''
            Connects a gateway object to multiple nodes. 
            Can be diverging (from gateway to nodes) or converging (from nodes to gateway)
        '''
        for n in node_list:
            if isinstance(n, Node):
                self.connect(node, n) if diverge else self.connect(n, node)
            else:
                self.connect(node, n.n1) if diverge else self.connect(n.n2, node)

    def connect(self, task1: Node, task2: Node):
        '''
            Connects one Node to another. 
            Generates a random sequence flow.
        '''
        sf = SequenceFlow(task1, task2)

        self.add_task(task1)
        self.add_task(task2) 

        self.update_node_outgoing(task1, task2)
        self.update_node_incoming(task2, task1)
        
        self.add_sequence_flow(sf)

    def __init__(self, name: str):
        self.name = name 
        self.graph = nx.DiGraph()
        self.tasks = []

    def view(self):
        bpmn_utils.view(self)