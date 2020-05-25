# Pyflow

Build BPMN diagrams using _airflow DAG-like_ syntax. 

## Usage

#### BPMN 

```python
from pyflow.diagrams.bpmn import BPMNDiagram
from pyflow.elements.bpmn.task import Task
from pyflow.elements.bpmn.exclusive_gateway import ExclusiveGateway
from pyflow.elements.bpmn.parallel_gateway import ParallelGateway

# Diagram
bpmn = BPMNDiagram("bpmn1")

# Tasks must be assigned to a BPMNDiagram
a1 = Task("a1",bpmn)
a2 = Task("a2",bpmn)
a3 = Task("a3",bpmn)

# Gateways must be assigned to a BPMNDiagram
pgt_div = ParallelGateway(bpmn,id="pgt_div")
pgt_conv = ParallelGateway(bpmn,id="pgt_conv",diverge=False)

# Build diagram as a networkx graph
a1 >> pgt_div >> [a2, a3] >> pgt_conv
```

