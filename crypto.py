def encrypt_text(text, shift):
    result = ""
    for char in text:
        if "a" <= char <= "z":
            shift_char = (ord(char) - ord("a") + shift) % 26 + ord("a")
            result += chr(shift_char)
        else:
            result += char
    return result


def decrypt_text(text, shift):
    result = ""
    for char in text:
        if "a" <= char <= "z":
            shift_char = (ord(char) - ord("a") - shift) % 26 + ord("a")
            result += chr(shift_char)
        else:
            result += char
    return result
