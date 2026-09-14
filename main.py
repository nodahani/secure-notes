from app import create_file
import constants

# UI
while True:
    print("1. New Note Safe")
    # print("2. Show Notes")
    # print("3. Edit Note")
    # print("4. Delete note")
    print("5. Exit!")

    choise = input("What do you want to do...? ")

    # Create note
    if choise == "1":
        state = create_file()
        if state == constants.DUPLICATE_NAME:
            print("** This name already exists. **")
        elif state == constants.STATUS_BACK:
            print("** You have returned to the previous menu. **")
        elif state == constants.STATUS_EXIT:
            print("** You are out. **")
        else:
            print("** You cannot leave the input blank! **")

    # # Display notes
    # elif choise == "2":
    #     pure_names = get_list_files()
    #     result = display_file(pure_names)
    #     if result:
    #         print(f'"""\n{result}\n"""')
    #     else:
    #         print(">> Please choose from the options. <<")

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
