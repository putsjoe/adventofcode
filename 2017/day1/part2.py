
f = open('input.txt', 'r')
line = list(f.readline().strip())

total = 0

for position, number in enumerate(line):
    previous_number = line[position-int(len(line)/2)]

    if number == previous_number:
        total += int(number)

print total

