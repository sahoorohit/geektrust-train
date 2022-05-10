import sys
from enum import Enum
from typing import List

from bogies import Bogie
from railways import Railway


def show(output: List, arrival=True):
    if isinstance(output, Enum):
        print(output.value)
        return

    journey_status = "ARRIVAL" if arrival else "DEPARTURE"
    print(journey_status, end=' ')

    for item in output:
        if isinstance(item, Bogie):
            print(item.destination, end=' ')
        else:
            print(item, end=' ')

    print()


def main():
    input_file = sys.argv[1]

    with open(input_file) as file:
        lines = file.readlines()

    railway = Railway()

    train_a_bogies = list(map(str, lines[0].split()))
    train_a = railway.create_train(name=train_a_bogies[0], bogies=train_a_bogies[1:])

    train_b_bogies = list(map(str, lines[1].split()))
    train_b = railway.create_train(name=train_b_bogies[0], bogies=train_b_bogies[1:])

    railway.train_arrived_at_junction(train=train_a)
    railway.train_arrived_at_junction(train=train_b)

    show(railway.traverse_train(train=train_a))
    show(railway.traverse_train(train=train_b))

    train_ab = railway.merge_trains(name="TRAIN_AB", train_a=train_a, train_b=train_b)
    railway.depart_train_from_junction(train=train_ab)
    show(railway.traverse_train(train=train_ab), arrival=False)


if __name__ == "__main__":
    main()
