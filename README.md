Simple Python Calculator (Tkinter)

This is a basic desktop calculator application built using Python's built-in tkinter library. It provides four fundamental arithmetic operations: addition, subtraction, multiplication, and division.

🚀 Features

GUI: A simple graphical user interface using tkinter.

Operations: Supports four core functions: +, -, *, and /.

In-App Calculation: Takes numerical inputs from two separate entry fields.

Dynamic Output: Displays the result in a large, clear output label.

📋 Prerequisites

To run this application, you only need a standard Python installation (version 3.x is recommended). tkinter is included in most standard Python distributions, so no extra installations should be necessary.

Python 3.x

⚙️ How to Run

Save the Code: Save the provided Python code into a file named calculator.py.

Run from Terminal: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the script:

python calculator.py


🖥️ Usage

Input: Enter the first number in the "Value 1" entry field and the second number in the "Value 2" entry field. The application expects valid numbers (integers or floating-point numbers).

Operation: Click one of the operation buttons:

+ (Add)

- (Subtract)

* (Multiply)

/ (Division)

Output: The result of the operation will be displayed in the large "Output" box at the bottom of the window.

Error Handling Note

If you attempt to divide by zero, the application will display inf (infinity) in the output label, which is standard Python behavior for floating-point division by zero. If you enter non-numeric text, the application will crash with a ValueError (this is a simple implementation and does not include advanced error checking).

🗃️ File Structure

The entire application is self-contained in a single Python file:

calculator.py: Contains all GUI setup, function definitions for the operations, and the main application loop.
