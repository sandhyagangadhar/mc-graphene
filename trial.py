import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random as rd

import constants as const
from dumbbell import Dumbbell
from point3d import Point

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.view_init(azim=90, elev=0)

def print_two_d_array(arr):
    print(arr.shape)
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            print(arr[i, j])


def get_input_data():
    input_file = open("config/smallripplocation.dat", "r")
    d = []
    for i in range(0, const.ATOM_SIZE):
        line = input_file.readline()
        x, y, z, q = line.split()
        d.append([float(x), float(y), float(z)])
    input_file.close()
    return d


def get_sorted_points(p_input_data):
    y_sorted_list_desc = sorted(p_input_data, key=lambda k: [(k[1])], reverse=True)
    point_list = []
    for i in range(0, const.ATOM_SIZE, const.X_SIZE):
        t = sorted(y_sorted_list_desc[i:i + const.X_SIZE], key=lambda k: [(k[0])], reverse=False)
        point_list.append([Point(val[0], val[1], val[2]) for val in t])
    return point_list

def is_boundary_point(px, py):
    return px < 0 or py < 0 or px >= const.X_SIZE or py >= const.Y_SIZE


def get_mid_point(p_sorted_point_array, ppt, nbr_pt_x, nbr_pt_y):
    if is_boundary_point(nbr_pt_x, nbr_pt_y) is False:
        nbr_pt = p_sorted_point_array[nbr_pt_x, nbr_pt_y]
        if nbr_pt.visited is False:
            return (ppt.x + nbr_pt.x) / 2.0, (ppt.y + nbr_pt.y) / 2.0, (ppt.z + nbr_pt.z)/2.0
    return None


def get_mid_of_nbr_pts(p_sorted_point_array):
    mid_x_list = []
    mid_y_list = []
    mid_z_list =[]
    mid_pt_list = []
    for i in range(0, p_sorted_point_array.shape[0]):
        for j in range(0, p_sorted_point_array.shape[1]):
            pt = p_sorted_point_array[i, j]

            nbt_pt3 = get_mid_point(p_sorted_point_array, pt, i - 1, j)
            if nbt_pt3 is not None:
                mid_pt_list.append(Point(nbt_pt3[0], nbt_pt3[1], nbt_pt3[2]))
                mid_x_list.append(nbt_pt3[0])
                mid_y_list.append(nbt_pt3[1])
                mid_z_list.append(nbt_pt3[2])

            nbt_pt4 = get_mid_point(p_sorted_point_array, pt, i + 1, j)
            if nbt_pt4 is not None:
                mid_pt_list.append(Point(nbt_pt4[0], nbt_pt4[1], nbt_pt4[2]))
                mid_x_list.append(nbt_pt4[0])
                mid_y_list.append(nbt_pt4[1])
                mid_z_list.append(nbt_pt4[2])

            pt.visited = True

    return mid_x_list, mid_y_list, mid_z_list, mid_pt_list


def plot_points_with_mid_points(p_sorted_point_array, mid_pt_x_values, mid_pt_y_values,mid_pt_z_values):
    x_values = []
    y_values = []
    z_values = []
    labels = []
    for i in range(0, p_sorted_point_array.shape[0]):
        for j in range(0, p_sorted_point_array.shape[1]):
            pt = p_sorted_point_array[i, j]
            x_values.append(pt.x)
            y_values.append(pt.y)
            z_values.append(pt.z)
    ax.scatter(mid_pt_x_values, mid_pt_y_values, mid_pt_z_values, c='r', marker='o')

    #fig = plt.figure()
    #ax = fig.add_subplot(212, projection='3d')
    ax.scatter(x_values, y_values, z_values, c='b', marker='o')

    #  plt.plot(x_values, y_values, z_values, c='b')
    # plt.scatter(mid_pt_x_values, mid_pt_y_values, mid_pt_z_values, c='r', marker='o')
    plt.show()


def plot_sorted_point_array(p_sorted_point_array):
    x_values = []
    y_values = []
    z_values = []
    labels = []
    for i in range(0, p_sorted_point_array.shape[0]):
        for j in range(0, p_sorted_point_array.shape[1]):
            pt = p_sorted_point_array[i, j]
            x_values.append(pt.x)
            y_values.append(pt.y)
            z_values.append(pt.z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_values, y_values, z_values, c='r', marker='o')
    #          labels.append("(" + str(i) + "," + str(j) + ")")
    #  fig, ax = plt.subplots()
    #  ax.scatter(x_values, y_values)
    # for i, txt in enumerate(labels):
    #    ax.annotate(txt, (x_values[i], y_values[i]))
    #   plt.plot(x_values, y_values, z_values)
    plt.show()


def isPointOutOfBoundary(px, py):
    return px < 0 or py < 0 or px >= const.X_SIZE - 1 or py >= const.Y_SIZE

def get_dumbbell(ppt):
    u = Point(ppt.x, ppt.y + (const.CCDISTANCE / 2.0), ppt.z)
    c = ppt
    d = Point(ppt.x, ppt.y - (const.CCDISTANCE / 2.0), ppt.z)
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
    u_z_values = []
    c_z_values = []
    d_z_values = []
    for dumbbell in p_dumbbell_list:
        u_x_values.append(dumbbell.u.x)
        c_x_values.append(dumbbell.c.x)
        d_x_values.append(dumbbell.d.x)
        u_y_values.append(dumbbell.u.y)
        c_y_values.append(dumbbell.c.y)
        d_y_values.append(dumbbell.d.y)
        u_z_values.append(dumbbell.u.y)
        c_z_values.append(dumbbell.c.y)
        d_z_values.append(dumbbell.d.y)

    labels = []
    for i in range(0, const.X_SIZE - 1):
        for j in range(0, const.Y_SIZE):
            labels.append("(" + str(i) + "," + str(j) + ")")
    for i, txt in enumerate(labels):
        ax.annotate(txt, (c_x_values[i], c_y_values[i]))
    ax.scatter(c_x_values, c_y_values, c='y')
    ax.scatter(u_x_values, u_y_values, c='b')
    ax.scatter(d_x_values, d_y_values, c='b')
    plt.show()
    print(p_dumbbell_list)

def connect(pd: Dumbbell, p_dumbbell_array: [], pi: int, pj: int):
    if isPointOutOfBoundary(pi, pj) is False:
        sourceDumbell = p_dumbbell_array[pi, pj]
        plt.plot([pd.u.x, sourceDumbell.d.x], [pd.u.y, sourceDumbell.d.y], c='b')
     #   ax.plot([pd.u.x, pd.d.x], [pd.u.y, pd.d.y], [pd.u.z, pd.u.z+10], c='r')
     #   ax.plot([sourceDumbell.u.x, sourceDumbell.d.x], [sourceDumbell.u.y, sourceDumbell.d.y], [sourceDumbell.u.z, sourceDumbell.u.z+10], c='r')

def plot_dumbbell_array(p_dumbbell_list):
    u_x_values = []
    c_x_values = []
    d_x_values = []
    u_y_values = []
    c_y_values = []
    d_y_values = []
    u_z_values = []
    c_z_values = []
    d_z_values = []
    for dumbbell in p_dumbbell_list:
        u_x_values.append(dumbbell.u.x)
        c_x_values.append(dumbbell.c.x)
        d_x_values.append(dumbbell.d.x)
        u_y_values.append(dumbbell.u.y)
        c_y_values.append(dumbbell.c.y)
        d_y_values.append(dumbbell.d.y)
        u_z_values.append(dumbbell.u.z)
        c_z_values.append(dumbbell.c.z)
        d_z_values.append(dumbbell.d.z)

    labels = []
    for i in range(0, const.X_SIZE - 1):
        for j in range(0, const.Y_SIZE):
            labels.append("(" + str(i) + "," + str(j) + ")")
    fig, ax = plt.subplots()
    for i, txt in enumerate(labels):
        ax.annotate(txt, (c_x_values[i], c_y_values[i]))
    plt.scatter(c_x_values, c_y_values, c='y')
  #  plt.plot(u_x_values, u_y_values, c='b')
   # plt.plot(d_x_values, d_y_values, c='b')

    dumbbell_array = np.array(p_dumbbell_list).reshape(const.X_SIZE - 1, const.Y_SIZE)
    for i in range(0, dumbbell_array.shape[0]):
        for j in range(0, dumbbell_array.shape[1]):
            d = dumbbell_array[i, j]
            plt.plot([d.u.x, d.d.x], [d.u.y, d.d.y],c='b',marker='o')
            # ax.plot([d.u.x, d.u.y,0],[d.d.x, d.d.y,0],  c='b',marker='o')
            if isPointOutOfBoundary(i, j - 1) is False:
                ld = dumbbell_array[i, j - 1]
                if ld.d.x < d.u.x:
                    connect(d, dumbbell_array, i, j - 1)
                    connect(d, dumbbell_array, i + 1, j - 1)
                else:
                    connect(d, dumbbell_array, i - 1, j - 1)
                    connect(d, dumbbell_array, i, j - 1)
    plt.show()





input_data = get_input_data()
#plt.plot(input_data)
sorted_point_list = get_sorted_points(input_data)
sorted_point_array = np.transpose(np.array(sorted_point_list))
#print(sorted_point_array)
#plot_sorted_point_array(sorted_point_array)
mid_x_list, mid_y_list, mid_z_list, mid_pt_list = get_mid_of_nbr_pts(sorted_point_array)
#print(mid_pt_list)
#plot_points_with_mid_points(sorted_point_array, mid_x_list, mid_y_list, mid_z_list)
dumbbell_list = get_dumbbell_list(mid_pt_list)
plot_dumbbell_array(dumbbell_list)


#...........Monte Carlo simulation to get equilibrium Configuration............#

#def mc_simulation(p_dumbbell_list):
#   d = np.array(dumbbell_list).reshape(const.X_SIZE - 1, const.Y_SIZE)
#  i=np.random.randint(0, const.X_SIZE - 1)

#d=dumbbell_array(2,3)

#mc_simulation(dumbbell_list)

#dumbbell_array = np.array(dumbbell_list).reshape(const.X_SIZE - 1, const.Y_SIZE)
#i=np.random.randint(0, const.X_SIZE - 1)
#j=np.random.randint(0, const.Y_SIZE)
#d=dumbbell_array[i,j]
#print(d.u)















































