def new_note(name_note):
    with open("./notes/" + name_note + ".txt", "w") as file:
        file.write(input("Write...: "))
        return True
    return False


def show_notes(name_note):
    with open("./notes/" + name_note + ".txt", "r") as file:
        return file.read()
    return False


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
        if new_note(name_note):
            print(">> Note made. <<")
        else:
            print(">> Note not created. <<")

    if choise == "2":
        name_note = input("I want to see the note...: ")
        if show_notes(name_note):
            print(f"...\n{show_notes(name_note)}\n...")
        else:
            print(">> Note not found. <<")

    if choise == "5":
        print("Goodbay!")
        break
