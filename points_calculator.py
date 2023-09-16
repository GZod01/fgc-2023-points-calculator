import sys
def intinput(prompt:str):
    while True:
        try:
            return int(input(prompt))
            break
        except ValueError:
            print("Value must be int")
def calcul_point(h:int,o:int,c:str):
    hydrogen_number:int=h
    oxygen_number:int=o


    conv_mult = {
        "N":1.0,
        "P":1.2,
        "F":1.3
    }

    conv_type:str=c
    conversion_multiplier:float=conv_mult[conv_type]

    proficiency_dict = {
        "D":0,
        "I":5,
        "E":10
    }
    rp:list = [0,0,0,0,0,0]
    exp_number:int=0
    for i in range(0,5):
        proficiency_type:str=input("proficiency_type (D for Developing, I for Intermediate, E for Expert): ")
        rp[i] = proficiency_dict[proficiency_type]
        if proficiency_type=="E":
            exp_number+=1
    bcp:int=0
    if exp_number==6:
        bcp = 30
    elif exp_number==5:
        bcp=15
    else:
        bcp = 0


    final_score = ((hydrogen_number+oxygen_number)*conversion_multiplier)+(rp[0]+rp[1]+rp[2]+rp[3]+rp[4]+rp[5])+bcp
    print(f"({hydrogen_number}+{oxygen_number})* {conversion_multiplier} + ({rp[0]}+{rp[1]}+{rp[2]}+{rp[4]}+{rp[5]})+{bcp}")
    return final_score

if len(sys.argv)>=2 and (sys.argv[1]=="help" or sys.argv[1]=="-h" or sys.argv[1]=="--help"):
    print("""Usage: points_calculator <hydrogen_number> <oxygen_number> <conversion_type>
    The Conversion Type can be N for No Alignment, P for Partial Alignment, F for Full Alignment""")
elif (len(sys.argv)<2):
    print(calcul_point(
        intinput("hydrogen_number: "),
        intinput("oxygen_number: "),
        input("conversion_type (N for No Alignment, P for Partial Alignment, F for Full Alignment): ")
    ))
else:
    print(calcul_point(sys.argv[1],sys.argv[2],sys.argv[3]))
