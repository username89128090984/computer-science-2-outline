import json, datetime

subjectList = {
    1 : "Math 2 (algebra)",
    2 : "Math 3 (geometry)",

    3 : "English",
    4 : "Filipino",

    5 : "ES",
    6 : "Physics",
    7 : "Chemistry",
    8 : "Biology",

    9 : "PE",
    10 : "Health",
    11 : "Music",

    12 : "ADTech",
    13 : "Computer Science"
}

def gradeManagement():

    activityData = {
        "name" : "",
        "type" : "",
        "subject" : "",
        "score" : 0,
        "maximum" : 0
    }

    while True:
        print("1. Record grades")
        print("2. Display grade summary")
        print("3. Back")
        choice = int(input("Enter the number corresponding to your choice: "))

        match choice:
            case 1:
                while True:
                    print()
                    print("How will you enter this activity's information?")
                    print("1. Manual entry")
                    print("2. Select an activity recorded from the schedule tracker")
                    choice = int(input("Enter the number corresponding to your choice: "))
                    print()

                    match choice:
                        case 1:
                            name = input("Enter a name for the activity... ")
                            type = input("Is this an AA or an FA? ").upper()
                            maximum = float(input("What is its maximum possible score? "))
                            score = float(input("What is your score on this activity? "))
                            print()

                            print("List of subjects:")
                            for identifier, subject in subjectList.items():
                                print(f"{identifier}. {subject}")
                            subject = int(input("Enter the number corresponding to this activity's subject... "))

                            print("Are these details correct?")

                            print("[PLACEHOLDER - insert code for writing data to file once database is figured out]")
                            print()

                        case 2:
                            print("[PLACEHOLDER - finish scheduler first, then insert code for retrieval from file]")
                        case _:
                            print("Please enter a number between 1 and 2.")

                    choice = input("Would you like to record another activity? (y/n) ").lower()
                    match choice:
                        case "y":
                            pass
                        case "n":
                            break
                        case _:
                            print("Please enter either y(es) or n(o).")
                            print()

            case 2:
                print("[PLACEHOLDER - insert code for displaying a summary of the grades]")
                print()
            case 3:
                break
            case _:
                print("Please enter a number between 1 and 3.")
                print()


def scheduler():
    print("[PLACEHOLDER - insert grade manager code]")
    print()

def main():
    while True:
        print()
        print("Menu:")
        print("1. Grade Management System")
        print("2. Schedule Tracker")
        print("3. Exit")
        choice = int(input("Enter the number corresponding to your choice: "))

        match choice:
            case 1:
                print()
                gradeManagement()
            case 2:
                print()
                scheduler()
            case 3:
                break
            case _:
                print("Please enter a number between 1 and 3.")

main()