def main():
    name = input("Please enter your name: ").strip()

    if name == "":
        name = "friend"

    print(f"Hello, {name}!")
    print("This script is running on the remote Ubuntu server.")
    print("Python project file is working correctly.")


if __name__ == "__main__":
    main()
    