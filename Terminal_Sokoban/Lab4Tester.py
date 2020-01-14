def read_level():
    local_plan = []
    file = "testlevel.txt"
    test_level = open(file, "r")
    x = 0
    for line in test_level:
        local_plan.append(level_render(line, x))
        x = x + 1
    return local_plan

def level_render(line, x):
    obj_inv = {"#": 1, " ": 2, "@": 3, "O": 4}
    local_lst = []
    y = 0
    for v in line:
        if v == "\n":
            return local_lst
        else:
            local_lst.append([x, y, obj_inv[v]])
        y = y + 1

def print_level(level):
    obj = {1: "#", 2: "", 3: "@", 4: "O"}
    for x in range(len(level)):
        print(level[x])

def grid():
    x_axis = 10
    field = []
    for x in range(x_axis):
        field.append(gird_render(x))
    return field

def gird_render(x):
    y_axis = 10
    local_field = []
    for y in range(y_axis):
        local_field.append([x, y])
    return local_field

def sokoban_walls(field, x, y):
    for render in field:
        for obj_render in render:
            if x == obj_render[0] and y == obj_render[1]:
                obj_render.append(int(1))
    return field

def sokoban_player(field, x, y):
    for render in field:
        for obj_render in render:
            if x == obj_render[0] and y == obj_render[1]:
                obj_render.append(int(3))
    return field

def sokoban_display(field):
    obj_translate = {1: "#", 3: "@", 4: "O"}
    for render in field:
        printline = ""
        for obj_render in render:
            try:
                if obj_render[2] == None:
                    continue
                else:
                    printline += (str(obj_translate[obj_render[2]]))
            except:
                printline += " "
        print(printline)

level = grid()
sokoban_walls(level, 1, 4)
sokoban_walls(level, 3, 4)
sokoban_walls(level, 2, 6)
sokoban_walls(level, 2, 2)
sokoban_player(level, 2, 4)
sokoban_display(level)
print(level)
