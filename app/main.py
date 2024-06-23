import sys
import os


def main():
    # Constants
    COMMANDS = ["exit", "echo", "type"]
    PATH = os.environ.get("PATH")

    # Print shell prompt
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    args = input().split(" ")
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
        print(PATH)
        if cmd_arg in COMMANDS:
            print(f"{cmd_arg} is a shell builtin")
        elif PATH:
            # Check each path in PATH env
            paths = cmd_arg.split(":")
            for path in paths:
                # Command is found
                if os.path.isfile(f"{path}/{cmd_arg}"):
                    sys.stdout.write(f"{cmd} is {cmd_arg}\n")
                    break
        else:
            print(f"{cmd_arg}: not found")
    # Handle missing commands
    else:
        sys.stdout.write(f"{cmd}: command not found\n")

    # Make shell recursively call itself
    main()


if __name__ == "__main__":
    main()
