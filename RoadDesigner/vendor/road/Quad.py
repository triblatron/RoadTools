try:
    from pyglm import glm
    from . import Vertex
except ImportError:
    import Vertex
from functools import cmp_to_key

class Quad:
    def __init__(self):
        self.verts = []
        self.index = 0

    def configure(self, config):
        if "verts" in config:
            for vertConfig in config["verts"]:
                vert = Vertex.Vertex()
                vert.configure(vertConfig)
                self.verts.append(vert)
        self.sort()

    def sort(self):
        self.verts = sorted(self.verts, key=cmp_to_key(Vertex.Vertex.compare) )

    def addVertex(self, vertex: Vertex.Vertex):
        self.verts.append(vertex)

    def begin(self):
        pass

    def end(self, op=None):
        self.sort()
        s = f"Quad.end():sorted verts now: {self.verts}"
        if op is not None:
            op.report({'INFO'}, s)
        else:
            print(s)

    def vertex(self, x, y, z, u, v):
        self.verts.append(Vertex.Vertex())
        self.verts[-1].position = glm.vec3(x, y, z)
        self.verts[-1].tex_coord = glm.vec2(u, v)

    def width(self):
        return glm.length(self.verts[1].position-self.verts[0].position)

    def length(self):
        return glm.length(self.verts[2].position - self.verts[0].position)

    verts : list[Vertex.Vertex]
