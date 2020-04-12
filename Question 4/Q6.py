# which group provided more unified answers to the questions?

# go through each question in the group
import csv
import groupSeparation
from statistics import mean

group_object = groupSeparation.Groups("../G1.csv", "../G2.csv", "../G3.csv", "../G4.csv")

# find g1's average internal agreement
g1_highest_values = []
# find percent of each value (y/n/u) within the question
for i in range(0, len(group_object.g1_data)):
    biggest_attribute = 0
    for j in range(0, len(group_object.g1_data[i])):
        percent = group_object.g1_data[i][j]/sum(group_object.g1_data[i])
        if percent > biggest_attribute:
            biggest_attribute = percent
    # the highest percent found = % agreement for that question
    g1_highest_values.append([biggest_attribute, i])
# print("All of g1's highest values: " + str(g1_highest_values))

g1_sorted_list = sorted(g1_highest_values, key=lambda x: x[0], reverse=True)
print("G1 [agreement level, question #]: " + str(g1_sorted_list))

# find g2's average internal agreement
g2_highest_values = []
# find percent of each value (y/n/u) within the question
for i in range(0, len(group_object.g2_data)):
    biggest_attribute = 0
    for j in range(0, len(group_object.g2_data[i])):
        percent = group_object.g2_data[i][j]/sum(group_object.g2_data[i])
        if percent > biggest_attribute:
            biggest_attribute = percent
    # the highest percent found = % agreement for that question
    g2_highest_values.append([biggest_attribute, i])
# print("All of g2's highest values: " + str(g2_highest_values))

g2_sorted_list = sorted(g2_highest_values, key=lambda x: x[0], reverse=True)
print("G2 [agreement level, question #]: " + str(g2_sorted_list))


# find g3's average internal agreement
g3_highest_values = []
# find percent of each value (y/n/u) within the question
for i in range(0, len(group_object.g3_data)):
    biggest_attribute = 0
    for j in range(0, len(group_object.g3_data[i])):
        percent = group_object.g3_data[i][j]/sum(group_object.g3_data[i])
        if percent > biggest_attribute:
            biggest_attribute = percent
    # the highest percent found = % agreement for that question
    g3_highest_values.append([biggest_attribute, i])
# print("All of g3's highest values: " + str(g3_highest_values))

g3_sorted_list = sorted(g3_highest_values, key=lambda x: x[0], reverse=True)
print("G3 [agreement level, question #]: " + str(g3_sorted_list))

# find g4's average internal agreement
g4_highest_values = []
# find percent of each value (y/n/u) within the question
for i in range(0, len(group_object.g4_data)):
    biggest_attribute = 0
    for j in range(0, len(group_object.g4_data[i])):
        percent = group_object.g4_data[i][j]/sum(group_object.g4_data[i])
        if percent > biggest_attribute:
            biggest_attribute = percent
    # the highest percent found = % agreement for that question
    g4_highest_values.append([biggest_attribute, i])
# print("All of g4's highest values: " + str(g4_highest_values))

g4_sorted_list = sorted(g4_highest_values, key=lambda x: x[0], reverse=True)
print("G4 [agreement level, question #]: " + str(g4_sorted_list))


