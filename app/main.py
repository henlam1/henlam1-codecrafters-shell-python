import sys


def main():
    # Print shell prompt
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()

    # Handle missing commands
    sys.stdout.write(f"{command}: command not found\n")

    # Make shell recursively call itself
    main()


if __name__ == "__main__":
    main()
