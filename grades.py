# Import necessary modules
import json, datetime

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

    # Set target file
    activityFilename = "activities.json"

    # Load data from file, store it in memory as a variable
    with open(activityFilename, 'r') as loadedFile:
        activityData = json.load(loadedFile)

    while True:
        # Display menu and take user's choice as input
        print("1. Record activities")
        print("2. Display grade summary")
        print("3. Back")
        choice = int(input("Enter the number corresponding to your choice: "))

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
                                # Take inputs for each piece of information and store them in the buffer
                                activityToBeLoaded = {
                                    "name": input("Enter a name for the activity... "),
                                    "type": input("Is this an [FA] or an [AA]? ").upper(),
                                    "subject": "",
                                    "score": float(input("What is your score on this activity? ")),
                                    "maximum": float(input("What is its maximum possible score? "))
                                }

                                print()
                                printSubjectList()
                                subjectID = int(input("Enter the number corresponding to this activity's subject... "))
                                print()

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
                actTypeFA = []
                actTypeAA = []
                for activities in activityData:
                    actTypeFA.append(activities["type"])
                for item in actTypeFA:
                    if item == "FA":
                        print("FA")
                        print(activities)
                        print()

                for activities in activityData:
                    actTypeAA.append(activities["type"])
                for item in actTypeAA:
                    if item == "AA":
                        print("AA")
                        print(activities)
                        print()
                print()
            case 3:
                break
            case _:
                print("Please enter a number between 1 and 3.")
                print()

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
        print("1. Record due dates")
        print("2. Display deadline summary")
        print("3. Back")
        choice = int(input("Enter the number corresponding to your choice: "))

        match choice:
            case 1:
                while True:
                    # Display menu, take user's choice
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
                print("[PLACEHOLDER - insert code for displaying a summary of the recorded deadlines]")
                print()
            case 3:
                break
            case _:
                print("Please enter a number between 1 and 3.")
                print()

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

def printSubjectList():
    print("List of subjects:")
    # The enumerate() function allows you to grab the index of a list element alongside the element
    for index, subject in enumerate(subjectList):
        print(f"{index}. {subject}")

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
        print("Menu:")
        print("1. Grade Management System")
        print("2. Schedule Tracker")
        print("3. Instructions")
        print("4. Exit")
        choice = int(input("Enter the number corresponding to your choice: "))

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