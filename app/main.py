import sys

COMMANDS = ["exit", "echo", "type"]

def main():
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
        if cmd_arg in COMMANDS:
            print(f"{cmd_arg} is a shell builtin")
        else:
            print(f"{cmd_arg}: not found")
    # Handle missing commands
    else:
        sys.stdout.write(f"{cmd}: command not found\n")

    # Make shell recursively call itself
    main()


if __name__ == "__main__":
    main()
