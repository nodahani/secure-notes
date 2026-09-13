import os
import crypto


def create_file():
    """Create an encrypted file.

    Returns:
        bool: True if the file was create, False if a file with the sam name already exist.
    """
    file_name = input("The name of the note is...: ")

    if file_name + ".txt" not in os.listdir("data"):
        with open("./data/" + file_name + ".txt", "w") as file:
            while True:
                user_input = input(
                    "Type and press Enter; leave empty and press Enter to finish: "
                )
                if user_input == "":
                    break
                else:
                    file.write(crypto.caesar_cipher(user_input, 3) + "\n")
        return True
    return False


def get_list_files():
    """Get list of files

    Returns:
        list: A list of file names (strings)
    """

    file_names = os.listdir("data")
    pure_names = []
    for file_name in file_names:
        if file_name.endswith(".txt"):
            pure_names.append(file_name[:-4])
    return pure_names


def get_multiline_input(file):
    """Read a file line by line and let the user edit each line.

    Args:
        file (file object): An open file object to read from.
    Returns:
        list: A list of lines (with newline characters) after editing.

    """

    lines = []
    for count, line in enumerate(file, start=1):
        print(f"{count}. {line}")

        edit_line_file = input("If you want to edit, type, otherwise press Enter... :")
        if edit_line_file != "":
            lines.append(edit_line_file + "\n")
        else:
            lines.append(line)
    return lines


def edit_file(file_name):
    """Edit the file.

    Args:
        file_name (str): The name of the file to edit.

    Returns:
        None

    """

    print(file_name)
    with open("./data/" + file_name + ".txt", "r") as file:
        text = file.read()
        print(text)
        result = crypto.caesar_cipher(text, -3)
        print(result)
        final_file = get_multiline_input(result)

    with open("./data/" + file_name + ".txt", "w") as file:
        file.writelines(crypto.caesar_cipher(final_file, 3))


def delete_file(file_name):
    """Delete file.

    Args:
        file_name (str): The name of the file to delete.

    Returns:
        None
    """
    if file_name is None:
        print("Invalid selection")
        return

    confirm = input(f"Delete {file_name}? (y/n): ")
    if confirm.lower() != "y":
        print("Cancelled")
        return

    path = "./data/" + file_name + ".txt"
    os.remove(path)
    print("Note DELETED!")
