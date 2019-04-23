import matplotlib.pyplot as plt
import numpy as np
import random

import constants as const
from dumbbell import Dumbbell
from point import Point


def print_two_d_array(arr):
    print(arr.shape)
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            print(arr[i, j])

f1 = open("cmdata.dat", "w")

def get_input_data():
    input_file = open("config/input1.dat", "r")
    d = []
    for i in range(0, const.ATOM_SIZE):
        line = input_file.readline()
        x, y, z, q = line.split()
        d.append([float(x), float(y)])
    input_file.close()
    return d


def get_sorted_points(p_input_data):
    y_sorted_list_desc = sorted(p_input_data, key=lambda k: [(k[1])], reverse=True)
    point_list = []
    for i in range(0, const.ATOM_SIZE, const.X_SIZE):
        t = sorted(y_sorted_list_desc[i:i + const.X_SIZE], key=lambda k: [(k[0])], reverse=False)
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


def isPointOutOfBoundary(px, py):
    return px < 0 or py < 0 or px >= const.X_SIZE - 1 or py >= const.Y_SIZE


def connect(pd: Dumbbell, p_dumbbell_array: [], pi: int, pj: int):
    if isPointOutOfBoundary(pi, pj) is False:
        sourceDumbell = p_dumbbell_array[pi, pj]
        plt.plot([pd.u.x, sourceDumbell.d.x], [pd.u.y, sourceDumbell.d.y], c='b')


def plot_dumbbell_array(p_dumbbell_list):
    u_x_values = []
    c_x_values = []
    d_x_values = []
    u_y_values = []
    c_y_values = []
    d_y_values = []
    for dumbbell in p_dumbbell_list:
        u_x_values.append(dumbbell.u.x)
        c_x_values.append(dumbbell.c.x)
        d_x_values.append(dumbbell.d.x)
        u_y_values.append(dumbbell.u.y)
        c_y_values.append(dumbbell.c.y)
        d_y_values.append(dumbbell.d.y)

    labels = []
    for i in range(0, const.X_SIZE - 1):
        for j in range(0, const.Y_SIZE):
            labels.append("(" + str(i) + "," + str(j) + ")")
    fig, ax = plt.subplots()
    ax.scatter(c_x_values, c_y_values)
    for i, txt in enumerate(labels):
        ax.annotate(txt, (c_x_values[i], c_y_values[i]))
    plt.scatter(c_x_values, c_y_values, c='y')
    plt.scatter(u_x_values, u_y_values, c='b')
    plt.scatter(d_x_values, d_y_values, c='b')
    # plt.show()

    dumbbell_array = np.array(p_dumbbell_list).reshape(const.X_SIZE - 1, const.Y_SIZE)

    for i in range(0, dumbbell_array.shape[0]):
        for j in range(0, dumbbell_array.shape[1]):
            d = dumbbell_array[i, j]
            f1.write(str(d))
            plt.plot([d.u.x, d.d.x], [d.u.y, d.d.y], c='r')
            if isPointOutOfBoundary(i, j - 1) is False:
                ld = dumbbell_array[i, j - 1]
                # if ld.d.x < d.u.x:
                    # connect(d, dumbbell_array, i, j - 1)
                    # connect(d, dumbbell_array, i + 1, j - 1)
                # else:
                #     connect(d, dumbbell_array, i - 1, j - 1)
                #     connect(d, dumbbell_array, i, j - 1)
    f1.close()
    plt.show()

def is_boundary_point(px, py):
    return px < 0 or py < 0 or px >= const.X_SIZE or py >= const.Y_SIZE


def get_mid_point(p_sorted_point_array, ppt, nbr_pt_x, nbr_pt_y):
    if is_boundary_point(nbr_pt_x, nbr_pt_y) is False:
        nbr_pt = p_sorted_point_array[nbr_pt_x, nbr_pt_y]
        if nbr_pt.visited is False:
            return (ppt.x + nbr_pt.x) / 2.0, (ppt.y + nbr_pt.y) / 2.0
    return None


def get_mid_of_nbr_pts(p_sorted_point_array):
    mid_x_list = []
    mid_y_list = []
    mid_pt_list = []
    for i in range(0, p_sorted_point_array.shape[0]):
        for j in range(0, p_sorted_point_array.shape[1]):
            pt = p_sorted_point_array[i, j]

            # nbt_pt1 = get_mid_point(p_sorted_point_array, pt, i, j - 1)
            # if nbt_pt1 is not None:
            #     mid_x_list.append(nbt_pt1[0])
            #     mid_y_list.append(nbt_pt1[1])
            #
            # nbt_pt2 = get_mid_point(p_sorted_point_array, pt, i + 1, j - 1)
            # if nbt_pt2 is not None:
            #     mid_x_list.append(nbt_pt2[0])
            #     mid_y_list.append(nbt_pt2[1])

            nbt_pt3 = get_mid_point(p_sorted_point_array, pt, i - 1, j)
            if nbt_pt3 is not None:
                mid_pt_list.append(Point(nbt_pt3[0], nbt_pt3[1]))
                mid_x_list.append(nbt_pt3[0])
                mid_y_list.append(nbt_pt3[1])

            nbt_pt4 = get_mid_point(p_sorted_point_array, pt, i + 1, j)
            if nbt_pt4 is not None:
                mid_pt_list.append(Point(nbt_pt4[0], nbt_pt4[1]))
                mid_x_list.append(nbt_pt4[0])
                mid_y_list.append(nbt_pt4[1])

            # nbt_pt5 = get_mid_point(p_sorted_point_array, pt, i, j + 1)
            # if nbt_pt5 is not None:
            #     mid_x_list.append(nbt_pt5[0])
            #     mid_y_list.append(nbt_pt5[1])
            #
            # nbt_pt6 = get_mid_point(p_sorted_point_array, pt, i + 1, j + 1)
            # if nbt_pt6 is not None:
            #     mid_x_list.append(nbt_pt6[0])
            #     mid_y_list.append(nbt_pt6[1])

            pt.visited = True

    return mid_x_list, mid_y_list, mid_pt_list


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
    plt.scatter(x_values, y_values, c='b')
    plt.scatter(mid_pt_x_valus, mid_pt_y_values, c='r', marker='o', s=10)
    plt.show()

def get_dumbbell(ppt):
    u = Point(ppt.x, ppt.y + (const.CCDISTANCE / 2.0))
    c = ppt
    d = Point(ppt.x, ppt.y - (const.CCDISTANCE / 2.0))
    return Dumbbell(u, c, d)


def get_dumbbell_list(p_mid_pt_list):
    dumbbell_list = []
    for pt in p_mid_pt_list:
        dumbbell_list.append(get_dumbbell(pt))
    return dumbbell_list


def plot_dumbbell_list(p_dumbbell_list):
    u_x_values = []
    c_x_values = []
    d_x_values = []
    u_y_values = []
    c_y_values = []
    d_y_values = []
    for dumbbell in p_dumbbell_list:
        u_x_values.append(dumbbell.u.x)
        c_x_values.append(dumbbell.c.x)
        d_x_values.append(dumbbell.d.x)
        u_y_values.append(dumbbell.u.y)
        c_y_values.append(dumbbell.c.y)
        d_y_values.append(dumbbell.d.y)

    labels = []
    for i in range(0, const.X_SIZE - 1):
        for j in range(0, const.Y_SIZE):
            labels.append("(" + str(i) + "," + str(j) + ")")
    fig, ax = plt.subplots()
    ax.scatter(c_x_values, c_y_values)
    for i, txt in enumerate(labels):
        ax.annotate(txt, (c_x_values[i], c_y_values[i]))
    plt.scatter(c_x_values, c_y_values, c='y')
    plt.scatter(u_x_values, u_y_values, c='b')
    plt.scatter(d_x_values, d_y_values, c='b')
    plt.show()
    print(p_dumbbell_list)

# def write_data_to_file(p_dumbbell_list):
#     dumbbell_array = np.array(p_dumbbell_list).reshape(const.X_SIZE - 1, const.Y_SIZE)
#     for i in range(0, dumbbell_array.shape[0]):
#         for j in range(0, dumbbell_array.shape[1]):
#             data = dumbbell_array[i, j]
#             f1.write(str(data))
#     f1.close()

input_data = get_input_data()
sorted_point_list = get_sorted_points(input_data)
sorted_point_array = np.transpose(np.array(sorted_point_list))
# print_two_d_array(sorted_point_array)
# plot_sorted_point_array(sorted_point_array)
mid_x_list, mid_y_list, mid_pt_list = get_mid_of_nbr_pts(sorted_point_array)
# write_mid_points_to_a_file(mid_x_list,mid_y_list)
# plot_points_with_mid_points(sorted_point_array, mid_x_list, mid_y_list)
dumbbell_list = get_dumbbell_list(mid_pt_list)
#d= np.array(dumbbell_list).reshape(const.X_SIZE - 1, const.Y_SIZE)
#np.savetxt("cm",)
#f1.write(str(d))
#print(d)
#f1.close()
# plot_dumbbell_list(dumbbell_list)
plot_dumbbell_array(dumbbell_list)
#f1.write(float(dumbbell_list))
#write_data_to_file(dumbbell_list)

print(len(dumbbell_list))
rand_db = dumbbell_list[random.randrange(len(dumbbell_list))]
print(rand_db)
#print(rand_db.u,rand_db.c,rand_db.d)



