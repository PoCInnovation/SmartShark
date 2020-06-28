from threading import Thread
from subprocess import Popen, PIPE
import pandas as pd
import numpy as np
import tensorflow.keras as tf_keras
from typing import List
from datetime import datetime
from sklearn.preprocessing import StandardScaler
import os, signal, time

def ApplyCommand(Commande: str):
    if not Commande:
        raise Exception("Use a valide and not empty string")
    Process = Popen(Commande, shell=True, stdout=PIPE, stderr=PIPE)
    _, stderr = Process.communicate()
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
    Path = {"PATH_SAVE": "./SmartShark/save/",
            "PATH_PREPROCESS_SCRIPT": "./SmartShark/",
            "PATH_MODEL": './SmartShark/model-001-batche_size20.h5'}

    Status = {"CAPTURE": True,
              "PROCESS": False,
              "STOP": False,
              "NEW": False,
              "GO": False}

    IA = {"MODEL": 0,
          "PACKETS": [],
          "NUMBER_BAD_PACKETS": 0,
          "NUMBER_PACKETS": 0,
          "PREDICTION": 0,
          "PACKETS_FLOW": 20}

    def StartSmSh(self):
        self.IA["MODEL"] = tf_keras.models.load_model(self.Path["PATH_MODEL"])

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
            if self.Status['CAPTURE'] and self.Status['GO']:
                open(f"{self.Path['PATH_SAVE']}main.pcap", "w+").close()
                try:
                    CapturingProcess = Popen(f"tshark -F pcap -i any -w {self.Path['PATH_SAVE']}main.pcap", shell=True, stdout=PIPE, stderr=PIPE)
                    time.sleep(2)
                    while self.Status['PROCESS']:
                        pass
                    os.kill(CapturingProcess.pid, signal.SIGINT)
                except Exception as e:
                    print(e)

                self.Status['CAPTURE'] = False
                self.Status['PROCESS'] = True

            time.sleep(1)

    def Processing(self):
        while not self.Status['STOP']:
            if self.Status['PROCESS'] and self.Status['GO']:
                os.rename(f"{self.Path['PATH_SAVE']}main.pcap", f"{self.Path['PATH_SAVE']}temp.pcap")
                self.Status['CAPTURE'] = True
                open(f"{self.Path['PATH_SAVE']}first.csv", "w").close()
                try:
                    ApplyCommand(f"tshark -r {self.Path['PATH_SAVE']}temp.pcap -T fields -E separator=, -e frame.len -e frame.time_delta -e ip.proto > {self.Path['PATH_SAVE']}first.csv")
                except Exception as e:
                    print(e)
                os.rename(f"{self.Path['PATH_SAVE']}temp.pcap", f"{self.Path['PATH_SAVE'] + datetime.now().strftime('%H:%M:%S')}.pcap")
                open(f"{self.Path['PATH_SAVE']}clean.csv", "w").close()
                try:
                    ApplyCommand(f"sudo python3.7 {self.Path['PATH_PREPROCESS_SCRIPT']}ds_preprocess.py > {self.Path['PATH_SAVE']}clean.csv")
                except Exception as e:
                    print(e)
                os.remove(f"{self.Path['PATH_SAVE']}first.csv")
                try:
                    RemoveFirstLine(f"{self.Path['PATH_SAVE']}clean.csv")
                except Exception as e:
                    print(e)

                self.IA["NUMBER_BAD_PACKETS"] = 0
                self.IA["PACKETS"] = pd.read_csv(f"{self.Path['PATH_SAVE']}clean.csv", names=["deltaTime", "len", "proto", "totalDelta", "totalLen", "averageDelta", "averageLen", "deltaStd", "lenStd"], dtype='float')
                self.IA["NUMBER_PACKETS"] = len(self.IA["PACKETS"])
                if len(self.IA["PACKETS"]) > 0:
                    scaler = StandardScaler()
                    self.IA["PACKETS"] = scaler.fit_transform(self.IA["PACKETS"])
                    result = []
                    tmp = []
                    for index, line in enumerate(self.IA["PACKETS"]):
                        tmp.append(line)
                        if index % self.IA["PACKETS_FLOW"] == self.IA["PACKETS_FLOW"] - 1:
                            result.append(tmp)
                            tmp = []
                    result = np.array(result)
                    self.IA["PREDICTION"] = self.IA["MODEL"].predict(result)
                    for i in range(len(result)):
                        if self.IA["PREDICTION"][i][1] > 0.5:
                            self.IA["NUMBER_BAD_PACKETS"] = self.IA["NUMBER_BAD_PACKETS"] + 1
                os.remove(f"{self.Path['PATH_SAVE']}clean.csv")

                self.Status['PROCESS'] = False
                self.Status['NEW'] = True

            time.sleep(1)