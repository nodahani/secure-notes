# SecureVault

A simple command-line file encryption tool written in Python.

## Features

- Create encrypted files
- View decrypted content
- Edit encrypted files
- Delete files
- Caesar cipher encryption

## How It Works

Each file is encrypted using a Caesar cipher.
The shift value is defined in constants.py and can be changed.
Only lowercase English letters are shifted; other characters stay unchanged.

## Requirements

- Python 3.10 or higher

## Installation

git clone https://github.com/nodahani/secure-vault.git
cd secure-vault

## Usage

python main.py

## Project Structure

secure-vault/
main.py # Entry point and menu
app.py # Controllers
ui.py # User interface functions
file_manager.py # Logic for file operations
crypto.py # Encryption/decryption
constants.py # Shared constants
data/ # Encrypted files

## License

MIT
