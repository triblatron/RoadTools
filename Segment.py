from pyglm import glm

class Segment:
    def __init__(self):
        self.points = []
        self.tangents = []
        self.normals = []
        self.binormals = []

    def length(self):
        raise NotImplementedError

    def inertialCoord(self, offset:float, distance:float, loft:float):
        raise NotImplementedError

    def curveCoord(self, x:float, y:float, z:float):
        raise NotImplementedError

    points: list[glm.vec3]
    tangents: list[glm.vec3]
    normals: list[glm.vec3]
    binormals: list[glm.vec3]
