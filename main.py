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
                                    "type": input("Is this an AA or an FA? ").upper(),
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
                print("[PLACEHOLDER - insert code for displaying a summary of the grades]")
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
                                "type": input("Is this an AA or an FA? ").upper(), "subject": "",
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

def main():
    while True:
        # Display menu and take user's choice as input
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

# Call the main() function to set everything in motion
main()