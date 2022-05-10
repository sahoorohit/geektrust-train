from typing import List
from unittest import TestCase

from railways import Railway
from trains import Train


class TrainTestCase(TestCase):

    def setUp(self) -> None:
        self.railway = Railway()

    def set_input_and_execute(self) -> None:
        train_a_bogies = list(map(str, self.train_a_bogies_input.split()))
        train_a = self.railway.create_train(name=train_a_bogies[0], bogies=train_a_bogies[1:])

        train_b_bogies = list(map(str, self.train_b_bogies_input.split()))
        train_b = self.railway.create_train(name=train_b_bogies[0], bogies=train_b_bogies[1:])

        self.railway.train_arrived_at_junction(train=train_a)
        self.railway.train_arrived_at_junction(train=train_b)

        self.train_ab = self.railway.merge_trains(name="TRAIN_AB", train_a=train_a, train_b=train_b)
        self.railway.depart_train_from_junction(train=self.train_ab)

        arrival_at_hyb_train_a = self.traverse_train(train=train_a)
        arrival_at_hyb_train_b = self.traverse_train(train=train_b)
        dep_from_hyb = self.traverse_train(train=self.train_ab)

        self.assertEqual(arrival_at_hyb_train_a, self.expected_arrival_at_hyb_train_a)
        self.assertEqual(arrival_at_hyb_train_b, self.expected_arrival_at_hyb_train_b)
        self.assertEqual(dep_from_hyb, self.expected_dep_from_hyb)

    def traverse_train(self, train: Train) -> List:
        return [train.name] + [bogie.destination for bogie in train.bogies]

    def test_passenger_for_all_the_stations_in_both_trains(self):
        self.train_a_bogies_input = "TRAIN_A ENGINE CHN SLM BLR KRN HYB NGP ITJ BPL AGA NDL"
        self.train_b_bogies_input = "TRAIN_B ENGINE TVC SRR MAQ MAO PNE HYB NGP ITJ BPL PTA NJP GHY"

        self.expected_arrival_at_hyb_train_a = ['TRAIN_A', 'ENGINE', 'HYB', 'NGP', 'ITJ', 'BPL', 'AGA', 'NDL']
        self.expected_arrival_at_hyb_train_b = ['TRAIN_B', 'ENGINE', 'HYB', 'NGP', 'ITJ', 'BPL', 'PTA', 'NJP', 'GHY']
        self.expected_dep_from_hyb = ['TRAIN_AB', 'ENGINE', 'ENGINE', 'GHY', 'NJP', 'PTA', 'NDL', 'AGA', 'BPL', 'BPL',
                                      'ITJ', 'ITJ', 'NGP', 'NGP']

        self.set_input_and_execute()

    def test_passenger_for_stations_till_hyb_in_both_trains(self):
        self.train_a_bogies_input = "TRAIN_A ENGINE CHN SLM BLR KRN HYB"
        self.train_b_bogies_input = "TRAIN_B ENGINE TVC SRR MAQ MAO PNE HYB"

        self.expected_arrival_at_hyb_train_a = ['TRAIN_A', 'ENGINE', 'HYB']
        self.expected_arrival_at_hyb_train_b = ['TRAIN_B', 'ENGINE', 'HYB']
        self.expected_dep_from_hyb = ['TRAIN_AB', 'ENGINE', 'ENGINE']

        self.set_input_and_execute()

    def test_passenger_for_stations_before_hyb_in_both_trains(self):
        self.train_a_bogies_input = "TRAIN_A ENGINE CHN SLM BLR KRN"
        self.train_b_bogies_input = "TRAIN_B ENGINE TVC SRR MAQ MAO PNE"

        self.expected_arrival_at_hyb_train_a = ['TRAIN_A', 'ENGINE']
        self.expected_arrival_at_hyb_train_b = ['TRAIN_B', 'ENGINE']
        self.expected_dep_from_hyb = ['TRAIN_AB', 'ENGINE', 'ENGINE']

        self.set_input_and_execute()

    def test_passenger_for_stations_till_hyb_in_train_a_and_before_hyb_in_train_b(self):
        self.train_a_bogies_input = "TRAIN_A ENGINE SLM BLR KRN HYB SLM"
        self.train_b_bogies_input = "TRAIN_B ENGINE SRR MAO PNE"

        self.expected_arrival_at_hyb_train_a = ['TRAIN_A', 'ENGINE', 'HYB']
        self.expected_arrival_at_hyb_train_b = ['TRAIN_B', 'ENGINE']
        self.expected_dep_from_hyb = ['TRAIN_AB', 'ENGINE', 'ENGINE']

        self.set_input_and_execute()

    def test_when_train_a_starts_from_tvc(self):
        self.train_a_bogies_input = "TRAIN_A ENGINE TVC SRR MAQ MAO PNE HYB NGP ITJ BPL PTA NJP GHY"
        self.train_b_bogies_input = "TRAIN_B ENGINE CHN SLM BLR KRN HYB NGP ITJ BPL AGA NDL"

        self.expected_arrival_at_hyb_train_a = ['TRAIN_A', 'ENGINE', 'HYB', 'NGP', 'ITJ', 'BPL', 'PTA', 'NJP', 'GHY']
        self.expected_arrival_at_hyb_train_b = ['TRAIN_B', 'ENGINE', 'HYB', 'NGP', 'ITJ', 'BPL', 'AGA', 'NDL']
        self.expected_dep_from_hyb = ['TRAIN_AB', 'ENGINE', 'ENGINE', 'GHY', 'NJP', 'PTA', 'NDL', 'AGA', 'BPL', 'BPL',
                                      'ITJ', 'ITJ', 'NGP', 'NGP']

        self.set_input_and_execute()

    def test_passenger_in_train_a_for_2nd_route(self):
        self.train_a_bogies_input = "TRAIN_A ENGINE CHN SLM GHY BLR KRN NGP ITJ BPL NDL NJP"
        self.train_b_bogies_input = "TRAIN_B ENGINE TVC SRR MAQ MAO PNE HYB NGP ITJ BPL PTA NJP GHY"

        self.expected_arrival_at_hyb_train_a = ['TRAIN_A', 'ENGINE', 'GHY', 'NGP', 'ITJ', 'BPL', 'NDL', 'NJP']
        self.expected_arrival_at_hyb_train_b = ['TRAIN_B', 'ENGINE', 'HYB', 'NGP', 'ITJ', 'BPL', 'PTA', 'NJP', 'GHY']
        self.expected_dep_from_hyb = ['TRAIN_AB', 'ENGINE', 'ENGINE', 'GHY', 'GHY', 'NJP', 'NJP', 'PTA', 'NDL',
                                      'BPL', 'BPL', 'ITJ', 'ITJ', 'NGP', 'NGP']

        self.set_input_and_execute()

    def test_passenger_in_train_b_for_1st_route(self):
        self.train_a_bogies_input = "TRAIN_A ENGINE CHN SLM BLR KRN NGP ITJ BPL NDL"
        self.train_b_bogies_input = "TRAIN_B ENGINE TVC AGA SRR MAQ MAO PNE HYB NDL NGP ITJ BPL PTA NJP GHY"

        self.expected_arrival_at_hyb_train_a = ['TRAIN_A', 'ENGINE', 'NGP', 'ITJ', 'BPL', 'NDL']
        self.expected_arrival_at_hyb_train_b = ['TRAIN_B', 'ENGINE', 'AGA', 'HYB', 'NDL', 'NGP', 'ITJ', 'BPL', 'PTA',
                                                'NJP', 'GHY']
        self.expected_dep_from_hyb = ['TRAIN_AB', 'ENGINE', 'ENGINE', 'GHY', 'NJP', 'PTA', 'NDL', 'NDL', 'AGA',
                                      'BPL', 'BPL', 'ITJ', 'ITJ', 'NGP', 'NGP']

        self.set_input_and_execute()

    def test_passenger_for_all_the_stations_in_both_trains_twice(self):
        self.train_a_bogies_input = "TRAIN_A ENGINE CHN SLM ITJ BLR HYB NGP NDL SLM KRN CHN BPL HYB NGP ITJ BLR BPL " \
                                    "KRN AGA NDL AGA"
        self.train_b_bogies_input = "TRAIN_B ENGINE TVC MAO SRR ITJ MAQ GHY HYB MAO PTA PNE TVC HYB NGP MAQ NGP NJP " \
                                    "BPL ITJ BPL PNE PTA NJP GHY SRR"

        self.expected_arrival_at_hyb_train_a = ['TRAIN_A', 'ENGINE', 'ITJ', 'HYB', 'NGP', 'NDL', 'BPL', 'HYB', 'NGP',
                                                'ITJ', 'BPL', 'AGA', 'NDL', 'AGA']
        self.expected_arrival_at_hyb_train_b = ['TRAIN_B', 'ENGINE', 'ITJ', 'GHY', 'HYB', 'PTA', 'HYB', 'NGP', 'NGP',
                                                'NJP', 'BPL', 'ITJ', 'BPL', 'PTA', 'NJP', 'GHY']
        self.expected_dep_from_hyb = ['TRAIN_AB', 'ENGINE', 'ENGINE', 'GHY', 'GHY', 'NJP', 'NJP', 'PTA', 'PTA',
                                      'NDL', 'NDL', 'AGA', 'AGA', 'BPL', 'BPL', 'BPL', 'BPL', 'ITJ', 'ITJ', 'ITJ',
                                      'ITJ', 'NGP', 'NGP', 'NGP', 'NGP']

        self.set_input_and_execute()

    def test_passenger_in_train_a_for_2nd_route_and_train_b_for_1st_route(self):
        self.train_a_bogies_input = "TRAIN_A ENGINE CHN SLM BLR KRN NJP HYB NGP ITJ BPL GHY AGA NDL"
        self.train_b_bogies_input = "TRAIN_B ENGINE TVC SRR AGA MAQ MAO PNE HYB NDL NDL NGP ITJ BPL PTA NJP GHY"

        self.expected_arrival_at_hyb_train_a = ['TRAIN_A', 'ENGINE', 'NJP', 'HYB', 'NGP', 'ITJ', 'BPL', 'GHY', 'AGA',
                                                'NDL']
        self.expected_arrival_at_hyb_train_b = ['TRAIN_B', 'ENGINE', 'AGA', 'HYB', 'NDL', 'NDL', 'NGP', 'ITJ', 'BPL',
                                                'PTA', 'NJP', 'GHY']
        self.expected_dep_from_hyb = ['TRAIN_AB', 'ENGINE', 'ENGINE', 'GHY', 'GHY', 'NJP', 'NJP', 'PTA', 'NDL', 'NDL',
                                      'NDL', 'AGA', 'AGA', 'BPL', 'BPL', 'ITJ', 'ITJ', 'NGP', 'NGP']

        self.set_input_and_execute()

    def test_sample_input_1(self):
        self.train_a_bogies_input = "TRAIN_A ENGINE NDL NDL KRN GHY SLM NJP NGP BLR"
        self.train_b_bogies_input = "TRAIN_B ENGINE NJP GHY AGA PNE MAO BPL PTA"

        self.expected_arrival_at_hyb_train_a = ['TRAIN_A', 'ENGINE', 'NDL', 'NDL', 'GHY', 'NJP', 'NGP']
        self.expected_arrival_at_hyb_train_b = ['TRAIN_B', 'ENGINE', 'NJP', 'GHY', 'AGA', 'BPL', 'PTA']
        self.expected_dep_from_hyb = ['TRAIN_AB', 'ENGINE', 'ENGINE', 'GHY', 'GHY', 'NJP', 'NJP', 'PTA', 'NDL', 'NDL',
                                      'AGA', 'BPL', 'NGP']

        self.set_input_and_execute()

    def test_sample_input_2(self):
        self.train_a_bogies_input = "TRAIN_A ENGINE SLM BLR KRN HYB SLM NGP ITJ"
        self.train_b_bogies_input = "TRAIN_B ENGINE SRR MAO NJP PNE PTA"

        self.expected_arrival_at_hyb_train_a = ['TRAIN_A', 'ENGINE', 'HYB', 'NGP', 'ITJ']
        self.expected_arrival_at_hyb_train_b = ['TRAIN_B', 'ENGINE', 'NJP', 'PTA']
        self.expected_dep_from_hyb = ['TRAIN_AB', 'ENGINE', 'ENGINE', 'NJP', 'PTA', 'ITJ', 'NGP']

        self.set_input_and_execute()
