from Road import Road


class RoadBuildCommand:
    def __init__(self, args) -> None:
        self.args = args

    def makeItSo(self, road):
        if len(self.args) > 0:
            if self.args[0] == "beginProfile":
                road.beginProfile()
            elif self.args[0] == "endProfile":
                road.endProfile()
            elif self.args[0] == "vertex" and len(self.args) == 6:
                road.vertex(self.args[1], self.args[2], self.args[3], self.args[4], self.args[5])

    args: list[str]

class RoadBuildScript:
    def __init__(self):
        self.cmds = []

    def configure(self,config):
        if "script" in config:
            script = config["script"]
            if "cmds" in script:
                cmds = script["cmds"]
                if cmds is not None:
                    for cmd in cmds:
                        self.cmds.append(RoadBuildCommand(cmd))

    def build(self):
        road = Road()
        for cmd in self.cmds:
            cmd.makeItSo(road)

        return road

    cmds : list[RoadBuildCommand]