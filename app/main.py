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

def path_valid(path):
    if os.path.isfile(path) or os.path.isdir(path):
        return True
    
    return False

def go_up_one_level(path):
    parts = path.split('/')
    return ''.join(parts[:-1])

def main():
    # Constants
    COMMANDS = ["exit", "echo", "type", "pwd"]
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
    # Pwd command
    elif cmd == "pwd":
        print(os.getcwd())
    # Cd command
    elif cmd == "cd":
        # Absolute path
        if cmd_arg.startswith('/'):
            if path_valid(cmd_arg):
                os.chdir(cmd_arg)
            else:
                print(f"cd: {cmd_arg}: No such file or directory")
        elif cmd_arg.startswith('.'):
            new_dir = os.getcwd()
            # Iterate each part between slashes
            parts = cmd_arg.split('/')
            for part in parts:
                if part == ".":
                    continue
                elif part == "..":
                    new_dir = go_up_one_level(new_dir)
                else:
                    new_dir = os.path.join(new_dir, part)
            
            # Check if path is valid
            if path_valid(cmd_arg):
                os.chdir(new_dir)

        elif cmd_arg.startswith('~'):
            pass
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
