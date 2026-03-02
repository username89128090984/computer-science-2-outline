import json

def gradeManagement():
    while True:
        print("1. Record grades")
        print("2. Display grade summary")
        print("3. Exit")
        choice = int(input("Enter the number corresponding to your choice: "))

        match choice:
            case 1:
                print("[PLACEHOLDER - insert code for recording grades to a file]")
            case 2:
                print("[PLACEHOLDER - insert code for displaying a summary of the grades]")
            case 3:
                break
            case _:
                print("Please enter a number between 1 and 3.")


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