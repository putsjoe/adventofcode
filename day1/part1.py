

x = 0
y = 0

with open('input.txt', 'r') as input_txt:
    data = input_txt.read().split(', ')

# import ipdb; ipdb.set_trace()

for index, e in enumerate(data):
    direction = e[0]
    distance = int(e.strip('L').strip('R'))
    
    if index == 0:
        if direction == 'L':
            facing = 'w'
            x = x - distance
        elif direction == 'R':
            facing = 'e'
            x = x + distance
    elif index > 0:
        if facing == 'n':
            if direction == 'L':
                x = x - distance
                facing = 'w'
                
            elif direction == 'R':
                x = x + distance
                facing = 'e'
                
        elif facing == 'e':
            if direction == 'L':
                y = y + distance
                facing = 'n'
            elif direction == 'R':
                y = y - distance
                facing = 's'
            
        elif facing == 's':
            if direction == 'L':
                x = x + distance
                facing = 'e'
            elif direction == 'R':
                x = x - distance
                facing = 'w'
            
        elif facing == 'w':
            if direction == 'L':
                y = y - distance
                facing = 's'
            elif direction == 'R':
                y = y + distance
                facing = 'n'
        
    print e, x, y
            
print x
print y

print x - y

