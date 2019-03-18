from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Graph:
    graph: dict
    vertices: int

    def __init__(self, vert):
        self.graph = defaultdict(list)
        self.vertices = vert
