import copy
import math
import numpy as np
import matplotlib.pyplot as plt


class Centroid:
    def __init__(self, colour):
        self.x = np.random.randint(0, 100)
        self.y = np.random.randint(0, 100)
        self.colour = colour
        self.points = []

    def add_point(self, x, y):
        self.points.append([x, y])

    def update_centroid(self):
        xs = self.get_xs()
        ys = self.get_ys()
        self.x = sum(xs) / len(xs)
        self.y = sum(ys) / len(ys)

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


def initialize_components(x, y):
    # randomly initialize centroid values
    k = 4
    centroids = []
    centroid_colours = ['r', 'b', 'g', 'y']

    for i in range(k):
        centroids.append(Centroid(centroid_colours[i]))
    # print(centroids)

    # assign each variable to the closest centroid
    find_closest_centroid(x, y, centroids)
    # loop through each variables, find the centroid with the smallest euclidean distance
    return centroids


def find_closest_centroid(x, y, centroids):
    for i in range(0, len(x)):
        smallest_euclidean_distance = 10000
        chosen_centroid = 0
        # loop through each of the centroid's coordinates, calculate the distance
        for j in range(0, len(centroids)):
            euclidean_distance = math.sqrt((((x[i] - centroids[j].x) ** 2) + ((y[i] - centroids[j].y) ** 2)))
            if euclidean_distance < smallest_euclidean_distance:
                smallest_euclidean_distance = euclidean_distance
                chosen_centroid = j
        # add this value to the centroid's cluster
        centroids[chosen_centroid].add_point(x[i], y[i])
    return centroids


def verify_centroids(centroids):
    # make sure that all centroids have at least one point in the cluster
    for element in centroids:
        if len(element.get_xs()) == 0:
            return False
    return True
    # update the centroid to the mean of the cluster


def plot_final_results(centroids):
    # define the matplotlib properties
    plt.figure(figsize=(5, 5))
    for i in range(0, len(centroids)):
        plt.scatter(centroids[i].get_xs(), centroids[i].get_ys(), color=centroids[i].colour)
        plt.scatter(centroids[i].x, centroids[i].y, color=centroids[i].colour, marker="^")
    # show the final plot
    plt.show()


if __name__ == '__main__':
    np.random.seed(200)

    # take in the data
    x_values = [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72]
    y_values = [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]

    # initialize all of the elements
    keep_looping = True
    list_of_centroids = []

    while keep_looping:
        list_of_centroids = initialize_components(x_values, y_values)

        # make sure each centroid has at least one point within its cluster
        verification = verify_centroids(list_of_centroids)
        print("does every centroid have a point?: " + str(verification))
        # if there's a point in each cluster, leave the loop
        if verification:
            keep_looping = False

    finding_optimal_centroids = True
    while finding_optimal_centroids:
        # log centroid results
        old_centroids = copy.deepcopy(list_of_centroids)
        # update the centroid to the mean of the cluster
        for centroid in list_of_centroids:
            centroid.update_centroid()
        print("AFTER UPDATE")

        # check if the centroids have changed since last time
        changed_flag = False
        for i in range(0, len(old_centroids)):
            if (list_of_centroids[i].x != old_centroids[i].x) | (list_of_centroids[i].y != old_centroids[i].y):
                changed_flag = True

        # if the centroids have not changed, stop looping through
        if not changed_flag:
            finding_optimal_centroids = False

        # recalculate which points belong to which cluster
        list_of_centroids = find_closest_centroid(x_values, y_values, list_of_centroids)

    # plot the final graph
    plot_final_results(list_of_centroids)
