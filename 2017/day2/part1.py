
with open('input.txt', 'r') as f:
    lines = f.readlines()
    totals = []

    for line in lines:
        line = sorted(
            [int(num) for num in line.split()]
        )
        totals.append(line[-1] - line[0])

print sum(totals)
