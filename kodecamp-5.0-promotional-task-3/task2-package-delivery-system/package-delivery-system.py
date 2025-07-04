# Task 2: Package Delivery System
# Goal: Track packages and manage their delivery status.
# Features:
# - Create a Package class with: id (use uuid.uuid4()), sender, recipient, status.
# - Store multiple packages in a list.
# - Use the 'json' module to save and load delivery data.
# - Use a separate module (delivery_utils.py) for file operations.
# Menu Options:
# - Register a package
# - Mark package as delivered
# - View all packages
# - Save/Load from file

import delivery_utils as utils
import uuid

class Package:
    def __init__(self, sender, recipient):
        self.id = str(uuid.uuid4()) # Generate a unique ID for each package
        self.sender = sender
        self.recipient = recipient
        self.status = 'Pending'

    def mark_as_delivered(self):
        self.status = 'Delivered'

    def to_list(self):
        return [self.id, self.sender, self.recipient, self.status]

    @classmethod
    def from_list(cls, data):
        return cls(data[1], data[2])

class PackageList:
    def __init__(self):
        self.packages = [Package.from_list(p) for p in utils.load_packages(filename='packages.json')] 
        
    def add_package(self, sender, recipient):
        self.packages.append(Package(sender, recipient))
        print(f"Package to '{recipient}' from '{sender}' added.")

    def mark_delivered(self, package_id):
        for package in self.packages:
            if package.id == package_id:
                package.mark_as_delivered()
                print(f"Package {package_id} marked as delivered.")
                return
        print(f"Package {package_id} not found.")
    def view_packages(self):
        count = 0
        if not self.packages:
            print("No packages available.")
            return
        for package in self.packages:
            count += 1
            print(f"{count}. ID: {package.id}, Sender: {package.sender}, Recipient: {package.recipient}, Status: {package.status}")
    def save_packages(self, filename='packages.json'):
        utils.save_packages(filename, [package.to_list() for package in self.packages])
        print("Packages saved to file.")

def main():
    package_list = PackageList()

    while True:
        print("\nPackage Delivery System")
        print("1. Register a package")
        print("2. Mark package as delivered")
        print("3. View all packages")
        print("4. Save & Exit")
        option = input("Choose an option: ")

        if option == '1':
            sender = input("Enter sender's name: ")
            recipient = input("Enter recipient's name: ")
            package_list.add_package(sender, recipient)

        elif option == '2':
            package_id = input("Enter package ID to mark as delivered: ")
            package_list.mark_delivered(package_id)

        elif option == '3':
            package_list.view_packages()

        elif option == '4':
            package_list.save_packages()
            break

        else:
            print("Invalid option. Please try again.")
            continue

if __name__ == "__main__":
    main()