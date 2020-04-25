###############################################
#                                             #
#              PoC: Smartshark                #
#                                             #
#                  USAGE:                     #
#                                             #
#   Script to check quality of the dataset    #
#                                             #
#                                             #
#     Be shure there is no empty line at      #
#           the end of your file              #
#                                             #
###############################################

fichier = open("the_file.csv", "r")

#give the position of the packets' len /!\ IMPORTANT /!\
len_pckt_pos = 0

average_pckt_len = 0
nb_pckt_checked = 0

first = True
def get_len_of_this_packet(line, len_pckt_pos):
    tmp = 0
    comma_pos = 0
    result = ""
    while (tmp != len_pckt_pos):
        if (line[comma_pos == ',']):
            tmp += 1
        comma_pos += 1
    while (line[comma_pos] != ',' and line[comma_pos] != '\n'):
        result += line[comma_pos]
        comma_pos += 1
    return float(result)

for line in fichier:
        if first:
            first = False
        else:
            average_pckt_len += get_len_of_this_packet(line, len_pckt_pos)
        nb_pckt_checked += 1
average_pckt_len = average_pckt_len / nb_pckt_checked

print('average packets\'slen=', average_pckt_len)
print('nb of pckets checked=', nb_pckt_checked)

fichier.close()
