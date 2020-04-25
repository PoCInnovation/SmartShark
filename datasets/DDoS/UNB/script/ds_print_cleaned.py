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
fichier = open("the_file.csv", "r")
row = dict([('Unnamed', False), ('FlowID', False), ('SourceIP', True), ('SourcePort', True), ('DestinationIP', True), ('DestinationPort', True), ('Protocol', True), ('Timestamp', True), ('FlowDuration', False), ('TotalFwdPackets', False), ('TotalBackwardPackets', False), ('TotalLengthofFwdPackets', False), ('TotalLengthofBwdPackets', False), ('FwdPacketLengthMax', False), ('FwdPacketLengthMin', False), ('FwdPacketLengthMean', False), ('FwdPacketLengthStd', False), ('BwdPacketLengthMax', False), ('BwdPacketLengthMin', False), ('BwdPacketLengthMean', False), ('BwdPacketLengthStd', False), ('FlowBytes/s', False), ('FlowPackets/s', False), ('FlowIATMean', False), ('FlowIATStd', False), ('FlowIATMax', False), ('FlowIATMin', False), ('FwdIATTotal', False), ('FwdIATMean', False), ('FwdIATStd', False), ('FwdIATMax', False), ('FwdIATMin', False), ('BwdIATTotal', False), ('BwdIATMean', False), ('BwdIATStd', False), ('BwdIATMax', False), ('BwdIATMin', False), ('FwdPSHFlags', False), ('BwdPSHFlags', False), ('FwdURGFlags', False), ('BwdURGFlags', False), ('FwdHeaderLength', False), ('BwdHeaderLength', False), ('FwdPackets/s', False), ('BwdPackets/s', False), ('MinPacketLength', False), ('MaxPacketLength', False), ('PacketLengthMean', False), ('PacketLengthStd', False), ('PacketLengthVariance', False), ('FINFlagCount', False), ('SYNFlagCount', False), ('RSTFlagCount', False), ('PSHFlagCount', False), ('ACKFlagCount', False), ('URGFlagCount', False), ('CWEFlagCount', False), ('ECEFlagCount', False), ('Down/UpRatio', False), ('AveragePacketSize', False), ('AvgFwdSegmentSize', False), ('AvgBwdSegmentSize', False), ('FwdHeaderLength.1', False), ('FwdAvgBytes/Bulk', False), ('FwdAvgPackets/Bulk', False), ('FwdAvgBulkRate', False), ('BwdAvgBytes/Bulk', False), ('BwdAvgPackets/Bulk', False), ('BwdAvgBulkRate', False), ('SubflowFwdPackets', False), ('SubflowFwdBytes', False), ('SubflowBwdPackets', False), ('SubflowBwdBytes', False), ('Init_Win_bytes_forward', False), ('Init_Win_bytes_backward', False), ('act_data_pkt_fwd', False), ('min_seg_size_forward', False), ('ActiveMean', False), ('ActiveStd', False), ('ActiveMax', False), ('ActiveMin', False), ('IdleMean', False), ('IdleStd', False), ('IdleMax', False), ('IdleMin', False), ('SimillarHTTP', False), ('Inbound', False), ('Label', True)])

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
