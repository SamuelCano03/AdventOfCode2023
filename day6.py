with open("entrada.txt") as file:
    inp=file.readlines()
    inp = [line.strip() for line in inp]
    inp = [line for line in inp if line != ""]
inp = [line.split(':')[1] for line in inp]
inp = [[int(e) for e in line.split()] for line in inp]
time, dist=inp[0], inp[1]
ans = 1
for i in range(len(time)):
    aux = 0
    for t in range(1,time[i]):
        if (time[i]-t)*t>dist[i]: aux+=1
    ans*=aux
print("Part 1: ", ans)

# For part 2
time = int(''.join([str(e) for e in time]))
dist = int(''.join([str(e) for e in dist]))
ans = 0
for i in range(1,time):
    if (time-i)*i>dist: ans+=1
print("Part 2: ", ans)


