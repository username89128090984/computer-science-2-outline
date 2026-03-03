import json, datetime

subjectList = [
    "Math 2 (algebra)",
    "Math 3 (geometry)",

    "English",
    "Filipino",

    "ES",
    "Physics",
    "Chemistry",
    "Biology",

    "PE",
    "Health",
    "Music",

    "ADTech",
    "Computer Science"
]

def gradeManagement():

    activityData = {
        "name" : "",
        "type" : "",
        "subject" : "",
        "score" : 0.0,
        "maximum" : 0.0
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
                            while True:
                                activityData["name"] = input("Enter a name for the activity... ")
                                activityData["type"] = input("Is this an AA or an FA? ").upper()
                                activityData["maximum"] = float(input("What is its maximum possible score? "))
                                activityData["score"] = float(input("What is your score on this activity? "))
                                print()

                                print("List of subjects:")
                                for index, subject in enumerate(subjectList):
                                    print(f"{index}. {subject}")
                                subjectID = int(input("Enter the number corresponding to this activity's subject... "))
                                print()

                                activityData["subject"] = subjectList[subjectID]

                                for key, value in activityData.items():
                                    print(f"{key.title()}: {value}")
                                choice = input("Are these details correct? (y/n) ")

                                match choice:
                                    case "y":
                                        print("[PLACEHOLDER - insert code for writing data to file once database is figured out]")
                                        break
                                    case "n":
                                        continue
                                    case _:
                                        print("Please enter either y(es) or n(o).")
                                        print()

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