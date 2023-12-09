from collections import defaultdict

# Reading input from file

with open("entrada.txt") as file:
    inp = file.readlines()
    inp = [line.strip() for line in inp]
    inp = [line for line in inp if line != ""]
seeds = inp[0].split(':')[1].split()
seeds=[int(e) for e in seeds]
maps=[]
ax = []
for e in inp[1:]:
    if e[-1] != ':':
        ax.append(e)
    elif len(ax)>0:
        maps.append(ax)
        ax=[]
maps.append(ax)
maps = [[[int(e) for e in m.split()] for m in mm] for mm in maps]
lditi=[]
diti=defaultdict(int)
for e in seeds:
    diti[e]=e
for j,mapi in enumerate(maps):
    vals=diti.values()
    diti=defaultdict(int)
    for i in vals: diti[i]=i
    for rng in mapi:
        for e in vals:
            if rng[1]<=e<rng[1]+rng[2]:
                diti[e]=e+rng[0]-rng[1]
            
    lditi.append(diti)
locations=[]
for e in seeds:
    ax=e
    for dit in lditi:
        ax=dit[ax]
    locations.append(ax)
print("Part1: ", min(locations))
