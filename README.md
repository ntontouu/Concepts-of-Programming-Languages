# Sorting Points: Python vs Haskell

[![University](https://img.shields.io/badge/University-University%20of%20Ioannina-blue.svg)](https://www.uoi.gr)
[![Department](https://img.shields.io/badge/Department-Informatics%20%26%20Telecommunications-lightgrey.svg)](https://www.cs.uoi.gr/)
[![Language](https://img.shields.io/badge/Language-Python%20%7C%20Haskell-blueviolet.svg)]()

A comparative benchmarking study of **Imperative/OOP (Python)** versus **Purely Functional (Haskell)** programming paradigms, evaluated through sorting algorithms applied to massive datasets of coordinate points.

---

## 📚 Table of Contents
1. [Overview](#-overview)
2. [Theoretical Background](#-theoretical-background)
3. [Project Structure](#-project-structure)
4. [Experimental Results & Scalability](#-experimental-results--scalability)
5. [Author & Credits](#-author--credits)

---

## 🔍 Overview
How does the paradigm of a language affect its performance and code expressiveness? This project implements sorting logic for 3D/2D points based on their coordinates and distances. The algorithms are tested under heavy loads, ranging from 1,000 to 1,000,000 data points, to observe execution time, memory management, and syntax elegance.

---

## 📐 Theoretical Background
### Imperative Paradigm (Python)
- **State & Mutation:** Uses variables that change state over time. Loops explicitly define *how* to iterate over the dataset.
- **Approaches:** Evaluated using both basic scripting (`python_sketo.py`) and optimized/idiomatic Python (`python_metrio.py`).

### Functional Paradigm (Haskell)
- **Immutability & Recursion:** Variables cannot be mutated. Iteration is achieved through recursion and higher-order functions (e.g., `map`, `filter`, `fold`).
- **Lazy Evaluation:** Haskell computes values only when they are strictly necessary, which can drastically alter memory consumption patterns during massive I/O operations compared to Python's strict evaluation.

---

## 🛠️ Project Structure
| File | Description |
| :--- | :--- |
| **`haskell_sketo.hs`** | Functional sorting implementation using Haskell. |
| **`python_sketo.py`** | Basic imperative sorting implementation in Python. |
| **`python_metrio.py`** | Optimized Python implementation. |
| **`input*.txt`** | Benchmarking datasets (1K, 10K, 100K points). |
| **`input1000000.zip`** | Stress-test dataset containing 1,000,000 points. |

---

## 📊 Experimental Results & Scalability
*Observations based on paradigm comparison:*
- **Expressiveness:** Haskell's pattern matching and declarative syntax result in mathematically elegant sorting definitions (e.g., QuickSort in 3 lines).
- **Execution Speed:** While Python benefits from highly optimized C-backed built-in functions (like Timsort), Haskell's compiled binary (via GHC) and lazy evaluation provide unique performance characteristics, especially evident in the 1,000,000 points stress test.

---

## 🚀 Getting Started
1. **Python:** Execute `python python_metrio.py`
2. **Haskell:** Compile using GHC (`ghc -O2 haskell_sketo.hs`) and run the resulting executable. 
3. Feed the `input.txt` files through standard input or modify the file paths inside the scripts to benchmark.

---

## 📝 Author & Academic Use
- **Student:** Maria Alexandra Ntontou (2799)
- **Institution:** University of Ioannina
