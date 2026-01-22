# Queue Management System

queue = []

while True:
    print("\n--- Queue Menu ---")
    print("1. Add to Queue")
    print("2. Serve Next")
    print("3. View Queue")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        person_name = input("Enter person name: ")
        queue.append(person_name)
        print("Person added to queue.")

    elif choice == "2":
        if not queue:
            print("Queue is empty.")
        else:
            served = queue.pop(0)
            print("Serving:", served)

    elif choice == "3":
        if not queue:
            print("Queue is empty.")
        else:
            print("Current Queue:")
            for person in queue:
                print("-", person)

    elif choice == "4":
        print("Exiting system...")
        break

    else:
        print("Invalid choice. Try again.")
