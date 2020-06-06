import os, sys, stat
import subprocess as sp
from datetime import datetime
from threading import Thread

import signal
import time

#import tensorflow as tf
#import numpy as np
#import pandas as pd
#
#model = tf.keras.models.load_model('./IA_temp.h5')

CAPTURE = True
PROCESSING = False
EXIT = False

def main():
    global EXIT
    t1 = Thread(target = capturing)
    t1.daemon = True
    t1.start()
    t2 = Thread(target = processing)
    t2.daemon = True
    t2.start()
    t3 = Thread(target = commande)
    t3.daemon = True
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    exit(0)

def commande():
    global EXIT
    while not EXIT :
        val = input()
        if (val == 'exit') :
            EXIT = True

def capturing():
    global CAPTURE
    global PROCESSING
    global EXIT
    while not EXIT :
        if (CAPTURE):
            captur_paquets(stream = "any", path_to_data = "save", size = 1000, format = "pcap")
            CAPTURE = False
            PROCESSING = True
        time.sleep(1)

def processing():
    global CAPTURE
    global EXIT
    global PROCESSING
    while not EXIT :
        if (PROCESSING):
            transform_paquets(path_to_cicflow = "/home/Fringhian/GitHub/CICFlowMeter/build/distributions/CICFlowMeter-4.0/bin/", path_to_data = "save")
            os.rename("save/temp.pcap", "save/" + datetime.now().strftime("%H:%M:%S")  + ".pcap")
            CAPTURE = True
            open("save/clean.csv", "w")
            preprocess_paquets(path_to_data = "save")
            os.remove("save/temp.pcap_Flow.csv")
            IA(path_to_data = "save")
            os.remove("save/clean.csv")
            print('\n')
            PROCESSING = False
        time.sleep(1)



def captur_paquets(stream: str, path_to_data: str, size: int, format: str) -> bool:
    global PROCESSING
    print("DO Capturing pakets\n")
    open("{}/main.pcap".format(path_to_data), "w+")
    pipe = sp.Popen( 'sudo tshark ' + '-F ' + format
                                    + ' -i ' + stream
                                    + ' -w ' + path_to_data + '/main.pcap',
                                    shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    time.sleep(3)
    while (PROCESSING) :
        pass
    print("DONE Capturing pakets\n")
    os.kill(pipe.pid, signal.SIGINT)
    os.rename(path_to_data + '/main.pcap', path_to_data + "/temp.pcap")


def transform_paquets(path_to_cicflow: str, path_to_data: str) -> bool:
    temp_dir = os.getcwd()
    temp_dir = temp_dir + '/'
    if (not os.path.exists(path_to_cicflow)):
        print("Didn't manage to find CiCFlowMeter at {}\n".format(path_to_cicflow))
        exit(2)
    if (not os.path.exists(path_to_data)):
        print("Didn't manage to find where to store data\n")
        exit(2)
    os.chdir(path_to_cicflow)
    print("DO Transforming pakets\n")
    pipe = sp.Popen("sudo ./cfm {}/temp.pcap {}/".format(temp_dir + path_to_data, temp_dir + path_to_data), shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    os.chdir(temp_dir)
    res = pipe.communicate()
    if (pipe.returncode != 0):
        print(res[1], "\n")
        exit(2)
    print("DONE Transforming pakets\n")


def preprocess_paquets(path_to_data: str) -> bool:
    print("DO preprocessing pakets\n")
    pipe = sp.Popen("sudo python3.7 {}ds_print_cleaned.py > {}/clean.csv".format("./../datasets/script/", path_to_data), shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    print("DONE preprocessing pakets\n")
    res = pipe.communicate()
    if (pipe.returncode != 0):
        print(res[1], "\n")
        exit(2)

def IA(path_to_data: str) -> bool:
    #data = pd.read_csv("{}/temp.csv".format(path_to_data), names=["SourcePort", "DestinationPort", "Protocol", "FlowDuration", "TotalFwdPackets", "TotalBackwardPackets", "TotalLengthofFwdPackets", "TotalLengthofBwdPackets", "FwdPacketLengthMean", "FwdPacketLengthStd", "BwdPacketLengthMean", "BwdPacketLengthStd", "PacketLengthMean", "PacketLengthStd", "PacketLengthVariance", "AveragePacketSize"], dtype='float')
    #data = data.values.reshape(len(data), 8)
    #prediction = model.predict(data)
    #for i in range in (data):
    #    print(prediction[i])
    #    if (prediction[i] > 0.80):
    #        print("ce paquet est tous caca !")
    print("DO analyse pakets\n")
    time.sleep(10)
    print("DONE analyse pakets\n")
    return True

if __name__ == "__main__":
    main()
