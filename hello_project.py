def get_name():
    name = input("Please enter your name: ").strip()

    if name == "":
        return "friend"

    return name


def greet_user(name):
    print(f"Hello, {name}!")
    print(f"Your name has {len(name)} characters.")

    if len(name) <= 3:
        print("That is a short name.")
    elif len(name) >= 8:
        print("That is a long name.")
    else:
        print("That is a medium-length name.")

    print("This script is running on the remote Ubuntu server.")
    print("Python project file is working correctly.")


def main():
    name = get_name()
    greet_user(name)


if __name__ == "__main__":
    main()


