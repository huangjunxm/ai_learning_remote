def get_name():
    name = input("Please enter your name: ").strip()

    if name == "":
        return "friend"

    return name


def greet_user(name):
    print(f"Hello, {name}!")
    print("This script is running on the remote Ubuntu server.")
    print("Python project file is working correctly.")


def main():
    name = get_name()
    greet_user(name)


if __name__ == "__main__":
    main()
    