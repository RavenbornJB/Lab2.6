DAYS = 4
SESSION_TIME = 30
TO_PASS = 20
MOVE_COST = 10

default_stats = {
    "money": 100,
    "energy": 100,
    "fitness": 100,
    "intelligence": 30,
    "faith": 25
}

weights = {
    "bank": 1,
    "bfs": 1,
    "church": 1,
    "center": 1
}

energy_costs = {
    "bank": 40,
    "bfs": 20,
    "church": 10,
    "center": 20
}

stat_changes = {
    "bank": 75,
    "bfs": (-50, 50),
    "church": 3,
    "center": 5
}
