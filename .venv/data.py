from typing import Union

f_teams = [
    {
        "team":"Mercedes",
        "drivers": ["Lewis Hamilton", "Valtteri Bottas"],
        "engine": "Mercedes"
    },
    {
        "team":"Red Bull Racing",
        "drivers": ["Max Verstappen", "Sergio Perez"],
        "engine": "Honda"
    },
    {
        "team":"Ferrari",
        "drivers": ["Charles Leclerc", "Carlos Sainz"],
        "engine": "Ferrari"
    },
    {
        "team":"Alpine",
        "drivers": ["Fernando Alonso", "Esteban Ocon"],
        "engine": "Renault"
    },
    {
        "team":"Alfa Romeo",
        "drivers": ["Pierre Gasly", "Guanyu Zhou"],
        "engine": "Ferrari"
    },
    {
        "team":"Haas",
        "drivers": ["Nico Hulkenberg", "Kevin Magnussen"],
        "engine": "Ferrari"
    },
    {
        "team":"McLaren",
        "drivers": ["Lando Norris", "Oscar Piastri"],
        "engine": "Mercedes"
    },
    {
        "team":"AlphaTauri",
        "drivers": ["Yuki Tsunoda", "Nyck de Vries"],
        "engine": "Honda"
    },
    {
        "team":"Aston Martin",
        "drivers": ["Fernando Alonso", "Lance Stroll"],
        "engine": "Mercedes"
    },
    {
        "team":"Williams",
        "drivers": ["Logan Sargeant", "Alex Albon"],
        "engine": "Mercedes"
    }
]

def get_all_teams_from_fake_db() -> list:
    """Return a list of F1 teams"""
    return f_teams

def get_team_from_fake_db(team: str) -> Union[dict, None]:
    for f_team in f_teams:
        if team.lower() == f_team['team'].lower():
            return f_team
    return None