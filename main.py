def gradeManagement():
    pass

def scheduler():
    pass

def main():
    while True:
        print("Menu:")
        print("1. Grade Management System")
        print("2. Schedule Tracker")
        print("3. Exit")
        choice = int(input("Enter the number corresponding to your choice: "))

        match choice:
            case 1:
                gradeManagement()
            case 2:
                scheduler()
            case 3:
                break
            case _:
                print("Please enter a number between 1 and 3.")