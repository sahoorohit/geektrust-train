from bogies import Bogie, BogieType
from constants import JUNCTION_STATION


class Train:

    def __init__(self, name: str):
        self.name = name
        self.bogies = []

    def add_bogie(self, destination: str):
        bogie = Bogie(destination=destination)
        self.bogies.append(bogie)

    def remove_bogies_before_junction(self):
        bogies = [bogie for bogie in self.bogies if bogie.distance_to_junction >= 0]
        self.bogies = bogies

    def remove_junction_bogies(self):
        bogies = [bogie for bogie in self.bogies if bogie.destination != JUNCTION_STATION]
        self.bogies = bogies

    def sort_bogies_in_order_of_distance(self):
        bogies = []
        bogies_dict = {}
        for bogie in self.bogies:
            if bogie.destination == BogieType.ENGINE.value:
                bogies.append(bogie)
            else:
                bogies_dict[bogie] = bogie.distance_to_junction

        bogies_dict = dict(sorted(bogies_dict.items(), key=lambda item: item[1], reverse=True))
        bogies.extend(list(bogies_dict.keys()))
        self.bogies = bogies

    def has_only_engines(self) -> bool:
        only_engines = True
        for bogie in self.bogies:
            if bogie.destination != BogieType.ENGINE.value:
                only_engines = False
                break

        return only_engines
