# Reading input from file
with open("entrada.txt") as file:
    inp = file.readlines()
    inp = [line.strip() for line in inp]
    inp = [line for line in inp if line != ""]
seeds = inp[0].split(':')[1].split()
seeds=[int(e) for e in seeds]
ranges=[(seeds[i],seeds[i+1],seeds[i]) for i in range(0,len(seeds), 2)]
maps=[]
ax = []
for e in inp[2:]:
    if e[-1] != ':':
        ax.append([int(d) for d in e.split()])
    else:
        maps.append(ax)
        ax=[]
maps.append(ax)
diti={}
for e in seeds: diti[e]=e

# For part 1
for mapi in maps:
    vals=diti.values()
    diti={}
    for i in vals: diti[i]=i
    for rng in mapi:
        for e in vals:
            if rng[1]<=e<rng[1]+rng[2]:
                diti[e]=e+rng[0]-rng[1]

ans = min(diti.values())
print("Part 1: ", ans)

# For part 2
for mapi in maps:
    auxrange=[]
    while ranges:
        _,le,st=ranges.pop()
        for rmapi in mapi:
            if le==0: break
            stRmapi=rmapi[1]
            leRmapi =rmapi[2]
            destRmapi =rmapi[0]
            if stRmapi <= st< stRmapi + leRmapi:
                if le <= leRmapi:
                    auxrange.append((st,le,destRmapi+st-stRmapi))
                    st=st+le
                    le=0
                else:
                    nle= leRmapi - (st-stRmapi)
                    auxrange.append((st, nle,destRmapi+st-stRmapi))
                    st=st+nle
                    le=le - nle
            elif st < stRmapi < st+le:
                if le <= leRmapi:
                    nle = le - (stRmapi - st)
                    auxrange.append((stRmapi,nle,destRmapi ))
                    le = le- nle
                else : 
                    nle = leRmapi
                    auxrange.append((stRmapi,nle, destRmapi))
                    dif = stRmapi - st
                    ranges.append((stRmapi+nle,le-nle-dif,stRmapi+nle))
                    le = stRmapi - st
        if le != 0:
            auxrange.append((st, le, st))
    ranges = auxrange
ans =ranges[0][2]
for rng in ranges:
    ans= min(ans, rng[2])
print("Part 2: ", ans)
