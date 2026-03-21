import traceback

import bpy
try:
    from road import Road
    from . import SweptSurfaceConverter
    from . import CreateRoad
except ImportError:
    traceback.print_exc()
    import vendor.road
    import CreateRoad

class CreateStraight(CreateRoad.CreateRoad):
    bl_idname = "object.create_straight"
    bl_label = "Create a straight road"

    def create(self, road, props):
        road.create_straight(props.road_length,props.num_divisions)

