from threading import Thread
from subprocess import Popen, PIPE
import pandas as pd
import tensorflow as tf
from typing import List
from datetime import datetime
import os, signal, time

def ApplyCommand(Commande: str):
    if not Commande:
        raise Exception("Use a valide and not empty string")
    Process = Popen(Commande, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = Process.communicate()
    if (Process.returncode != 0):
        raise Exception(f"Error while using the commande [{Commande}] and returned [{stderr}]")
    return Process

def RemoveFirstLine(PathFile: str):
    if not PathFile:
        raise Exception("Use a valide and not empty string")
    if not os.path.exists(PathFile):
        raise Exception(f"Could not find {PathFile}")
    with open(PathFile, 'r') as fin:
        data: List[str] = fin.read().splitlines(True)
    with open(PathFile, 'w') as fout:
        fout.writelines(data[1:])

class SmSh():
    Path = {"PATH_CICFLOW": "./CICFlowMeter/build/distributions/CICFlowMeter-4.0/bin/",
            "PATH_SAVE": "./app/static/SmartShark/save/",
            "PATH_PREPROCESS_SCRIPT": "./app/static/SmartShark/",
            "PATH_CURRENT": f"{os.getcwd()}/",
            "PATH_MODEL": './app/static/SmartShark/IA_temp.h5'}

    Status = {"CAPTURE": True,
              "PROCESS": False,
              "STOP": False,
              "NEW": False}

    IA = {"MODEL": 0,
          "PACKETS": [],
          "NUMBER_BAD_PACKETS": 0,
          "PREDICTION": 0}

    def StartSmSh(self):
        self.IA["MODEL"] = tf.keras.models.load_model(self.Path["PATH_MODEL"])

        self.CapturingThread = Thread(target=self.Capturing)
        self.ProcessingThread = Thread(target=self.Processing)

        self.CapturingThread.daemon = True
        self.ProcessingThread.daemon = True

        self.CapturingThread.start()
        self.ProcessingThread.start()

        self.CapturingThread.join()
        self.ProcessingThread.join()

    def Capturing(self):
        while not self.Status['STOP']:
            if self.Status['CAPTURE']:

                open(f"{self.Path['PATH_SAVE']}/main.pcap", "w+").close()
                try:
                    CapturingProcess = Popen(f"sudo tshark -F pcap -i any -w {self.Path['PATH_SAVE']}main.pcap", shell=True, stdout=PIPE, stderr=PIPE)
                    time.sleep(3)
                    while self.Status['PROCESS']:
                        pass
                    os.kill(CapturingProcess.pid, signal.SIGINT)
                    os.rename(f"{self.Path['PATH_SAVE']}main.pcap", f"{self.Path['PATH_SAVE']}temp.pcap")
                except Exception as e:
                    print(e)

                self.Status['CAPTURE'] = False
                self.Status['PROCESS'] = True

            time.sleep(1)

    def Processing(self):
        while not self.Status['STOP']:
            if self.Status['PROCESS']:
                os.chdir(self.Path['PATH_CICFLOW'])
                try:
                    ApplyCommand(f"sudo ./cfm {self.Path['PATH_CURRENT'] + self.Path['PATH_SAVE']}temp.pcap {self.Path['PATH_CURRENT'] + self.Path['PATH_SAVE']}")
                except Exception as e:
                    print(e)
                os.chdir(self.Path['PATH_CURRENT'])
                os.rename(f"{self.Path['PATH_SAVE']}temp.pcap", f"{self.Path['PATH_SAVE'] + datetime.now().strftime('%H:%M:%S')}.pcap")
                self.Status['CAPTURE'] = True

                open(f"{self.Path['PATH_SAVE']}clean.csv", "w").close()
                try:
                    ApplyCommand(f"sudo python3.7 {self.Path['PATH_PREPROCESS_SCRIPT']}ds_print_cleaned.py > {self.Path['PATH_SAVE']}/clean.csv")
                except Exception as e:
                    print(e)
                os.remove(f"{self.Path['PATH_SAVE']}temp.pcap_Flow.csv")
                try:
                    RemoveFirstLine(f"{self.Path['PATH_SAVE']}clean.csv")
                except Exception as e:
                    print(e)

                self.IA["NUMBER_BAD_PACKETS"] = 0
                self.IA["PACKETS"] = pd.read_csv(f"{self.Path['PATH_SAVE']}clean.csv", names=["SourcePort", "DestinationPort", "Protocol", "FlowDuration", "TotalFwdPackets", "TotalBackwardPackets", "TotalLengthofFwdPackets", "TotalLengthofBwdPackets", "FwdPacketLengthMean", "FwdPacketLengthStd", "BwdPacketLengthMean", "BwdPacketLengthStd", "PacketLengthMean", "PacketLengthStd", "PacketLengthVariance", "AveragePacketSize"], dtype='float')
                self.IA["PACKETS"] = self.IA["PACKETS"].values.reshape(len(self.IA["PACKETS"]), 16)
                self.IA["PREDICTION"] = self.IA["MODEL"].predict(self.IA["PACKETS"])
                for i in range(len(self.IA["PACKETS"])):
                        if self.IA["PREDICTION"][i][1]:
                            self.IA["NUMBER_BAD_PACKETS"]  = self.IA["NUMBER_BAD_PACKETS"]  + 1
                os.remove(f"{self.Path['PATH_SAVE']}clean.csv")

                self.Status['PROCESS'] = False
                self.Status['NEW'] = True

            time.sleep(1)