# Solves problem 09 - queen moves
import chess_game


def _main():
    x1 = int(input('Enter queen\'s current X position: '))
    y1 = int(input('Enter queen\'s current Y position: '))

    x2 = int(input('Enter queen\'s target X position: '))
    y2 = int(input('Enter queen\'s target Y position: '))

    is_valid = chess_game.is_valid_queen_move(x1, y1, x2, y2)

    print('{0}'.format('YES' if is_valid is True else 'NO'))


if __name__ == '__main__':
    _main()
