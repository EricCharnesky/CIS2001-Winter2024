from Infantry import Infantry
from Unit import Unit


class Captain(Infantry):

    def __init__(self, x_position: int, y_position: int, team: str):
        super().__init__(x_position, y_position, team)
        self._hit_points = 20
        self._attack_power = 1

    def attack(self, target: Unit):
        if self._is_within_range(target) and self._team == target._team and target._is_alive:
            target._hit_points = target._max_hit_points



