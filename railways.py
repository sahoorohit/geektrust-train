from typing import List, Union

from constants import Responses
from trains import Train


class Railway:

    def create_train(self, name: str, bogies: List) -> Train:
        train = Train(name=name)
        for bogie in bogies:
            train.add_bogie(destination=bogie)
        return train

    def train_arrived_at_junction(self, train: Train):
        train.remove_bogies_before_junction()

    def depart_train_from_junction(self, train: Train):
        train.remove_junction_bogies()

    def merge_trains(self, name: str, train_a: Train, train_b: Train) -> Train:
        train_ab = Train(name=name)
        train_ab.bogies = train_a.bogies + train_b.bogies
        train_ab.sort_bogies_in_order_of_distance()
        return train_ab

    def traverse_train(self, train: Train) -> Union[List, Responses]:
        if train.has_only_engines():
            return Responses.JOURNEY_ENDED
        return [train.name, *train.bogies]
