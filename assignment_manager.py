from validators import valid_number


def add_assignment(assignments):
    name = input("Enter assignment name: ")
    subject = input("Enter subject: ")
    due_date = input("Enter due date: ")

    assignment = [name, subject, due_date, "Pending"]
    assignments.append(assignment)

    print("Assignment added successfully.")


def view_assignments(assignments):
    if len(assignments) == 0:
        print("No assignments found.")
    else:
        print("\nYour Assignments:")

        i = 1
        for assignment in assignments:
            print(i, assignment[0], "|", assignment[1],
                  "| Due:", assignment[2], "|", assignment[3])
            i = i + 1


def edit_assignment(assignments):
    if len(assignments) == 0:
        print("No assignments found.")
    else:
        view_assignments(assignments)

        number = input("Enter assignment number to edit: ")

        if valid_number(number, len(assignments)):
            number = int(number)

            name = input("Enter new assignment name: ")
            subject = input("Enter new subject: ")
            due_date = input("Enter new due date: ")

            assignments[number - 1][0] = name
            assignments[number - 1][1] = subject
            assignments[number - 1][2] = due_date

            print("Assignment updated successfully.")
        else:
            print("Invalid assignment number.")


def delete_assignment(assignments):
    if len(assignments) == 0:
        print("No assignments found.")
    else:
        view_assignments(assignments)

        number = input("Enter assignment number to delete: ")

        if valid_number(number, len(assignments)):
            number = int(number)

            del assignments[number - 1]

            print("Assignment deleted successfully.")
        else:
            print("Invalid assignment number.")