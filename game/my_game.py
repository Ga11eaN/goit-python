from action import *
from map_generation import *


size_n = 10
size_m = 10

game_world = []
char = []
result = True

while True:
    game_option = input('Choose: new_game(n), load(l), top-scores(t), help(h) or quit(q)?')
    if game_option in ('new_game', 'n'):
        game_map = generate_map(size_n, size_m)
        game_world, char = generate_world(game_map)
        #print_map(game_world)
        break
    elif game_option in ('load','l'):
        game_world, char = load_game(game_world, char)
        #print_map(game_world)
        print(char)
        break
    elif game_option in ('top-scores','t'):
        top_scores()
    elif game_option in ('help','h'):
        help()
    elif game_option in ('quit','q'):
        log('Good bye!')
        result = False
        break
    else:
        print('Choose correct game option')


hidden_map = hidden_map(game_world, char)
print_map(hidden_map)

while result:

    action = input('Choose action: ')

    result, game_world, char = action_check(action, game_world, char)
