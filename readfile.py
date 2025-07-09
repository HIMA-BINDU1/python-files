f = open("data.txt", "r")
cnt = 1
for line in f:
    linee = line
for i in range(len(linee)-1):
    if linee[i+1] == " ":
        cnt += 1
print(cnt)