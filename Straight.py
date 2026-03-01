from Segment import Segment
from pyglm import glm

class Straight(Segment):
    def length(self):
        if len(self.points) == 2:
            diff =  self.points[1] - self.points[0]
            return glm.length(diff)
        else:
            return 0.0
