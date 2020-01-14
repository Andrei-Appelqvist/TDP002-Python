import os


def read_level():
    obj_inv = {"#": 1, "@": 3, "o": 4, ".": 5}
    y = 0
    x = 0
    field = []
    file = ""
    print("Please choose a level:")
    print("1. first level")
    print("2. second level")

    lvl = input("")
    if lvl == "1":
        file = "first_level.sokoban"
    elif lvl == "2":
        file = "second_level.sokoban"

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
    for x in range(width(field)+1):
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


def inp_check(key):
    movements = {"W": 1, "A": 2, "S": 3, "D": 4, "Q": 5}
    if key == "W" or key == "A" or key == "S" or key == "D":
        return movements[key]
    elif key == "Q":
        return 5

def player_search(field):
    for p in field:
        if p[2] == 3:
            return p


def move_player(field):
    movements = ["W", "A", "S", "D", "Q"]
    while True:
        move_key = str(input("Ange W = Upp, A = Vänster, S = Ner, D = Höger: "))
        if move_key.upper() not in movements or len(move_key) > 1:
            True
        else:
            break
    dry_key = inp_check(move_key.upper())
    player = player_search(field)
    move(player, field, dry_key)

def object_y_value(object):
    return object[0]

def object_x_value(object):
    return object[1]

def object_type_value(object):
    return object[2]

def object_new_position(object, move_value):
    if move_value == 1:
        obj_new_pos = [object_y_value(object) - 1, object_x_value(object), object_type_value(object)]
        return obj_new_pos

    elif move_value == 2:
        obj_new_pos = [object_y_value(object), object_x_value(object) - 1, object_type_value(object)]
        return obj_new_pos

    elif move_value == 3:
        obj_new_pos = [object_y_value(object) + 1, object_x_value(object), object_type_value(object)]
        return obj_new_pos

    elif move_value == 4:
        obj_new_pos = [object_y_value(object), object_x_value(object) + 1, object_type_value(object)]
        return obj_new_pos

def move(object, field, move_value):
    obj_new_pos = object_new_position(object, move_value)
    if move_value == 1:
        if move_checker(obj_new_pos, field, move_value) == True:
            object[0] -= 1
            return field
        else:
            return field

    if move_value == 2:
        if move_checker(obj_new_pos, field, move_value) == True:
            object[1] -= 1
            return field
        else:
            return field
    if move_value == 3:
        if move_checker(obj_new_pos, field, move_value) == True:
            object[0] += 1
            return field
        else:
            return field

    if move_value == 4:
        obj_new_pos = [object_y_value(object), object_x_value(object) + 1, object_type_value(object)]
        if move_checker(obj_new_pos, field, move_value) == True:
            object[1] += 1
            return field
        else:
            return field

    if move_value == 5:
        field[0][2] = 3 #Det här är fult men funkar
        return field

def move_checker(obj_new_pos, field, move_value):
    for checker in field:
        if obj_new_pos[1] == checker[1] and obj_new_pos[0] == checker[0]:
            if checker[2] == 1:
                return False
            elif checker[2] == 4:
                if obj_new_pos[2] == 4:
                    return False
                elif next_checker(checker, field, move_value) == False:
                    return False
                else:
                    box_mover(checker, field, move_value)
            else:
                return True
    return True


def box_mover(box, field, move_value):
    move(box, field, move_value)

def next_checker(object, field, move_value):
    obj_new_pos = object_new_position(object, move_value)
    if move_checker(obj_new_pos, field, move_value) == False:
        return False
    else:
        return True

def done_check(field):
    val_box = []
    val_goal = []
    for i in field:
        if i[2] == 4:
            val_box.append([i[0], i[1]])
    for b in field:
        if b[2] == 5:
            val_goal.append([b[0], b[1]])
    #print(val_box)
    #print(val_goal)
    for box in val_box:
        if box not in val_goal:
            return False
    return True

def start_game():
    level = read_level()
    is_done = False

    while not is_done:
        sokoban_display(level)
        move_player(level)
        if level[0][2] == 3:
            print("You quit!")
            break
        if done_check(level) == False:
            is_done = False
            os.system('clear')
        else:
            print("You won!")
            is_done = True




start_game()