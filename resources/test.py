userbase = []

input = open("resources/matches.txt", "r")
for line in input:
    userbase.append(line.split())

for list in userbase:
        for i in range(1,len(list)):
            list[i] = int(list[i])
    

liste1 = ["Superrafi",0,0,0,0,0]

matches = []
for list in userbase:
    score = 0
    count = 0
    match = []
    for i in range(1,len(list)):
        if liste1[i] == 1 and liste1[i] == list[i]:
            score += 1
        if liste1[i] == 1:
             count += 1
        elif list[i] == 1:
             count += 1
    ergebnis = int(score*100/count)
    match.append(ergebnis)
    match.append(list[0])    
    matches.append(match)

matches.sort(reverse=True)

for entry in range(10):
    prozent = matches[entry][0]
    name = matches[entry][1]
    print(f"{name}: {prozent} %")