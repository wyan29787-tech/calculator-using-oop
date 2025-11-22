# Calculator Using OOP

A simple command-line calculator application built using Object-Oriented Programming principles in Python.

## Description

This application implements a basic calculator that can perform the following operations:

- Addition
- Subtraction
- Multiplication
- Division

The calculator uses OOP concepts such as classes, methods, and attributes to organize the code structure. It also includes a history feature that saves all calculations to a text file.

## Features

- Simple command-line interface
- Support for basic arithmetic operations
- Input validation
- Calculation history saved to a text file
- Built using Object-Oriented Programming principles

## How to Use

1. Run the Python script:

   ```
   python calcu.py
   ```

2. Follow the prompts:

   - Enter the first number
   - Enter the second number
   - Choose an operation (add, subtract, multiply, divide)

3. The result will be displayed and automatically saved to the calculation history file.

## Files

- `calcu.py` - The main calculator application
- `calculation_history.txt` - Stores the history of all calculations performed

## Code Structure

The application is built around the `Calculator` class which contains:

- `__init__` method: Initializes the calculator with default values
- `calcu` method: Handles user input and performs the selected operation
- `total` method: Displays the result of the calculation
- `history` method: Saves the calculation to the history file

## Requirements

- Python 3.x

## Example Usage

```
Enter a number: 10
Enter a number: 5
What mathematical operation would you like to perform? (add, subtract, multiply, divide): multiply
The total is 50
Calculation saved to history file.
```

## Future Enhancements

Possible future improvements could include:

- Support for more complex mathematical operations
- A graphical user interface
- Option to view calculation history from within the application

## Author

wyan29787-tech


