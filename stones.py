def remempty(piles):
    while 0 in piles:
        piles.remove(0)
    return piles

def newpile(piles):
    p = 0
    for i in range(len(piles)):
        if piles[i] > 0:
            piles[i] -= 1
            p += 1
    piles.append(p)
    piles = remempty(piles)
    return piles

def move(piles):
    if piles[0] == 1:
        del piles[0]
    else:
        piles = newpile(piles)
    return piles

def play(piles):
    while len(piles) > 0:
        print(piles)
        piles = move(piles)
