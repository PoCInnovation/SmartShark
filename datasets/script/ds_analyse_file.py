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

fichier = open("your_file", "r")

#give the position of the packets' len /!\ IMPORTANT /!\
len_pckt_pos = 1
date_pos = 0

average_pckt_len = 0
nb_pckt_checked = 0
first = True
second = False

def get_date(line, date_pos):
    tmp = 0
    comma_pos = 0
    result = ""
    while (tmp != date_pos):
        if (line[comma_pos == ',']):
            tmp += 1
        comma_pos += 1
    while (line[comma_pos] != ',' and line[comma_pos] != '\n'):
        result += line[comma_pos]
        comma_pos += 1
    return result

def get_len_of_this_packet(line, len_pckt_pos):
    tmp = 0
    comma_pos = 0
    result = ""
    while (tmp != len_pckt_pos):
 #       print("1)", tmp)
        if (line[comma_pos] == ','):
            tmp += 1
        comma_pos += 1
#        print("2)", tmp)
    while (line[comma_pos] != ',' and line[comma_pos] != '\n'):
        result += line[comma_pos]
        comma_pos += 1
    return float(result)

def get_nb_packet_minutes(start_date, end_date, nb_pckt_checked):
    s_year = float(start_date[:4])
    e_year = float(end_date[:4])
    s_month = float(start_date[5:7])
    e_month = float(end_date[5:7])
    s_day = float(start_date[8:10])
    e_day = float(end_date[8:10])
    s_hour = float(start_date[11:13])
    e_hour = float(end_date[11:13])
    s_min = float(start_date[14:16])
    e_min = float(end_date[14:16])
    s_sec = float(start_date[17:19])
    e_sec = float(end_date[17:19])
    return nb_pckt_checked / (((e_year - s_year) * 31556926 + (e_month - s_month) * 2629744 + (e_day - s_day) * 86400 + (e_hour - s_hour)  * 3600 + (e_min - s_min) * 60 + e_sec - s_sec) / 60)

for line in fichier:
        if first:
            first = False
            second = True
        elif second:
            start_date = get_date(line, date_pos)
            second = False
        else:
            average_pckt_len += get_len_of_this_packet(line, len_pckt_pos)
        nb_pckt_checked += 1
        end_date = get_date(line, date_pos)

average_pckt_len = average_pckt_len / nb_pckt_checked
print('average packets\'slen=', average_pckt_len)
print('nb of pckets checked=', nb_pckt_checked)
print('between', start_date, 'to', end_date, 'there was:', nb_pckt_checked, "packets", "wich correspond to", get_nb_packet_minutes(start_date, end_date, nb_pckt_checked), "pckts/mins", sep=" ")

fichier.close()
