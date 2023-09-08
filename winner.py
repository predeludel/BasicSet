from import_this import RACE_DATA
import datetime

RACE_DATA = RACE_DATA
print(RACE_DATA)
winners = {}
for team in RACE_DATA:
    value = RACE_DATA.get(team)
    for place in value:
        if value.get('FinishedPlace') in [1, 2, 3]:
            winners.update({value.get('FinishedPlace'):
                                value})
            break
wine = winners.get(1)
print(f'Выиграл - {wine.get("RacerName")}!!! Поздравляем!!')
print(f'_______________________________')
print(f'Первые три места:\n')
for i in dict(sorted(winners.items())):
    value = winners.get(i)
    time = str(datetime.timedelta(seconds=int(value.get('FinishedTimeSeconds'))))

    print(f'Гонщик на {i} метсте')
    print(f"\t\tИмя: {value.get('RacerName')}")
    print(f"\t\tКоманда: {value.get('RacerTeam')}")
    print(f"\t\tВремя: {time} (H:M:S)\n ")