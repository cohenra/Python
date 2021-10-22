direction = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}

def find_start(data):
    for y in data:
        for x in y:
            if x in direction:
                dir_x, dir_y = direction[x]
                return (x, y, dir_x, dir_y)


def laser_dir(data, dir):
    i = data[dir[0]]
    z = i[dir[1]]
    print(i, z)
    for i in data:
        for z in i:
            if z == "/":
                print(z)



data = open("data1.txt").readlines()
x, y, dir_x, dir_y = find_start(data)
x += dir_x
y += dir_y
laser_dir(data, x, y)