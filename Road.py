from enum import Enum

from mathutils import Vector
from mathutils import Matrix
from Segment import Segment

class RoadType(Enum):
    STRAIGHT = 0
    ARC=1,
    CLOTHOID=2

class Road:
    def __init__(self):
        pass

    # type of geometry
    type: RoadType
    segment: Segment
    first_point: Vector
    middle_point: Vector
    last_point: Vector
    # length along centreline [m]
    length: float
    # width [m]
    width: float
    # signed radius [m], positive ccw
    radius: float
