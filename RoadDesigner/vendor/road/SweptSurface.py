try:
    from road import Quad
    from road import Polyline
    from road import Segment
    from road import Vertex
    from road import Polyline
    from pyglm import glm
except ImportError:
    import Quad
    import Polyline
    import Segment
    import Vertex
    import Polyline
    from pyglm import glm

class SweptSurface:
    def __init__(self, profile:list[Quad.Quad], axis:Segment.Segment):
        self.profile = profile
        self.axis = axis
        self.points = []
        self.quads = []

    def num_points(self):
        return len(self.points)

    def add_point(self, vert:Vertex.Vertex):
        v = Vertex.Vertex()
        v.position = self.axis.inertial_coord(vert.position.x, vert.position.y, vert.position.z)
        v.tex_coord.x = vert.tex_coord.x
        v.tex_coord.y = vert.tex_coord.y
        self.points.append(v)

    # Note that the vertices are output in Blender CCW winding
    # not the internal sorted order
    def build(self):
        # Somehow build the surface.
        # for each point in the axis do:
        #   generate a quad
        vert_index = 0
        vert = Vertex.Vertex()
        # We need point_index+1 to be valid so don't include the last point in the loop
        for point_index in range(len(self.axis.tessellation.points)-1):
            for quad in self.profile:
                width = glm.length(quad.verts[1].position - quad.verts[0].position)
                length = glm.length(self.axis.tessellation.points[point_index+1] - self.axis.tessellation.points[point_index])
                real_world_size = glm.vec2(width/quad.verts[1].tex_coord.x, quad.verts[2].position.y / quad.verts[2].tex_coord.y)
                vert.position.x = quad.verts[0].position.x
                vert.position.y = self.axis.tessellation.distance[point_index]
                vert.position.z = quad.verts[0].position.z
                vert.tex_coord.x = quad.verts[0].tex_coord.x
                vert.tex_coord.y = quad.verts[0].tex_coord.y
                self.quads.append([-1,-1,-1,-1])
                self.add_point(vert)
                self.quads[-1][0] = vert_index
                vert.position.x = quad.verts[1].position.x
                vert.position.y = self.axis.tessellation.distance[point_index]
                vert.position.z = quad.verts[1].position.z
                vert.tex_coord.x = quad.verts[1].tex_coord.x
                vert.tex_coord.y = quad.verts[1].tex_coord.y
                self.add_point(vert)
                self.quads[-1][1] = vert_index + 1
                vert.position.x = quad.verts[2].position.x
                vert.position.y = self.axis.tessellation.points[point_index+1].y
                vert.position.z = quad.verts[2].position.z
                vert.tex_coord.x = quad.verts[2].tex_coord.x
                vert.tex_coord.y = length / real_world_size.y
                self.add_point(vert)
                # self.points[-1].position.x = quad.verts[2].position.x
                # self.points[-1].position.y = self.axis.tessellation.points[point_index+1].y
                self.quads[-1][2] = vert_index + 3
                # self.points.append(Vertex.Vertex())
                vert.position.x = quad.verts[3].position.x
                vert.position.y = self.axis.tessellation.points[point_index+1].y
                vert.position.z = quad.verts[3].position.z
                vert.tex_coord.x = width / real_world_size.x
                vert.tex_coord.y = length / real_world_size.y
                self.add_point(vert)
                self.quads[-1][3] = vert_index + 2

                vert_index += 4

