# Hardware Management Application

# Database to store hardware information
hardware_db = {}


def display_menu():
    print("\nCapstone Program Menu Options:")
    print("1. Display Hardware Data")
    print("2. Add Hardware Data")
    print("3. Update Hardware Data")
    print("4. Delete Hardware Data")
    print("5. Exit Program")


def display_hardware_data():
    if not hardware_db:
        print("Notification: Data does not exist.")
        return
    print("\nDisplay Data Menu:")
    print("1. Display All Data")
    print("2. Search by Primary Key")
    print("3. Return to Main Menu")
    option = input("Choose an option: ")

    if option == '1':
        # Display all data
        print("\nAll Hardware Data:")
        for key, details in hardware_db.items():
            print(f"{key}: {details}")
    elif option == '2':
        # Search by primary key
        primary_key = input("Enter the primary key to search: ")
        if primary_key in hardware_db:
            print(f"\nHardware Data for {primary_key}: {hardware_db[primary_key]}")
        else:
            print("Notification: Data does not exist.")
    elif option == '3':
        return
    else:
        print("Notification: The option you entered is not valid.")


def add_hardware_data():
    print("\nAdd Data Menu:")
    primary_key = input("Enter primary key for new hardware: ")
    if primary_key in hardware_db:
        print("Notification: Data already exists.")
        return

    # Collect other data
    hardware_type = input("Enter hardware type: ")
    hardware_brand = input("Enter hardware brand: ")
    hardware_db[primary_key] = {'type': hardware_type, 'brand': hardware_brand}
    print("Notification: Data successfully saved.")


def update_hardware_data():
    print("\nEdit Data Menu:")
    primary_key = input("Enter the primary key of the hardware to update: ")

    if primary_key not in hardware_db:
        print("Notification: The data you are looking for does not exist.")
        return

    # Display current data
    print(f"\nCurrent Data for {primary_key}: {hardware_db[primary_key]}")
    confirm = input("Do you want to continue with the update? (yes/no): ")
    if confirm.lower() != 'yes':
        return

    # Choose field to update
    field = input("Enter the field to update (type/brand): ")
    if field not in hardware_db[primary_key]:
        print("Notification: Invalid field.")
        return

    new_value = input(f"Enter new value for {field}: ")
    hardware_db[primary_key][field] = new_value
    print("Notification: Data successfully updated.")


def delete_hardware_data():
    print("\nDelete Data Menu:")
    primary_key = input("Enter the primary key of the hardware to delete: ")

    if primary_key not in hardware_db:
        print("Notification: The data you are looking for does not exist.")
        return

    confirm = input("Do you want to delete this data? (yes/no): ")
    if confirm.lower() == 'yes':
        del hardware_db[primary_key]
        print("Notification: Data successfully deleted.")
    else:
        print("Deletion canceled.")


def main():
    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            display_hardware_data()
        elif choice == '2':
            add_hardware_data()
        elif choice == '3':
            update_hardware_data()
        elif choice == '4':
            delete_hardware_data()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Notification: The option you entered is not valid.")


# Run the main program
if __name__ == "__main__":
    main()
