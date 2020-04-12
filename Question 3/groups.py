import random
import math 



class Groups:
    def __init__(self, fileNameG1, fileNameG2, fileNameG3, fileNameG4):
        print("Called the groups class")
        self.numOfGroups = 4
        self.numOfQuestions = 15
        self.numOfOptions = 3
        self.numOfSamples = 10

        # obtain data from files
        self.orignalFiles = [fileNameG1, fileNameG2, fileNameG3, fileNameG4]
        self.all_original_data = []

        self.obtainData()

        # create sample data
        self.all_sample_data = []

        self.createSample()

        # seperating the data into testing and training
        self.training_data = [] 
        self.testing_data = []
        
        self.seperateData()

        # populating the desired lists and final lists of testing and training
        self.desired_training = []
        self.desired_testing = []
        self.final_training_data = []
        self.final_testing_data = []
        
        self.creatingDesiredLists("training",self.training_data)
        self.creatingDesiredLists("testing",self.testing_data)

    # obtains the data from the files and places it into one big array
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
    
    # creates a the sample data based on the oringal data
    def createSample(self):
        
        for groupNum in range(self.numOfGroups):
            f = open("sample-data/sample-data-G"+str(groupNum+1)+".csv", "w")
            self.all_sample_data.append([])
            for i in range(self.numOfSamples):
                self.all_sample_data[groupNum].append([])
                self.all_sample_data[groupNum][i].append("G"+str(groupNum+1))
                for questionNum in range(self.numOfQuestions):
                    
                    # obtaining new data and writing it to approperiate file
                    data = self.all_original_data[groupNum][questionNum]
                    newData = self.createData(data)
                    add = ','.join([str(ele) for ele in newData])
                    f.write(add)
                    f.write("\n")

                    # adding new data to all_sample_data array 
                    
                    for j in range (len(newData)):
                        self.all_sample_data[groupNum][i].append(newData[j])
            f.close()
    
    # creates the indvidual data (i.e. the 3 elements in the array)
    def createData(self, data):
        newData = []                # new data to be returned to the createSample function
        numOfZeros = 0              # used to count the number of zeros
        peeps_remaining = 100       # used to count the number of people that are left to distribute among the three elements
        change = 101                # the amount the data will increase or decrease

        # counts the number of zeros
        for item in data:
            if item == 0:
                numOfZeros = numOfZeros + 1

        # if there is one zero it will increase one of the other two values and decrease the other 
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
                
        # if there are two zeros it will return the data (everyone has the same answer)
        elif numOfZeros == 2:
            newData = data

        # if are no zeros it will increase or decrease one value and then distribute the changes accordingly
        else:
            isItemSelected = False
            

            # select index at random --> that value will be increased/decreased
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
                    # if change is one or -1
                    if change == 1 or change == -1:
                        if isItemSelected == False:
                            while item_choosen == item_to_change:
                                item_choosen = random.randint(0,2)
                                
                            
                            newData.append(data[item] - change)
                            isItemSelected = True
                        else:
                            newData.append(data[item])
                    
                    # if the change is an odd number (that's not one)
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
                    # if the change is an even number
                    else:
                        data[item] = data[item] - int(math.floor(float(change)/2))
                        newData.append(data[item])

        return newData

    # sperates the data into training and testing data 
    def seperateData(self): 
        
        # Fining the total number of training and testing data
        totalNumOfSamples = self.numOfGroups * self.numOfSamples

        numOfTrainingData = self.numOfSamples * 0.7
        numOfTestingData = self.numOfSamples - numOfTrainingData

        num_of_training_data_added = 0
        num_of_testing_data_added = 0

        
        for group in self.all_sample_data:
            for item in group:
                # generate a random number between 0-10
                rand_num = random.randint(0, 10)

                # if it's >=2 the data will be in the testing set otherwise it will be in the training set
                if rand_num >= 2 and num_of_testing_data_added < numOfTestingData:
                    self.testing_data.append(item)
                    num_of_testing_data_added = num_of_testing_data_added + 1
                else:
                    self.training_data.append(item)
                    num_of_training_data_added = num_of_training_data_added + 1
            num_of_training_data_added = 0
            num_of_testing_data_added = 0
    
    
    # creates the final testing and training data and desired lists for each
    def creatingDesiredLists(self, type, list_of_data):
        
        # mix the array
        random.shuffle(list_of_data)
        
        # go though each element and add data to apporiate list
        for index in range(len(list_of_data)):
            group = list_of_data[index].pop(0)
           
            if group == "G1":
                data = [1,0,0,0]
            
            elif group == "G2":
                data = [0,1,0,0]
            
            elif group == "G3":
                data = [0,0,1,0]
            
            else:
                data = [0,0,0,1]

            if type == 'training':
                self.final_training_data.append(list_of_data[index])
                self.desired_training.append(data)
            if type == 'testing':
                self.final_testing_data.append(list_of_data[index])
                self.desired_testing.append(data)
                
            








        

