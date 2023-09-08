from import_this import (generate_race_data, RaceInfo)
import datetime
from typing import TypeAlias

RACE_DATA: RaceInfo = generate_race_data(10)
FinishedPlace: TypeAlias = int
FinishedTimeSeconds: TypeAlias = str | int | float
RacerName: TypeAlias = str
RacerTeam: TypeAlias = str

RacerInfo: TypeAlias = dict[
    str, FinishedPlace | FinishedTimeSeconds | RacerName | RacerTeam
]
WINNERS: dict[int, RacerInfo] = {}


def get_array(race_data: dict) -> dict:
    for team in race_data:
        value = race_data.get(team)
        for i in value:
            if value.get('FinishedPlace') in [1, 2, 3]:
                WINNERS.update({value.get('FinishedPlace'): value})
                break
    return WINNERS


def get_text() -> None:
    wine = WINNERS.get(1)
    print(f'Выиграл - {wine.get("RacerName")}!!! Поздравляем!!')
    print('_' * (27 + (len(wine.get('RacerName')))))
    print(f'Первые три места:\n')
    for i in dict(sorted(WINNERS.items())):
        value = WINNERS.get(i)
        time = str(datetime.timedelta(seconds=int(value.get('FinishedTimeSeconds'))))

        print(f'Гонщик на {i} метсте')
        print(f"\t\tИмя: {value.get('RacerName')}")
        print(f"\t\tКоманда: {value.get('RacerTeam')}")
        print(f"\t\tВремя: {time} (H:M:S)\n ")


if __name__ == '__main__':
    get_array(RACE_DATA)
    get_text()
