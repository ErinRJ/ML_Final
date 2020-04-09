import csv


class Groups:
    def __init__(self, g1, g2, g3, g4):
        self.final_labels = []
        self.final_x = []
        self.final_y = []
        self.final_z = []

        self.obtain_data(g1)
        self.obtain_data(g2)
        self.obtain_data(g3)
        self.obtain_data(g4)
        print(self.final_labels)


    def obtain_data(self, fileName):
        with open(fileName) as f:
            so = csv.reader(f, delimiter=',', quotechar='"')
            so = list(so)
        print(so)
        label = ""
        # add label to the end
        if(fileName == "G1.csv"):
            label = "g1"
        elif (fileName == "G2.csv"):
            label = "g2"
        elif (fileName == "G3.csv"):
            label = "g3"
        elif (fileName == "G4.csv"):
            label = "g4"

        # split up the data into x, y, and z arrays
        for i in range(0, len(so)):
            self.final_x.append(int(so[i][0]))
            self.final_y.append(int(so[i][1]))
            self.final_z.append(int(so[i][2]))
            self.final_labels.append(label)


