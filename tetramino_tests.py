from tetramino import *
from getkey import getkey

def print_grid2(a_grid):
    for i in a_grid:
        for j in range(len(i)-1):
            print(i[j], end="")
        print(i[len(i)-1])

def test_import_tetraminos():
    expected_import = ((5, 4), [[[(0, 0), (0, 1), (0, 2), (1, 1)], '0;37;43', (0, 0)],
                                [[(0, 0), (0, 1), (0, 2)], '0;37;41', (0, 0)],
                                [[(1, 0), (1, 1), (0, 1), (0, 2)],
                                 '0;37;45', (0, 0)],
                                [[(0, 0)], '0;37;46', (0, 0)],
                                [[(0, 0), (1, 0), (1, 1)], '0;37;42', (0, 0)],
                                [[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], '0;37;44', (0, 0)]])
    return (import_card('carte_1.txt')) == expected_import


def test_create_grid():
    expected_grid = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                         '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                         '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                         '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                         '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                         '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                         '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--',
                         '--', '--', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                         '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                         '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                         '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                         '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                         '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                         '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                         '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--',
                         '--', '--', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                         '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                         '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                         '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                         '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                         '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                         '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                     ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
    return (create_grid(5, 7)) == expected_grid


def test_place_tetramino():
    initial_grid = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m', '  ',
                     '  ', '  ', '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '  ', '  ', '  '],
                    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m', '  ', '  ',
                     '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '\x1b[0;37;45m3 \x1b[0m', '  ', '  ', '  '],
                    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m', '  ',
                     '  ', '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '  ', '  ', '  ', '  '],
                    ['  ', '  ', '  ', '  ', '  ', '\x1b[0;37;43m1 \x1b[0m', '\x1b[0;37;43mXX\x1b[0m',
                     '\x1b[0;37;43mXX\x1b[0m', '--', '--', '--', '  ', '  ', '  ', '  ', '  ', '  '],
                    ['  ', '  ', '  ', '  ', '  ', ' |', '\x1b[0;37;43m1 \x1b[0m',
                     '\x1b[0;37;44m6 \x1b[0m', '  ', '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
                    ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '\x1b[0;37;44m6 \x1b[0m', '  ',
                     '  ', '  ', '\x1b[0;37;42mXX\x1b[0m', '\x1b[0;37;42m5 \x1b[0m', '  ', '  ', '  ', '  '],
                    ['  ', '  ', '  ', '  ', '  ', '\x1b[0;37;44mXX\x1b[0m', '\x1b[0;37;44m6 \x1b[0m',
                     '\x1b[0;37;44m6 \x1b[0m', '  ', '  ', '  ', '| ', '\x1b[0;37;42m5 \x1b[0m', '  ', '  ', '  ', '  '],
                    ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                     '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
                    ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--',
                     '--', '--', '  ', '  ', '  ', '  ', '  ', '  '],
                    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                     '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                     '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                     '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
    tetramino = [[[(1, 1), (2, 1), (3, 1), (2, 2)], '0;37;43', [4, 3]],
                 [[(2, 1), (2, 2), (2, 3)], '0;37;41', (5, 0)],
                 [[(3, 1), (3, 2), (2, 2), (2, 3)], '0;37;45', (10, 0)],
                 [[
                     (2, 2)], '0;37;46', (0, 4)],
                 [[(1, 2), (2, 2), (2, 3)], '0;37;42', (10, 4)],
                 [[(3, 0), (3, 1), (3, 2), (2, 2), (1, 2)], '0;37;44', [4, 5]]]

    final_grid = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m', '  ',
                      '  ', '  ', '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m', '  ', '  ',
                      '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '\x1b[0;37;45m3 \x1b[0m', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m', '  ',
                   '  ', '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '\x1b[0;37;43m1 \x1b[0m', '\x1b[0;37;43mXX\x1b[0m',
                   '\x1b[0;37;43mXX\x1b[0m', '--', '--', '--', '  ', '  ', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', ' |', '\x1b[0;37;43m1 \x1b[0m',
                   '\x1b[0;37;44m6 \x1b[0m', '  ', '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '\x1b[0;37;46m4 \x1b[0m', '  ', '  ', ' |', '  ', '\x1b[0;37;44m6 \x1b[0m', '  ',
                   '  ', '  ', '\x1b[0;37;42mXX\x1b[0m', '\x1b[0;37;42m5 \x1b[0m', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '\x1b[0;37;44mXX\x1b[0m', '\x1b[0;37;44m6 \x1b[0m',
                   '\x1b[0;37;44m6 \x1b[0m', '  ', '  ', '  ', '| ', '\x1b[0;37;42m5 \x1b[0m', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                   '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--',
                   '--', '--', '  ', '  ', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                   '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                   '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                   '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                  ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
    
    #print_grid2(initial_grid)
    #print_grid2(place_tetraminos(tetramino, initial_grid))
    #print_grid2(final_grid)
    return (place_tetraminos(tetramino, initial_grid) == final_grid)


def test_rotate_tetramino_1():
    tetramino = [[(0, 0), (0, 1), (1, 1)], '0;37;45', '']
    expected_rotation = [[(0, 0), (-1, 0), (-1, 1)], '0;37;45', '']
    return (rotate_tetramino(tetramino) == expected_rotation)


def test_rotate_tetramino_2():
    tetramino = [[(0, 0)], '0;37;45', '']
    expected_rotation = [[(0, 0)], '0;37;45', '']
    return (rotate_tetramino(tetramino) == expected_rotation)


def test_setup_tetraminos():
    tetraminos = [[[(1, 1), (2, 1), (3, 1), (2, 2)], '0;37;43', (0, 0)],
                  [[(2, 1), (2, 2), (2, 3)], '0;37;41', (0, 0)],
                  [[(3, 1), (3, 2), (2, 2),
                    (2, 3)], '0;37;45', (0, 0)],
                  [[(2, 2)], '0;37;46', (0, 0)],
                  [[(1, 2), (2, 2), (2, 3)], '0;37;42', (0, 0)],
                  [[(0, 1), (1, 1), (2, 1), (2, 2), (2, 3)], '0;37;44', (0, 0)]]
    expected_setup = ([['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '\x1b[0;37;43m1 \x1b[0m', '\x1b[0;37;43m1 \x1b[0m', '\x1b[0;37;43m1 \x1b[0m', '  ', '  ', '  ',
                          '  ', '\x1b[0;37;41m2 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '  '],
                      ['  ', '  ', '\x1b[0;37;43m1 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m',
                          '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '\x1b[0;37;45m3 \x1b[0m', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m',
                          '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--',
                          '--', '--', '  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                          '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                          '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '\x1b[0;37;46m4 \x1b[0m', '  ', '  ', ' |', '  ', '  ', '  ', '  ',
                          '  ', '| ', '  ', '\x1b[0;37;42m5 \x1b[0m', '\x1b[0;37;42m5 \x1b[0m', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ', '  ',
                          '  ', '| ', '  ', '  ', '\x1b[0;37;42m5 \x1b[0m', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--',
                          '--', '--', '  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                          '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                      ['\x1b[0;37;44m6 \x1b[0m', '\x1b[0;37;44m6 \x1b[0m', '\x1b[0;37;44m6 \x1b[0m', '  ',
                          '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '\x1b[0;37;44m6 \x1b[0m', '  ', '  ', '  ', '  ',
                          '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '\x1b[0;37;44m6 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']])
    grid = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--',
                '--', '--', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
                '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--',
                '--', '--', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
    
    #print_grid2(setup_tetraminos(tetraminos, grid)[0])
    #print_grid2(expected_setup)
    return (setup_tetraminos(tetraminos, grid)[0] == expected_setup)


def test_check_move_1():
    tetramino = [[(0, 0), (1, 0), (1, 1)], '0;37;42', [12, 1]]
    grid = [['\x1b[0;37;43m1 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '  ', '  ', '  '], ['\x1b[0;37;43m1 \x1b[0m', '\x1b[0;37;43m1 \x1b[0m', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;42mXX\x1b[0m', '\x1b[0;37;42mXX\x1b[0m', '  ', '  ', '  '], ['\x1b[0;37;43m1 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '\x1b[0;37;42m5 \x1b[0m', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--', '--', '--', '  ', '  ', '  ', '  ', '  ', '  '], ['\x1b[0;37;46m4 \x1b[0m', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ', '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 '  ', '  ', ' |', '  ', '  ', '  ', '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ', '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ', '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--', '--', '--', '  ', '  ', '  ', '  ', '  ', '  '], ['\x1b[0;37;44m6 \x1b[0m', '\x1b[0;37;44m6 \x1b[0m', '\x1b[0;37;44m6 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '\x1b[0;37;44m6 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '\x1b[0;37;44m6 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
    #print(check_move(tetramino, grid))
    return (check_move(tetramino, grid) == False)


def test_check_move_2():
    tetramino = [[(0, 0), (0, 1), (0, 2), (1, 1)], '0;37;43', (0, 0)]
    grid = ([['\x1b[0;37;43m1 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '  ', '  ', '  '], ['\x1b[0;37;43m1 \x1b[0m', '\x1b[0;37;43m1 \x1b[0m', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '\x1b[0;37;45m3 \x1b[0m', '  ', '  ', '  '],
            ['\x1b[0;37;43m1 \x1b[0m', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m',
                '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--',
            '--', '--', '  ', '  ', '  ', '  ', '  ', '  '],
             ['\x1b[0;37;46m4 \x1b[0m', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ', '  ',
             '  ', '| ', '\x1b[0;37;42m5 \x1b[0m', '\x1b[0;37;42m5 \x1b[0m', '  ', '  ', '  '],
             ['  ', '  ', '  ',
             '  ', '  ', ' |', '  ', '  ', '  ', '  ', '  ', '| ', '  ', '\x1b[0;37;42m5 \x1b[0m', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
             '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
             '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--',
             '--', '--', '  ', '  ', '  ', '  ', '  ', '  '],
             ['\x1b[0;37;44m6 \x1b[0m', '\x1b[0;37;44m6 \x1b[0m', '\x1b[0;37;44m6 \x1b[0m', '  ',
             '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '\x1b[0;37;44m6 \x1b[0m', '  ', '  ', '  ', '  ',
             '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '\x1b[0;37;44m6 \x1b[0m', '  ', '  ', '  ', '  ',
             '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
             ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']])
    return (check_move(tetramino, grid) == True)


def test_check_win_1():
    grid = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--', '--', '--', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', ' |', '\x1b[0;37;46m1 \x1b[0m', '\x1b[0;37;41m4 \x1b[0m', '\x1b[0;37;41m4 \x1b[0m', '\x1b[0;37;41m4 \x1b[0m', '\x1b[0;37;41m4 \x1b[0m', '| ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', ' |', '\x1b[0;37;46m1 \x1b[0m', '\x1b[0;37;44m5 \x1b[0m', '\x1b[0;37;44m5 \x1b[0m', '\x1b[0;30;47m7 \x1b[0m', '\x1b[0;37;42m2 \x1b[0m', '| ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', ' |', '\x1b[0;37;46m1 \x1b[0m', '\x1b[0;37;46m1 \x1b[0m', '\x1b[0;37;44m5 \x1b[0m', '\x1b[0;30;47m7 \x1b[0m', '\x1b[0;37;42m2 \x1b[0m', '| ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', ' |', '\x1b[0;37;46m1 \x1b[0m', '\x1b[0;37;44m5 \x1b[0m', '\x1b[0;37;44m5 \x1b[0m', '\x1b[0;37;42m2 \x1b[0m', '\x1b[0;37;42m2 \x1b[0m', '| ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', ' |', '\x1b[0;37;43m3 \x1b[0m', '\x1b[0;37;43m3 \x1b[0m', '\x1b[0;37;43m3 \x1b[0m', '\x1b[0;37;42m2 \x1b[0m', '\x1b[0;37;45m6 \x1b[0m', '| ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', ' |', '\x1b[1;37;40m8 \x1b[0m', '\x1b[0;37;43m3 \x1b[0m', '\x1b[0;37;45m6 \x1b[0m', '\x1b[0;37;45m6 \x1b[0m', '\x1b[0;37;45m6 \x1b[0m', '| ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--', '--', '--', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
    return (check_win(grid) == True)


def test_check_win_2():
    grid = [['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m', '  ',
             '  ', '  ', '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m', '  ', '  ',
             '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '\x1b[0;37;45m3 \x1b[0m', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '\x1b[0;37;41m2 \x1b[0m', '  ',
             '  ', '  ', '  ', '\x1b[0;37;45m3 \x1b[0m', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '\x1b[0;37;43m1 \x1b[0m', '\x1b[0;37;43mXX\x1b[0m',
             '\x1b[0;37;43mXX\x1b[0m', '--', '--', '--', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', ' |', '\x1b[0;37;43m1 \x1b[0m',
             '\x1b[0;37;44m6 \x1b[0m', '  ', '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '\x1b[0;37;44m6 \x1b[0m', '  ',
             '  ', '  ', '\x1b[0;37;42mXX\x1b[0m', '\x1b[0;37;42m5 \x1b[0m', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '\x1b[0;37;44mXX\x1b[0m', '\x1b[0;37;44m6 \x1b[0m',
             '\x1b[0;37;44m6 \x1b[0m', '  ', '  ', '  ', '| ', '\x1b[0;37;42m5 \x1b[0m', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', ' |', '  ', '  ', '  ',
             '  ', '  ', '| ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '--', '--', '--',
             '--', '--', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
             '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
             '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
             '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]
    return (check_win(grid) == False)


print(test_check_win_2(), test_check_win_1(), test_check_move_1(), test_check_move_2(), test_create_grid(), test_import_tetraminos(), test_place_tetramino(), test_setup_tetraminos(), test_rotate_tetramino_1(), test_rotate_tetramino_2())