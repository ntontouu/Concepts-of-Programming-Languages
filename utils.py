import math

#ΣΥΝΑΡΤΗΣΗ ΠΟΥ ΒΡΙΣΚΕΙ ΤΗΝ ΑΠΟΣΤΑΣΗ ΜΕΤΑΞΥ ΤΩΝ 2 ΔΥΟ ΣΗΜΕΙΩΝ ΜΕ ΒΑΣΗ ΤΟΝ ΤΥΠΟ ΠΟΥ ΔΩΘΗΚΕ
def distance_between_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

#ΣΥΝΑΡΤΗΣΗ ΓΙΑ ΤΗΝ ΕΥΡΕΣΗ ΤΟΥ ΕΜΒΑΔΟΥ ΤΟΥ ΤΡΙΓΩΝΟΥ
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = s * (s - a) * (s - b) * (s - c)
    if area <= 0:
        return None
    else:
        return math.sqrt(area)

#ΣΥΝΑΡΤΗΣΗ ΓΙΑ ΝΑ ΒΡΕΘΕΙ Η ΜΕΣΗ ΤΙΜΗ ΤΟΥ ΤΡΙΓΩΝΟΥ
def mean(numbers):
    if len(numbers) > 0:
        return sum(numbers) / len(numbers)
    else:
        return None

#ΣΥΝΑΡΤΗΣΗ ΓΙΑ ΝΑ ΒΡΕΘΕΙ Η ΔΙΑΜΕΣΟΣ ΤΟΥ ΤΡΙΓΩΝΟΥ
def median(numbers):
    sorted_numbers = numbers.copy()
    sorted_numbers.sort()
    n = len(numbers)
    #ΑΝ ΤΟ ΠΛΗΘΟΣ ΤΩΝ ΑΡΙΘΜΩΝ ΕΙΝΑΙ ΖΥΓΟ ΤΌΤΕ Ο ΔΙΑΜΕΣΟΣ ΕΙΝΑΙ Ο ΜΕΣΟΣ ΟΡΟΣ ΤΩΝ ΔΥΟ ΜΕΣΑΙΩΝ ΑΡΙΘΜΩΝ
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    #ΑΛΛΙΩΣ ΕΙΝΑΙ ΤΟ ΜΕΣΑΙΟ ΣΤΟΙΧΕΙΟ
    else:
        return sorted_numbers[n // 2]

#ΣΥΝΑΡΤΗΣΗ ΠΟΥ ΕΛΕΓΧΕΙ ΑΜΑ ΥΠΑΡΧΟΥΝ ΑΚΟΜΑ ΣΗΜΕΙΑ ΓΙΑ ΝΑ ΥΠΟΛΟΓΙΣΤΟΥΝ
def range_list(numbers):
    #ΑΝ ΥΠΑΡΧΕΙ ΕΣΤΩ ΚΑΙ ΕΝΑ ΣΤΟΙΧΕΙΟ
    if len(numbers) > 0:
        return max(numbers) - min(numbers)
    else:
        return None

#ΣΥΝΑΡΤΗΣΗ ΓΙΑ ΝΑ ΒΡΕΘΕΙ Η ΤΥΠΙΚΗ ΑΠΟΚΛΙΣΗ ΤΟΥ ΤΕΤΡΑΓΩΝΟ
def standard_deviation(numbers):
    #ΑΝ ΔΕΝ ΥΠΑΡΧΕΙ ΚΑΝΕΝΑΣ ΑΡΙΘΜΟΣ ΕΠΙΣΤΡΕΦΕΙ ΚΕΝΟ
    if len(numbers) == 0:
        return None
    #ΥΠΟΛΟΓΙΣΜΟΣ ΜΕΣΟΥ
    mean_value = mean(numbers)
    #ΥΠΟΛΟΓΙΣΜΟΣ
    variance = sum((x - mean_value) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)
