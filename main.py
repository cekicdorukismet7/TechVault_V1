devices = []
choice = ""
id_counter = 1

while choice != "q":
    choice = input(
        "\nWelcome to TechVault!\n"
        "Enter 'a' to add a device.\n"
        "Enter 'l' to list devices.\n"
        "Enter 'd' to delete a device.\n"
        "Enter 's' to search a device.\n"
        "Enter 'q' to quit.\n"
        "Your choice: "
    ).lower().strip()

  
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
        if len(devices) == 0:
            print("No devices available to delete.")
        else:
            device_delete_id = input(
                "Enter the Inventory ID to delete: "
            ).strip().upper()

            device_found = False

            for device in devices:
                if device_delete_id == device["id"]:
                    devices.remove(device)
                    device_found = True
                    print("Device deleted successfully!")
                    break

            if not device_found:
                print("Device not found!")

   
    elif choice == "s":
        if len(devices) == 0:
            print("No devices available to search.")
        else:
            search_id = input(
                "Enter the Inventory ID to search for: "
            ).strip().upper()

            device_found = False

            for device in devices:
                if search_id == device["id"]:
                    print("\nDevice found!")
                    print(f"Inventory ID: {device['id']}")
                    print(f"Device: {device['name']}")
                    print(f"Brand: {device['brand']}")
                    print(f"Model: {device['model']}")

                    device_found = True
                    break

            if not device_found:
                print("Device not found!")

  
    elif choice == "q":
        print("Shutting down TechVault...")

    
    else:
        print("Invalid choice! Please try again.")
