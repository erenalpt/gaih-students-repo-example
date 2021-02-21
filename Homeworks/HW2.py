grades = [[50.0,70.0,100.0], [90.0,65.0,80.0], [100.0,90.0,90.0],[50.0,40.0,80.0],[75.0,90.0,75.0]]
name = [["Bahtiyar CAN"], ["Necdet KIRCA"], ["Ahmet KONAK"], ["Bahar CAN"], ["Omar CHENGIZ"]]
info = {}

for key in range(len(name)):
    info[name[key][0]] = (grades[[key][0]][0]*0.25)+(grades[[key][0]][1]*0.25)+(grades[[key][0]][2]*0.5)

dscOrd = sorted(info.items(), key=lambda x: x[1], reverse=True)

print("Student Descending List")

for i in range(len(dscOrd)):
    print("{}. {} - {}".format(i+1,dscOrd[i][0],dscOrd[i][1], sep="\n"))


star = "*"
star *= len(dscOrd[0][0])+19

print("\n"+star)
print("** Congratulate {} **".format(dscOrd[0][0]))
print(star)

# OUTPUT
"""
Student Descending List
1. Ahmet KONAK - 92.5
2. Bahtiyar CAN - 80.0
3. Necdet KIRCA - 78.75
4. Omar CHENGIZ - 78.75
5. Bahar CAN - 62.5

******************************
** Congratulate Ahmet KONAK **
******************************
"""
