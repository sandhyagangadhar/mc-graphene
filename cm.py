# A program constuct dumbbell from mid points calculated from trinagular_lattice_cm.py
import matplotlib.pyplot as plt
import numpy as np
from point import Point
import csv
CCDISTANCE=0.154
X_SIZE = 29
Y_SIZE = 100
ATOM_SIZE = X_SIZE * Y_SIZE

def print_two_d_array(arr):
    print(arr.shape)
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            print(arr[i, j])


def get_input_data():
    input_file = open("config/cm-data.dat", "r")
    d = []
    for i in range(0, ATOM_SIZE):
        line = input_file.readline()
        x, y = line.split()
        d.append([float(x), float(y)])
    input_file.close()
    return d

def get_CM2darray(p_input_data):
    point_list = []
    for i in range(0, ATOM_SIZE, Y_SIZE):
        t = p_input_data[i:i + Y_SIZE]
        point_list.append([Point(val[0], val[1]) for val in t])
    return point_list


def get_dumbbell(ppt):
    return (ppt.y, ppt.y - (CCDISTANCE / 2.0), ppt.y + (CCDISTANCE / 2.0))


def get_mid_of_nbr_pts(p_CM_array):
    db_dny_list = []
    db_upy_list = []
    db_list = []
    for i in range(0, p_CM_array.shape[0]):
        for j in range(0, p_CM_array.shape[1]):
            pt1 = p_CM_array[i, j]

            db_pt1 = get_dumbbell(pt1)
            if db_pt1 is not None:
                db_list.append(db_pt1[0])
                db_dny_list.append(db_pt1[1])
                db_upy_list.append(db_pt1[2])
    return db_dny_list, db_list, db_upy_list


def plot_p_CM_array(p_CM_array):
    x_values = []
    y_values = []
    labels = []
    for i in range(0, p_CM_array.shape[0]):
        for j in range(0, p_CM_array.shape[1]):
            pt = p_CM_array[i, j]
            x_values.append(pt.x)
            y_values.append(pt.y)
            labels.append("(" + str(i) + "," + str(j) + ")")
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values)
    for i, txt in enumerate(labels):
        ax.annotate(txt, (x_values[i], y_values[i]))
    plt.scatter(x_values, y_values)
    plt.show()

def plot_dbpts_withindex(p_CM_array, db_dny_list, db_upy_list):
    x_values = []
    y_values = []
    
    for i in range(0, p_CM_array.shape[0]):
        for j in range(0, p_CM_array.shape[1]):
            pt = p_CM_array[i, j]
            x_values.append(pt.x)
            y_values.append(pt.y)
    fig1, dny = plt.subplots()
#    dny.scatter(x_values, db_dny_list)
#     for i in range(0,len(db_dny_list)):
#         dny.annotate(0, (x_values[i], db_dny_list[i]))
    # fig2, upy = plt.subplots()
 #   upy.scatter(x_values, db_upy_list)
 #    for j in range(0,len(db_upy_list)):
 #        upy.annotate(1, (x_values[j], db_upy_list[j]))
 #    plt.scatter(x_values, db_dny_list)
 #    plt.scatter(x_values, y_values)
    # plt.scatter(x_values, db_upy_list)
    plt.scatter(x_values, y_values,c='b')
    # plt.scatter(x_values, db_dny_list,c='r',marker='o',s=10)

    plt.show()


input_data = get_input_data()

CM_list = get_CM2darray(input_data)
# CM_array = np.transpose(np.array(CM_list))
CM_array = np.array(CM_list)
print(CM_array.shape[0])
print(CM_array.shape[1])

db_dny_list, db_list, db_upy_list = get_mid_of_nbr_pts(CM_array)

#plot_p_CM_array(CM_array)

#plot_dbpoints(CM_array, db_dny_list, db_upy_list)
plot_dbpts_withindex(CM_array, db_dny_list, db_upy_list)

