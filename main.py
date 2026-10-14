devices = []
choice = ""
id_counter = 1

while choice != "q":
    choice = input(
        "\nWelcome to TechVault!\n"
        "Enter 'a' to add a device.\n"
        "Enter 'l' to list devices.\n"
        "Enter 'd' to delete a device.\n"
        "Enter 'q' to quit.\n"
        "Your choice: "
    ).lower()

    if choice == "a":
        device_name = input("Device name: ")
        brand = input("Brand: ")
        model = input("Model: ")

        device = {
            "id": f"TV-{id_counter:03}",
            "name": device_name,
            "brand": brand,
            "model": model
        }

        devices.append(device)
        id_counter += 1

        print("Device added successfully!")

    elif choice == "l":
        if len(devices) == 0:
            print("No devices registered yet.")
        else:
            for number, device in enumerate(devices, start=1):
                print(f"{number}. Inventory ID: {device['id']}")
                print(f"   Device: {device['name']}")
                print(f"   Brand: {device['brand']}")
                print(f"   Model: {device['model']}")
                print()

    elif choice == "d":
        print("Device deletion is currently under development.")

    elif choice == "q":
        print("Shutting down TechVault...")

    else:
        print("Invalid choice! Please try again.")
