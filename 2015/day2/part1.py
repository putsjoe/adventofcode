

total = 0
with open('input.txt', 'r') as input_txt:
    for line in input_txt:
        line = line.split('x')
        l = int(line[0])
        w = int(line[1])
        h = int(line[2].replace('\n', ''))
        
        calc = [(l*w), (w*h), (h*l)]
        slack = min(calc)
        
        total +=  sum(calc) * 2
        total += slack

print total
