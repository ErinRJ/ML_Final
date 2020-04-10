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

    def add_point(self, x, y, z):
        self.points.append([x, y, z])

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

def find_closest_centroid(x, y, z, centers):
    for center in centers:
        center.clear_points()
    for i in range(0, len(x)):
        smallest_euclidean_distance = 10000
        chosen_centroid = 0
        # loop through each of the centroid's coordinates, calculate the distance
        for j in range(0, len(centers)):
            euclidean_distance = math.sqrt(
                (((x[i] - centers[j].x) ** 2) + ((y[i] - centers[j].y) ** 2) + ((z[i] - centers[j].z) ** 2)))
            if euclidean_distance < smallest_euclidean_distance:
                smallest_euclidean_distance = euclidean_distance
                chosen_centroid = j
        # add this value to the centroid's cluster
        centers[chosen_centroid].add_point(x[i], y[i], z[i])
    return


if __name__ == '__main__':
    # take in the data from the csv
    group_object = groupSeparation.Groups("G1.csv", "G2.csv", "G3.csv", "G4.csv")
    data = group_object.final_data

    x = group_object.final_x
    y = group_object.final_y
    z = group_object.final_z

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
    find_closest_centroid(x, y, z, cluster_objects)

    for cluster in cluster_objects:
        print("Coordinates: X: " + str(cluster.x) + " Y: " + str(cluster.y) + " Z: " + str(cluster.z))
        print("Points: " + str(cluster.points))
        print(cluster.get_xs())
    # generate labels for clusters
    number_of_clusters = len(np.unique(ms.labels_))

    # configure matplotlib information
    fig = plt.figure()
    plt.clf()
    ax = fig.add_subplot(111, projection='3d')



    # for point in data:
    #     ax.scatter(point[0], point[1], point[2], marker='o')
    # for i in range(0, len(cluster_objects)):
    #     ax.scatter(cluster_objects[i].x, cluster_objects[i].y, cluster_objects[i].z, marker='^', color=colours[i],
    #                linewidth=5, zorder=10)
        # for j in range(0, len(cluster_objects[i].points)):
        #     ax.scatter(cluster_objects[i].points[j][0], cluster_objects[i].points[j][1], cluster_objects[i].points[j][2], marker='o',
        #                color=colours[i],
        #                linewidth=5, zorder=10)
    for i in range(0, len(cluster_objects)):
        ax.scatter(cluster_objects[i].get_xs(),cluster_objects[i].get_ys(), cluster_objects[i].get_zs(), color= cluster_objects[i].colour)
        ax.scatter(cluster_objects[i].x, cluster_objects[i].y, cluster_objects[i].z, color=cluster_objects[i].colour, marker="^")
    plt.show()
