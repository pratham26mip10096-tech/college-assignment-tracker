# College Assignment Tracker - Project Statement

## Problem Statement

College students often have multiple assignments from different subjects.
It can become difficult to keep track of assignment names, subjects, due
dates and completion status.

The College Assignment Tracker is designed to provide a simple way to
manage these assignments through a command-line interface.

## Objectives

- To add and manage college assignments.
- To keep track of assignment due dates.
- To mark assignments as completed.
- To search assignments by name or subject.
- To view pending assignments.
- To display assignment progress.
- To edit or delete assignments.

## Functional Requirements

1. The user should be able to add a new assignment.
2. The user should be able to view all assignments.
3. The user should be able to mark an assignment as completed.
4. The user should be able to search for an assignment.
5. The user should be able to view pending assignments.
6. The user should be able to view a progress report.
7. The user should be able to edit an assignment.
8. The user should be able to delete an assignment.
9. The user should be able to exit the program.

## Non-Functional Requirements

- The program should be simple and easy to use.
- The program should run through the command line.
- The program should provide clear messages to the user.
- The program should handle invalid input appropriately.
- The program should not require external libraries.

## Input

The program takes the following inputs from the user:

- Assignment name
- Subject
- Due date
- Assignment number
- Menu choice

## Output

The program displays:

- Assignment details
- Pending assignments
- Completed assignments
- Progress report
- Success and error messages

## Technologies Used

- Python
- Command Line Interface

## Project Modules

- main.py - Controls the main menu and program flow.
- assignment_manager.py - Handles adding, viewing, editing and deleting assignments.
- search.py - Handles searching and viewing pending assignments.
- reports.py - Generates the progress report.
- validators.py - Contains basic input validation.

## Data Storage

Assignments are stored temporarily in a Python list while the program is
running. The data is cleared when the program is closed.

## Conclusion

The College Assignment Tracker provides a simple command-line solution for
managing college assignments. It helps the user organize assignments,
track their completion status and view overall progress.