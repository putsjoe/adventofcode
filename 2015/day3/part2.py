positions = [(0, 0), (0, 0) ]
pos = {'lat': 0, 'lon': 0}
robo-pos = {'lat': 0, 'lon': 0}

robo = False

with open('input.txt', 'r') as input_txt:
    while True:
        char = input_txt.read(1)
        if not char:
            break
        if char == '^':
            pos['lat'] -= 1
        elif char == '>':
            pos['lon'] += 1
        elif char == 'v':
            pos['lat'] += 1
        elif char == '<':
            pos['lon'] -= 1

        positions.append((pos['lat'], pos['lon']))
    
unique = len(set(positions))

print unique

