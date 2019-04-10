import matplotlib.pyplot as plt
import numpy as np
from point import Point

X_SIZE = 30
Y_SIZE = 100
ATOM_SIZE = X_SIZE * Y_SIZE


def print_two_d_array(arr):
    print(arr.shape)
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            print(arr[i, j])


def get_input_data():
    input_file = open("config/input.dat", "r")
    d = []
    for i in range(0, ATOM_SIZE):
        line = input_file.readline()
        x, y, z, q = line.split()
        d.append([float(x), float(y)])
    input_file.close()
    return d


def get_sorted_points(p_input_data):
    y_sorted_list_desc = sorted(p_input_data, key=lambda k: [(k[1])], reverse=True)
    point_list = []
    for i in range(0, ATOM_SIZE, X_SIZE):
        t = sorted(y_sorted_list_desc[i:i + X_SIZE], key=lambda k: [(k[0])], reverse=False)
        point_list.append([Point(val[0], val[1]) for val in t])
    return point_list


def plot_sorted_point_array(p_sorted_point_array):
    x_values = []
    y_values = []
    labels = []
    for i in range(0, p_sorted_point_array.shape[0]):
        for j in range(0, p_sorted_point_array.shape[1]):
            # print(p_sorted_point_array[i,j])
            pt = p_sorted_point_array[i, j]
            x_values.append(pt.x)
            y_values.append(pt.y)
            labels.append("(" + str(i) + "," + str(j) + ")")
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values)
    for i, txt in enumerate(labels):
        ax.annotate(txt, (x_values[i], y_values[i]))
    plt.scatter(x_values, y_values)
    plt.show()


def is_boundary_point(px, py):
    return px < 0 or py < 0 or px >= X_SIZE or py >= Y_SIZE


def get_mid_point(p_sorted_point_array, ppt, nbr_pt_x, nbr_pt_y):
    if is_boundary_point(nbr_pt_x, nbr_pt_y) is False:
        nbr_pt = p_sorted_point_array[nbr_pt_x, nbr_pt_y]
        if nbr_pt.visited is False:
            return (ppt.x + nbr_pt.x) / 2.0, (ppt.y + nbr_pt.y) / 2.0
    return None


def get_mid_of_nbr_pts(p_sorted_point_array):
    mid_x_list = []
    mid_y_list = []
    for i in range(0, p_sorted_point_array.shape[0]):
        for j in range(0, p_sorted_point_array.shape[1]):
            pt = p_sorted_point_array[i, j]

            nbt_pt1 = get_mid_point(p_sorted_point_array, pt, i, j - 1)
            if nbt_pt1 is not None:
                mid_x_list.append(nbt_pt1[0])
                mid_y_list.append(nbt_pt1[1])

            nbt_pt2 = get_mid_point(p_sorted_point_array, pt, i + 1, j - 1)
            if nbt_pt2 is not None:
                mid_x_list.append(nbt_pt2[0])
                mid_y_list.append(nbt_pt2[1])

            nbt_pt3 = get_mid_point(p_sorted_point_array, pt, i - 1, j)
            if nbt_pt3 is not None:
                mid_x_list.append(nbt_pt3[0])
                mid_y_list.append(nbt_pt3[1])

            nbt_pt4 = get_mid_point(p_sorted_point_array, pt, i + 1, j)
            if nbt_pt4 is not None:
                mid_x_list.append(nbt_pt4[0])
                mid_y_list.append(nbt_pt4[1])

            nbt_pt5 = get_mid_point(p_sorted_point_array, pt, i, j + 1)
            if nbt_pt5 is not None:
                mid_x_list.append(nbt_pt5[0])
                mid_y_list.append(nbt_pt5[1])

            nbt_pt6 = get_mid_point(p_sorted_point_array, pt, i + 1, j + 1)
            if nbt_pt6 is not None:
                mid_x_list.append(nbt_pt6[0])
                mid_y_list.append(nbt_pt6[1])

            pt.visited = True

    return mid_x_list, mid_y_list


def plot_points_with_mid_points(p_sorted_point_array, mid_pt_x_valus, mid_pt_y_values):
    x_values = []
    y_values = []
    labels = []
    for i in range(0, p_sorted_point_array.shape[0]):
        for j in range(0, p_sorted_point_array.shape[1]):
            # print(p_sorted_point_array[i,j])
            pt = p_sorted_point_array[i, j]
            x_values.append(pt.x)
            y_values.append(pt.y)
            labels.append("(" + str(i) + "," + str(j) + ")")
    plt.scatter(x_values, y_values,c='b')
    plt.scatter(mid_pt_x_valus, mid_pt_y_values,c='r',marker='o',s=10)
    plt.show()

input_data = get_input_data()
sorted_point_list = get_sorted_points(input_data)
sorted_point_array = np.transpose(np.array(sorted_point_list))
# print_two_d_array(sorted_point_array)
# plot_sorted_point_array(sorted_point_array)
mid_x_list, mid_y_list = get_mid_of_nbr_pts(sorted_point_array)
with open('CM-data.dat', 'w') as f:
    for f1, f2 in zip(mid_x_list, mid_y_list):
        print(f1, f2, file=f)
plot_points_with_mid_points(sorted_point_array, mid_x_list, mid_y_list)
