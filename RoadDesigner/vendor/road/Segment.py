from pyglm import glm
from typing import Protocol

class Segment(Protocol):
    def __init__(self):
        self.points = []
        self.tangents = []
        self.normals = []
        self.binormals = []

    def build(self) -> None: ...

    def length(self) -> None: ...

    def inertial_coord(self, offset:float, distance:float, loft:float) -> None: ...

    def curve_coord(self, x:float, y:float, z:float) -> None: ...

