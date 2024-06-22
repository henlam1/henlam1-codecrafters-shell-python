import sys


def main():
    # Print shell prompt
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    args = input().split()
    cmd = args[0]
    cmd_arg = ' '.join(args[1:])

    # Exit command
    if cmd == "exit":
        exit(cmd_arg)
    # Echo command
    elif cmd == "echo":
        print(cmd_arg)
    # Handle missing commands
    else:
        sys.stdout.write(f"{cmd}: command not found\n")

    # Make shell recursively call itself
    main()


if __name__ == "__main__":
    main()
