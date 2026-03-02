from enum import Enum

from Quad import Quad
from Segment import Segment
from pyglm import glm

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
                quad = Quad()
                quad.configure(meshConfig)
                self.meshes.append(quad)

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

