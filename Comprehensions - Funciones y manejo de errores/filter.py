# filter nos sirve para filtrar elementos de una lista 
from unittest import result


numbers = [1, 2, 3, 4, 5]
new_number = list(filter(lambda x: x % 2 ==0, numbers))
print(numbers)
print(new_number)

# FILTRAR DICCIONARIO 

resultados = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(len(resultados))

ganadores = list(filter(lambda x: x['home_team_result'] == 'Win', resultados))

print(ganadores)
print(len(ganadores))