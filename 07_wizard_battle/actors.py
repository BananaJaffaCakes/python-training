
class Creature:
    def __init__(self, arg_name, arg_level):
        self.name = arg_name
        self.level = arg_level

    def __repr__(self):
        return "Lvl {} {}".format(self.level, self.name)


class Wizard:
    def __init__(self, arg_name, arg_level):
        self.name = arg_name
        self.level = arg_level

    def __repr__(self):
        return "Lvl {} {}".format(self.level, self.name)

