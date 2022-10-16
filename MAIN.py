import scripts
import random
list=[["1","2","3"],["4","5","6"],["7","8","9"]]
#user
c=scripts.x_o()
#computer
pc=scripts.inv(c)
#print(random.randint(1,9))
nbr_c=0
nbr_p=0
auth=True
mode=1
while auth:
    scripts.l_print(list)
    if (nbr_c != 5):
        p=scripts.place()
        i=int(p[0])
        j=int(p[2])
    else:
        #no one wins
        break
    if(list[i][j]!="X" and list[i][j]!="O"):
        list[i][j] = c
        nbr_c+=1
        auth=scripts.check(list)
        if(nbr_c!=5 and mode==0):
            scripts.pc_turn(list,pc)
            nbr_p+=1
            auth=scripts.check(list)
        elif(nbr_c!=5 and mode==1):
            scripts.pc_turn2(list,pc)
            nbr_p+=1
            auth=scripts.check(list)
    else:
        print("Already Taken")





