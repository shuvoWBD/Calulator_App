# Calulator_App
This is a Python-based calculator developed using the Tkinter GUI library. The calculator performs standard arithmetic operations such as +, −, ×, ÷, percentage, square root, and positive/negative toggle. It displays results directly on the interface and is suitable for beginners learning Python GUI development.



Key Features:

1.Scientific-Style Calculator Interface:
The calculator follows a familiar layout similar to modern mobile calculators, making it intuitive for users.

2.Basic and Advanced Operations:
It supports:

. Basic arithmetic: addition, subtraction, multiplication, division

. Percentage calculation

. Square root operation

. Sign toggle (+/-)

3.Dynamic Button Layout:
Buttons are generated from a 2D list, which makes the layout easy to modify or extend without rewriting UI code.

4.Real-Time Display Update:
The display updates instantly as buttons are pressed, showing the current expression or result.

5.Clear and Error Handling:

. “AC” clears the entire expression

.Invalid expressions are safely handled and show an “Error” message instead of crashing

6.Visual Button Categorization:
Different colors are used for:

. Operator buttons

. Top function buttons

. Number buttons:
This improves usability and visual clarity.




Technical Architecture:

1.Programming Language and Libraries:

. Language: Python

. GUI Framework: Tkinter

. Math Functions: math module

2.State Management:
  A single string variable expression stores the entire user input and current calculation state.

3.Event-Driven Design:
Each button click triggers the button_clicked() function, which processes the input based on button type.

4.Expression Parsing and Evaluation:

. User-friendly symbols (×, ÷) are internally converted to Python operators

. The built-in eval() function is used to evaluate expressions

5.Modular UI Construction:

. Button labels and layout are defined separately from logic

. UI elements are created dynamically using loops, reducing repetition

6.Error Control Flow:
try-except blocks prevent runtime errors during evaluation, square root, and percentage operations.

7.Separation of Logic and Presentation:

. Calculation logic handled in button_clicked()

. Display rendering handled by the update_label() function

.Styling handled through predefined color constants
