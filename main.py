import crypto
from file_manager import delete_file, edit_file, create_file, get_list_files


def select_file(pure_names):
    """It takes a number from the user and returns that file.

    Args:
        pure_name (list): List of file titles.

    Returns:
        str: Name of the selected file.
        None: If the input non-numeric or out of range.

    """

    index = input("Selection index note: ")
    try:
        index = int(index)
    except ValueError:
        return None

    if index < 1 or index > len(pure_names):
        return None

    return pure_names[index - 1]


def display_file(pure_names):
    """Display file titles and the content of the selected file.

    Args:
        pure_name (list): List of file titles.

    Returns:
        str: The decrypted content of the selected file.
    """

    result = ""
    for i, file_name in enumerate(pure_names, start=1):
        print(f"''{i}. {file_name}''")

    file = select_file(pure_names)
    if file:
        with open("./data/" + file + ".txt", "r") as file:
            text = file.read()
            result += crypto.caesar_cipher(text, -3)
    else:
        return False
    return result


# UI
while True:
    print("1. New Note Safe")
    print("2. Show Notes")
    print("3. Edit Note")
    print("4. Delete note")
    print("5. Exit!")

    choise = input("What do you want to do...? ")

    # Create note
    if choise == "1":
        if create_file():
            print(">> Note successfully created. <<")
        else:
            print(">> This name is already taken. <<")

    # Display notes
    elif choise == "2":
        pure_names = get_list_files()
        result = display_file(pure_names)
        if result:
            print(f'"""\n{result}\n"""')
        else:
            print(">> Please choose from the options. <<")

    # Edit note
    elif choise == "3":

        pure_names = get_list_files()
        for i, file_name in enumerate(pure_names, start=1):
            print(f"''{i}. {file_name}''")

        file_name = select_file(pure_names)
        print(f"Selected file: {file_name}")

        if edit_file(file_name):
            print(">> Note successfully edited. <<")
        else:
            print(">> Note edit failed. <<")

    # Delete note
    elif choise == "4":
        pure_names = get_list_files()
        for i, file_name in enumerate(pure_names, start=1):
            print(f"''{i}. {file_name}''")
        file_name = select_file(pure_names)
        if file_name:
            if delete_file(file_name):
                print("Note DELETED!")
            else:
                print("Cancelled")

        else:
            print(">> Please choose from the options. <<")

    # Exit
    elif choise == "5":
        print("Goodbay!")
        break

    else:
        print(">> Please choose from the options. <<")
