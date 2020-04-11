import random
import math 


class Groups:
    def __init__(self, fileNameG1, fileNameG2, fileNameG3, fileNameG4):
        self.numOfGroups = 4
        self.numOfQuestions = 15
        self.numOfOptions = 3

        # obtain data from files
        self.orignalFiles = [fileNameG1, fileNameG2, fileNameG3, fileNameG4]
        
        self.all_original_data = []

        self.obtainData()

        # create sample data
        self.all_sample_data = []
        self.createSample()

    def obtainData(self):
        data_in_group = []

        for groupNum in range (len(self.orignalFiles)):
            with open(self.orignalFiles[groupNum]) as f:
                
                contentInFile = f.readlines()

                for data in contentInFile:
                    data = data.replace("\n","")
                    data = [int(x) for x in data.split(",")]
                    data_in_group.append(data)
            self.all_original_data.append(data_in_group)
            data_in_group = []
        print("------------------------------Data in collected--------------------------------")
        print(self.all_original_data)
    

    def createSample(self):
        print("----------------------------sample created ------------------------------------")
        
        for groupNum in range(self.numOfGroups):
            f = open("sample-data/sample-data-G"+str(groupNum+1)+".csv", "w")
            for i in range(20):
                for questionNum in range(self.numOfQuestions):
                    data = data = self.all_original_data[groupNum][questionNum]
                    self.all_sample_data.append(data)
                    newData = self.createData(data)
                    add = ','.join([str(ele) for ele in newData])
                    f.write(add)
                    f.write("\n")
            f.close()
        print(self.all_sample_data)

    def createData(self, data):
        newData = []
        numOfZeros = 0
        peeps_remaining = 100
        change = 101

        for item in data:
            if item == 0:
                numOfZeros = numOfZeros + 1

        if numOfZeros == 1:    
            location = data.index(0)

            for i in range(len(data)):
                if (i == location):
                    newData.append(0)
                    
                elif peeps_remaining > 0 and peeps_remaining < 100:
                    peeps_remaining = peeps_remaining - data[i]
                    newData.append(peeps_remaining + data[i])
                else:
                    while True:
                        precentage = random.randint(-5,5)/100  
                        change = int(math.floor(float(data[i]) * precentage))
                
                        if (data[i] + change) < 100 and (data[i] + change ) > 0:
                            break
                
                    newData.append(data[i] + change)
                    peeps_remaining = peeps_remaining - (data[i]+ change)
                

        elif numOfZeros == 2:
            newData = data

        else:
            isItemSelected = False
            

            # select index at random --> that value will be increased 
            item_to_change = random.randint(0,2)
            
            item_choosen = item_to_change

            while True:
                precentage = random.randint(-5,5)/100  
                change = int(math.floor(float(data[item_to_change]) * precentage))
                
                if (data[item_to_change] + change) < 100 and (data[item_to_change] + change ) > 0:
                    break
            dataChange = (data[item_to_change] + change)

            

            # go through the data and decrease the other two
            for item in range(len(data)):
                if item == item_to_change:
                    newData.append(dataChange)
                
                else:
                    # for one
                    if change == 1 or change == -1:
                        if isItemSelected == False:
                            while item_choosen == item_to_change:
                                item_choosen = random.randint(0,2)
                                
                            
                            newData.append(data[item] - change)
                            isItemSelected = True
                        else:
                            newData.append(data[item])
                    # for odd numbers
                    elif change % 2 == 1 and (change != 1 or change !=-1):
                        if isItemSelected == False:
                            if (change > 0):
                                x = random.randint(0, change)
                                x2 = change + x
                            else:
                                x = random.randint(change,0)
                                x2 = change - x
                            
                            
                            newData.append(data[item] - x)
                            isItemSelected = True
                        else:
                            if change > 0:
                                newData.append(data[item] + x2)
                            else:
                                newData.append(data[item] - x2)
                    # for even numbers
                    else:
                        data[item] = data[item] - int(math.floor(float(change)/2))
                        newData.append(data[item])


        #print("\n newData: " + str(newData))
        return newData
            
            