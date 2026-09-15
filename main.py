from app import create_file, display_file
import constants

# UI
while True:
    print("1. Create New File")
    print("2. View Files")
    # print("3. Edit File")
    # print("4. Delete File")
    print("5. Exit")

    choise = input("What do you want to do...? ")

    # Create file
    if choise == "1":
        state = create_file()
        if state == constants.STATUS_SAVE:
            print("** file saved successfully. **")
        elif state == constants.DUPLICATE_NAME:
            print("** This name already exists. **")
        elif state == constants.STATUS_BACK:
            print("** You have returned to the previous menu. **")
        elif state == constants.STATUS_EXIT:
            print("** You are out. **")
            break
        elif state == constants.EMPTY_INPUT:
            print("** You cannot leave the input blank! **")
        else:
            print(f"** Unexpected status: {state} **")

    # Display files
    elif choise == "2":
        state = display_file()
        if state == constants.STATUS_OK:
            pass
        elif state == constants.STATUS_BACK:
            print("** You have returned to the previous menu. **")
        elif state == constants.STATUS_EXIT:
            print("** You are out. **")
            break
        elif state == constants.EMPTY_INPUT:
            print("** You cannot leave the input blank! **")
        elif state == constants.NOT_NUMBER:
            print("** Please enter a valid number. **")
        elif state == constants.INVALID_INPUT:
            print("** Your choice is not in the list **")

    # # Edit note
    # elif choise == "3":

    #     pure_names = get_list_files()
    #     for i, file_name in enumerate(pure_names, start=1):
    #         print(f"''{i}. {file_name}''")

    #     file_name = select_file(pure_names)
    #     print(f"Selected file: {file_name}")

    #     if edit_file(file_name):
    #         print(">> Note successfully edited. <<")
    #     else:
    #         print(">> Note edit failed. <<")

    # # Delete note
    # elif choise == "4":
    #     pure_names = get_list_files()
    #     for i, file_name in enumerate(pure_names, start=1):
    #         print(f"''{i}. {file_name}''")
    #     file_name = select_file(pure_names)
    #     if file_name:
    #         if delete_file(file_name):
    #             print("Note DELETED!")
    #         else:
    #             print("Cancelled")

    #     else:
    #         print(">> Please choose from the options. <<")

    # Exit
    elif choise == "5":
        print("Goodbay!")
        break

    else:
        print(">> Please choose from the options. <<")
