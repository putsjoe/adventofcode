
with open('input.txt', 'r') as f:
    lines = f.readlines()
    totals = []

    for line in lines:
        line = [int(num) for num in line.split()]
        for value in line:
            for val in line:
                if value != val and value % val == 0:
                    totals.append(value / val)

print sum(totals)
