fichier = open("/run/media/Thytu/TOSHIBA EXT/PoC/Smartshark/DS/ds_benign_cleaned_div_3.csv", "r")

pos = 12 #pos to flatten

def flat_line(line, target):
    index = 0
    pos = 0
    for l in line:
        pos += 1
        if (l == ','):
            index += 1
        if index == target:
            break;
    print(line[:pos - 1])

for line in fichier:
    flat_line(line, pos)
