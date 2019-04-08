import random

EMPTY_MARK = 'x'

MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}

def shuffle_field():
    field = list(range(1, 17))
    field[-1] = EMPTY_MARK
    random.shuffle(field)


    possible_moves = list(MOVES.keys())
    for move in range(100):
        random_move = random.choice(possible_moves)
        try:
            field = perform_move(field, random_move)
        except IndexError:
            continue
    return field

def print_field(field):
    for i in range(0, 16, 4):
        print(field[i:i + 4])
    print('\n')

def is_game_finished(field):
    ideal = list(range(1, 16))
    ideal.append(EMPTY_MARK)

    return ideal == field

def perform_move(field, key):
    current_position = field.index(EMPTY_MARK)
    if key == 's' and current_position >= 12:
        raise IndexError('Не могу идти вниз')

    if key == 'd' and current_position % 4 == 3:
        raise IndexError('Не могу идти вправо')

    if key == 'w' and current_position < 4:
        raise IndexError('Не могу ходить вверх')

    if key == 'a' and current_position % 4 ==0:
        raise IndexError('Не могу ходить влево')

    delta = MOVES[key]
    field[current_position], field[current_position + delta] =field[
    current_position + delta], field[current_position]
    return field


def handle_user_input():
    while True:
        user_move = input('Пожалуйста, нажмите кнопку: ')
        if user_move in MOVES.keys():
            return user_move

def main():
    field = shuffle_field()

    while not is_game_finished(field):
        try:
            print_field(field)
            move = handle_user_input()
            field = perform_move(field, move)
        except IndexError as e:
            print(e)
    print('Игра пройдена!')

if __name__ == '__main__':
    main()
