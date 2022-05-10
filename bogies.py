from enum import Enum

from constants import JUNCTION_STATION, ROUTE_1, ROUTE_2


class BogieType(Enum):
    ENGINE = "ENGINE"
    COACH = "COACH"


class Bogie:

    def __init__(self, destination: str = ''):
        self.destination = destination

    @property
    def distance_to_junction(self) -> int:
        if self.destination == BogieType.ENGINE.value:
            return 0

        distance = ROUTE_1.get(self.destination)
        if isinstance(distance, int):
            _distance_to_junction = distance - ROUTE_1.get(JUNCTION_STATION)
        else:
            distance = ROUTE_2.get(self.destination)
            _distance_to_junction = distance - ROUTE_2.get(JUNCTION_STATION)

        return _distance_to_junction
