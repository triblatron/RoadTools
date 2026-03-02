from pyglm import glm
from Vertex import Vertex

class Quad:
    def __init__(self):
        self.verts = []

    def configure(self, config):
        if "verts" in config:
            for vertConfig in config["verts"]:
                vert = Vertex()
                vert.configure(vertConfig)
                self.verts.append(vert)

    verts : list[Vertex]
