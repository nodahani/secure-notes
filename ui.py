import constants


def get_user_lines(message):
    text = []
    status = constants.STATUS_SAVE
    while True:
        user_input = input(message)
        if user_input == constants.STATUS_EXIT:
            return [], constants.STATUS_EXIT
        elif user_input == "":
            break
        else:
            text.append(user_input)

    return text, status


def getting_input_user(message):
    """Prompt the user and return their input.

    Returns a status constant if user types 'back' or 'exit'."""
    user_input = input(message)
    if user_input == constants.STATUS_BACK:
        return constants.STATUS_BACK
    elif user_input == constants.STATUS_EXIT:
        return constants.STATUS_EXIT
    else:
        return user_input


def select_file(pure_names, message):
    """It takes a number from the user and returns that file.

    Args:
        pure_name (list): List of file titles.

    Returns:
        str: Name of the selected file.
        None: If the input non-numeric or out of range.

    """

    index = input(message)
    try:
        index = int(index)
    except ValueError:
        return None

    if index < 1 or index > len(pure_names):
        return None

    return pure_names[index - 1]


def edit_lines_in_ui(lines, message):
    """Edit import file lines

    Args:
        lines (list): list of lines

    Returns:
        list: List of edited lines
    """

    edit_lines = []
    for line in lines:
        print(line)
        user_input = input(message)
        if user_input != "":
            edit_lines.append(user_input)
        else:
            edit_lines.append(line)
    return edit_lines
