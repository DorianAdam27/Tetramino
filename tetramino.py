import sys
from getkey import getkey
import os


def import_card(file_path):
    """We use the open() function which is used to open external files, something like a txt file containing Names, or in our case all of the info about the tetraminos and grid."""
    carte = open(file_path)
    """Creating size, tetraminos and useful_counter_I_promise2. You will see later what they do"""
    size = None
    tetraminos = []
    useful_counter_I_promise2 = -1
    """We take carte(the file), use read() in order to see what is in the file and then split('/n') because /n appears at the end of each line inside the file, I think is means 'new line', 
    we split the entire file after each /n, which means we will be able to loop through the file and take each line instead of each character of the file for processing"""
    for i in carte.read().split('\n'):
        useful_counter_I_promise2 += 1
        """I used the useful_counter_I_promise2 to check if I'm curently at the first line, -1 +1 = 0 and that says that we are checking the first line which is the grid size. I know
        for sure that there is a better way to do this, but I was really tired that night and this is all I could come up with."""
        if useful_counter_I_promise2 == 0:
            """If we are indeed at the first line which is going to look something like this '5, 3', we take the line and split it on , and then we get two different values respresenting the dimentions
            of the grid. After we split the whole line, the values will come back as string, so we need to turn them into integers. Then we create a tuple holding these two values"""
            size1 = int(i.split(",")[0])
            size2 = int(i.split(",")[1])
            size = (size1, size2)
        else:
            """If the useful_counter_I_promise2 is greater than 0, it means that we are not at the first line, meaning we can start processing for the tetraminos. We go line by line
            and everytime we reach a new line we add another list inside tetraminos which holds all of the tetraminos(each ones info, piece location and color)"""
            tetraminos.append([])
            """Because we used useful_counter_I_promise2 to count each line, we can also use it to index each tetramino inside the tetraminos list. if useful_counter_I_promise2 is equal to 1
            we subtract 1 and end up with 0 which represents the first position inside of a list"""
            tetraminos[useful_counter_I_promise2-1].append([])
            useful_counter_I_promise = 0
            """Each line holds the piece's parts locations along with the color. These two are seperated with ;; and since we want to start with the locations we can split on ;;
            and take the first part which holds the locations
            After that the first part will hold the locations, but we want to go through the locations one by one and since they are seperated with ; we can also split on that."""
            for j in i.split(";;")[0].split(";"):
                """We take each locations tuple and we split it on the , and also get rid of the parenthesis, turn them into integers since they are now just strings and then just save them into a tuple"""
                coordinates_tuple = (int(j[1:-1].split(",")[0]), int(j[1:-1].split(",")[1]))
                """Here we just add that tuple to the tetraminos list, making sure that it goes to the right tetramino useful_counter_I_promise2-1 and to the right place inside that tetramino useful_counter_I_promise"""
                tetraminos[useful_counter_I_promise2-1][useful_counter_I_promise].append(coordinates_tuple)
                """Now we need the color of the tetramino and since we did split(";;")[0] to get the piece location, now we need split(";;")[1] to get the color. After that we also place it in the tetraminos list and to the right tetramino"""
            tetraminos[useful_counter_I_promise2-1].append(i.split(";;")[1][0:len(i.split(";;")[1])])
            tetraminos[useful_counter_I_promise2-1].append((0,0))
    """Now we just return the whole thing"""
    return (size, tetraminos)





def create_grid(w, h):
    width = 3 * w + 2
    height = 3 * h + 2

    grid = []

    current_w_of_grid = 0
    current_h_of_grid = 0

    for i in range(height):
        current_h_of_grid += 1
        grid.append([])
        for j in range(width):
            current_w_of_grid += 1
            if current_w_of_grid > ((width - w) / 2) and current_w_of_grid < (width - w) / 2 + w + 1 and (current_h_of_grid == ((height - h) / 2) or current_h_of_grid == (height - h) / 2 + h + 1):
                grid[i].append("--")
            elif current_w_of_grid == (width - w) / 2 and current_h_of_grid >= (height - h) / 2 + 1 and current_h_of_grid < (height - h) / 2 + h + 1:
                grid[i].append(" |")
            elif current_w_of_grid == (width - w) / 2 + w + 1 and current_h_of_grid >= (height - h) / 2 + 1 and current_h_of_grid < (height - h) / 2 + h + 1:
                grid[i].append("| ")
            else:
                grid[i].append("  ")
        current_w_of_grid = 0
    
    return grid

def setup_tetraminos(tetraminos, grid):
    sections = [(0, 0), (0, int((len(grid[0])+1)/3)), (0, int(2*((len(grid[0])+1)/3))), (int((len(grid)+1)/3), 0), (int((len(grid)+1)/3), int(2*((len(grid[0])+1)/3))), (int(2*((len(grid)+1)/3)), 0), (int(2*((len(grid)+1)/3)), int((len(grid[0])+1)/3)), (int(2*((len(grid)+1)/3)), int(2*((len(grid[0])+1)/3)))]
    for i in tetraminos:
        i[2] = sections[tetraminos.index(i)][::-1]
        for j in i[0]:
            grid[i[2][1] + j[1]][i[2][0] + j[0]] = '\x1b[' + i[1] + 'm' + str(tetraminos.index(i) + 1) + ' \x1b[0m'
    
    return (grid, tetraminos)

def place_tetraminos(tetraminos, grid):
    if grid[-1][0] == "order":
        order = grid[-1][1:]
        grid = grid[0:-1]
        for i in order:
            for j in tetraminos[i-1][0]:
                if tetraminos[i-1][2][1] + j[1] < len(grid) and tetraminos[i-1][2][0] + j[0] < len(grid[0]) and tetraminos[i-1][2][1] + j[1] > - 1 and tetraminos[i-1][2][0] + j[0] > - 1:
                    if grid[tetraminos[i-1][2][1] + j[1]][tetraminos[i-1][2][0] + j[0]] == "  " or grid[tetraminos[i-1][2][1] + j[1]][tetraminos[i-1][2][0] + j[0]] == '\x1b[' + tetraminos[i-1][1] + 'm' + str(i) + ' \x1b[0m':
                        grid[tetraminos[i-1][2][1] + j[1]][tetraminos[i-1][2][0] + j[0]] = '\x1b[' + tetraminos[i-1][1] + 'm' + str(i) + ' \x1b[0m'
                    else:
                        grid[tetraminos[i-1][2][1] + j[1]][tetraminos[i-1][2][0] + j[0]] = '\x1b[' + tetraminos[i-1][1] + 'm' + "XX" + '\x1b[0m'
    else:
        for i in tetraminos:
            for j in i[0]:
                if i[2][1] + j[1] < len(grid) and i[2][0] + j[0] < len(grid[0]) and i[2][1] + j[1] > - 1 and i[2][0] + j[0] > - 1:
                    if grid[i[2][1] + j[1]][i[2][0] + j[0]] == "  " or grid[i[2][1] + j[1]][i[2][0] + j[0]] == '\x1b[' + i[1] + 'm' + str(tetraminos.index(i) + 1) + ' \x1b[0m':
                        grid[i[2][1] + j[1]][i[2][0] + j[0]] = '\x1b[' + i[1] + 'm' + str(tetraminos.index(i) + 1) + ' \x1b[0m'
                    else:
                        grid[i[2][1] + j[1]][i[2][0] + j[0]] = '\x1b[' + i[1] + 'm' + "XX" + '\x1b[0m'
    
    return grid

def rotate_tetramino(tetramino, clockwise=True):
    if clockwise == True:
        for i in range(len(tetramino[0])):
            holderX = tetramino[0][i][0]
            holderY = tetramino[0][i][1] * -1
            tetramino[0][i] = (holderY, holderX)
    else:
        for i in range(len(tetramino[0])):
            holderX = tetramino[0][i][0] * -1
            holderY = tetramino[0][i][1]
            tetramino[0][i] = (holderY, holderX)
    
    return tetramino

def check_move(tetramino, grid):
    for i in tetramino[0]:
        if "XX" in grid[i[1] + tetramino[2][1]][i[0] + tetramino[2][0]]:
            return False
    return True

def check_win(grid):
    for i in range(int((len(grid) - 2) / 3 + 1), int(2 * ((len(grid) - 2) / 3 + 1) - 1)):
        for j in range(int((len(grid[0]) - 2) / 3 + 1), int(2 * ((len(grid[0]) - 2) / 3 + 1) - 1)):
            if grid[i][j] == "  ":
                return False
    
    return True

def tetramino_inside_grid(tetramino, grid):
    for i in tetramino[0]:
        if not ((i[1] + tetramino[2][1]) > ((len(grid) - 2)/3) and (i[1] + tetramino[2][1]) < (2 * ((len(grid) - 2)/3) + 1) and (i[0] + tetramino[2][0]) > ((len(grid[0]) - 2)/3) and (i[0] + tetramino[2][0]) < (2 * ((len(grid[0]) - 2)/3) + 1)):
            return False
    return True

def print_grid(grid, no_number):
    safe_piece = grid[-1][0]
    grid = grid[0:-1]
    max_width = 1
    for i in grid:
        if len(i) > max_width:
            row = i
            max_width = len(i)
    max_width = max_width * 2

    for i in range(max_width-1):
        print('\x1b[' + "107;1;1" + 'm' + "-" + '\x1b[0m', end="")
    print('\x1b[' + "107;1;1" + 'm' + "-" + '\x1b[0m', end="")
    print('\x1b[' + "107;1;1" + 'm' + "-" + '\x1b[0m', end="")
    print('\x1b[' + "107;1;1" + 'm' + "-" + '\x1b[0m')
    
    for i in grid:
        print('\x1b[' + "107;1;1" + 'm' + "|" + '\x1b[0m', end="")
        for j in range(0, len(i)):
            if i[j] == "--" or i[j] == " |" or i[j] == "| " or i[j] == "  ":
                print('\x1b[' + "107;1;1" + 'm' + i[j] + '\x1b[0m', end="")
            else:
                if no_number and i[j].split("m")[1][0] != str(safe_piece):
                    string = i[j]
                    print(string.split("m")[0] + "m" + " " + string.split("m")[1][1:] + "m", end="")
                else:
                    print(i[j], end="")
        print('\x1b[' + "107;1;1" + 'm' + "|" + '\x1b[0m')
    #str(tetraminos.index(i) + 1)

    for i in range(max_width-1):
        print('\x1b[' + "107;1;1" + 'm' + "-" + '\x1b[0m', end="")
    print('\x1b[' + "107;1;1" + 'm' + "-" + '\x1b[0m', end="")
    print('\x1b[' + "107;1;1" + 'm' + "-" + '\x1b[0m', end="")
    print('\x1b[' + "107;1;1" + 'm' + "-" + '\x1b[0m')

def main():
    width = import_card(sys.argv[1])[0][0]
    height = import_card(sys.argv[1])[0][1]

    initial_grid = create_grid(width, height)
    initial_tetraminos = import_card(sys.argv[1])[1]

    current_piece = 0

    tetraminos = setup_tetraminos(initial_tetraminos, initial_grid)[1]
    grid = setup_tetraminos(initial_tetraminos, initial_grid)[0]
    
    show_numbers = True
    show_piece_number = 0
    key_pressed = 0

    show_order = ["order"]
    for i in range(len(tetraminos)):
        show_order.append(i + 1)

    valid = False

    while True:
        if current_piece != 0:
            switch = show_order[show_order.index(current_piece)]
            show_order[show_order.index(current_piece)] = show_order[-1]
            show_order[-1] = switch

        empty_grid = create_grid(width, height)
        empty_grid.append(show_order)
        grid = place_tetraminos(tetraminos, empty_grid)
        grid.append([show_piece_number])
        #print(tetraminos)

        os.system('cls' if os.name == 'nt' else 'clear')
        if show_numbers:
            print_grid(grid, False)
        else:
            print_grid(grid, True)
        show_piece_number = 0

        if check_win(grid):
            break

        key_pressed = getkey()
        if key_pressed == b'1':
            current_piece = 1
            show_piece_number = 1
        if key_pressed == b'2':
            current_piece = 2
            show_piece_number = 2
        if key_pressed == b'3':
            current_piece = 3
            show_piece_number = 3
        if key_pressed == b'4':
            current_piece = 4
            show_piece_number = 4
        if key_pressed == b'5':
            current_piece = 5
            show_piece_number = 5
        if key_pressed == b'6':
            current_piece = 6
            show_piece_number = 6
        if key_pressed == b'7':
            current_piece = 7
            show_piece_number = 7
        if key_pressed == b'8':
            current_piece = 8
            show_piece_number = 8
        if current_piece <= len(tetraminos):
            if current_piece != 0:
                show_numbers = False
                if key_pressed == b'l':
                    tetraminos[current_piece - 1][2] = (tetraminos[current_piece - 1][2][0] + 1, tetraminos[current_piece - 1][2][1])
                if key_pressed == b'j':
                    tetraminos[current_piece - 1][2] = (tetraminos[current_piece - 1][2][0] - 1, tetraminos[current_piece - 1][2][1])
                if key_pressed == b'i':
                    tetraminos[current_piece - 1][2] = (tetraminos[current_piece - 1][2][0], tetraminos[current_piece - 1][2][1] - 1)
                if key_pressed == b'k':
                    tetraminos[current_piece - 1][2] = (tetraminos[current_piece - 1][2][0], tetraminos[current_piece - 1][2][1] + 1)
                if key_pressed == b'o':
                    rotate_tetramino(tetraminos[current_piece - 1], True)
                if key_pressed == b'u':
                    rotate_tetramino(tetraminos[current_piece - 1], False)
                if key_pressed == b'v' and tetramino_inside_grid(tetraminos[current_piece - 1], grid):
                    valid = check_move(tetraminos[current_piece - 1], grid)

        if valid:
            current_piece += 1
            if current_piece > len(tetraminos):
                current_piece = 1
            show_piece_number = current_piece

        valid = False
    return True
    




if __name__ == "__main__":
    main()
