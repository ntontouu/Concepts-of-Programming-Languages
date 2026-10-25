import statistics
import random
import numpy
import utils as u
import math
import unittest

"""ΣΤΗΝ ΠΕΡΙΠΤΩΣΗ ΠΟΥ Ο ΧΡΗΣΤΗΣ ΕΠΙΛΕΞΕΙ ΕΝΑ ΤΥΧΑΙΟ ΑΡΧΕΙΟ ΠΕΡΑ ΑΠΟ ΤΟ POINTS.TXT ΕΝΑ ΑΡΧΕΙΟ ΜΕ ΟΝΟΜΑ MYPOINTS.TXT ΘΑ
ΔΗΜΙΟΥΡΓΗΘΕΙ ΠΟΥ ΘΑ ΠΕΡΙΕΧΕΙ ΤΥΧΑΙΑ ΣΗΜΕΙΑ ΠΟΥ ΔΗΜΙΟΥΡΓΗΘΗΚΑΝ ΑΠΟ ΤΟ ΠΡΟΓΡΑΜΜΑ"""


def createRandomPoints(
    n=100, _min=-100, _max=100, filename="mypoints.txt", seperator=" "
):
    f = open(filename, "w")
    for i in range(0, n):
        x = random.randrange(_min, _max)
        y = random.randrange(_min, _max)
        f.write(str(x) + seperator + str(y) + "\n")
    f.close()


# ΣΥΝΑΡΤΗΣΗ ΠΟΥ ΕΛΕΓΧΕΙ ΕΝΑ ΠΡΟΚΕΙΤΑΙ ΓΙΑ ΤΟ POINTS.TXT Η RANDOM ΓΙΑ ΑΡΧΗ, Κ ΕΦΟΣΟΝ ΙΣΧΥΕΙ ΤΟ ΠΡΩΤΟ ΓΙΝΟΝΤΑΙ ΟΙ ΣΥΝΑΡΤΗΣΕΙΣ ΤΟΥ UTILS
def triangles(filename="points.txt", separetor=" "):
    if filename == "Randoms":
        createRandomPoints()
        filename = "mypoints.txt"
        seperator = " "
    f = open(filename, "r")
    points_lines = f.read()
    points_list = points_lines.split("\n")
    points = []
    for p in points_list:
        x = p.split(separetor)
        if len(x) == 2:
            points.append((float(x[0]), float(x[1])))
    f.close()
    areas = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                dist_i_j = u.distance_between_points(points[i], points[j])
                dist_j_k = u.distance_between_points(points[j], points[k])
                dist_k_i = u.distance_between_points(points[k], points[i])
                _area = u.triangle_area(dist_i_j, dist_j_k, dist_k_i)
                if _area is not None:
                    areas.append(_area)

    result = "Έγκυρα Τρίγωνα:" + str(len(areas)) + "\n"
    result += "Αριθμητικός Μέσος Εμβαδών:" + str(u.mean(areas)) + "\n"
    result += "Διάμεσος Εμβαδών:" + str(u.median(areas)) + "\n"
    result += "Τυπική Απόκλιση Εμβαδών:" + str(u.standard_deviation(areas)) + "\n"
    return result


# TO UNIT TEST ΓΙΑ ΤΟ ΑΝ ΤΑ ΤΡΙΓΩΝΑ ΕΧΟΥΝ ΥΠΟΛΟΓΙΣΤΕΙ ΣΩΣΤΑ
class TestTriangleAreas(unittest.TestCase):
    def setUp(self):
        pass

    def testTriangles(self):
        result = """Έγκυρα Τρίγωνα:161673
Αριθμητικός Μέσος Εμβαδών:3206.818862768401
Διάμεσος Εμβαδών:2392.5
Τυπική Απόκλιση Εμβαδών:2843.237119834114
"""

        self.assertEqual(triangles("points.txt", " "), result)


if __name__ == "__main__":
    triangles(filename="Randoms")
    unittest.main()
