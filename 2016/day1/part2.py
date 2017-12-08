

x = 0
y = 0
locations = []
blocks = 0

with open('input.txt', 'r') as input_txt:
    data = input_txt.read().split(', ')


def addx(x, y, distance, blocks):
    print x
    print x + distance
    while x != (x + distance):
        x = x + 1
        blocks += 1
        if (x, y) in locations:
            assert False, blocks
        locations.append((x, y))


def minusx(x, y, distance, blocks):
    while x != (x - distance):
        x -= 1
        blocks += 1
        if (x, y) in locations:
            assert False, blocks
        locations.append((x, y))


def addy(x, y, distance, blocks):
    while y != (y + distance):
        y += 1
        blocks += 1
        if (x, y) in locations:
            assert False, blocks
        locations.append((x, y))


def minusy(x, y, distance, blocks):
    while y != (y - distance):
        y -= 1
        blocks += 1
        if (x, y) in locations:
            assert False, blocks
        locations.append((x, y))


for index, e in enumerate(data):
    direction = e[0]
    distance = int(e.strip('L').strip('R'))

    if index == 0:
        if direction == 'L':
            facing = 'w'
            minusx(x, y, distance, blocks)
            x = x - distance
        elif direction == 'R':
            facing = 'e'
            addx(x, y, distance, blocks)
            x = x + distance
    elif index > 0:
        if facing == 'n':
            if direction == 'L':
                minusx(x, y, distance, blocks)
                x = x - distance
                facing = 'w'
                
            elif direction == 'R':
                addx(x, y, distance, blocks)
                x = x + distance
                facing = 'e'
                
        elif facing == 'e':
            if direction == 'L':
                addy(x, y, distance, blocks)
                y = y + distance
                facing = 'n'
            elif direction == 'R':
                minusy(x, y, distance, blocks)
                y = y - distance
                facing = 's'
            
        elif facing == 's':
            if direction == 'L':
                addx(x, y, distance, blocks)
                x = x + distance
                facing = 'e'
            elif direction == 'R':
                minusx(x, y, distance, blocks)
                x = x - distance
                facing = 'w'
            
        elif facing == 'w':
            if direction == 'L':
                minusy(x, y, distance, blocks)
                y = y - distance
                facing = 's'
            elif direction == 'R':
                addy(x, y, distance, blocks)
                y = y + distance
                facing = 'n'
        print facing
        blocks = blocks + distance

    print e, x, y
            
print x
print y

print x - y
print '--'
