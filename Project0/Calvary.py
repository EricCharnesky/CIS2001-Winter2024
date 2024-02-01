from Unit import Unit


class Calvary(Unit):
    MAX_MOVE_UNITS = 10
    ATTACK_POWER = 5
    HIT_POINTS = 10
    RANGE = 5

    def __init__(self, x_position: int, y_position: int, team: str):
        super().__init__(self.ATTACK_POWER, self.HIT_POINTS, self.RANGE, x_position, y_position, team,
                       self.MAX_MOVE_UNITS)



