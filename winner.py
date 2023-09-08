from import_this import RACE_DATA
import datetime
from typing import TypeAlias

RACE_DATA = RACE_DATA
FinishedPlace: TypeAlias = int
FinishedTimeSeconds: TypeAlias = str | int | float
RacerName: TypeAlias = str
RacerTeam: TypeAlias = str

RacerInfo: TypeAlias = dict[
    str, FinishedPlace | FinishedTimeSeconds | RacerName | RacerTeam
]
WINNERS: dict[int, RacerInfo] = {}


def get_array(race_data) -> dict:
    for team in race_data:
        value = race_data.get(team)
        for i in value:
            if value.get('FinishedPlace') in [1, 2, 3]:
                WINNERS.update({value.get('FinishedPlace'): value})
                break
    return WINNERS


def get_text():
    wine = WINNERS.get(1)
    print(f'Выиграл - {wine.get("RacerName")}!!! Поздравляем!!')
    print(f'_______________________________')
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
