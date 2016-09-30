
total = 0
with open('input.txt', 'r') as input_txt:
    for line in input_txt:
        line = line.split('x')
        l = int(line[0])
        w = int(line[1])
        h = int(line[2].replace('\n', ''))

        all = [l, w, h]
        all.remove(max(all))
        total += sum(all) * 2
        total += l*w*h

print total
