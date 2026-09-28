def progress_report(assignments):
    total = len(assignments)
    completed = 0

    for assignment in assignments:
        if assignment[3] == "Completed":
            completed = completed + 1

    pending = total - completed

    print("\n===== Progress Report =====")
    print("Total assignments:", total)
    print("Completed:", completed)
    print("Pending:", pending)

    if total > 0:
        progress = (completed / total) * 100
        print("Completion:", round(progress, 2), "%")
    else:
        print("Completion: 0%")