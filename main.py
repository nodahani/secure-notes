import os


def create_note(name_note):
    with open("./notes/" + name_note + ".txt", "w") as file:
        file.write(input("Write...: "))
        return True
    return False


def get_note_list():
    files = os.listdir("notes")
    list_note = []
    for fileName in files:
        if fileName.endswith(".txt"):
            list_note.append(fileName[:-4])
    return list_note


def display_note(note_names):
    index = int(input("Index note... "))
    for i, fileName in enumerate(note_names, start=1):
        if index == i:
            with open("./notes/" + fileName + ".txt", "r") as file:
                return file.read()


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


def edit_note():
    fileNames = get_note_list()
    for i, fileName in enumerate(fileNames, start=1):
        print(f"{i}. {fileName}")

    index = int(input("Index note... "))
    for i, fileName in enumerate(fileNames, start=1):
        if index == i:

            with open("./notes/" + fileName + ".txt", "r") as file:
                new_note = get_multiline_input(file)

            with open("./notes/" + fileName + ".txt", "w") as file:
                file.writelines(new_note)


# UI
while True:
    print("1. New Note Safe")
    print("2. Show Notes")
    print("3. Edit Note")
    print("4. Delete note")
    print("5. Exit!")

    choise = input("What do you want to do...? ")

    if choise == "1":
        name_note = input("The name of the note is...: ")
        if create_note(name_note):
            print(">> Note made. <<")
        else:
            print(">> Note not created. <<")

    if choise == "2":
        notes = get_note_list()
        print("...")
        for i, note_names in enumerate(notes, start=1):
            print(f"{i}. {note_names}")
        print("...")

        selected_note = display_note(notes)
        print(f"...\n{selected_note}\n...")

    if choise == "3":
        print(edit_note())

    if choise == "5":
        print("Goodbay!")
        break
