import collections
from datetime import datetime
import json
from random import randint


def hidden_map(game_map, char_position):
    def check_vision(char_position, w,h):
        if abs(w - char_position[0]) < 3 and abs(h - char_position[1]) < 3:
            return True
        else:
            return False
    
    hidden_game_up = []
    for i in range(len(game_map)):
        hidden_game_up.append([])
        for j in range(len(game_map[0])):
            if check_vision(char_position, i, j):
                hidden_game_up[i].append(game_map[i][j])
            else:
                hidden_game_up[i].append(' ')

    return hidden_game_up
    
def print_map(game_map):

    for row in game_map:
        print(f"|{'|'.join(row)}|") 

def log(action):

    current_time = datetime.strftime(datetime.now(), '%H:%M:%S')
    message = f'[{current_time}] {action}'

    print(message)
    with open('logs.txt', 'a') as file:
        file.write(f'{message}\n')

def final_score(char_position):
    name = input('Enter your name: ')
    #message = "{:*<12}{:*>8}".format(name, char_position[2])
    with open('Score.txt', 'a') as file:
        file.write(f'{name}:{char_position[2]}\n')

def help():
    print('X - your character, O - gold, & - ORC, _ - trap, G - Holy Grail')
    print('You need to find max amount of gold and grab the Holy Grail')
    print('Your vision is 2 tiles around your character')
    print('You can earn gold from the ground or from killing Orcs')
    print('Available actions: type move(m) and the direction up(u), down(d), left(l), right(r)')

def top_scores():
    with open('Score.txt', 'r') as file:
        d = []
        while True:
            row = file.readline()
            if not row:
                break
            r_list = row.split(':')
            d.append((int(r_list[1][:-1]), r_list[0]))

    d.sort(reverse = True)

    deq = collections.deque(d, maxlen = 10)

    for item in deq:
        mes = "{:*<12}{:*>8}".format(item[1], str(item[0]))
        print(mes)

def do_action(game_world, char_position):
    #ACTIONS = {'O': gold, '&': ORC, '_': trap, 'G': Holy Grail}
    game_over = False
    if game_world[char_position[0]][char_position[1]] == 'O':
        gold = randint(100,500)
        char_position[2] += gold
        log(f'You pick up {gold} gold. Total gold: {char_position[2]}')
    
    elif game_world[char_position[0]][char_position[1]] == 'G':
        gold = randint(500,1000)
        char_position[2] += gold
        log(f'You found the Holy Grail which values:{gold} gold. Total gold: {char_position[2]}.')
        game_over = True
        
    elif game_world[char_position[0]][char_position[1]] == '&':
        if randint(0,3) < 1:
            log(f'You were killed by Orc!')
            game_over = True
        else:
            gold = randint(50,200)
            char_position[2] += gold
            log(f'You killed Orc and gain {gold} gold! Total gold: {char_position[2]}.')
    
    elif game_world[char_position[0]][char_position[1]] == '_':
        if randint(0,9) < 2:
            log(f'You step into the trap and died!')
            game_over = True
        else:
            log(f'You step into the trap but you survived!')
        
    return game_world, char_position, game_over

def move(game_world, char_position):

    while True:
        direction = input('Choose direction: ')
        if direction not in ('up' ,'u', 'down','d', 'left','l', 'right','r'):
            log('Wrong direction. Try again! Should be: u, l, d, r')
        else:
            break
            
    log(f'Moving {direction} from position ({char_position[0]}, {char_position[1]})')

    old_char_pos = tuple(char_position)
    game_world[char_position[0]][char_position[1]] = ' '
    
    if direction in ('down','d'):
        char_position[0] += 1
    elif direction in ('up','u'):
        char_position[0] -= 1
    elif direction in ('left','l'):
        char_position[1] -= 1
    elif direction in ('right','r'):
        char_position[1] += 1
    
    if char_position[0] in range(len(game_world)) and char_position[1] in range(len(game_world[0])):
        game_world, char_position, game_over = do_action(game_world, char_position)
        if game_over:
            return game_world, char_position, game_over
        game_world[char_position[0]][char_position[1]] = 'X'  
        log(f'New position ({char_position[0]}, {char_position[1]})')
    else:
        char_position = list(old_char_pos)
        game_world[old_char_pos[0]][old_char_pos[1]] = 'X'
        log('You cannot leave the map!')

    return game_world, char_position, game_over


def save_game(game_world, char_postition):

    log('Saving game...')

    game_save = {'game_world': game_world, 'char_position': char_postition}

    with open('save.txt', 'w') as file:
        json.dump(game_save, file)

    log('Game has been saved')


def load_game(game_world, char_position):

    log('Loading game...')

    with open('save.txt') as file:
        game_save = json.load(file)

    game_world = game_save['game_world']
    char_position = game_save['char_position']

    log('Game has been loaded')

    return game_world, char_position
       
def action_check(action_name, game_world, char_position):

    #ACTION_LIST = ('move', 'save', 'load', 'm', 's', 'l','q','quit')
    action_result = True
    
    if action_name in ('move', 'm'):
        game_world, char_position ,game_over = move(game_world, char_position)
        if game_over:
            print(f'Total score: {char_position[2]}\nThank you for playing my game!')
            action_result =  False
    elif action_name in ('save', 's'):
        save_game(game_world, char_position)
    elif action_name in ('load', 'l'):
        game_world, char_position = load_game(game_world, char_position)
    elif action_name in ('quit', 'q'):
        log('Good bye!')
        action_result =  False
        return action_result, game_world, char_position
    elif action_name in ('help', 'h'):
        help()
        return action_result, game_world, char_position
    else:
        log('Wrong action! Use help(h) to see available options')
        return action_result, game_world, char_position
        
    if action_result:
        print_map(hidden_map(game_world, char_position))
    else:
        final_score(char_position)

    return action_result, game_world, char_position
