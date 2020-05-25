from copy import deepcopy
import tempfile
from PIL import Image
import networkx as nx

def dict_from_task(task):
    final_dct = {}
    dct = deepcopy(vars(task))

    for k, v in dct.items():
        final_dct[k[1:]] = v

    del final_dct['diagram']
    
    return final_dct

def view(bpmn):
    dot = nx.nx_pydot.to_pydot(bpmn.graph)
    dot.set_rankdir("LR")

    f = tempfile.NamedTemporaryFile()
 
    dot.write_png(f.name)
    
    img = Image.open(f.name)
    img.show()