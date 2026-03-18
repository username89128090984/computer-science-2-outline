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


def printSubjectList():
    print("List of subjects:")
    for index, subject in enumerate(subjectList):
        print(f"{index}. {subject}")

def SubjectGradeManagement():

    activityData = {
        "name": "",
        "type": "",
        "subject": "",
        "score": 0.0,
        "maximum": 0.0
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

                                printSubjectList()
                                subjectID = int(
                                    input("Enter the number corresponding to this activity's subject... "))
                                print()

                                activityData["subject"] = subjectList[subjectID]

                                for key, value in activityData.items():
                                    print(f"{key.title()}: {value}")
                                choice = input("Are these details correct? (y/n) ")

                                match choice:
                                    case "y":
                                        print(
                                            "[PLACEHOLDER - insert code for writing data to file once database is figured out]")
                                        break
                        case 2:
                            print("[PLACEHOLDER - insert code for displaying a summary of the recorded deadlines]")
                            print() #yyy
                        case 3:
                            break
                        case _:
                            print("Please enter a number between 1 and 3.")
                            print()

SubjectGradeManagement()