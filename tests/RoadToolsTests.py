import unittest

from parameterized import parameterized
from pyglm import glm

from Straight import Straight

class RoadToolsTests(unittest.TestCase):
    @parameterized.expand([
        (glm.vec3(0.0,0.0,0.0), glm.vec3(0.0, 252.0, 0.0), 252.0)
    ])
    def test_length(self, start_point: glm.vec3, end_point: glm.vec3, length: float):
        sut = Straight()
        sut.points = [start_point, end_point]
        self.assertEqual(length, sut.length())