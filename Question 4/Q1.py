# which group provided more unified answers to the questions?

# go through each question in the group
import csv
import groupSeparation
from statistics import mean

group_object = groupSeparation.Groups("../G1.csv", "../G2.csv", "../G3.csv", "../G4.csv")

# find g1's average internal agreement
g1_highest_values = []
# find percent of each value (y/n/u) within the question
for data in group_object.g1_data:
    biggest_attribute = 0
    for i in range(0, len(data)):
        percent = data[i]/sum(data)
        if percent > biggest_attribute:
            biggest_attribute = percent
    # the highest percent found = % agreement for that question
    g1_highest_values.append(biggest_attribute)
# print("All of g1's highest values: " + str(g1_highest_values))

# find the average agreement for the group
g1_avg = mean(g1_highest_values)
print("G1's Average Internal Agreement: " + str(g1_avg))

# find g2's average internal agreement
g2_highest_values = []
# find percent of each value (y/n/u) within the question
for data in group_object.g2_data:
    biggest_attribute = 0
    for i in range(0, len(data)):
        percent = data[i]/sum(data)
        if percent > biggest_attribute:
            biggest_attribute = percent
    # the highest percent found = % agreement for that question
    g2_highest_values.append(biggest_attribute)
# print("All of g2's highest values: " + str(g2_highest_values))

# find the average agreement for the group
g2_avg = mean(g2_highest_values)
print("G2's Average Internal Agreement: " + str(g2_avg))

# find g3's average internal agreement
g3_highest_values = []
# find percent of each value (y/n/u) within the question
for data in group_object.g3_data:
    biggest_attribute = 0
    for i in range(0, len(data)):
        percent = data[i]/sum(data)
        if percent > biggest_attribute:
            biggest_attribute = percent
    # the highest percent found = % agreement for that question
    g3_highest_values.append(biggest_attribute)
# print("All of g3's highest values: " + str(g3_highest_values))

# find the average agreement for the group
g3_avg = mean(g3_highest_values)
print("G3's Average Internal Agreement: " + str(g3_avg))


# find g4's average internal agreement
g4_highest_values = []
# find percent of each value (y/n/u) within the question
for data in group_object.g4_data:
    biggest_attribute = 0
    for i in range(0, len(data)):
        percent = data[i]/sum(data)
        if percent > biggest_attribute:
            biggest_attribute = percent
    # the highest percent found = % agreement for that question
    g4_highest_values.append(biggest_attribute)
# print("All of g4's highest values: " + str(g4_highest_values))

# find the average agreement for the group
g4_avg = mean(g4_highest_values)
print("G4's Average Internal Agreement: " + str(g4_avg))

# repeat the whole process for each group, determine which group had the highest average %

