import tkinter as tk
from random import randint
import utilsvb as util

# ΑΡΧΙΚΟΠΟΙΗΣΗ ΠΡΟΣΠΑΘΕΙΩΝ
tries = 0
matching_percentage = 0.00
best_score = 0.00


# ΣΥΝΑΡΤΗΣΗ ΓΙΑ ΔΗΜΙΟΥΡΓΙΑ ΤΥΧΑΙΟΥ ΧΡΩΜΑΤΟΣ ΣΤΟΧΟΥ
def generate_random_color():
    # ΔΗΜΙΟΥΓΕΙ ΤΥΧΑΙΕΣ ΤΙΜΕΣ ΓΙΑ ΤΑ ΧΡΩΜΑΤΑ
    red_val = randint(0, 255)
    green_val = randint(0, 255)
    blue_val = randint(0, 255)

    # ΜΕΤΑΤΡΟΠΗ ΑΠΟ RGB ΣΕ 16ΔΙΚΟ
    hexcolor = f"#{red_val:02x}{green_val:02x}{blue_val:02x}"

    # ΑΝΑΝΕΩΝΕΙ ΤΟ ΑΡΙΣΤΕΡΟ ΠΛΑΙΣΙΟ
    target_color_frame.config(bg=hexcolor)
    return (red_val, green_val, blue_val)


# ΣΥΝΑΡΤΗΣΗ ΓΙΑ ΠΡΟΣΠΑΘΕΙΑ ΣΥΝΔΙΑΣΜΟΥ ΧΡΩΜΑΤΩΝ
def detect_color():
    global tries
    global best_score
    global R
    global G
    global B
    red_val = red_slider.get()
    green_val = green_slider.get()
    blue_val = blue_slider.get()
    redHex = hex(red_val)
    greenHex = hex(green_val)
    blueHex = hex(blue_val)
    hexcolor = "#"
    if red_val < 16:
        hexcolor = hexcolor + "0" + str(redHex).replace("0x", "")
    else:
        hexcolor = hexcolor + str(redHex).replace("0x", "")
    if green_val < 16:
        hexcolor = hexcolor + "0" + str(greenHex).replace("0x", "")
    else:
        hexcolor = hexcolor + str(greenHex).replace("0x", "")
    if blue_val < 16:
        hexcolor = hexcolor + "0" + str(blueHex).replace("0x", "")
    else:
        hexcolor = hexcolor + str(blueHex).replace("0x", "")

    # ΚΑΛΕΙ ΤΗΝ matchpc function ΑΠΟ ΤΟ utils ΓΙΑ ΝΑ ΥΠΟΛΟΓΙΣΕΙ ΤΗΝ ΑΠΟΣΤΑΣΗ ΤΩΝ ΔΥΟ ΧΡΩΜΑΤΩΝ
    matching_percentage = util.matchpc(red_val, green_val, blue_val, R, G, B)
    color_label.config(text="Detected Color: Unknown", bg=hexcolor)
    user_color_frame.config(bg=hexcolor)
    tries += 1
    # ΑΝΑΝΕΩΣΗ ΤΟΥ ΣΚΟΡ ΑΜΑ ΕΠΙΤΕΥΧΘΕΙ ΚΑΛΥΤΕΡΟ ΠΟΣΟΣΤΟ
    if matching_percentage > best_score:
        best_score = matching_percentage
        best_score_label.config(text=f"Best Score: {best_score:.2f}%")
    # ΕΛΕΓΧΟΣ ΓΙΑ ΤΟΝ ΑΝ Ο ΠΑΙΚΤΗΣ ΕΧΕΙ ΧΡΗΣΙΜΟΠΟΙΗΣΕΙ ΚΑΙ ΤΙΣ 5 ΠΡΟΣΠΑΘΕΙΕΣ
    if tries >= 5:
        # ΤΣΕΚΑΡΕΙ ΑΝ ΤΑΙΡΙΑΖΟΥΝ ΤΑ ΧΡΩΜΑΤΑ ΤΟΥΛΑΧΙΣΤΟΝ ΣΤΟ 90%
        if matching_percentage >= 90:
            result_label.config(text="ΩΡΑΙΟΣ")
            best_score_label.config(text=f"Best Score: {best_score:.2f}%")
        else:
            result_label.config(text="ΑΣΤΟ ΔΕΝ")
            best_score_label.config(text=f"Best Score: {best_score:.2f}%")
        # ΑΦΟΠΛΙΖΕΙ ΤΑ ΔΙΚΑΙΩΜΑΤΑ ΤΟΥ ΠΑΙΚΤΗ
        detect_button.config(state=tk.DISABLED)
    else:
        # ΑΝΑΝΕΩΝΕΙ ΤΑ ΑΠΟΤΕΛΕΣΜΑΤΑ ΜΕ ΤΟ ΠΑΡΟΝ ΠΟΣΟΣΤΟ
        result_label.config(
            text=f"Matching Percentage: {matching_percentage:.2f}% (Try {tries}/5)"
        )


root = tk.Tk()
# ΤΙΤΛΟΣ ΠΑΡΑΘΥΡΟΥ
root.title("Συνδιασμός Βασικών Χρωμάτων")
# ΜΠΑΡΕΣ ΧΡΩΜΑΤΩΝ
red_slider = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Red")
red_slider.pack()

green_slider = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Green")
green_slider.pack()

blue_slider = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Blue")
blue_slider.pack()
# "ΔΟΚΙΜΗ" ΚΟΥΜΠΙ
detect_button = tk.Button(root, text="Δοκιμή", command=detect_color)
detect_button.pack()
# ΠΛΕΥΡΑ ΠΡΟΣΠΑΘΕΙΑΣ ΧΡΩΜΑΤΟΣ
color_label = tk.Label(root, text="Detected Color: None", bg="white", width=30)
color_label.pack()

# ΔΕΙΧΝΕΙ ΑΠΟΤΕΛΕΣΜΑ ΠΟΣΟΣΤΟΥ Κ ΜΕΤΡΗΤΗ ΠΡΟΣΠΑΘΕΙΩΝ
result_label = tk.Label(
    root, text="Matching Percentage: 0% (Try 0/5)", bg="white", width=30
)
result_label.pack()

# ΔΕΙΧΝΕΙ ΤΟ ΚΑΛΥΤΕΡΟ ΠΟΣΟΣΤΟ ΠΟΥ ΚΑΤΑΦΕΡΕ Ο ΧΡΗΣΤΗΣ
best_score_label = tk.Label(root, text="Best Score: 0.00%", bg="white", width=30)
best_score_label.pack()

# ΠΛΑΙΣΙΟ ΧΡΩΜΑΤΟΣ ΠΟΥ ΔΗΜΙΟΥΡΓΕΙΤΑΙ ΤΥΧΑΙΑ ΑΠΟ ΤΟ ΠΡΟΓΡΑΜΜΑ
target_color_frame = tk.Frame(
    root, width=100, height=100, bg="white", bd=2, relief="solid"
)
target_color_frame.pack(side=tk.LEFT, padx=20, pady=10)

# ΠΛΑΙΣΙΟ ΧΡΩΜΑΤΟΣ ΠΟΥ ΔΗΜΙΟΥΓΕΙ Ο ΧΡΗΣΤΗΣ
user_color_frame = tk.Frame(
    root, width=100, height=100, bg="white", bd=2, relief="solid"
)
user_color_frame.pack(side=tk.RIGHT, padx=20, pady=10)

# ΚΛΗΣΗ ΣΥΝΑΡΤΗΣΗΣ ΓΙΑ ΔΗΜΙΟΥΡΓΙΑ ΤΥΧΑΙΟΥ ΧΡΩΜΑΤΟΣ
(R, G, B) = generate_random_color()

root.mainloop()
