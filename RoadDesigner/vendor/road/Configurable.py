class Configurable:
    @classmethod
    def readConfig(cls, config:dict, name:str, default_value):
        if name in config:
            return config[name]
        else:
            return default_value