angol_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
eltolt_abc = angol_abc[16:] + angol_abc[:16]
# print(angol_abc)
# print(eltolt_abc)
vers = ''
with open('caesar.txt', 'r', encoding='utf-8') as file:
    for line in file:
        for ch in line:
            if ch.upper() in angol_abc:
                index = eltolt_abc.find(ch.upper())
                if ch.upper() == ch:
                    vers += angol_abc[index]
                else:
                    vers += angol_abc[index].lower()
            else:
                vers += ch

print(vers)