###############################################
#                                             #
#              PoC: Smartshark                #
#                                             #
#                  USAGE:                     #
#      python3 ds_preprocess.py > FILE        #
#                                             #
#                                             #
# Script to preprocess datasets and redirect  #
#         output to your new file             #
#                                             #
###############################################

import statistics as st

fichier = open("app/static/SmartShark/save/temp_2.pcap_Flow.csv", "r")

result = {
    "Delta time" : [],
    "Len" : [],
    "Proto": [],
    "Total delta": [],
    "Total len": [],
    "Average delta": [],
    "Average len": [],
    "Delta std": [],
    "Len std": []
}

def Get_X_value(value_nb, line):
    index1 = 0
    index2 = 0
    for index1, char in enumerate(line):
        if char == ',' or char == '\n' or char == "\0":
            break
    for index2, char in enumerate(line):
        if (char == ',' or char == '\n' or char == "\0") and index2 > index1:
            break
    return float(line[index1 + 1:index2])

for index, line in enumerate(fichier):
    result["Delta time"].append(Get_X_value(0, line))
    result["Len"].append(Get_X_value(1, line))
    result["Proto"].append(Get_X_value(2, line))
    if index > 0:
        result["Total delta"].append(result["Total delta"][index - 1] + result["Delta time"][index])
        result["Total len"].append(result["Total len"][index - 1] + result["Len"][index])
        result["Average delta"].append(result["Total delta"][index] / index)
        result["Average len"].append(result["Total len"][index] / index)
        result["Delta std"].append(st.pstdev(result['Delta time']))
        result["Len std"].append(st.pstdev(result['Len']))
    else:
        result["Total delta"].append(result["Delta time"][0])
        result["Total len"].append(result["Len"][0])
        result["Average delta"].append(result["Delta time"][0])
        result["Average len"].append(result["Len"][0])
        result["Delta std"].append(0.0)
        result["Len std"].append(0.0)

for index, dict_name in enumerate(result):
    if index != 0:
        print(", " + dict_name, end="")
    else:
        print(dict_name, end="")

print()
for i in range(len(result["Len"])):
    print(f'{result["Total delta"][i]}, {result["Total len"][i]}, {result["Average delta"][i]}, {result["Average len"][i]}, {result["Delta std"][i]}, {result["Len std"][i]}')
fichier.close()