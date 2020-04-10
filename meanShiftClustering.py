import math

import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets.samples_generator import make_blobs
from itertools import cycle
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import groupSeparation


class Center:
    def __init__(self, x, y, z, colour):
        self.x = x
        self.y = y
        self.z = z
        self.points = []
        self.colour = colour

    def add_point(self, x, y, z, group):
        self.points.append([x, y, z, group])

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

def find_closest_centroid(points, centers):
    for center in centers:
        center.clear_points()
    for i in range(0, len(x)):
        smallest_euclidean_distance = 10000
        chosen_centroid = 0
        # loop through each of the centroid's coordinates, calculate the distance
        for j in range(0, len(centers)):
            euclidean_distance = math.sqrt(
                (((points[i].x - centers[j].x) ** 2) + ((points[i].y - centers[j].y) ** 2) + ((points[i].z - centers[j].z) ** 2)))
            if euclidean_distance < smallest_euclidean_distance:
                smallest_euclidean_distance = euclidean_distance
                chosen_centroid = j
        # add this value to the centroid's cluster
        centers[chosen_centroid].add_point(points[i].x, points[i].y, points[i].z, points[i].group)
    return


if __name__ == '__main__':
    # take in the data from the csv
    group_object = groupSeparation.Groups("G1.csv", "G2.csv", "G3.csv", "G4.csv")
    data = group_object.final_data

    x = group_object.final_x
    y = group_object.final_y
    z = group_object.final_z

    list_of_points = []
    for i in range(0, len(group_object.final_data)):
        list_of_points.append(Point(group_object.final_data[i][0], group_object.final_data[i][1], group_object.final_data[i][2], group_object.final_labels[i]))


    # estimate the centers given the data
    bandwidth = estimate_bandwidth(data)
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(data)
    cluster_centers = ms.cluster_centers_
    print(cluster_centers)

    # place the found clusters in the list of cluster objects
    cluster_objects = []
    colours = ['y', 'b', 'g', 'r', 'c']
    for i in range(0, len(cluster_centers)):
        cluster_objects.append(Center(cluster_centers[i][0], cluster_centers[i][1], cluster_centers[i][2], colours[i]))


    # assign the closest points to each cluster
    find_closest_centroid(list_of_points, cluster_objects)

    for cluster in cluster_objects:
        print("Coordinates: X: " + str(cluster.x) + " Y: " + str(cluster.y) + " Z: " + str(cluster.z))
        print("Points: " + str(cluster.points))
        print(cluster.get_xs())
    # generate labels for clusters
    number_of_clusters = len(np.unique(ms.labels_))

    for cluster in cluster_objects:
        # print(centroid.points)
        # count each of the groups per point
        g1_tally = 0
        g2_tally = 0
        g3_tally = 0
        g4_tally = 0
        for i in range(0, len(cluster.points)):
            if cluster.points[i][3] == "g1":
                g1_tally = g1_tally + 1
            elif cluster.points[i][3] == "g2":
                g2_tally = g2_tally + 1
            elif cluster.points[i][3] == "g3":
                g3_tally = g3_tally + 1
            elif cluster.points[i][3] == "g4":
                g4_tally = g4_tally + 1
        print("The total tallies:\n G1: " + str(g1_tally) + " | G2: " + str(g2_tally) + " | G3: " + str(g3_tally)  + " | G4: " + str(g4_tally))


    # configure matplotlib information
    fig = plt.figure()
    plt.clf()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('"Yes" Responses')
    ax.set_ylabel('"No" Responses')
    ax.set_zlabel('"Undecided" Responses')
    ax.set_title("Mean Shift Clustering")
    for i in range(0, len(cluster_objects)):
        ax.scatter(cluster_objects[i].get_xs(),cluster_objects[i].get_ys(), cluster_objects[i].get_zs(), color= cluster_objects[i].colour)
        ax.scatter(cluster_objects[i].x, cluster_objects[i].y, cluster_objects[i].z, color=cluster_objects[i].colour, marker="^")
    plt.show()
