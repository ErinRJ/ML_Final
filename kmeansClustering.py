import copy
import groupSeparation
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Centroid:
    def __init__(self, colour):
        self.x = np.random.randint(0, 100)
        self.y = np.random.randint(0, 100)
        self.z = np.random.randint(0, 100)
        self.colour = colour
        self.points = []
        self.g1_matches = 0
        self.g2_matches = 0
        self.g3_matches = 0
        self.g4_matches = 0

    # def add_point(self, x, y, z):
    #     self.points.append([x, y, z])
    def add_point(self, x, y, z, group):
        self.points.append([x, y, z, group])

    def update_centroid(self):
        xs = self.get_xs()
        ys = self.get_ys()
        zs = self.get_zs()
        self.x = sum(xs) / len(xs)
        self.y = sum(ys) / len(ys)
        self.z = sum(zs) / len(zs)

    def clear_points(self):
        self.points = []

    def get_xs(self):
        temp_array = []
        for i in range(0, len(self.points)):
            temp_array.append(self.points[i][0])
        return temp_array

    def get_ys(self):
        temp_array = []
        for i in range(0, len(self.points)):
            temp_array.append(self.points[i][1])
        return temp_array

    def get_zs(self):
        temp_array = []
        for i in range(0, len(self.points)):
            temp_array.append(self.points[i][2])
        return temp_array

class Point:
    def __init__(self, x, y, z, group):
        self.x = x
        self.y = y
        self.z = z
        self.group = group


def initialize_components(points):
    # randomly initialize centroid values
    k = 4
    centroids = []
    centroid_colours = ['r', 'b', 'g', 'y']

    for i in range(k):
        centroids.append(Centroid(centroid_colours[i]))
    # print(centroids)

    # assign each variable to the closest centroid
    find_closest_centroid(points, centroids)
    # loop through each variables, find the centroid with the smallest euclidean distance
    return centroids


def find_closest_centroid(points, centroids):
    # first clear up the points belonging to each centroid
    for centroid in centroids:
        centroid.clear_points()
    for i in range(0, len(points)):
        smallest_euclidean_distance = 10000
        chosen_centroid = 0
        # loop through each of the centroid's coordinates, calculate the distance
        for j in range(0, len(centroids)):
            euclidean_distance = math.sqrt((((points[i].x - centroids[j].x) ** 2) + ((points[i].y - centroids[j].y) ** 2) + ((points[i].z - centroids[j].z) ** 2)))
            if euclidean_distance < smallest_euclidean_distance:
                smallest_euclidean_distance = euclidean_distance
                chosen_centroid = j
        # add this value to the centroid's cluster
        # print("Chosen centroid: " + str(chosen_centroid))
        centroids[chosen_centroid].add_point(points[i].x, points[i].y, points[i].z, points[i].group)
    return centroids


def verify_centroids(centroids):
    # make sure that all centroids have at least one point in the cluster
    for element in centroids:
        if len(element.get_xs()) <= 1:
            return False
    return True



def plot_final_results(centroids):
    # define the matplotlib properties
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('"Yes" Responses')
    ax.set_ylabel('"No" Responses')
    ax.set_zlabel('"Undecided" Responses')
    ax.set_title("K Means Clustering")


    plt.figure(figsize=(5, 5))
    for i in range(0, len(centroids)):
        ax.scatter(centroids[i].get_xs(), centroids[i].get_ys(), centroids[i].get_zs(), color=centroids[i].colour)
        ax.scatter(centroids[i].x, centroids[i].y, centroids[i].z, color=centroids[i].colour, marker="^")
    # show the final plot
    plt.show()


if __name__ == '__main__':
    np.random.seed(200)
    group_object = groupSeparation.Groups("G1.csv", "G2.csv", "G3.csv", "G4.csv")

    x_values = group_object.final_x
    y_values = group_object.final_y
    z_values = group_object.final_z

    # define object array of all points
    list_of_points = []
    for i in range(0, len(group_object.final_data)):
        list_of_points.append(Point(group_object.final_data[i][0], group_object.final_data[i][1], group_object.final_data[i][2], group_object.final_labels[i]))

    # initialize all of the elements
    keep_looping = True
    list_of_centroids = []

    while keep_looping:
        list_of_centroids = initialize_components(list_of_points)

        # make sure each centroid has at least one point within its cluster
        verification = verify_centroids(list_of_centroids)
        # if there's a point in each cluster, leave the loop
        if verification:
            keep_looping = False


    finding_optimal_centroids = True
    while finding_optimal_centroids:
        print("new loop")
        # log centroid results
        old_centroids = copy.deepcopy(list_of_centroids)
        # update the centroid to the mean of the cluster
        for centroid in list_of_centroids:
            centroid.update_centroid()

        # check if the centroids have changed since last time
        changed = False
        for i in range(0, len(old_centroids)):
            print("OLD: \nX: " + str(old_centroids[i].x) + " Y: " + str(old_centroids[i].y) + " Z: " + str(old_centroids[i].x))
            print("NEW: \nX: " + str(list_of_centroids[i].x) + " Y: " + str(list_of_centroids[i].y) + " Z: " + str(list_of_centroids[i].x))
            if (list_of_centroids[i].x != old_centroids[i].x) | (list_of_centroids[i].y != old_centroids[i].y) | (list_of_centroids[i].z != old_centroids[i].z):
                print("It changed!")
                changed = True

        if changed == False:
            finding_optimal_centroids = False

        # recalculate which points belong to which cluster
    list_of_centroids = find_closest_centroid(list_of_points, list_of_centroids)
    # print("These are the centroid's points: ")
    for centroid in list_of_centroids:
        # print(centroid.points)
        # count each of the groups per point
        g1_tally = 0
        g2_tally = 0
        g3_tally = 0
        g4_tally = 0
        for i in range(0, len(centroid.points)):
            if centroid.points[i][3] == "g1":
                g1_tally = g1_tally + 1
            elif centroid.points[i][3] == "g2":
                g2_tally = g2_tally + 1
            elif centroid.points[i][3] == "g3":
                g3_tally = g3_tally + 1
            elif centroid.points[i][3] == "g4":
                g4_tally = g4_tally + 1
        print("The total tallies:\n G1: " + str(g1_tally) + " | G2: " + str(g2_tally) + " | G3: " + str(g3_tally)  + " | G4: " + str(g4_tally))

    # plot the final graph
    plot_final_results(list_of_centroids)