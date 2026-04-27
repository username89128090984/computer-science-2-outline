# Import necessary modules
import json, datetime, math

# Initialize list of subjects
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

    "Social Sciences",
    "ADTech",
    "Computer Science"
]

# Function for the grade manager
def gradeManagement():
    # Initialize activity data buffer
    activityToBeLoaded = {
        "name": "",
        "type": "",
        "subject": "",
        "score": 0.0,
        "maximum": 0.0
    }

    gradeSum = {
        "subject": "",
        "units": 0.0,
        "grade": 0.0,
    }

    # Set target file
    activityFilename = "activities.json"
    gradesFilename = ""
    # Load data from file, store it in memory as a variable
    with open(activityFilename, 'r') as loadedFile:
        activityData = json.load(loadedFile)

    while True:
        # Display menu and take user's choice as input
        print("1. Record activities")
        print("2. Display grade summary")
        print("3. Back")

        try:
            choice = int(input("Enter the number corresponding to your choice: "))
        except:
            print("Please enter a number.")
            print()
            continue

        # If the user chose to...
        match choice:
            # ...record activities:
            case 1:
                while True:
                    # Display menu and take user's choice as input
                    print()
                    print("How will you enter this activity's information?")
                    print("1. Manual entry")
                    print("2. Select an activity recorded from the schedule tracker")
                    choice = int(input("Enter the number corresponding to your choice: "))
                    print()

                    # If the user chose...
                    match choice:
                        # ...manual entry:
                        case 1:
                            while True:
                                syntaxFail = False
                                # Take inputs for each piece of information and store them in the buffer

                                activityToBeLoaded = {
                                    "name": input("Enter a name for the activity... "),
                                    "type": input("Is this an [FA] or an [AA]? ").upper(),
                                    "subject": ""
                                }

                                while True:
                                    try:
                                        activityToBeLoaded = {
                                            "score": float(input("What is your score on this activity? ")),
                                            "maximum": float(input("What is its maximum possible score? "))
                                        }
                                    except:
                                        print("score/maximum may only be a number")
                                        continue
                                    else:
                                        break

                                print()
                                printSubjectList()
                                subjectID = int(input("Enter the number corresponding to this activity's subject... "))
                                print()

                                # add input validation here!!!
                                errors = []
                                if activityToBeLoaded["type"] not in ["FA", "AA"]:
                                    errors.append("type must be either 'FA' or 'AA'")
                                if subjectID not in range(0, 14):
                                    errors.append("subject ID does not match any subjects")
                                if activityToBeLoaded["score"] < 0 or activityToBeLoaded["maximum"] < 0:
                                    errors.append("neither the score nor maximum score may be negative")
                                if activityToBeLoaded["maximum"] == 0:
                                    errors.append("maximum score may not be 0")

                                if errors != []:
                                    print("Activity not recorded due to one or more errors:")
                                    for error in errors:
                                        print(error)
                                    input("Press enter to continue... ")
                                    print()
                                    continue

                                # Fill in the "subject" field based on the provided subject's ID
                                activityToBeLoaded["subject"] = subjectList[subjectID]

                                # Display confirmation prompt
                                for key, value in activityToBeLoaded.items():
                                    print(f"{key.title()}: {value}")
                                choice = input("Are these details correct? (y/n) ").lower()

                                match choice:
                                    case "y":
                                        # Append buffer contents to the data in memory, write data to file
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

                    # Prompt user to record another activity (or not...)
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
                # Initialize dictionary of dictionaries of sums
                gradeTotals = {}

                # For each subject...
                for subject in subjectList:
                    # ...create a key for it, then construct separate sum dictionaries for FAs and AAs (this is necessary, due to weightings)
                    gradeTotals[subject] = {"FA" : {"scoreSum" : 0, "totalSum" : 0, "average" : 0},
                                            "AA" : {"scoreSum" : 0, "totalSum" : 0, "average" : 0}}

                # For each activity in the Files...
                for activity in activityData:
                    # Access the dict of totals and the dict of types corresponding to the subject
                    # Access the dict of sums corresponding to the type
                    # Access and update the sums
                    gradeTotals[activity["subject"]][activity["type"]]["scoreSum"] += activity["score"]
                    gradeTotals[activity["subject"]][activity["type"]]["totalSum"] += activity["maximum"]
                    gradeTotals[activity["subject"]][activity["type"]]["average"] = (
                            gradeTotals[activity["subject"]][activity["type"]]["scoreSum"] /
                            gradeTotals[activity["subject"]][activity["type"]]["totalSum"]
                            if gradeTotals[activity["subject"]][activity["type"]]["totalSum"] != 0 else 0)

                print()
                print("Grade summary:")

                for subject in gradeTotals:
                    weightFA = 0.3
                    weightAA = 0.7

                    if gradeTotals[subject]["FA"]["totalSum"] == 0:
                        weightFA = 0
                    if gradeTotals[subject]["AA"]["totalSum"] == 0:
                        weightAA = 0
                        
                    print(subject)
                    print(f"{"Component":<10}|{"Total":^7}|{"Maximum":^9}|{"Percentage":^12}|{"Weighted%":^11}|")

                    print(f"{"FA":<10}|"
                          f"{gradeTotals[subject]["FA"]["scoreSum"]:^7}|"
                          f"{gradeTotals[subject]["FA"]["totalSum"]:^9}|"
                          f"{gradeTotals[subject]["FA"]["average"] * 100:^12.2f}|"
                          f"{(gradeTotals[subject]["FA"]["average"] * weightFA) * 100:^11.2f}|")

                    print(f"{"AA":<10}|"
                          f"{gradeTotals[subject]["AA"]["scoreSum"]:^7}|"
                          f"{gradeTotals[subject]["AA"]["totalSum"]:^9}|"
                          f"{gradeTotals[subject]["AA"]["average"] * 100:^12.2f}|"
                          f"{(gradeTotals[subject]["AA"]["average"] * weightAA) * 100:^11.2f}|")


                    print(f"Final percentage: {((gradeTotals[subject]["FA"]["average"] * weightFA) * 100) +
                                               ((gradeTotals[subject]["AA"]["average"] * weightAA) * 100):.2f}%")

                    if input("Press enter to continue to next subject, type 'exit' to cancel: ").lower() == "exit":
                        break

                with open("test.json", 'w') as anotherFile:
                    json.dump(gradeTotals, anotherFile, indent = 4)

            case 3:
                break
            case _:
                print("Please enter a number between 1 and 3.")

# Function for the scheduler
def scheduler():
    # Initialize data buffer
    deadlineToBeLoaded = {
        "name": "",
        "type": "",
        "subject": "",
        "deadline": datetime.datetime.min
    }

    # Set target file
    deadlineFilename = "deadlines.json"

    # Load data from file into memory
    with open(deadlineFilename, 'r') as loadedFile:
        deadlineData = json.load(loadedFile)

    # Specify date format to use
    dateFormat = "%m/%d/%Y"

    while True:
        # Display menu, take user's choice
        checkDeadlines(deadlineData, dateFormat)
        print("1. Record due dates")
        print("2. Display deadline summary")
        print("3. Back")

        try:
            choice = int(input("Enter the number corresponding to your choice: "))
        except:
            print("Please enter a number.")
            print()
            continue

        match choice:
            case 1:
                while True:
                    # Display menu, take user's choice
                    print()
                    print("How will you enter this activity's information?")
                    print("1. Manual entry")
                    print("2. Select an activity recorded from the schedule tracker")

                    try:
                        choice = int(input("Enter the number corresponding to your choice: "))
                    except:
                        print("Please enter a number.")
                        print()
                        continue

                    print()

                    # If the user chose...
                    match choice:
                        # ...manual entry:
                        case 1:
                            # Take inputs, store them in the buffer
                            deadlineToBeLoaded = {
                                "name": input("Enter a name for the activity... "),
                                "type": input("Is this an [FA] or an [AA]? ").upper(),
                                "subject": "",
                                # Format the date object into a string, for json files can't store date objects outright
                                "deadline": datetime.datetime.strftime(
                                    # Convert inputted date string to a date object
                                    datetime.datetime.strptime(
                                        # Take date as input
                                        input("When is this due? (mm/dd/yyyy) "),
                                        dateFormat).date(), # Get a date without the time
                                        dateFormat
                                    )
                            }

                            print()

                            # Ask for a subject ID, fill in "subject" field based on said ID
                            printSubjectList()
                            subjectID = int(input("Enter the number corresponding to this activity's subject... "))
                            print()

                            deadlineToBeLoaded["subject"] = subjectList[subjectID]

                            # Display confirmation prompt
                            for key, value in deadlineToBeLoaded.items():
                                print(f"{key.title()}: {value}")
                            choice = input("Are these details correct? (y/n) ").lower()

                            match choice:
                                case "y":
                                    # Append buffer's data to current data in memory, write current data to file
                                    deadlineData.append(deadlineToBeLoaded)
                                    with open(deadlineFilename, 'w') as loadedFile:
                                        json.dump(deadlineData, loadedFile, indent = 4)
                                    break
                                case "n":
                                    print()
                                    continue
                                case _:
                                    print("Please enter either y(es) or n(o).")
                                    print()

                        case 2:
                            print("[PLACEHOLDER - functionality not yet implemented]")

                    # Prompt user to record another activity (or not...)
                    while True:
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
                sortedDeadlines = []
                print()
                for deadlines in deadlineData:
                    sortedDeadlines.append(deadlines)
                sortedDeadlines.sort(key=lambda deadline: datetime.datetime.strptime(deadline["deadline"], dateFormat))

                for item in sortedDeadlines:
                    dueTime = datetime.datetime.now() - datetime.datetime.strptime(item["deadline"], dateFormat)
                    if dueTime.days < 0:
                        print(f"Activity \"{item["name"]}\" was due {abs(dueTime.days)} days ago.")
                    else:
                        print(f"Activity \"{item["name"]}\" is due in {dueTime.days} days.")
                print()

            case 3:
                break
            case _:
                print("Please enter a number between 1 and 3.")
                print()

def printSubjectList():
    print("List of subjects:")
    # The enumerate() function allows you to grab the index of a list element alongside the element
    for index, subject in enumerate(subjectList):
        print(f"{index}. {subject}")

def checkDeadlines(data, format):
    almostDue = {}
    for activity in data:
        timeUntil = datetime.datetime.strptime(activity["deadline"], format) - datetime.datetime.now()
        if timeUntil <= datetime.timedelta(days = 7):
            almostDue[activity["name"]] = timeUntil
    print("Note: the following activities are either almost due or overdue:")


def instructions():
    print("Most, if not all, of this program's menus are navigated by entering a number based on your desired outcome.")
    print("At the prompt for your choice, enter the number and ONLY the number. (input validation will be added at a later point in time)\n")
    print("When recording activities, the program will ask for information, one piece at a time.")
    print("Most prompts will require you to simply enter a string or a number, which should be typed as-is without any other content.")
    print("If the prompt requires a specific input/format (i.e., 'FA or AA', date inputs), the required input/format will be in square brackets/parentheses.\n")
    print("Notes:")
    print("NONE of the activity's data will be saved to the file until you confirm that the supplied information is correct.")
    print("This is not the final product. Features are subject to addition and removal at any time, without due notice.")
    print("This section may be revised heavily in the future.")
    input("\nIf you've finished reading, press enter to continue. ")

def main():
    while True:
        # Display menu and take user's choice as input
        print()
        print(".d8888b.       ooooooooooooooo      88888      88888     8888888888          8888888888      88888           888     ooooooooooooooo\n"
              "d88p Y88b      8'    888    '8      88888      88888     8888888888888       888             888888          888     8'    888    '8\n"
              "Y88b.                888            88888      88888     8888     88888      888             8888888         888           888\n"
              "  Y888b              888            88888      88888     8888      8888      888______       8888  8888      888           888\n"
              "     Y88b.           888            88888      88888     8888      8888      888''''''       8888   8888     888           888\n"
              "       888           888            88888      88888     8888     88888      888             8888    88888   888           888\n"
              "Y88b  d88p           888             Y88b      8888      88888888888888      888             8888     8888888888           888\n"           
              " Y88888P            o888o             Y88888888888       88888888888         8888888888      8888      888888888          o888o\n")
        print()
        print("88888                  88888             .o.             88888           888         .o.                 8888888888            8888888888        88888                  88888        8888888888      88888           888     ooooooooooooooo\n"
              "888888                888888            .888.            888888          888        .888.              888888888888            888               888888                888888        888             888888          888     8'    888    '8\n"
              "8888888              8888888           .8''888.          8888888         888       .8''888.          8888                      888               8888888              8888888        888             8888888         888           888\n"
              "8888  8888        8888  8888          .8'  `888.         8888  8888      888      .8'  `888.         888    88888888888        888______         8888  8888        8888  8888        888______       8888  8888      888           888\n"
              "8888   8888      8888   8888         .8ooooo8888.        8888   8888     888     .8ooooo8888.        888    88888888888        888''''''         8888   8888      8888   8888        888''''''       8888   8888     888           888\n"
              "8888    88888  88888    8888        .8'      `888.       8888    88888   888    .8'      `888.       888           8888        888               8888    88888  88888    8888        888             8888    88888   888           888\n"
              "8888     8888888888     8888       .8'        `888.      8888     8888888888   .8'        `888.      8888        8888          888               8888     8888888888     8888        888             8888     8888888888           888\n"
              "8888      888888888     8888      o88o        o8888o     8888      888888888  o88o        o8888o       888888888888            8888888888        8888      888888888     8888        8888888888      8888      888888888          o888o\n")
        print()
        print("8888          8888       88888      88888        8888888888888\n"
              "8888          8888       88888      88888        88888888888888\n"
              "8888          8888       88888      88888        8888     888888\n"
              "8888          8888       88888      88888        8888      8888\n"
              "8888          8888       88888      88888        8888888888888\n"
              "888888888888888888       88888      88888        88888888888888\n"
              "888888888888888888       88888      88888        8888      88888\n"
              "8888          8888       88888      88888        8888      888888\n"
              "8888          8888        Y88b      8888         88888888888888\n"
              "8888          8888         Y88888888888          8888888888888\n")

        print("Menu:")
        print("1. Grade Management System")
        print("2. Schedule Tracker")
        print("3. Instructions")
        print("4. Exit")

        try:
            choice = int(input("Enter the number corresponding to your choice: "))
        except:
            print("Please enter a number.")
            print()
            continue

        match choice:
            case 1:
                print()
                gradeManagement()
            case 2:
                print()
                scheduler()
            case 3:
                print()
                instructions()
            case 4:
                break
            case _:
                print("Please enter a number between 1 and 3.")

# Call the main() function to set everything in motion
main()