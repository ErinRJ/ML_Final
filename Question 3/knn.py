import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import groups

# load in info from the csvs as the data
question_object = groups.Groups("G1-Sheet1.csv", "G2-Sheet1.csv", "G3-Sheet1.csv", "G4-Sheet1.csv")
training_data = question_object.final_training_data
training_results = question_object.desired_training
testing_data = question_object.final_testing_data
testing_results = question_object.desired_testing

# convert the data to dataframes
columns = ['yes', 'no', 'undecided', 'yes', 'no', 'undecided','yes', 'no', 'undecided', 'yes', 'no', 'undecided',
           'yes', 'no', 'undecided', 'yes', 'no', 'undecided','yes', 'no', 'undecided', 'yes', 'no', 'undecided',
           'yes', 'no', 'undecided', 'yes', 'no', 'undecided','yes', 'no', 'undecided', 'yes', 'no', 'undecided',
           'yes', 'no', 'undecided', 'yes', 'no', 'undecided','yes', 'no', 'undecided']
df_train_data = pd.DataFrame(training_data, columns=columns)
df_test_data = pd.DataFrame(testing_data, columns=columns)
print(df_train_data)
print(df_test_data)

# create the model
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')

# train the model to fit the training data provided
knn.fit(df_train_data, training_results)

# predict the outputs, given the testing data
predicted_values = knn.predict(testing_data)

# find the percent accuracy of the system
total_matches = 0
for i in range(0, len(predicted_values)):
    # print(predicted_values[i])
    # print(testing_results[i])
    # compare each predicted result against the actual result
    if (predicted_values[i] == testing_results[i]).all():
        total_matches = total_matches + 1
percent_accuracy = total_matches / len(testing_results) * 100
print("Percent Accuracy: " + str(percent_accuracy) + "%")
#
