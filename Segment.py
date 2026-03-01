from pyglm import glm


class Segment:
    def __init__(self):
        self.points = []

    def length(self):
        return 0.0

    points: list[glm.vec3]

