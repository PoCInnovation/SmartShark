###############################################
#                                             #
#              PoC: Smartshark                #
#                                             #
#                  USAGE:                     #
#                                             #
#        Script to clean datasets             #
#                                             #
#                                             #
#    Put in row every Label and redirect      #
#         output to your new file             #
#                                             #
#                                             #
#   You can use 'ds_create_row_label.py'      #
#       to create your row variable           #
#                                             #
###############################################

#Choose your file
fichier = open("/run/media/Thytu/TOSHIBA EXT/PoC/Smartshark/DS/ds_benign_cleared_div_3_18rows.csv", "r")

#FOR DDOS
row = dict([('SourcePort', True), ('DestinationPort', True), ('Protocol', True), ('FlowDuration', True), ('TotalFwdPackets', True), ('TotalBackwardPackets', True), ('TotalLengthofFwdPackets', True), ('TotalLengthofBwdPackets', True), ('FwdPacketLengthMean', True), ('FwdPacketLengthStd', True), ('BwdPacketLengthMean', True), ('BwdPacketLengthStd', True), ('FlowBytes/s', False), ('FlowPackets/s', False), ('PacketLengthMean', True), ('PacketLengthStd', True), ('PacketLengthVariance', True), ('AveragePacketSize', True)])
"""
#FOR CLEANED
row = dict([('SrcPort', True), ('DstPort', True), ('Protocol', True), ('FlowDuration', True), ('TotalFwdPacket', True), ('TotalBwdpackets', True), ('TotalLengthofFwdPacket', True), ('TotalLengthofBwdPacket', True), ('FwdPacketLengthMean', True), ('FwdPacketLengthStd', True), ('BwdPacketLengthMean', True), ('BwdPacketLengthStd', True), ('FlowBytes/s', False), ('FlowPackets/s', False), ('PacketLengthMean', True), ('PacketLengthStd', True), ('PacketLengthVariance', True), ('AveragePacketSize', True)])
"""

def get_next_value(i, str, first):
    if first:
        result = ""
    else:
         result = ","
    while (str[i] != ',' and str[i] != '\n'):
        result = result + str[i]
        i += 1
    return (i, result)

result = ""
tmp = ""
for line in fichier:
    first = True
    index = 0
    for i in row:
        index, tmp = get_next_value(index, line, first)
        if row.get(i):
            first = False
            result += tmp
        index += 1
    if (len(result) > 0 and result[len(result) - 1] != '\n'):
        result += '\n'
print(result, end="", sep="")
fichier.close()
