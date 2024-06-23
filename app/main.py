import sys
import os


def get_file_path(PATH, file_name):
    # Check each directory
    dirs = PATH.split(":")
    for dir in dirs:
        path = os.path.join(dir, file_name)
        # Command is found
        if os.path.isfile(path):
            return path
    
    return None

def main():
    # Constants
    COMMANDS = ["exit", "echo", "type"]
    PATH = os.environ.get("PATH")

    # Print shell prompt
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    user_in = input()
    args = user_in.split(" ")
    cmd = args[0]
    cmd_arg = ' '.join(args[1:])

    # Exit command
    if cmd == "exit":
        exit(0)
    # Echo command
    elif cmd == "echo":
        print(cmd_arg)
    # Type command
    elif cmd == "type":
        # Builtin commands
        if cmd_arg in COMMANDS:
            print(f"{cmd_arg} is a shell builtin")
        # Executable files
        elif PATH:
            file_path = get_file_path(PATH, cmd_arg)
            if file_path:
                print(f"{cmd_arg} is {file_path}")
            else:
                print(f"{cmd_arg}: not found")
        else:
            print(f"{cmd_arg}: not found")
    # Run program/Missing commands
    else:
        # Run program
        file_path = get_file_path(PATH, cmd)
        if file_path:
            os.system(user_in)
        # Missing commands
        else:
            # print(f"cmd is {cmd}, cmd_arg is {cmd_arg}, PATH is {PATH}")
            print(f"{cmd}: command not found")

    # Make shell recursively call itself
    main()


if __name__ == "__main__":
    main()
