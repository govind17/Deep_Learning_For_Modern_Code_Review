clines = []

with open('/project/gshukla/GSCS/java3/train/code', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        words = line.lower().strip().split(' ')
        #words = line.strip().split(' ')
        clines.append(words)
    print(clines[3185])
    print('--------------------------')
nlines = []

with open('/project/gshukla/GSCS/java3/train/node', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        words = line.lower().strip().split(' ')
        #words = line.strip().split(' ')
        nlines.append(words)
    print(nlines[3185])
    print('--------------------------')
rlines = []
with open('/project/gshukla/GSCS/java3/train/review', 'r', encoding='utf-8') as file:
    count = 0
    for line in file.readlines():
        count = count + 1
        words = line.lower().strip().split(' ')
        #words = line.strip().split(' ')
        rlines.append(words)
    print(rlines[3185])
    print(len(clines),len(nlines),len(rlines), count)