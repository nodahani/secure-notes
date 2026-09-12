import os


def encrypt_text(text, shift):
    result = ""
    for char in text:
        if "a" <= char <= "z":
            shift_char = (ord(char) - ord("a") + shift) % 26 + ord("a")
            result += chr(shift_char)
        else:
            result += char
    return result


def decrypt_text(text, shift):
    result = ""
    for char in text:
        if "a" <= char <= "z":
            shift_char = (ord(char) - ord("a") - shift) % 26 + ord("a")
            result += chr(shift_char)
        else:
            result += char
    return result


def create_note(note_name):
    if note_name + ".txt" not in os.listdir("notes"):
        with open("./notes/" + note_name + ".txt", "w") as file:
            while True:
                user_input = input(
                    "Type and press Enter; leave empty and press Enter to finish: "
                )
                if user_input == "":
                    break
                else:
                    file.write(encrypt_text(user_input, 3) + "\n")
        return True
    return False


def get_list_notes():
    # Getting the list
    file_names = os.listdir("notes")
    pure_names = []
    for file_name in file_names:
        if file_name.endswith(".txt"):
            pure_names.append(file_name[:-4])
    return pure_names


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


# edit note
def get_multiline_input(file):
    lines = []
    for count, line in enumerate(file, start=1):
        # Display note line by line
        print(f"{count}. {line}")

        edit_line_note = input("If you want to edit, type, otherwise press Enter... :")
        if edit_line_note != "":
            lines.append(edit_line_note + "\n")
        else:
            lines.append(line)
    return lines


def edit_note(note_name):
    print(note_name)
    with open("./notes/" + note_name + ".txt", "r") as file:
        new_note = get_multiline_input(file)

    with open("./notes/" + note_name + ".txt", "w") as file:
        file.writelines(new_note)


def display_note(notes_name):
    result = ""
    for i, note_name in enumerate(notes_name, start=1):
        print(f"''{i}. {note_name}''")
    with open("./notes/" + select_note(notes_name) + ".txt", "r") as file:
        text = file.read()
        result += decrypt_text(text, 3)

    return result


def delete_note(notes_name):
    note_name = select_note(notes_name)
    if note_name is None:
        print("Invalid selection")
        return

    confirm = input(f"Delete {note_name}? (y/n): ")
    if confirm.lower() != "y":
        print("Cancelled")
        return

    path = "./notes/" + note_name + ".txt"
    os.remove(path)
    print("Note DELETED!")


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
        delete_note(notes_name)

    # Exit
    elif choise == "5":
        print("Goodbay!")
        break

    else:
        print(">> Please choose from the options. <<")
