from enum import Enum


class Responses(Enum):
    JOURNEY_ENDED = "JOURNEY_ENDED"


JUNCTION_STATION = "HYB"


ROUTE_1 = {
    "CHN": 0,
    "SLM": 350,
    "BLR": 550,
    "KRN": 900,
    "HYB": 1200,
    "NGP": 1600,
    "ITJ": 1900,
    "BPL": 2000,
    "AGA": 2500,
    "NDL": 2700
}

ROUTE_2 = {
    "TVC": 0,
    "SRR": 300,
    "MAQ": 600,
    "MAO": 1000,
    "PNE": 1400,
    "HYB": 2000,
    "NGP": 2400,
    "ITJ": 2700,
    "BPL": 2800,
    "PTA": 3800,
    "NJP": 4200,
    "GHY": 4700
}
