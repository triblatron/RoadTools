import bpy
try:
    from .vendor.road import Road
    from . import SweptSurfaceConverter
    from . import CreateRoad
except ImportError:
    import vendor.road

class CreateArc(CreateRoad.CreateRoad):
    bl_idname = "object.create_arc"
    bl_label = "Create a circular arc road"

    def create(self,road, props):
        road.create_arc(props.road_length, props.road_radius, props.num_divisions)
