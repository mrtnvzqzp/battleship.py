#setup
scores = [0, 0]
turn = "p1"
def checkscore():
    print("p1: " + str(scores[0]))
    print("p2: " + str(scores[1]))
checkscore()


#boards
def board():
    B = [[0, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]]
    i = 1
    while i < 11:
        B.append([i, " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
        i += 1
    return B
    
P1S = board()
P1A = board()
P2S = board()
P2A = board()

def boardn():
    N = [["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"]]
    i = 1
    while i < 11:
        N.append(["N", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "N"])
        i += 1
    N.append(["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N"])
    return N

P1N = boardn()
P2N = boardn()


#players
player1 = []
player2 = []

#display
def display(S, sign):
    print(sign)
    for i in S:
        print(i)


#set up ships
#NNN

def setb(ss, su):
    ss.append(ss[0])
    ss.append(ss[0])
    diff = su[1] - su[0]
    su.insert(0, su[0] - diff)
    su.append(su[-1] + diff)

def NNN(pship, N):
    sx = pship[2]
    sy = pship[3]
    if same(sx):
        setb(sx, sy)
    elif same(sy):
        setb(sy, sx)
    i = 0
    while i < len(sx):
        N[sx[i]][sy[i]] = "N"
        i += 1

#procesship
def stringtoint(strin):
    intl = []
    for i in strin:
        intl.append(int(i))
    return intl


def processship(inp, life):
    shipcoor = []
    inpu = stringtoint(inp)
    shipx = inpu[::2]
    shipy = inpu[1::2]
    i = 0
    while i < life:
        inc = [shipx[i], shipy[i]]
        shipcoor.append(inc)
        i += 1
    pship = [life, shipcoor, shipx, shipy]
    return pship
    
#checkship

#gri
def same(check):
    c = check[0]
    samecheck = True
    for i in check:
        if i != c:
            samecheck = False
    return samecheck
    
def checkstep(thing):
    check = False
    diff = int(thing[1]) - int(thing[0])
    if diff != 0:
        check = True
    i = 1
    while i < len(thing):
        if int(thing[i]) - int(thing[i - 1]) != diff:
            check = False
        i += 1
    return check

def gri(inp):
    shipx = inp[::2]
    shipy = inp[1::2]
   

    if (same(shipx) and checkstep(shipy)) or (same(shipy) and checkstep(shipx)):
        return True
  
    else:
        return False  
        
#allowed
def allowed(inp, N):
    alll = True
    i = 0
    while i < len(inp):
        if N[int(inp[i])][int(inp[i+1])] == "N":
            alll = False
        i += 2 
    return alll


def checkship(inp, life, N):
    if life == len(inp) / 2 and gri(inp) == True and allowed(inp, N) == True:
        return True
    else:
        return False
        
#attack
def attack(fire, B, C, i, player):
    print("a")
    
    ff = fire.split(" ")
    target = B[int(ff[0])][int(ff[1])]
    print("b")
    if target == "O":
        scores[i] += 1
        B[int(ff[0])][int(ff[1])] = "X"
        C[int(ff[0])][int(ff[1])] = "X"
        print("hit")
        shot = [int(ff[0]), int(ff[1])]
        for hitt in player:
            if shot in hitt[1]:
                hitt[0] -= 1
            if hitt[0] == 0:
                print("ship sank")
    elif target == " ":
        B[int(ff[0])][int(ff[1])] = "V"
        C[int(ff[0])][int(ff[1])] = "V"
        print("miss")        
    
#input ship     
def inship(ship, n, life, B, N, player):
    
    inp = ship.split(" ")
    while checkship(inp, life, N) == False:
        ship = input("ship" + str(n) + ":")
        inp = ship.split(" ")
        
    pship = processship(inp, life)
    for c in pship[1]:
        B[c[0]][c[1]] = "O"
    player.append(pship)
    
    NNN(pship, N)
  
 #game 
    
 # place ships
display(P1S, "p1 ships")
P1ship1 = input("ship1: ")
inship(P1ship1, 1, 3, P1S, P1N, player1)
display(P1S, "p1 ships")
display(P2S, "p2 ships")
P2ship1 = input("ship1: ")
inship(P2ship1, 1, 3, P2S, P2N, player2)
display(P2S, "p2 ships")

display(P1S, "p1 ships")
P1ship1 = input("ship2: ")
inship(P1ship1, 2, 3, P1S, P1N, player1)
display(P1S, "p1 ships")
display(P2S, "p2 ships")
P2ship1 = input("ship2: ")
inship(P2ship1, 2, 3, P2S, P2N, player2)
display(P2S, "p2 ships")

display(P1S, "p1 ships")
P1ship1 = input("ship3: ")
inship(P1ship1, 3, 4, P1S, P1N, player1)
display(P1S, "p1 ships")
display(P2S, "p2 ships")
P2ship1 = input("ship3: ")
inship(P2ship1, 3, 4, P2S, P2N, player2)
display(P2S, "p2 ships")


#game
while scores[0] < 10 and scores[1] < 10:
 
    if turn == "p1":
        
        display(P1S, "p1 ships")
        display(P1A, "p1 target")
        fire = input("p1 attack:")
        attack(fire, P2S, P1A, 0, player2)
        display(P1A, "p1 target")
        turn = "p2"
    else:
        
        display(P2S, "p2 ships")
        display(P2A, "p2 target")
        fire = input("p2 attack:")
        attack(fire, P1S, P2A, 1, player1)
        display(P2A, "p2 target")
        turn = "p1"
    checkscore()
    
    #result       
if scores[0] == 10:
    print("player 1 wins")
if scores[1] == 10:
    print("player 2 wins")


