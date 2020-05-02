###############################################
#                                             #
#              PoC: Smartshark                #
#                                             #
#                  USAGE:                     #
#                                             #
#        Script to clean datasets             #
#                                             #
#  Print only the asked rows (benign or not)  #
#     Select by pressing 1 for benign and     #
#        2 for not benign at the start        #
#                                             #
###############################################

import sys

#Choose your file
fichier = open("/run/media/Thytu/VDA/SmartShark/Datasets/DDoS/Portmap.csv", "r")

wanted = 0
while (wanted != '1\n' and wanted != '2\n'):
   #Press 1 to get only benigns packets and 2 to get DS whithout benigns packets
    wanted = sys.stdin.readline()


def is_a_benign_packet(line):
    if (len(line) >= len('benign\n') and line[len(line) - 1] == '\n' and line[len(line) - 2] == 'N' and line[len(line) - 3] == 'G' and line[len(line) - 4] == 'I' and line[len(line) - 5] == 'N' and line[len(line) - 6] == 'E' and line[len(line) - 7] == 'B'):
        return True
    elif (len(line) >= len('benign') and line[len(line) - 1] == 'N' and line[len(line) - 2] == 'G' and line[len(line) - 3] == 'I' and line[len(line) - 4] == 'N' and line[len(line) - 5] == 'E' and line[len(line) - 6] == 'B'):
        return True
    else:
        return False

result = ""
for line in fichier:
    if (wanted == '1\n' and is_a_benign_packet(line)):
        result = result + line
    elif (wanted == '2\n' and is_a_benign_packet(line) == False):
        result = result + line
print (result)
fichier.close()
