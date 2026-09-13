def encrypt_text(text, shift):
    """Encrypt a text using Caesar cipher.

    Args:
        text (str): The text to encrypt.
        shift (int): Number of positions to shift each letter

    Returns:
        str: The encrypt text.
    """

    result = ""
    for char in text:
        if "a" <= char <= "z":
            shift_char = (ord(char) - ord("a") + shift) % 26 + ord("a")
            result += chr(shift_char)
        else:
            result += char
    return result


def decrypt_text(text, shift):
    """decrypt a text using Caesar cipher.

    Args:
        text (str): The text to decrypt.
        shift (int): Number of positions to shift each letter

    Returns:
        str: The decrypt text.
    """
    result = ""
    for char in text:
        if "a" <= char <= "z":
            shift_char = (ord(char) - ord("a") - shift) % 26 + ord("a")
            result += chr(shift_char)
        else:
            result += char
    return result
