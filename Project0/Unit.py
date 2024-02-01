import math


class Unit:

    TEAM_US = "US"
    TEAM_THEM = "THEM"
    TEAM_CHAOTIC = "CHAOTIC"

    def __init__(self, attack_power: int, hit_points: int, range: int, x_position: int, y_position: int, team: str, max_move_units: int):
        self._attack_power = attack_power
        self._hit_points = hit_points
        self._range = range
        self._x_position = x_position
        self._y_position = y_position
        self._team = team
        self._is_alive = True
        self._max_move_units = max_move_units
        self._max_hit_points = hit_points

    def get_hit_points(self):
        return self._hit_points

    def get_x_position(self):
        return self._x_position

    def get_y_position(self):
        return self._y_position

    def get_attack_power(self):
        return self._attack_power

    def get_range(self):
        return self._range

    def get_team(self):
        return self._team

    def is_alive(self):
        return self._is_alive

    def attack(self, target):
        if self._is_within_range(target) and self._should_attack(target):
            target._hit_points -= self._attack_power
            if target._hit_points <= 0:
                target._is_alive = False
                target._hit_points = 0 # totally optional

    def move(self, x_move, y_move):
        if x_move and y_move:
            raise ValueError("Can't move x and y")
        if x_move:  # means x_move is not 0
            if abs(x_move) > self._max_move_units:
                if x_move < 0:
                    x_move = -self._max_move_units
                else:
                    x_move = self._max_move_units

                self._x_position += x_move
        else:
            if abs(y_move) > self._max_move_units:
                if y_move < 0:
                    y_move = -self._max_move_units
                else:
                    y_move = self._max_move_units
                self._y_position += y_move

    def _is_within_range(self, target):
        return self._range >= math.sqrt(math.pow(self._x_position - target._x_position, 2) + math.pow(self._y_position - target._y_position, 2) )

    def _should_attack(self, target):
        return self._is_alive and ( self._team == Unit.TEAM_CHAOTIC or self._team != target._team )
