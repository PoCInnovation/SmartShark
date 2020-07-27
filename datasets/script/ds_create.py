###############################################
#                                             #
#              PoC: Smartshark                #
#                                             #
#                  USAGE:                     #
#                                             #
#        Script to create the dataset         #
#                                             #
#   Use top variables to custom the script    #
#        It will print the dataset            #
#                                             #
#   WARNING: label must be always at the end  #
# ISSUE:get_val_without_label has to be fixed #
#                                             #
###############################################

fichier = open("/run/media/Thytu/TOSHIBA EXT/PoC/Smartshark/DS/flow_1_cleared.csv", "r")
keep_label = True # let the True value, need to be fixed
nb_of_packet_use_for_each = 5

tmp = 0
index = 0
result = ""
first = True

pos = dict([("Time", 5), ("Len_fwd", 6), ("Len_bwd", 7), ("Source IP", 0), ("Source Port", 1), ("Destination IP", 2), ("Destination Port", 3), ("Protocol", 4), ("Label", 8)])

def get_val_without_label(tmp):
    index = 0
    pos_com = 0
    while (pos_com != pos["Label"]):
        if (tmp[index] == ','):
            pos_com += 1
        index += 1
    return tmp[:index - 1]

def get_first_time_val(tmp, the_pos):
    index = 0
    index2 = 0
    pos_com = 0
    while (pos_com != the_pos + 1 and tmp[index] != "\n" and tmp[index] != "\0"):
        if (tmp[index] == ','):
            pos_com += 1
        index += 1
    pos_com = 0
    while (pos_com != the_pos and tmp[index2] != "\n" and tmp[index2] != "\0"):
        if (tmp[index2] == ','):
            pos_com += 1
        index2 += 1
    return tmp[index2:index - 1]

def get_last_time_val(old_tmp, the_pos):
    index = 0
    index2 = 0
    pos_com = 0
    index3 = 0
    index4 = 0

    for line in old_tmp:
        if line == '\n':
            index4 += 1
        index3 += 1
        if index4 == nb_of_packet_use_for_each - 1:
            break
    tmp = old_tmp[index3:]
    while (pos_com != the_pos + 1 and tmp[index] != "\n" and tmp[index] != "\0"):
        if (tmp[index] == ','):
            pos_com += 1
        index += 1
    pos_com = 0
    while (pos_com != the_pos and tmp[index2] != "\n" and tmp[index2] != "\0"):
        if (tmp[index2] == ','):
            pos_com += 1
        index2 += 1
    return tmp[index2:index - 1]

def calc_delta(start_date, end_date):
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
     s_micr = float(start_date[20:])
     e_micr = float(end_date[20:])
     tmp = ((e_year - s_year) * 31556926 + (e_month - s_month) * 2629744 + (e_day - s_day) * 86400 + (e_hour - s_hour)  * 3600 + (e_min - s_min) * 60 + e_sec - s_sec) * 1000000
     return (tmp + e_micr - s_micr)

def get_delta_time(tmp, the_pos):
    first_time = get_first_time_val(tmp, the_pos)
    last_time = get_last_time_val(tmp, the_pos)
    return calc_delta(first_time, last_time)

def get_x_len_packet(tmp, pos):
    pos_com = 0
    index = 0
    while (pos_com != pos):
        if tmp[index] == ',':
            pos_com += 1
        index += 1
    index2 = index
    while (tmp[index2] != ',' and tmp[index2] != '\n' and tmp[index2] != '\0'):
           index2 += 1
    return (float(tmp[index:index2]))

def get_x_line(tmp, line):
    pos_com = 0
    index = 0
    while (pos_com != line):
        if tmp[index] == '\n':
            pos_com += 1
        index += 1
    index2 = index
    while (tmp[index2] != '\n' and tmp[index2] != '\0'):
        index2 += 1
    return tmp[index:index2]

def get_len_fwd(tmp, pos):
    result = 0
    for i in range(nb_of_packet_use_for_each):
        result += get_x_len_packet(get_x_line(tmp, i), pos);
    return result

def get_len_bwd(tmp, pos):
    result = 0
    for i in range(nb_of_packet_use_for_each):
        result += get_x_len_packet(get_x_line(tmp, i), pos);
    return result

def get_protocol(tmp, pos):
    pos_com = 0
    index = 0
    while (pos_com != pos):
        if tmp[index] == ',':
            pos_com += 1
        index += 1
    index2 = index
    while (tmp[index2] != ',' and tmp[index2] != '\n' and tmp[index2] != '\0'):
           index2 += 1
    return (int(tmp[index:index2]))

def get_proto_maj(tmp, pos):
    ans = {}
    for i in range(nb_of_packet_use_for_each):
        if (str(get_protocol(get_x_line(tmp, i), pos))) in ans:
            ans[str(get_protocol(get_x_line(tmp, i), pos))] += 1
        else:
            ans[str(get_protocol(get_x_line(tmp, i), pos))] = 1
    index = 0
    result = 0
    for i in ans:
        if int(ans[i]) > int(index):
            result = ans[i]
            index = i
    return(index)

def get_src_ip(tmp, pos):
    pos_com = 0
    index = 0
    while (pos_com != pos):
        if tmp[index] == ',':
            pos_com += 1
        index += 1
    index2 = index
    while (tmp[index2] != ',' and tmp[index2] != '\n' and tmp[index2] != '\0'):
           index2 += 1
    return (tmp[index:index2])

def get_pourc_src_ip(tmp, pos):
    ans = {}
    for i in range(nb_of_packet_use_for_each):
        if (str(get_src_ip(get_x_line(tmp, i), pos))) in ans:
            ans[str(get_src_ip(get_x_line(tmp, i), pos))] += 1
        else:
            ans[str(get_src_ip(get_x_line(tmp, i), pos))] = 1
    index = 0
    result = 0
    for i in ans:
        if ans[i] > index:
            index = ans[i]
            result = i
    return(index * 100 / nb_of_packet_use_for_each)

def get_pourc_dst_ip(tmp, pos):
    ans = {}
    for i in range(nb_of_packet_use_for_each):
        if (str(get_src_ip(get_x_line(tmp, i), pos))) in ans:
            ans[str(get_src_ip(get_x_line(tmp, i), pos))] += 1
        else:
            ans[str(get_src_ip(get_x_line(tmp, i), pos))] = 1
    index = 0
    result = 0
    for i in ans:
        if ans[i] > index:
            index = ans[i]
            result = i
    return(index * 100 / nb_of_packet_use_for_each)

def get_pourc_src_port(tmp, pos):
    ans = {}
    for i in range(nb_of_packet_use_for_each):
        if (str(get_src_ip(get_x_line(tmp, i), pos))) in ans:
            ans[str(get_src_ip(get_x_line(tmp, i), pos))] += 1
        else:
            ans[str(get_src_ip(get_x_line(tmp, i), pos))] = 1
    index = 0
    result = 0
    for i in ans:
        if ans[i] > index:
            index = ans[i]
            result = i
    return(index * 100 / nb_of_packet_use_for_each)

def get_pourc_dst_port(tmp, pos):
    ans = {}
    for i in range(nb_of_packet_use_for_each):
        if (str(get_src_ip(get_x_line(tmp, i), pos))) in ans:
            ans[str(get_src_ip(get_x_line(tmp, i), pos))] += 1
        else:
            ans[str(get_src_ip(get_x_line(tmp, i), pos))] = 1
    index = 0
    result = 0
    for i in ans:
        if ans[i] > index:
            index = ans[i]
            result = i
    return(index * 100 / nb_of_packet_use_for_each)

def get_result(result, pos):
    the_result = []
    the_result.append(get_delta_time(result, pos["Time"]))
    the_result.append(get_len_fwd(result, pos["Len_fwd"]))
    the_result.append(get_len_bwd(result, pos["Len_bwd"]))
    the_result.append(int(get_proto_maj(result, pos["Protocol"])))
    the_result.append(get_pourc_src_ip(result, pos["Source IP"]))
    the_result.append(get_pourc_src_port(result, pos["Source Port"]))
    the_result.append(get_pourc_dst_ip(result, pos["Destination IP"]))
    the_result.append(get_pourc_dst_port(result, pos["Destination Port"]))
    return (the_result)


for line in fichier:
    if first:
        first = False
    else:
        result += line
        tmp += 1
        if tmp == nb_of_packet_use_for_each:
            tmp = 0
            index += 1
            if (keep_label == False):
                result = get_val_without_label(result)
            result = str(get_result(result, pos))
            print(result[1:len(result) - 1])
            result = ""
