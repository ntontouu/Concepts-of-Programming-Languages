# Cartesian Coordinates Processing

[![University](https://img.shields.io/badge/University-University%20of%20Ioannina-blue.svg)](https://www.uoi.gr)
[![Department](https://img.shields.io/badge/Department-Informatics%20%26%20Telecommunications-lightgrey.svg)](https://www.cs.uoi.gr/)
[![Language](https://img.shields.io/badge/Language-Python-blueviolet.svg)]()

A Python-based implementation for parsing, managing, and performing geometric computations on sets of Cartesian coordinates.

---

## 📚 Table of Contents
1. [Overview](#-overview)
2. [Theoretical Background](#-theoretical-background)
3. [Project Structure](#-project-structure)
4. [Getting Started](#-getting-started)
5. [Author & Credits](#-author--credits)

---

## 🔍 Overview
This project focuses on the foundational concepts of imperative programming and file I/O operations in Python. It involves reading spatial data (points) from text files, validating the input, and executing geometric algorithms (e.g., distance calculations, quadrant filtering) using modular utility functions.

---

## 📐 Theoretical Background
The project utilizes 2D Cartesian geometry principles. Given two points $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$, calculations such as the **Euclidean Distance** are implemented systematically:
$$d(P_1, P_2) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
The architecture emphasizes code reusability by separating mathematical logic into a dedicated `utils.py` module, demonstrating modular imperative design.

---

## 🛠️ Project Structure
| File | Description |
| :--- | :--- |
| **`erotima2.py`** | The main execution script handling data flow and user interaction. |
| **`utils.py`** | A helper module containing geometric formulas and data validation logic. |
| **`points.txt` / `mypoints.txt`** | Input datasets containing coordinate pairs. |

---

## 🚀 Getting Started
1. Ensure Python 3.x is installed.
2. Run the main script from the terminal: `python erotima2.py`
3. The script will automatically parse `points.txt` and output the geometric analysis.

---

## 📝 Author & Academic Use
- **Student:** Maria Alexandra Ntontou (2799)
- **Institution:** University of Ioannina
