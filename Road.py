from enum import Enum

from Quad import Quad
from Segment import Segment
from pyglm import glm

from Vertex import Vertex


class RoadType(Enum):
    STRAIGHT = 0
    ARC=1,
    CLOTHOID=2

class Road:
    def __init__(self):
        self.meshes = []

    def configure(self, config: dict):
        if "meshes" in config:
            for meshConfig in config["meshes"]:
                self.beginProfile()
                self.meshes[-1].configure(meshConfig)
                self.endProfile()

    def beginProfile(self):
        self.inMesh = True
        self.meshes.append(Quad())
        self.meshes[-1].begin()

    def vertex(self, x, y, z, u, v):
        if self.inMesh:
            self.meshes[-1].vertex(x, y, z, u, v)

    def endProfile(self):
        self.inMesh = False
        self.meshes[-1].end()

    # type of geometry
    type: RoadType
    meshes: list[Quad]
    segment: Segment
    first_point: glm.vec3
    middle_point: glm.vec3
    last_point: glm.vec3
    # length along centreline [m]
    length: float
    # width [m]
    width: float
    # signed radius [m], positive ccw
    radius: float
    inMesh: bool

