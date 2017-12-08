

f = open('input.txt', 'r')
line = f.readline().strip()

line = list(line) 

total = 0

for pos, number in enumerate(line):
    previous_number = line[pos-int(len(line)-1)]

    if number == previous_number:
        total += int(number)

print total



