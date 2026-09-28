from assignment_manager import add_assignment, view_assignments, edit_assignment, delete_assignment
from search import search_assignment, pending_assignments
from reports import progress_report
from validators import valid_number

assignments = []

print("================================")
print("   COLLEGE ASSIGNMENT TRACKER"   )
print("================================")

while True:
    print("\n1. Add Assignment")
    print("2. View Assignments")
    print("3. Mark Assignment Complete")
    print("4. Search Assignment")
    print("5. View Pending Assignments")
    print("6. Progress Report")
    print("7. Edit Assignment")
    print("8. Delete Assignment")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_assignment(assignments)

    elif choice == "2":
        view_assignments(assignments)

    elif choice == "3":
        if len(assignments) == 0:
            print("No assignments found.")
        else:
            print("\nAssignments:")

            i = 1
            for assignment in assignments:
                print(i, assignment[0], "-", assignment[3])
                i = i + 1

            number = input("Enter assignment number to mark complete: ")

            if number.isdigit():
                number = int(number)

                if 1 <= number <= len(assignments):
                    assignments[number - 1][3] = "Completed"
                    print("Assignment marked as completed.")
                else:
                    print("Invalid assignment number.")
            else:
                print("Please enter a valid number.")

    elif choice == "4":
        search_assignment(assignments)

    elif choice == "5":
        pending_assignments(assignments)

    elif choice == "6":
        progress_report(assignments)

    elif choice == "7":
        edit_assignment(assignments)

    elif choice == "8":
        delete_assignment(assignments)

    elif choice == "9":
        print("Thank you for using College Assignment Tracker.")
        break

    else:
        print("Invalid choice. Please select 1 to 9.")