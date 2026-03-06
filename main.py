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
    activityToBeLoaded = {
        "name": "",
        "type": "",
        "subject": "",
        "score": 0.0,
        "maximum": 0.0
    }

    activityFilename = "activities.json"

    with open(activityFilename, 'r') as loadedFile:
        activityData = json.load(loadedFile)

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
                                activityToBeLoaded = {
                                    "name": input("Enter a name for the activity... "),
                                    "type": input("Is this an AA or an FA? ").upper(),
                                    "subject": "",
                                    "score": float(input("What is your score on this activity? ")),
                                    "maximum": float(input("What is its maximum possible score? "))
                                }

                                print()

                                printSubjectList()
                                subjectID = int(input("Enter the number corresponding to this activity's subject... "))
                                print()

                                activityToBeLoaded["subject"] = subjectList[subjectID]

                                for key, value in activityToBeLoaded.items():
                                    print(f"{key.title()}: {value}")
                                choice = input("Are these details correct? (y/n) ").lower()

                                match choice:
                                    case "y":
                                        activityData.append(activityToBeLoaded)
                                        with open(activityFilename, 'w') as loadedFile:
                                            json.dump(activityData, loadedFile, indent = 4)
                                        break
                                    case "n":
                                        print()
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
    deadlineToBeLoaded = {
        "name": "",
        "type": "",
        "subject": "",
        "deadline": datetime.datetime.min
    }

    deadlineFilename = "deadlines.json"

    with open(deadlineFilename, 'r') as loadedFile:
        deadlineData = json.load(loadedFile)

    dateFormat = "%m/%d/%Y"

    while True:
        print("1. Record due dates")
        print("2. Display deadline summary")
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
                            deadlineToBeLoaded = {
                                "name": input("Enter a name for the activity... "),
                                "type": input("Is this an AA or an FA? ").upper(), "subject": "",
                                "deadline": datetime.datetime.strftime(
                                    datetime.datetime.strptime(
                                        input("When is this due? (mm/dd/yyyy) "),
                                        dateFormat).date(),
                                    dateFormat
                                    )
                            }

                            print()

                            printSubjectList()
                            subjectID = int(input("Enter the number corresponding to this activity's subject... "))
                            print()

                            deadlineToBeLoaded["subject"] = subjectList[subjectID]

                            for key, value in deadlineToBeLoaded.items():
                                print(f"{key.title()}: {value}")
                            choice = input("Are these details correct? (y/n) ").lower()

                            match choice:
                                case "y":
                                    with open(deadlineFilename, 'w') as loadedFile:
                                        deadlineData.append(deadlineToBeLoaded)
                                        json.dump(deadlineData, loadedFile, indent = 7)
                                    break
                                case "n":
                                    print()
                                    continue
                                case _:
                                    print("Please enter either y(es) or n(o).")
                                    print()

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
                print("[PLACEHOLDER - insert code for displaying a summary of the recorded deadlines]")
                print()
            case 3:
                break
            case _:
                print("Please enter a number between 1 and 3.")
                print()

def printSubjectList():
    print("List of subjects:")
    for index, subject in enumerate(subjectList):
        print(f"{index}. {subject}")

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