def search_assignment(assignments):
    search = input("Enter assignment name or subject to search: ").lower()

    found = False

    for assignment in assignments:
        if search in assignment[0].lower() or search in assignment[1].lower():
            print(assignment[0], "|", assignment[1],
                  "| Due:", assignment[2], "|", assignment[3])
            found = True

    if found == False:
        print("No matching assignment found.")


def pending_assignments(assignments):
    if len(assignments) == 0:
        print("No assignments found.")
    else:
        print("\nPending Assignments:")

        found = False
        i = 1

        for assignment in assignments:
            if assignment[3] == "Pending":
                print(i, assignment[0], "|", assignment[1],
                      "| Due:", assignment[2])
                found = True
            i = i + 1

        if found == False:
            print("No pending assignments.")