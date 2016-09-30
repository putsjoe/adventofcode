

floor = 0
with open('input.txt', 'r') as input_txt:
    while True:
        char = input_txt.read(1)
        if not char:
            print "End"
            break
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
            
print floor
