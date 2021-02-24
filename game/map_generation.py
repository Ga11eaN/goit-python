from random import randint
from action import log

def generate_map(n, m):

    log('Generating map...')

    game_map = []

    for _ in range(n):
        row = [' ' for _ in range(m)]
        game_map.append(row)

    log('Map has been generated')

    return game_map



def generate_world(game_map):

    log('Generating world...')
    
    objs = {'X': 1, 'O': 3, '&': 3, '_': 3, 'G':1}
    size_n, size_m = len(game_map), len(game_map[0])
    rnd_cells = []

    for obj, n in objs.items():
        for i in range(n):
            rand = True
            while rand:
                rnd_cell = randint(0, size_n - 1), randint(0, size_m - 1)
                if rnd_cell not in rnd_cells:
                    rnd_cells.append(rnd_cell)
                    rand = False

            if obj == 'X':
                char_position = list(rnd_cell)
                char_position.append(0)

            game_map[rnd_cell[0]][rnd_cell[1]] = obj

    log('World has been generated')
    print('X - your character, O - gold, & - ORC, _ - trap, G - Holy Grail')

    return game_map, char_position
