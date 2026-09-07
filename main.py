import os


def create_note(name_note):
    with open("./notes/" + name_note + ".txt", "w") as file:
        file.write(input("Write...: "))
        return True
    return False


def get_note_list():
    files = os.listdir("notes")
    list_note = []
    for filename in files:
        if filename.endswith(".txt"):
            list_note.append(filename[:-4])
    return list_note


def display_note(note_names):
    index = int(input("Index note... "))
    for i, filename in enumerate(note_names, start=1):
        if index == i:
            with open("./notes/" + filename + ".txt", "r") as file:
                return file.read()


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

    if choise == "5":
        print("Goodbay!")
        break
