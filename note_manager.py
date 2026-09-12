import os
import crypto


def create_note(note_name):
    if note_name + ".txt" not in os.listdir("data"):
        with open("./data/" + note_name + ".txt", "w") as file:
            while True:
                user_input = input(
                    "Type and press Enter; leave empty and press Enter to finish: "
                )
                if user_input == "":
                    break
                else:
                    file.write(crypto.encrypt_text(user_input, 3) + "\n")
        return True
    return False


def get_list_notes():
    # Getting the list
    file_names = os.listdir("data")
    pure_names = []
    for file_name in file_names:
        if file_name.endswith(".txt"):
            pure_names.append(file_name[:-4])
    return pure_names


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
    with open("./data/" + note_name + ".txt", "r") as file:
        new_note = get_multiline_input(file)

    with open("./data/" + note_name + ".txt", "w") as file:
        file.writelines(new_note)


def delete_note(note_name):
    if note_name is None:
        print("Invalid selection")
        return

    confirm = input(f"Delete {note_name}? (y/n): ")
    if confirm.lower() != "y":
        print("Cancelled")
        return

    path = "./data/" + note_name + ".txt"
    os.remove(path)
    print("Note DELETED!")
