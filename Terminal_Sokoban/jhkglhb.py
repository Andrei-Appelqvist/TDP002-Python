def read_level():
    obj_inv = {"#": 1, "@": 3, "o": 4, ".": 5}
    y = 0
    x = 0
    field = []
    file = "first_level.sokoban"
    test_level = open(file, "r")
    for line in test_level:
        for char in line:
            if char == " " or char == "\n":
                field = field
            else:
                field.append([y, x, obj_inv[char]])
            x += 1
        x = 0
        y += 1
    return field


def grid(field):
    print_grid = []
    for x in range(width(field) + 1):
        small_grid = []
        for y in range(height(field) + 1):
            small_grid.append([x, y])
        print_grid.append(small_grid)
    return print_grid


def grid_adapt(field, x, y, v):
    field.append([x, y, v])
    return field


def sokoban_walls(field, x, y):
    grid_adapt(field, x, y, 1)


def sokoban_player(field, x, y):
    grid_adapt(field, x, y, 3)


def sokoban_display(field):
    obj_translate = {1: "#", 2: " ", 3: "@", 4: "o", 5: "."}
    display_field = grid(field)
    for x_value in field:
        display_field[x_value[0]][x_value[1]].append(obj_translate[x_value[2]])
    for lines in display_field:
        clean_print = ""
        for spaces in lines:
            if len(spaces) == 2:
                spaces.append(obj_translate[2])
            clean_print += str(spaces[2])
        print(clean_print)


def width(field):
    max_width = 0
    for line in field:
        if line[0] > max_width:
            max_width = line[0]
    return max_width


def height(field):
    max_height = 0
    for line in field:
        if line[1] > max_height:
            max_height = line[1]
    return max_height


def player_search(field):
    for p in field:
        if p[2] == 3:
            return p

def get_box(field): #letar efter första lådan, behöver ändras
    for p in field:
        if p[2] == 4:
            return p

def get_key():
    key = input("Vad vill du göra? (WASD) :")
    return key

def get_object(y, x, field):
    for o in field:
        if o[0] == y and o[1] == x and len(o) == 3:
            if o[2] == 1:
                return "wall"
            elif o[2] == 3:
                return "player"
            elif o[2] == 4:
                return "box"
            elif o[2] == 5:
                return "goal"
        else:
           return "space"



def move(key, obj):
    if key == "d":
        obj[1] += 1
    elif key == "a":
        obj[1] -= 1
    elif key == "w":
        obj[0] -= 1
    elif key == "s":
        obj[0] += 1
    return obj

def player_check_next(key, field):
    p = player_search(field)
    cur_x = p[1]
    cur_y = p[0]
    if key == "d":
        next_x = cur_x + 1
        next_y = cur_y
    elif key == "a":
        next_x = cur_x - 1
        next_y = cur_y
    elif key == "w":
        next_x = cur_x
        next_y = cur_y - 1
    elif key == "s":
        next_x = cur_x
        next_y = cur_y + 1
    return get_object(next_y, next_x, level)




level = read_level()
sokoban_display(level)
print(player_check_next("w", level))


"""
level = read_level()
print(level)
print(get_object(2, 5, level))
box = get_box(level)
sokoban_display(level)
move("w", box)
sokoban_display(level)
"""