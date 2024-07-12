#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import math
import random
import time
import math


# In[7]:


#ΔΙΑΒΑΣΜΑ ΤΩΝ ΔΕΔΟΜΕΝΩΝ ΑΠΟ ΤΑ ΑΡΧΕΙΑ, ΥΠΟΛΟΓΙΣΜΟΣ ΤΩΝ ΑΠΟΣΤΑΣΕΩΝ ΚΑΙ ΤΑΞΙΝΟΜΗΣΗ ΤΩΝ ΣΗΜΕΙΩΝ
'''file_paths = ["input1000.txt", "input10000.txt", "input100000.txt", "input1000000.txt"]

for file_path in file_paths:
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())'''

#ΣΥΝΑΡΤΗΣΗ ΓΙΑ ΕΥΡΕΣΗ ΕΥΚΛΕΔΙΑΣ ΑΠΟΣΤΑΣΗΣ ΑΠΟ ΤΟ ΣΗΜΕΙΟ (0,0,0)
def distance_from_origin(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)


def compare(a, b):
    return (a[0] - b[0])


#ΥΛΟΠΟΙΗΣΗ ΤΟΥ ΑΛΓΟΡΙΘΜΟΥ QUICKSORT
def quicksort(arr):
    #ΑΝ Η ΛΙΣΤΑ ΕΧΕΙ ΜΗΔΕΝΙΚΟ Ή ΕΝΑ ΣΤΟΙΧΕΙΟ, ΕΠΙΣΤΡΕΦΕΙ ΤΗ ΛΙΣΤΑ ΩΣ ΕΧΕΙ
    if len(arr) <= 1:
        return arr
     #ΕΠΙΛΟΓΗ ΤΟΥ ΣΤΟΙΧΕΙΟΥ ΠΟΥ ΘΑ ΧΡΗΣΙΜΟΠΟΙΗΘΕΙ ΩΣ PIVOT
    pivot_pointer = random.randrange(len(arr))  
    pivot = arr[pivot_pointer]
    less = []
    larger = []
    for a in arr:
        if compare(a,pivot) < 0:
            less.append(a)
        elif compare(a,pivot) > 0:
            larger.append(a)
    left = quicksort(less)
    right = quicksort(larger)
    #ΕΠΙΣΤΡΕΦΕΙ ΤΗ ΣΥΝΕΝΩΣΗ ΤΩΝ ΑΡΙΣΤΕΡΩΝ, ΜΕΣΑΙΩΝ ΚΑΙ ΔΕΞΙΩΝ ΛΙΣΤΩΝ
    return left + ([pivot]) + right

#ΣΥΝΑΡΤΗΣΗ ΓΙΑ ΤΗΝ ΑΝΑΓΝΩΣΗ ΤΩΝ ΔΕΔΟΜΕΝΩΝ ΑΠΟ ΤΟ ΑΡΧΕΙΟ, ΤΟΝ ΥΠΟΛΟΓΙΣΜΟ ΤΩΝ ΑΠΟΣΤΑΣΕΩΝ ΚΑΙ ΤΗΝ ΤΑΞΙΝΟΜΗΣΗ ΤΩΝ ΣΗΜΕΙΩΝ
def read_file_and_calculate_distance(file_name):
    #ΛΙΣΤΑ ΓΙΑ ΤΗΝ ΑΠΟΘΗΚΕΥΣΗ ΤΩΝ ΣΗΜΕΙΩΝ ΚΑΙ ΤΩΝ ΑΠΟΣΤΑΣΕΩΝ ΤΟΥΣ
    points = []
    with open(file_name, 'r') as file:
        for line in file:
            data = line.split()
            x, y, z = map(float, data)
            dist = distance_from_origin(x, y, z)
            points.append((dist, x, y, z))
    #ΤΑΞΙΝΟΜΗΣΗ ΤΩΝ ΣΗΜΕΙΩΝ ΧΡΗΣΙΜΟΠΟΙΩΝΤΑΣ ΤΟΝ ΑΛΓΟΡΙΘΜΟ QUICKSORT
    sorted_points = quicksort(points)
    return sorted_points

#ΟΝΟΜΑΣΙΑ ΤΩΝ ΑΡΧΕΙΩΝ ΠΟΥ ΠΕΡΙΕΧΟΥΝ ΤΑ ΔΕΔΟΜΕΝΑ ΣΗΜΕΙΩΝ
file_paths = ["input1000.txt", "input10000.txt", "input100000.txt", "input1000000.txt"]

#ΔΙΑΒΑΖΕΙ ΤΑ ΔΕΔΟΜΕΝΑ ΑΠΟ ΤΑ ΑΡΧΕΙΑ, ΥΠΟΛΟΓΙΣΜΟΣ ΤΩΝ ΑΠΟΣΤΑΣΕΩΝ ΚΑΙ ΤΑΞΙΝΟΜΗΣΗ ΤΩΝ ΣΗΜΕΙΩΝ
for file_path in file_paths:
    sorted_points = read_file_and_calculate_distance(file_path)
    #ΕΚΤΥΠΩΣΗ ΤΩΝ ΤΑΞΙΝΟΜΗΜΕΝΩΝ ΣΗΜΕΙΩΝ
    for point in sorted_points:
        print(point)
        
'''file1_points = read_file_and_calculate_distance('input1000.txt')
file2_points = read_file_and_calculate_distance('input10000.txt')
file3_points = read_file_and_calculate_distance('input100000.txt')
file4_points = read_file_and_calculate_distance('input1000000.txt')'''


# In[8]:


# ΔΙΑΒΑΖΕΙ ΤΑ ΔΕΔΟΜΕΝΑ ΑΠΟ ΤΑ ΑΡΧΕΙΑ, ΥΠΟΛΟΓΙΣΜΟΣ ΤΩΝ ΑΠΟΣΤΑΣΕΩΝ ΚΑΙ ΤΑΞΙΝΟΜΗΣΗ ΤΩΝ ΣΗΜΕΙΩΝ
for file_path in file_paths:
    start_time = time.time()
    sorted_points = read_file_and_calculate_distance(file_path)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution time for {file_path}: {elapsed_time:.6f} seconds")
    


# In[ ]:




