from threading import Thread
from subprocess import Popen, PIPE
import pandas as pd
import numpy as np
from typing import List
from tensorflow.python.keras.models import load_model
from datetime import datetime
from sklearn.preprocessing import StandardScaler
import os, signal, time, re

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
              "GO": False,
              "SAVING": False,
              "DDOS": True,
              "MITM": True}

    IA = {"MODEL": 0,
          "PACKETS": [],
          "NUMBER_BAD_PACKETS": 0,
          "NUMBER_PACKETS": 0,
          "PREDICTION": 0,
          "PACKETS_FLOW": 20,
          "TIME": 3,
          "SPY": 0}

    def StartSmSh(self):
        self.IA["MODEL"] = load_model(self.Path["PATH_MODEL"])

        os.makedirs(self.Path['PATH_SAVE'], exist_ok=True)

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
                print(f"Capturing for {self.IA['TIME']} seconds")
                open(f"{self.Path['PATH_SAVE']}main.pcap", "w+").close()
                try:
                    CapturingProcess = Popen(f"tshark -F pcap -i any -w {self.Path['PATH_SAVE']}main.pcap", shell=True, stdout=PIPE, stderr=PIPE)
                    time.sleep(self.IA['TIME'])
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
                print("processing...")
                os.rename(f"{self.Path['PATH_SAVE']}main.pcap", f"{self.Path['PATH_SAVE']}temp.pcap")
                self.Status['CAPTURE'] = True

                if self.Status['DDOS']:
                    try:
                        self.DDoSCheck()
                    except Exception as e:
                        print(e)
                        self.Status['PROCESS'] = False
                        self.Status['NEW'] = True
                        continue

                if self.Status['MITM']:
                    try:
                        print("check !")
                        self.mitmCheck()
                        print("done !")
                        print(self.IA["SPY"])
                    except Exception as e:
                        print(e)
                        self.Status['PROCESS'] = False
                        self.Status['NEW'] = True
                        continue

                if self.Status['SAVING']:
                    print("saving...")
                    os.rename(f"{self.Path['PATH_SAVE']}temp.pcap", f"{self.Path['PATH_SAVE'] + datetime.now().strftime('%H:%M:%S')}.pcap")
                else:
                    print("NOT saving...")
                    os.remove(f"{self.Path['PATH_SAVE']}temp.pcap")

                self.Status['PROCESS'] = False
                self.Status['NEW'] = True

            time.sleep(1)

    def mitmCheck(self):
        self.IA["SPY"] = 0
        arp_table = {}
        try:
            with open(f"{self.Path['PATH_SAVE']}arp_table", "r") as f:
                for ligne in f:
                    arp_table[re.findall("(.+?);", ligne)[0]] = re.findall(";(.+?)\n", ligne)[0]
        except:
            pass

        try:
            ApplyCommand(f"sudo tshark -r {self.Path['PATH_SAVE']}temp.pcap -Y arp > {self.Path['PATH_SAVE']}log")
        except Exception as e:
            print(e)
            self.Status['PROCESS'] = False
            self.Status['NEW'] = True
            return

        with open(f"{self.Path['PATH_SAVE']}log", "r") as f:
            for ligne in f:
                if re.findall("Who has", ligne):
                    last_l = ligne
                    last_sp = re.findall("Tell (.+?)\n", ligne)[0]
                elif re.findall("is at", ligne) and re.findall("ARP .+? (.+?) ", ligne)[0] in arp_table:
                    if arp_table[re.findall("ARP .+? (.+?) ", ligne)[0]] != re.findall("is at (.+?)\n", ligne)[0]:
                        self.IA["SPY"] += 1
                else:
                    with open(f"{self.Path['PATH_SAVE']}arp_table", "a") as ARP:
                        ARP.write(re.findall("ARP .+? (.+?) ", ligne)[0])
                        ARP.write(";")
                        ARP.write(re.findall("is at (.+?)\n", ligne)[0])
                        ARP.write("\n")
                        arp_table[re.findall("ARP .+? (.+?) ", ligne)[0]] = re.findall("is at (.+?)\n", ligne)[0]
        return


    def DDoSCheck(self):
        open(f"{self.Path['PATH_SAVE']}first.csv", "w").close()
        try:
            ApplyCommand(f"tshark -r {self.Path['PATH_SAVE']}temp.pcap -T fields -E separator=, -e frame.len -e frame.time_delta -e ip.proto > {self.Path['PATH_SAVE']}first.csv")
        except Exception as e:
            print(e)
            self.Status['PROCESS'] = False
            self.Status['NEW'] = True
            return

        open(f"{self.Path['PATH_SAVE']}clean.csv", "w").close()

        try:
            ApplyCommand(f"sudo python3 {self.Path['PATH_PREPROCESS_SCRIPT']}ds_preprocess.py > {self.Path['PATH_SAVE']}clean.csv")
        except Exception as e:
            print(e)
            self.Status['PROCESS'] = False
            self.Status['NEW'] = True
            return

        os.remove(f"{self.Path['PATH_SAVE']}first.csv")
        try:
            RemoveFirstLine(f"{self.Path['PATH_SAVE']}clean.csv")
        except Exception as e:
            print(e)
            self.Status['PROCESS'] = False
            self.Status['NEW'] = True
            return

        print("check packets...")
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
            try:
                self.IA["PREDICTION"] = self.IA["MODEL"].predict(result)
            except Exception as e:
                print(e)
                return
            for i in range(len(result)):
                if self.IA["PREDICTION"][i][1] > 0.5:
                    self.IA["NUMBER_BAD_PACKETS"] = self.IA["NUMBER_BAD_PACKETS"] + 1

        os.remove(f"{self.Path['PATH_SAVE']}clean.csv")
        return
