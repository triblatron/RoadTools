from pyglm import glm

class Polyline:
    def __init__(self, num_divisions: int):
        self.points = [glm.vec3()] * (num_divisions + 1)

    def num_points(self):
        return len(self.points)

    def add_point(self, point):
        self.points.append(point)

    points : list[glm.vec3]