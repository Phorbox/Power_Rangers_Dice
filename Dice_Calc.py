from array import array
import random
from subprocess import ABOVE_NORMAL_PRIORITY_CLASS
DIE = [0,0,1,1,1,2]

def Roll_A_Die ():
    return random.choice(DIE)

def Roll_Dice(N_Rolls):
    Array = []
    for each in range(N_Rolls):
        Array.append(Roll_A_Die())
    Array.sort()
    return Array

def Reroll(Array, Minimum=1):
    i = 0
    while i < len(Array) and Array[i] < Minimum:
        Array[i] = Roll_A_Die()
        i+=1
    Array.sort()
    return Array

def Discard_Lowest(Array,Discard):
    i = 0
    while i < Discard:
        Array.pop(0)
        i+=1
    return Array

def Sum_Array(Array):
    total = 0
    for each in Array:
        total += each
    return total

def Get_Result(N_Dice ,Rerolling = False, Discarding = False):
    if Discarding:
        N_Dice = N_Dice*2
    Array = Roll_Dice(N_Dice)
    if(Rerolling):
        Array = Reroll(Array)
    if(Discarding):
        Array = Discard_Lowest(Array,(N_Dice/2))
    return Sum_Array(Array)

def Count_Sim(Sim_Array, Damage):
    Sim_Array[Damage] += 1

def Run_Sim(N_Rolls, N_Dice ,Rerolling = False, Discarding = False):
    i = 0
    Array = Make_Sim(N_Dice)
    while i < N_Rolls-(N_Dice*2)-1:
        tempy = Get_Result(N_Dice,Rerolling,Discarding)
        Array[tempy]+=1 
        i+=1
    return Array

def Make_Sim(N_Dice):
    Array = []
    i = 0
    while i <= (N_Dice*2):
        Array.append(1)
        i+=1

    return Array

def Print_Super_Sim(Max_Dice):
    i = 1
    while i <= Max_Dice:
        print("{} Dice".format(i))
        print(Run_Sim(10000,i,False,False))
        print(Run_Sim(10000,i,True,False))
        print(Run_Sim(10000,i,False,True))
        print(Run_Sim(10000,i,True,True))
        i+=1
    return


def Sim_header(Max_Dice):
    Array = []
    i = 0
    while i <= Max_Dice*2:
        Array.append(i)
        i+=1
    return Array

def Array_to_Line(Array):
    Returner = ""
    for each in Array:
        temp = "{}".format(each)
        Returner = Returner + temp
        Returner = Returner + ","
    return Returner[:-1]



def New_Line(File):
    File.write("\n")

def CSV_Super_Sim(Max_Dice):
    File_Name ="SimFile.csv"
    File = open(File_Name,"w")
    i = 1
    File.write(",,")
    File.write(Array_to_Line(Sim_header(Max_Dice)))
    New_Line(File)
    while i <= Max_Dice:
        # File.write("{} Dice\n".format(i))
        File.write("{},Base,".format(i))
        File.write(Array_to_Line(Run_Sim(10000,i,False,False)))
        New_Line(File)

        File.write(",Reroll,")
        File.write(Array_to_Line(Run_Sim(10000,i,True,False)))
        New_Line(File)

        File.write(",Discard,")
        File.write(Array_to_Line(Run_Sim(10000,i,False,True)))
        New_Line(File)

        File.write(",Both,")
        File.write(Array_to_Line(Run_Sim(10000,i,True,True)))
        New_Line(File)
        i+=1
    File.close()
    return 

Print_Super_Sim(6)
CSV_Super_Sim(6)

# attack = Reroll(attack)
# print(attack)
# attack = Discard_Lowest(attack,5)
# print(attack)
