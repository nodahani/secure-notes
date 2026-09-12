import crypto

from note_manager import delete_note, edit_note, create_note, get_list_notes


def select_note(pure_names):
    # Select a note
    index = input("Selection index note: ")

    try:
        index = int(index)
    except ValueError:
        print("Value error")
        return None

    if index < 1 or index > len(pure_names):
        return None

    return pure_names[index - 1]


def display_note(notes_name):
    result = ""
    for i, note_name in enumerate(notes_name, start=1):
        print(f"''{i}. {note_name}''")
    with open("./data/" + select_note(notes_name) + ".txt", "r") as file:
        text = file.read()
        result += crypto.decrypt_text(text, 3)

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
        note_name = input("The name of the note is...: ")
        if create_note(note_name):
            print(">> Note successfully created. <<")
        else:
            print(">> This name is already taken. <<")

    # Display notes
    elif choise == "2":
        notes_name = get_list_notes()
        result = display_note(notes_name)
        print(f'"""\n{result}\n"""')

    # Edit note
    elif choise == "3":
        notes_name = get_list_notes()
        for i, note_name in enumerate(notes_name, start=1):
            print(f"''{i}. {note_name}''")

        note_name = select_note(notes_name)
        edit_note(note_name)

    elif choise == "4":
        notes_name = get_list_notes()
        for i, note_name in enumerate(notes_name, start=1):
            print(f"''{i}. {note_name}''")
        note_name = select_note(notes_name)
        delete_note(note_name)

    # Exit
    elif choise == "5":
        print("Goodbay!")
        break

    else:
        print(">> Please choose from the options. <<")
