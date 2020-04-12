import random

import numpy as np

import matplotlib.pyplot as plt

import groups


# properties and functions of a neuron(step 1)
class HiddenNeuron:
    def __init__(self, n):
        self.n = n
        self.weights = []
        self.result = 0
        self.delta = 0

    def randomize_weight(self):
        for j in range(0, self.n):
            self.weights.append(random.uniform(-0.5, 0.5))

    def get_weight(self, m):
        return self.weights[m]

    def get_result(self):
        return (self.result)

    # activate perceptron (step 2)
    def activation(self, n, thresh, data):
        sum = 0
        # loop through all of the perceptron inputs, calculate the activation factor
        for j in range(0, n):
            sum += (data[j]) * self.get_weight(j) - thresh

        # activation function
        sig_result = 1 / (1 + np.exp(-sum))
        tan_result = np.tanh(sum)
        relu_result = max(0,sum)

        self.result = sig_result


        return self.result

    def print_weight(self):
        print(self.weights)


class FinalNeuron:
    def __init__(self, n):
        self.n = n
        self.final_sum = 0
        self.weights = []
        self.sum = 0
        self.delta = 0
        self.hidden_layer_sum = 0  ## without weights

    def randomize_weight(self):
        for j in range(0, self.n):
            self.weights.append(random.uniform(-0.5, 0.5))

    def calculate_weighted_sum(self, hidden_neurons):
        # find the sum of all the previous layer's results
        sum = 0
        for i in range(0, len(hidden_neurons)):
            self.hidden_layer_sum = self.hidden_layer_sum + hidden_neurons[i].result
            sum = sum + hidden_neurons[i].result * self.weights[i]

        # put the sum through an activation function
        sig_result = 1 / (1 + np.exp(-sum))
        tan_result = np.tanh(sum)
        relu_result = max(0,sum)

        self.sum = sig_result

    def print_weight(self):
        print(self.weights)

    def print_sum(self):
        print(self.sum)

    def update_weights(self, alph, hidden_neurons, error):
        # find delta weight
        delta_weights = []
        for k in range(0, self.n):
            delta = alph * hidden_neurons[k].result * error
            delta_weights.append(delta)
        for k in range(0, self.n):
            self.weights[k] = self.weights[k] + delta_weights[k]

    def set_weights(self, listOfWeights):
        self.weights = listOfWeights


# Step 2 : Activate the hidden layer perceptrons
def activate_perceptrons(neurons, pn, thresh, data):
    # loop through each neuron, perform the activation function
    for k in range(0, len(neurons)):
        result = neurons[k].activation(pn, thresh, data)


# Step 3: Weight training
def weight_training(actualOutput, desiredOutput):
    delta = 0.1
    errorValues = []

    # Compare values from the desiredOutput with the actualOutput
    for i in range(len(actualOutput)):
        print("The experimental: " + str(actualOutput[i].sum) + " | the desired: " + str(desiredOutput[i]))
        error = desiredOutput[i] - actualOutput[i].sum
        errorValues.append(error)

    print(errorValues)
    return errorValues


# Step 5: compeleting test cases
def completingTestCases(finalNeuronList, hiddenNeuronList, testData, desired_output, thresh):
    # confusion matrix variables (true/false positive, true/false negative)
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    total_yes_predicted = 0
    total_no_predicted = 0

    print("\n\n -----STARTING TESTING-----")
    perceptron_num = 45
    total_correct = 0

    for i in range(len(testData)):
        # Step 2: Activation Function
        activate_perceptrons(hiddenNeuronList, perceptron_num, thresh, testData[i])

        for j in range(len(finalNeuronList)):
            finalNeuronList[j].calculate_weighted_sum(hiddenNeuronList)

        max = -100
        maxIndex = 0
        print("---------------------------------------------------------------------")
        for k in range(0, len(finalNeuronList)):
            print("NEURON SUM: " + str(finalNeuronList[k].sum))
            if (finalNeuronList[k].sum > max):
                max = finalNeuronList[k].sum
                maxIndex = k

        expected_index = 0

        # find which number is selected within the desired case
        for k in range(0, len(desired_output[i])):
            if desired_output[i][k] == 1:
                expected_index = k

        if expected_index == maxIndex:
            print("CORRECT")
            total_correct = total_correct + 1

        if (maxIndex == 0) & (expected_index == 0):
            tp = tp + 1
        elif (maxIndex == 1) & (expected_index) == 1:
            tn = tn + 1
        elif (maxIndex == 0) & (expected_index) == 1:
            fn = fn + 1
        elif (maxIndex == 1) & (expected_index) == 0:
            fp = fp + 1
        else:
            print("Something went wrong. MaxIndex: " + str(maxIndex) + " | expected_index: " + str(expected_index))

        print("ANSWER: " + str(max) + " is at index : " + str(maxIndex) + ", DESIRED OUTPUT: " + str(desired_output[i]))
    average = total_correct / len(testData)

    print("\nThe accuracy rate: " + str(average*100) + "%")
    print("TRUE POSITIVE: " + str(tp))
    print("TRUE NEGATIVE: " + str(tn))
    print("FALSE POSITIVE: " + str(fp))
    print("FALSE NEGATIVE: " + str(fn))


# this is just the code from the main function - I moved it here so it's easier to run lol
def mainCode(training, desired_training, testing, desired_testing):
    # Step 1a: create neuron objects and initialize weights and threshold (theta) to random numbers between [-0.5,0.5]
    perceptron_num = 45
    hidden_neuron_num = 20
    final_neuron_num = 4

    # define lists which hold the hidden and final layers of neuron objects
    hidden_neuron_list = []
    final_neuron_list = []

    # randomly generate the weights for the hidden neural layer
    print("\nHIDDEN NEURON LAYER")
    for i in range(0, hidden_neuron_num):
        # create a hidden neuron object, add it to the list
        hidden_neuron_list.append(HiddenNeuron(perceptron_num))
        hidden_neuron_list[i].randomize_weight()
        hidden_neuron_list[i].print_weight()

    # randomly generate the weights for the final neural layer
    print("\nFINAL NEURON LAYER")
    for i in range(0, final_neuron_num):
        # create a final neuron object, add it to the list
        final_neuron_list.append(FinalNeuron(hidden_neuron_num))
        final_neuron_list[i].randomize_weight()
        final_neuron_list[i].print_weight()

    # Step 1b: initialize threshold value
    threshold = random.uniform(-0.5, 0.5)

    # define variables for iterations
    listOfEpoc = []


    errorRate = 0.1
    maxValue = 0
    epocNumList = []
    listOfSavedWeights = []

    # Step 2: Activate perceptron
    for case in range(0, len(training)):
        print("======================New training scenario======================")
        numOfEpocs = 0
        while (numOfEpocs < 50):

            # loop through each of the training data
            error_sum = 0
            actual_outputs = []
            indexOfHighest = 0

            weighted_sums = []
            activate_perceptrons(hidden_neuron_list, perceptron_num, threshold, training[case])

            # calculate the weighted sum, for each final neuron object in the final neuron layer
            for k in range(0, final_neuron_num):
                final_neuron_list[k].calculate_weighted_sum(hidden_neuron_list)

            # Step 3: Weight training
            errorValues = weight_training(final_neuron_list, desired_training[case])

            for i in range(0, final_neuron_num):
                final_neuron_list[i].update_weights(0.1, hidden_neuron_list, errorValues[i])

            listOfEpoc.append(np.square(error_sum))
            epocNumList.append(numOfEpocs)

            numOfEpocs = numOfEpocs + 1
            print("NUM_OF_EPOCS: " + str(numOfEpocs) + "\n")

    completingTestCases(final_neuron_list, hidden_neuron_list, testing, desired_testing, threshold)


if __name__ == '__main__':
    question_object = groups.Groups("G1-Sheet1.csv", "G2-Sheet1.csv", "G3-Sheet1.csv", "G4-Sheet1.csv")

    print(question_object.final_testing_data)
    print("-----------------------------------------------------------")
    print(question_object.final_training_data)
    print("-----------------------------------------------------------")
    print(question_object.desired_testing)
    print("-----------------------------------------------------------")
    print(question_object.desired_training)

    print("TESTING LEN: " + str(len(question_object.final_testing_data)))
    print("TRAINING LEN: " + str(len(question_object.final_training_data)))

    mainCode(question_object.final_training_data, question_object.desired_training, question_object.final_testing_data, question_object.desired_testing)
