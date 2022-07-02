import random, math, time

DIE = [0, 0, 1, 1, 1, 2]
N_ROLLS = 1000000
DIE_MAX = DIE[len(DIE)-1]
DISCARD_MAX = 3

def Roll_A_Die():
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
        i += 1
    Array.sort()
    return Array


def Discard_Lowest(Array, Discard):
    i = 0
    while i < Discard:
        Array.pop(0)
        i += 1
    return Array


def Sum_Array(Array):
    total = 0
    for each in Array:
        total += each
    return total


def Get_Result(N_Dice, Rerolling=False, Discarding=0):
    if Discarding:
        N_Dice = N_Dice+Discarding
    Array = Roll_Dice(N_Dice)
    if(Rerolling):
        Array = Reroll(Array)
    if(Discarding > 0):
        Array = Discard_Lowest(Array, Discarding)
    return Sum_Array(Array)


def Count_Sim(Sim_Array, Damage):
    Sim_Array[Damage] += 1


def Run_Sim(N_Rolls, N_Dice, Rerolling=False, Discarding=0):
    i = 0
    Array = Make_Sim(N_Dice)
    while i < N_Rolls-(N_Dice*DIE_MAX)-1:
        tempy = Get_Result(N_Dice, Rerolling, Discarding)
        Array[tempy] += 1
        i += 1
    # Array = Run_Math(Array)
    return Array


def Run_EV(Array):
    i = 0
    while i < len(Array):
        Array[i] = Array[i] / N_ROLLS * i
        i += 1
    return Array



def Make_Sim(N_Dice):
    Array = []
    i = 0
    while i <= (N_Dice*2):
        Array.append(1)
        i += 1

    return Array

def Sum_EV(Array):
    Totes = 0
    for each in Array:
        Totes += each
    return round(Totes,1)

def Run_Category(N_Dice):
    Stringer = f"{N_Dice},"
    TF = [False,True]
    for each in TF:
        j = 0
        while(j <= DISCARD_MAX):
            print(f"Dice:{N_Dice} Reroll:{each} Discard:{j}")
            Result = Run_Sim(N_ROLLS, N_Dice, each, j)
            Result = Run_EV(Result)
            Result = Sum_EV(Result)
            Stringer+= f"{Result},"
            j+=1
    return Stringer[:-1]


def Super_Sim(Max_Dice):
    i = 1
    Stringer = ""
    while i <= Max_Dice:
        Stringer += Run_Category(i)
        Stringer += f"\n"

        i += 1
    Stringer += f"\n"
    return Stringer


def Sim_header(Max_Dice):
    Stringer  = "Rereoll,"
    i = 0
    while (i <= Max_Dice / 2):
        Stringer += "False,"
        i+=1
    i = 0
    while (i <= Max_Dice / 2):
        Stringer += "True,"
        i+=1
    Stringer = Stringer[:-1] + "\n"
    
    Stringer += "Discard,"
    i = 0
    while (i <= Max_Dice / 2):
        Stringer += f"{i},"
        i+=1
    i = 0
    while (i <= Max_Dice / 2):
        Stringer += f"{i},"
        i+=1
    Stringer = Stringer[:-1] + "\n"
    return Stringer


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
    File_Name = "SimFile.csv"
    File = open(File_Name, "w")
    i = 1
    File.write(Sim_header(Max_Dice))
    New_Line(File)
    writer = Super_Sim(6)
    File.write(writer)
    File.close()


start_time1 = time.time()
print(Super_Sim(6))
end_time1 = time.time()-start_time1
start_time = time.time()
CSV_Super_Sim(6)
end_time = time.time()-start_time
print(f"Sim 1---{end_time1} seconds---")
print(f"sim 2---{end_time} seconds---")

# attack = Reroll(attack)
# print(attack)
# attack = Discard_Lowest(attack,5)
# print(attack)
