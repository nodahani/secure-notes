import crypto
import constants
from ui import getting_input_user, get_user_lines
from file_manager import file_exist, save_encrypted_file


def create_file():
    user_input = getting_input_user("Enter file name, or type 'exit' to quit: ")

    if user_input != constants.EMPTY_INPUT:
        if user_input == constants.STATUS_BACK:
            return constants.STATUS_BACK
        elif user_input == constants.STATUS_EXIT:
            return constants.STATUS_EXIT
        else:
            file_status = file_exist(user_input)
            if file_status:
                return constants.DUPLICATE_NAME
            else:
                return save_encrypted_file(
                    user_input,
                    get_user_lines(
                        "You are writing to the file. Press Enter to finish and save, or type 'exit' to cancel: \n"
                    ),
                )
    else:
        return constants.EMPTY_INPUT


# def edit_file(file_name):
#     """Edit the file.

#     Args:
#         file_name (str): The name of the file to edit.

#     Returns:
#         True
#     """
#     with open("./data/" + file_name + ".txt", "r") as file:
#         lines = crypto.caesar_cipher(file.read(), -3).splitlines()
#         content = "\n".join(get_multiline_input(lines))

#     with open("./data/" + file_name + ".txt", "w") as file:
#         file.write(crypto.caesar_cipher(content, 3))
#         return True


# def delete_file(file_name):
#     """Delete file.

#     Args:
#         file_name (str): The name of the file to delete.

#     Returns:
#         None
#     """

#     confirm = input(f"Delete {file_name}? (y/n): ")
#     if confirm.lower() != "y":
#         return False
#     else:
#         path = "./data/" + file_name + ".txt"
#         os.remove(path)
#         return True


# def display_file(pure_names):
#     """Display file titles and the content of the selected file.

#     Args:
#         pure_name (list): List of file titles.

#     Returns:
#         str: The decrypted content of the selected file.
#     """

#     result = ""
#     for i, file_name in enumerate(pure_names, start=1):
#         print(f"''{i}. {file_name}''")

#     file = select_file(pure_names)
#     if file:
#         with open("./data/" + file + ".txt", "r") as file:
#             text = file.read()
#             result += crypto.caesar_cipher(text, -3)
#     else:
#         return False
#     return result
