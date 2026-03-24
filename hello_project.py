def get_name():
    name = input("Please enter your name: ").strip()

    if name == "":
        return "friend"

    return name


def main():
    name = get_name()
    print(f"Hello, {name}!")
    print("This script is running on the remote Ubuntu server.")
    print("Python project file is working correctly.")


if __name__ == "__main__":
    main()
    