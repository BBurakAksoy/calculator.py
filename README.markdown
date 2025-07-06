# Simple Tkinter Calculator

## Overview
This is a simple graphical calculator built using Python's Tkinter library. It allows users to perform basic arithmetic operations (addition, subtraction, multiplication, and division) on two numbers through a user-friendly GUI.

## Features
- Input two numbers (supports decimal numbers).
- Perform basic operations: addition (+), subtraction (-), multiplication (*), and division (/).
- Error handling for invalid inputs (e.g., non-numeric values) and division by zero.
- Clear button to reset inputs and results.
- Simple and intuitive interface.

## Requirements
- Python 3.x
- Tkinter (included with standard Python installations)

## Installation
1. Ensure Python 3.x is installed on your system.
2. No additional libraries are required, as Tkinter is part of Python's standard library.
3. Download or copy the `calculator_gui.py` file to your local machine.

## Usage
1. Run the script using Python:
   ```bash
   python calculator_gui.py
   ```
2. A window will open with two input fields labeled "Number 1" and "Number 2".
3. Enter numbers (e.g., `5.5` and `3`) in the input fields.
4. Click one of the operation buttons (`+`, `-`, `*`, `/`) to calculate the result.
5. The result will appear in the "Result" label below.
6. Click the "Clear" button to reset the input fields and result.

## Error Handling
- If non-numeric values are entered, the result will display: `Error: Invalid input`.
- If division by zero is attempted, the result will display: `Error: Division by zero`.

## Example
- Input: Number 1 = `10.5`, Number 2 = `2`, Operation = `*`
- Output: `Result: 21.0`

## Notes
- The calculator supports floating-point numbers for more flexibility.
- The GUI is minimalistic but can be extended with additional features like exponentiation, history, or advanced operations.

## License
This project is unlicensed and free to use or modify.