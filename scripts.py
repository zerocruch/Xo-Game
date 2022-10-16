import random

def x_o():
    c=input("X Ou O : ")
    if(c.upper()!="X" and c.upper()!="O"):
        x_o()
    else:
        return c.upper()
def inv(c):
    if(c=="X"):
        return "O"
    else:
        return "X"

def place():
    print("chose place 1 -->9")
    x=int(input(":"))
    switcher = {
        1:"0,0",
        2:"0,1",
        3:"0,2",
        4:"1,0",
        5:"1,1",
        6:"1,2",
        7:"2,0",
        8:"2,1",
        9:"2,2"
    }
    return switcher.get(x)

def place2(x):
    switcher = {
        1:"0,0",
        2:"0,1",
        3:"0,2",
        4:"1,0",
        5:"1,1",
        6:"1,2",
        7:"2,0",
        8:"2,1",
        9:"2,2"
    }
    return switcher.get(x)

def l_print(l):
    for i in range(3):
        print(l[i][0]," | ",l[i][1]," | ",l[i][2])
def pc_turn(l,p):
    r=random.randint(1,9)
    x=place2(r)
    x1=int(x[0])
    x2=int(x[2])
    if (l[x1][x2] != "X" and l[x1][x2] != "O"):
        l[x1][x2] = p
    else:
        pc_turn(l,p)
def check(l):
    l1=[""]
    l2=[""]
    l3=[[""],[""],[""]]
    l4 = [["", "", ""], ["", "", ""], ["", "", ""]]
    s=""
    s2=""
    #diag 1
    for i in range(3):
        s+=l[i][i]
    l1[0]=s
    #diag 2
    for i in range(3):
        s2+=l[i][2-i]
    l2[0]=s2
    for i in range(3):
        l3[i]=l[i][0]+l[i][1]+l[i][2]
    for i in range(3):
        l4[i]=l[0][i]+l[1][i]+l[2][i]
    x_win=0
    o_win=0
    #check winner in l1
    if("XXX" in l1 and x_win+o_win==0):
        print("X Winner")
        x_win+=1
    elif("OOO" in l1 and x_win+o_win==0):
        print("O Winner")
        o_win+=1
    #check l2
    if("XXX" in l2 and x_win+o_win==0):
        print("X Winner")
        x_win+=1
    elif("OOO" in l2 and x_win+o_win==0):
        print("O Winner")
        o_win+=1
    #check l3
    for x in l3:
        if(x=="XXX" and x_win+o_win==0):
            print("X Winner")
            x_win+=1
        elif(x=="OOO" and x_win+o_win==0):
            print("O Winner")
            o_win+=1
    #check l4
    for x in l4:
        if(x=="XXX" and x_win+o_win==0):
            print("X Winner")
            x_win += 1
        elif(x=="OOO" and x_win+o_win==0):
            print("O Winner")
            o_win += 1
    if(x_win>0):
        return False
    elif(o_win>0):
        return False
    else:
        return True
def lists(l):
    l1 = [""]
    l2 = [""]
    l3 = [[""], [""], [""]]
    l4 = [["", "", ""], ["", "", ""], ["", "", ""]]
    s = ""
    s2 = ""
    # diag 1
    for i in range(3):
        s += l[i][i]
    l1[0] = s
    # diag 2
    for i in range(3):
        s2 += l[i][2 - i]
    l2[0] = s2
    for i in range(3):
        l3[i] = l[i][0] + l[i][1] + l[i][2]
    for i in range(3):
        l4[i] = l[0][i] + l[1][i] + l[2][i]

def pc_turn2(l,p):
    r=random.randint(1,9)
    x=place2(r)
    x1=int(x[0])
    x2=int(x[2])
    if (l[x1][x2] != "X" and l[x1][x2] != "O"):
        l[x1][x2] = p
    else:
        pc_turn(l,p)











