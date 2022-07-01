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

def Get_Result(N_Dice ,Rerolling = False, Discarding = 0):
    if Discarding:
        N_Dice = N_Dice+Discarding
    Array = Roll_Dice(N_Dice)
    if(Rerolling):
        Array = Reroll(Array)
    if(Discarding>0):
        Array = Discard_Lowest(Array,Discarding)
    return Sum_Array(Array)

def Count_Sim(Sim_Array, Damage):
    Sim_Array[Damage] += 1

def Run_Sim(N_Rolls, N_Dice ,Rerolling = False, Discarding = 0):
    i = 0
    Array = Make_Sim(N_Dice)
    while i < N_Rolls-(N_Dice*2)-1:
        tempy = Get_Result(N_Dice,Rerolling,Discarding)
        Array[tempy]+=1 
        i+=1
    # Array = Run_Math(Array)
    return Array

# def Run_Math(Array):
#     i = 0
#     while i < len(Array):
#         Array[i] =         
#         i+=1


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
        print(f"{i} Dice")
        j = 0
        while(j <= 3):
            Result = Run_Sim(10000,i,False,j)
            print(f"Rerolling {False} | Discarding {j} | Result {Result}")
            j+=1
        j = 0
        while(j <= 3):
            Result = Run_Sim(10000,i,False,j)
            print(f"Rerolling {False} | Discarding {j} | Result {Result}")
            j+=1

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
    File.write("N_Dice,Rerolling,Discarding,")
    File.write(Array_to_Line(Sim_header(Max_Dice)))
    New_Line(File)
    while i <= Max_Dice:
        j = 0
        while(j <= 3):
            Result = Array_to_Line(Run_Sim(10000,i,False,j))
            File.write(f"{i},{False},{j},{Result}")
            New_Line(File)
            j+=1
        j = 0
        while(j <= 3):
            Result = Array_to_Line(Run_Sim(10000,i,True,j))
            File.write(f"{i},{True},{j},{Result}")
            New_Line(File)
            j+=1

        i+=1
    File.close()
    return 

Print_Super_Sim(6)
CSV_Super_Sim(6)

# attack = Reroll(attack)
# print(attack)
# attack = Discard_Lowest(attack,5)
# print(attack)
