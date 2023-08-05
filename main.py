import os

from monkey_interpreter import repl


def main():
    print(f"Hello {os.getlogin()}! This is the Monkey programming language!")
    print("Feel free to type in commands")

    repl.start()


main()
