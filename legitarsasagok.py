legitarsasagok = []
with open('flights.csv', 'r') as f:
    f.readline()
    for line in f:
        carrier_name = (line.strip().split(',')[3]).replace('"', '')
        if not carrier_name in legitarsasagok:
            legitarsasagok.append(carrier_name)

with open('carriers.txt', 'w') as f:
    for legitarsasag in legitarsasagok:
        print(legitarsasag, file=f)