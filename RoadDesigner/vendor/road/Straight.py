try:
    from . import Polyline
    from . import Vertex
except ImportError:
    import Polyline
    import Vertex

from pyglm import glm

class Straight:
    def __init__(self):
        self.points = []
        self.binormals = []
        self.tangents = []
        self.normals = []
        self.tessellation = None

    def length(self):
        if len(self.points) == 2:
            diff =  self.points[1] - self.points[0]
            return glm.length(diff)
        else:
            return 0.0

    def inertial_coord(self, offset:float, distance:float, loft:float) -> glm.vec3:
        if len(self.points) >= 1 and len(self.binormals) == 1 and len(self.tangents)==1 and len(self.normals) == 1:
            v = self.points[0] + offset * self.binormals[0] + distance * self.tangents[0] + loft * self.normals[0]

            return v

    def build(self, num_divisions:int):
        self.tessellation = Polyline.Polyline(num_divisions)
        self.tessellation.points[0] = self.points[0]
        totalLength = self.length()
        point = glm.vec3()
        for point_index in range(1,self.tessellation.num_points()):
            distance = totalLength * point_index / num_divisions
            point = self.inertial_coord(0.0, distance, 0.0)
            self.tessellation.points[point_index] = point
            self.tessellation.distance[point_index] = distance

    points: list[glm.vec3]
    tangents: list[glm.vec3]
    normals: list[glm.vec3]
    binormals: list[glm.vec3]
