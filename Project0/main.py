from Unit import Unit
from Infantry import Infantry
from Calvary import Calvary
from Captain import Captain

us_1 = Infantry(1, 1, Unit.TEAM_US)
us_2 = Captain(1, 2, Unit.TEAM_US)
them_1 = Calvary(2, 1, Unit.TEAM_THEM)
chaotic_1 = Infantry(2, 2, Unit.TEAM_CHAOTIC)

us_1.attack(chaotic_1)
us_1.attack(us_2)
us_1.attack(them_1)
