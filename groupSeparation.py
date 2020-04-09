import csv

import numpy as np


class Groups:
    def __init__(self, g1, g2, g3, g4):
        self.final_labels = []

        self.g1_data = []
        self.g2_data = []
        self.g3_data = []
        self.g4_data = []

        self.final_x = []
        self.final_y = []
        self.final_z = []

        self.obtain_data(g1)
        self.obtain_data(g2)
        self.obtain_data(g3)
        self.obtain_data(g4)

        print(self.g1_data)
        print(self.g2_data)
        print(self.g3_data)
        print(self.g4_data)


    def obtain_data(self, fileName):
        with open(fileName) as f:
            so = csv.reader(f, delimiter=',', quotechar='"')
            so = list(so)
        # add all the data to their respective array
        label = ""
        # add label to the end
        if(fileName == "G1.csv"):
            label = "g1"
            self.g1_data = [list(map(int, i)) for i in so]
        elif (fileName == "G2.csv"):
            label = "g2"
            self.g2_data = [list(map(int, i)) for i in so]
        elif (fileName == "G3.csv"):
            label = "g3"
            self.g3_data = [list(map(int, i)) for i in so]
        elif (fileName == "G4.csv"):
            label = "g4"
            self.g4_data = [list(map(int, i)) for i in so]

        # split up the data into x, y, and z arrays
        for i in range(0, len(so)):
            self.final_x.append(int(so[i][0]))
            self.final_y.append(int(so[i][1]))
            self.final_z.append(int(so[i][2]))
            self.final_labels.append(label)


