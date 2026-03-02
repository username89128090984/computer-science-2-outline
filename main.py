def gradeManagement():
    print("[PLACEHOLDER - insert grade manager code]")

def scheduler():
    print("[PLACEHOLDER - insert grade manager code]")

def main():
    while True:
        print()
        print("Menu:")
        print("1. Grade Management System")
        print("2. Schedule Tracker")
        print("3. Exit")
        choice = int(input("Enter the number corresponding to your choice: "))
        print()

        match choice:
            case 1:
                gradeManagement()
            case 2:
                scheduler()
            case 3:
                break
            case _:
                print("Please enter a number between 1 and 3.")

main()