#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import time

file_paths = ["input1000.txt", "input10000.txt", "input100000.txt", "input1000000.txt"]

def distance_from_origin(x, y, z):
    return np.sqrt(x**2 + y**2 + z**2)

def read_file_and_calculate_distance(file_name):
    header = [('distance', float), ('x', float), ('y', float), ('z', float)]
    points = []
    with open(file_name, 'r') as file:
        for line in file:
            data = line.split()
            x, y, z = map(float, data)
            dist = distance_from_origin(x, y, z)
            points.append((dist, x, y, z))
    points_array = np.array(points, dtype=header) 
    points_array = np.sort(points_array,kind='quicksort',order='distance')
    return points_array


# In[10]:


import time
import numpy as np

# ΔΙΑΒΑΖΕΙ ΤΑ ΔΕΔΟΜΕΝΑ ΑΠΟ ΤΑ ΑΡΧΕΙΑ, ΥΠΟΛΟΓΙΣΜΟΣ ΤΩΝ ΑΠΟΣΤΑΣΕΩΝ ΚΑΙ ΤΑΞΙΝΟΜΗΣΗ ΤΩΝ ΣΗΜΕΙΩΝ
for file_path in file_paths:
    start_time = time.time()
    sorted_points = read_file_and_calculate_distance(file_path)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution time for {file_path}: {elapsed_time:.6f} seconds")
    
    # ΕΚΤΥΠΩΣΗ ΤΩΝ ΤΑΞΙΝΟΜΗΜΕΝΩΝ ΣΗΜΕΙΩΝ
    #for point in sorted_points:
    #    print(point)

