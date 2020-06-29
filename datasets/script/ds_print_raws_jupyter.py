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
fichier = open("/run/media/Thytu/TOSHIBA EXT/PoC/Smartshark/DS/LDAP.csv", "r")

row =
"""
#FOR DDOS
row = dict([('Unamed', False), ('FlowID', False), ('SourceIP', False), ('SourcePort', True), ('DestinationIP', False), ('DestinationPort', True), ('Protocol', True), ('Timestamp', False), ('FlowDuration', True), ('TotalFwdPackets', True), ('TotalBackwardPackets', True), ('TotalLengthofFwdPackets', True), ('TotalLengthofBwdPackets', True), ('FwdPacketLengthMax', False), ('FwdPacketLengthMin', False), ('FwdPacketLengthMean', True), ('FwdPacketLengthStd', True), ('BwdPacketLengthMax', False), ('BwdPacketLengthMin', False), ('BwdPacketLengthMean', True), ('BwdPacketLengthStd', True), ('FlowBytes/s', True), ('FlowPackets/s', True), ('FlowIATMean', False), ('FlowIATStd', False), ('FlowIATMax', False), ('FlowIATMin', False), ('FwdIATTotal', False), ('FwdIATMean', False), ('FwdIATStd', False), ('FwdIATMax', False), ('FwdIATMin', False), ('BwdIATTotal', False), ('BwdIATMean', False), ('BwdIATStd', False), ('BwdIATMax', False), ('BwdIATMin', False), ('FwdPSHFlags', False), ('BwdPSHFlags', False), ('FwdURGFlags', False), ('BwdURGFlags', False), ('FwdHeaderLength', False), ('BwdHeaderLength', False), ('FwdPackets/s', False), ('BwdPackets/s', False), ('MinPacketLength', False), ('MaxPacketLength', False), ('PacketLengthMean', True), ('PacketLengthStd', True), ('PacketLengthVariance', True), ('FINFlagCount', False), ('SYNFlagCount', False), ('RSTFlagCount', False), ('PSHFlagCount', False), ('ACKFlagCount', False), ('URGFlagCount', False), ('CWEFlagCount', False), ('ECEFlagCount', False), ('Down/UpRatio', False), ('AveragePacketSize', True), ('AvgFwdSegmentSize', False), ('AvgBwdSegmentSize', False), ('FwdHeaderLength.1', False), ('FwdAvgBytes/Bulk', False), ('FwdAvgPackets/Bulk', False), ('FwdAvgBulkRate', False), ('BwdAvgBytes/Bulk', False), ('BwdAvgPackets/Bulk', False), ('BwdAvgBulkRate', False), ('SubflowFwdPackets', False), ('SubflowFwdBytes', False), ('SubflowBwdPackets', False), ('SubflowBwdBytes', False), ('Init_Win_bytes_forward', False), ('Init_Win_bytes_backward', False), ('act_data_pkt_fwd', False), ('min_seg_size_forward', False), ('ActiveMean', False), ('ActiveStd', False), ('ActiveMax', False), ('ActiveMin', False), ('IdleMean', False), ('IdleStd', False), ('IdleMax', False), ('IdleMin', False), ('Label', False)])

#FOR CLEANED
row = dict([('FlowID', False), ('SrcIP', False), ('SrcPort', True), ('DstIP', False), ('DstPort', True), ('Protocol', True), ('Timestamp', False), ('FlowDuration', True), ('TotalFwdPacket', True), ('TotalBwdpackets', True), ('TotalLengthofFwdPacket', True), ('TotalLengthofBwdPacket', True), ('FwdPacketLengthMax', False), ('FwdPacketLengthMin', False), ('FwdPacketLengthMean', True), ('FwdPacketLengthStd', True), ('BwdPacketLengthMax', False), ('BwdPacketLengthMin', False), ('BwdPacketLengthMean', True), ('BwdPacketLengthStd', True), ('FlowBytes/s', True), ('FlowPackets/s', True), ('FlowIATMean', False), ('FlowIATStd', False), ('FlowIATMax', False), ('FlowIATMin', False), ('FwdIATTotal', False), ('FwdIATMean', False), ('FwdIATStd', False), ('FwdIATMax', False), ('FwdIATMin', False), ('BwdIATTotal', False), ('BwdIATMean', False), ('BwdIATStd', False), ('BwdIATMax', False), ('BwdIATMin', False), ('FwdPSHFlags', False), ('BwdPSHFlags', False), ('FwdURGFlags', False), ('BwdURGFlags', False), ('FwdHeaderLength', False), ('BwdHeaderLength', False), ('FwdPackets/s', False), ('BwdPackets/s', False), ('PacketLengthMin', False), ('PacketLengthMax', False), ('PacketLengthMean', True), ('PacketLengthStd', True), ('PacketLengthVariance', True), ('FINFlagCount', False), ('SYNFlagCount', False), ('RSTFlagCount', False), ('PSHFlagCount', False), ('ACKFlagCount', False), ('URGFlagCount', False), ('CWEFlagCount', False), ('ECEFlagCount', False), ('Down/UpRatio', False), ('AveragePacketSize', True), ('FwdSegmentSizeAvg', False), ('BwdSegmentSizeAvg', False), ('FwdBytes/BulkAvg', False), ('FwdPacket/BulkAvg', False), ('FwdBulkRateAvg', False), ('BwdBytes/BulkAvg', False), ('BwdPacket/BulkAvg', False), ('BwdBulkRateAvg', False), ('SubflowFwdPackets', False), ('SubflowFwdBytes', False), ('SubflowBwdPackets', False), ('SubflowBwdBytes', False), ('FWDInitWinBytes', False), ('BwdInitWinBytes', False), ('FwdActDataPkts', False), ('FwdSegSizeMin', False), ('ActiveMean', False), ('ActiveStd', False), ('ActiveMax', False), ('ActiveMin', False), ('IdleMean', False), ('IdleStd', False), ('IdleMax', False), ('IdleMin', False), ('Label', False)])
"""

for i in row:
    if row[i] is True:
#        print('"{}"'.format(i), end=', ')
        print('{}'.format(i), end=', ')
