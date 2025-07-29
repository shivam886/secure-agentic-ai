# threat_detection/attack_graph.py

import networkx as nx
from stix2 import FileSystemSource, Filter

class AttackGraph:
    """
    Builds a directed graph of intrusion-sets and techniques,
    allows shortest-path queries via Dijkstra’s algorithm.
    """
    def __init__(self, cti_path="cti/enterprise-attack"):
        self.fs = FileSystemSource(cti_path)
        self.graph = nx.DiGraph()
        self._build_graph()

    def _build_graph(self):
        for ins in self.fs.query([Filter("type","=","intrusion-set")]):
            self.graph.add_node(ins.id, name=ins.name, type="intrusion-set")
        for tech in self.fs.query([Filter("type","=","attack-pattern")]):
            self.graph.add_node(tech.id, name=tech.name, type="attack-pattern")
        for r in self.fs.query([Filter("type","=","relationship")]):
            if r.relationship_type == "uses":
                self.graph.add_edge(r.source_ref, r.target_ref)

    def find_shortest_path(self, src, tgt):
        return nx.dijkstra_path(self.graph, source=src, target=tgt)

    def get_node_name(self, nid):
        return self.graph.nodes[nid].get("name", nid)
