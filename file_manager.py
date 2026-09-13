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


def get_multiline_input(lines):
    """Edit import file lines

    Args:
        lines (list): list of lines

    Returns:
        list: List of edited lines
    """

    edit_lines = []
    for line in lines:
        print(line)
        user_input = input("Type to edit, or press Enter to dismiss:\n")
        if user_input != "":
            edit_lines.append(user_input)
        else:
            edit_lines.append(line)
    return edit_lines


def edit_file(file_name):
    """Edit the file.

    Args:
        file_name (str): The name of the file to edit.

    Returns:
        True
    """
    with open("./data/" + file_name + ".txt", "r") as file:
        lines = crypto.caesar_cipher(file.read(), -3).splitlines()
        content = "\n".join(get_multiline_input(lines))

    with open("./data/" + file_name + ".txt", "w") as file:
        file.write(crypto.caesar_cipher(content, 3))
        return True


def delete_file(file_name):
    """Delete file.

    Args:
        file_name (str): The name of the file to delete.

    Returns:
        None
    """

    confirm = input(f"Delete {file_name}? (y/n): ")
    if confirm.lower() != "y":
        return False
    else:
        path = "./data/" + file_name + ".txt"
        os.remove(path)
        return True
