angol_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
eoltolt_abc = angol_abc[16:] + angol_abc[:16]
# print(angol_abc)
# print(eoltolt_abc)
vers = ''
with open('caesar.txt', 'r', encoding='utf-8') as f:
    for line in f:
        for ch in line:
            if ch.upper() in angol_abc:
                index = eoltolt_abc.find(ch.upper())
                if ch.upper() == ch:
                    vers += angol_abc[index]
                else:
                    vers += angol_abc[index].lower()
            else:
                vers += ch
print(vers)
