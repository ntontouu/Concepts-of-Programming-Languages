# Chess Game Stats & Regular Expressions

[![University](https://img.shields.io/badge/University-University%20of%20Ioannina-blue.svg)](https://www.uoi.gr)
[![Department](https://img.shields.io/badge/Department-Informatics%20%26%20Telecommunications-lightgrey.svg)](https://www.cs.uoi.gr/)
[![Language](https://img.shields.io/badge/Language-Python-blueviolet.svg)]()

A text-processing pipeline utilizing **Regular Expressions (RegEx)** to parse, extract, and statistically analyze massive datasets of recorded chess matches in PGN (Portable Game Notation) format.

---

## 📚 Table of Contents
1. [Overview](#-overview)
2. [Theoretical Background](#-theoretical-background)
3. [Project Structure](#-project-structure)
4. [Getting Started](#-getting-started)
5. [Author & Credits](#-author--credits)

---

## 🔍 Overview
Portable Game Notation (PGN) files contain dense, unstructured text detailing chess games, including metadata (players, Elo ratings, dates) and the algebraic notation of the moves. This project demonstrates advanced string manipulation and pattern matching to extract specific openings (e.g., Réti Opening, King's Indian Attack) and calculate player statistics.

---

## 📐 Theoretical Background
The core of the assignment relies on **Regular Expressions**, a sequence of characters that specifies a search pattern. 
- Example pattern for extracting Elo ratings: `\[WhiteElo\s+"(\d+)"\]`
- By applying these deterministic finite automaton (DFA) principles, the Python `re` module can efficiently scan thousands of lines of text to build structured data models (dictionaries/lists) for further statistical analysis without relying on heavy external parsing libraries.

---

## 🛠️ Project Structure
| File | Description |
| :--- | :--- |
| **`my_re_functions.py`** | Contains the compiled RegEx patterns and extraction logic. |
| **`test_my_re_functions.py`** | Unit testing suite to validate the accuracy of the RegEx patterns. |
| **`erotima_1.py` / `erotima_2.py`** | Scripts executing the analysis on specific datasets. |
| **`WorldChamp2023.pgn`** | Official dataset from the 2023 World Chess Championship. |

---

## 🚀 Getting Started
1. Run the test suite to verify the RegEx logic: `python test_my_re_functions.py`
2. Execute the extraction scripts: `python erotima_1.py`
3. (Ensure `RetiKIA.zip` is extracted if requested by the scripts).

---

## 📝 Author & Academic Use
- **Student:** Maria Alexandra Ntontou (2799)
- **Institution:** University of Ioannina
