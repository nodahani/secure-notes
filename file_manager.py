import os
import crypto
import constants


def file_exist(stem):
    if stem + ".txt" in os.listdir("./data"):
        return True
    else:
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


def save_encrypted_file(stem, input_result):
    """Writing encrypted text to a file"""

    lines, status = input_result
    if status == constants.STATUS_SAVE:
        with open("./data/" + stem + ".txt", "w") as file:
            text = "\n".join(lines)
            file.write(crypto.caesar_cipher(text, 3))
            return status
    else:
        return status
