#!/data/data/com.termux/files/usr/bin/python3

from argparse import ArgumentError
from sys import argv, stderr
from subprocess import run
from json import load


def main():

    if len(argv) != 3:
        print(
            f"Wrong Number of arguments, needs path to <contacts.json> and <message.txt>",
            file=stderr,
        )
        raise ArgumentError

    _, CONTACTS_PATH, MESSAGE_PATH = argv

    contacts = load(open(CONTACTS_PATH, "r"))

    number_str: str = ""
    for contact in contacts:
        number_str += (f"{contact['number']},").replace("+49", "0")

    fstr = open(MESSAGE_PATH, "r")
    message = ""
    for line in fstr:
        message += line

    run(["termux-sms-send", "-n", number_str[:-1], "1", message])  # slot of sim card



if __name__ == "__main__":
    main()
