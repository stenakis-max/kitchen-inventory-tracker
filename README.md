# kitchen-inventory-tracker

A Python application that models a kitchen stock tracking system. This project demonstrates how functions isolate data within their local environments and how to correctly update global program states using functions, arguments, and return values.

## 🚀 Features
* Tracks raw ingredients (`eggs`, `flour`, `sugar`) using globally scoped state variables.
* Features a diagnostic function (`check_kitchen_stock`) using Python formatted f-strings.
* Implements safety validation logic (`use_eggs`) to prevent operations when raw inventory is insufficient.
* Shows function orchestration by nesting a data utility function within a broader recipe function (`make_fried_egg`).
* Overcomes the variable shadowing isolation constraint by explicitly reassigning global state from functional returns.

## 🧠 Concepts Practice
* **Variable Scope:** Mastered the structural behavior of Global vs. Local scope levels.
* **Functional Data Flow:** Passing parameters into functions as arguments and retrieving processed state using `return`.
* **State Mutability:** Mutating external variable data safely via explicit function outputs without breaking memory boundaries.
* **String Formatting:** Writing clean console reporting with Python f-strings.

## 🛠️ How to Run
Ensure you have Python installed, then run the script using your terminal:
```bash
python main.py
```
