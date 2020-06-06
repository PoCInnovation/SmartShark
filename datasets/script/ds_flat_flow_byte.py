fichier = open("/run/media/Thytu/TOSHIBA EXT/PoC/Smartshark/DS/test_ds_DDOS.csv", "r")

pos = 13 #pos to flatten

def flat_line(line, target):
    index = 0
    pos = 0
    for l in line:
        print(l, end="")
        pos += 1
        if (l == ','):
            index += 1
        if index == target:
            break;
    line = line[pos:]
    save = pos
    pos = 0
    index = 0
    for l in line:
        pos += 1
        if (l == ',' or l == '\0' or l == '\n'):
            break;
    ret = line[:pos - 1]
    if len(ret) > 1 and float(ret) <= 9999999999999999999.9:
        print(float(ret), end="")
    elif (len(ret) > 1):
        print(",", float(99999999999999), end="")
    else:
        print(",", float("0.0"), end="")
    print(line[pos - 1:], end="")

for line in fichier:
    flat_line(line, pos)
