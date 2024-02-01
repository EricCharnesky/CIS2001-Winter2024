from Unit import Unit


class Artillery(Unit):
    MAX_MOVE_UNITS = 1
    ATTACK_POWER = 10
    HIT_POINTS = 1
    RANGE = 10

    def __init__(self, x_position: int, y_position: int, team: str):
        super().__init__(self.ATTACK_POWER, self.HIT_POINTS, self.RANGE, x_position, y_position, team,
                       self.MAX_MOVE_UNITS)



