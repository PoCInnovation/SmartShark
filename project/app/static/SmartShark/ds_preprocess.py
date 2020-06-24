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
# import numpy as np

result = []
deltaArray = []
lenArray = []

class Packet :
  def __init__(self, line) :
    self.deltaTime = line[0]
    self.len = line[1]
    self.proto = line[2]

  def reset(self) :
    self.totalDelta = self.deltaTime
    self.averageDelta = self.deltaTime
    self.totalLen = self.len
    self.averageLen = self.len
    self.deltaStd = 0.0
    self.lenStd = 0.0

  def calc(self, previous, index) :
    self.totalDelta = self.deltaTime + previous.totalDelta
    self.totalLen = self.len + previous.totalLen

    self.averageDelta = self.totalDelta / index
    self.averageLen = self.totalLen / index
    self.deltaStd = st.pstdev(deltaArray)
    self.lenStd = st.pstdev(lenArray)

  def __repr__(self) :
    return f'{self.deltaTime} {self.len} {self.proto} {self.totalDelta} {self.totalLen} {self.averageDelta} {self.averageLen} {self.deltaStd} {self.lenStd}'

fichier = open("all_pcap_to_csv_1_000.csv", "r")

for index, line in enumerate(fichier):
    if len(line) == 0 : break
    line = [float(nb) if nb != '' else -1 for nb in line.replace('\n', '').split(',')]

    to_insert = Packet(line)

    if index % 5 != 0:
      to_insert.calc(result[index - 1], index)

      deltaArray.append(to_insert.deltaTime)
      lenArray.append(to_insert.len)
    else:
        to_insert.reset()
        deltaArray = [0.0]
        lenArray = [0.0]

    result.append(to_insert)
print(*result, sep='\n')