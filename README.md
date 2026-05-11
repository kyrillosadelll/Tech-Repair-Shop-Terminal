# Tech Repair Shop Terminal

A terminal-based repair shop management system developed using Python.
The project simulates the workflow of a technology repair center by allowing users to manage repair services, create customer invoices, calculate service costs, and generate detailed bills through an interactive command-line interface.

The system was designed using Object-Oriented Programming principles to provide clean code organization, reusable components, and structured program flow.

---

# Features

* Display available repair services
* Add repair jobs to customer invoices
* Automatic service cost calculation
* Generate detailed final bills
* Interactive menu-driven interface
* Input validation and error handling
* Organized object-oriented code structure
* Simple and user-friendly terminal interaction

---

# Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Command-Line Interface (CLI)

---

# Project Structure

```bash id="s4bzou"
Tech-Repair-Shop-Terminal/
│
├── main.py
├── README.md
├── screenshots/
└── demo-video.mp4
```

---

# System Workflow

The program follows a simple repair shop workflow:

1. The user selects a repair service from the menu.
2. Repair jobs are added to the customer invoice.
3. The system calculates the total repair cost.
4. A detailed final bill is generated and displayed.

---

# Code Illustration

## Main Components

### Service Class

The `Service` class stores repair service information such as:

* Service name
* Repair category
* Service price

Example responsibilities:

* Creating service objects
* Managing repair details

---

### Invoice Class

The `Invoice` class handles customer billing operations including:

* Adding repair services
* Calculating total cost
* Printing the final invoice

Example responsibilities:

* Storing selected services
* Managing billing calculations

---

### Menu System

The menu system controls user interaction through a continuous loop that allows the user to:

* View services
* Add repair jobs
* Generate invoices
* Exit the program

---

# Example Program Menu

```text id="5kl6m1"
=============================
 Tech Repair Shop System
=============================

1. View Services
2. Add Repair Job
3. Generate Invoice
4. Exit
```

---

# Example Invoice Output

```text id="5tdq31"
========== FINAL BILL ==========

Screen Repair      : $120
Battery Replacement: $60
Software Installation: $40

--------------------------------
Total Cost         : $220

Thank You For Visiting
```

---

# How to Run

1. Install Python 3 on your computer.
2. Download or clone the repository.
3. Open the project folder in the terminal.
4. Run the following command:

```bash id="czhujv"
python main.py
```

---

# Programming Concepts Applied

This project demonstrates the use of:

* Classes and Objects
* Functions and Modular Programming
* Lists and Data Handling
* Loops and Conditional Statements
* Input Validation
* Object-Oriented Design

---

# Demonstration Video

Google Drive Video Link:

[https://drive.google.com/file/d/1NKXas_EwczpL7B26EL2_R4Ic_BXFN7u7/view?usp=share_link](https://drive.google.com/file/d/1NKXas_EwczpL7B26EL2_R4Ic_BXFN7u7/view?usp=share_link)

---

# Author

Developed as part of a programming project submission.
