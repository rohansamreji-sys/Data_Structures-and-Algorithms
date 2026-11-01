# SmartCare Hospital OPD Token System
# Data Structure: Queue using Singly Linked List

class Node:
    # Create one patient node
    def __init__(self, token, name, age, department):
        self.token = token
        self.name = name
        self.age = age
        self.department = department
        self.next = None


# Start with an empty queue
front = None
rear = None
token_no = 101


# Add a patient to the rear
def enqueue():
    global front, rear, token_no

    name = input("Enter patient name: ").strip()

    if name == "":
        print("Patient name cannot be blank.")
        return

    try:
        age = int(input("Enter age: "))

        if age <= 0:
            print("Age must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid age.")
        return

    department = input("Enter department: ").strip()

    if department == "":
        print("Department cannot be blank.")
        return

    try:
        new_node = Node(token_no, name, age, department)
    except MemoryError:
        print("Queue Overflow - memory not available.")
        return

    if front is None:
        front = rear = new_node
    else:
        rear.next = new_node
        rear = new_node

    print("Token", token_no, "issued to", name)
    token_no += 1


# Remove the patient from the front
def dequeue():
    global front, rear

    if front is None:
        print("No patients waiting.")
        return

    patient = front
    front = front.next

    if front is None:
        rear = None

    print("Now calling Token", patient.token, "-", patient.name,
          "to", patient.department)


# Show the next patient without removing them
def peek():
    if front is None:
        print("No patients waiting.")
        return

    print("Next Patient:")
    print("Token:", front.token)
    print("Name:", front.name)
    print("Age:", front.age)
    print("Department:", front.department)


# Display all patients
def display():
    if front is None:
        print("No patients waiting.")
        return

    current = front
    count = 0

    print("\nWaiting List")

    while current is not None:
        print(current.token, "-", current.name, "-",
              current.age, "-", current.department)
        current = current.next
        count += 1

    print("Count =", count)


# Check whether queue is empty and show count
def is_empty_count():
    if front is None:
        print("Queue is empty.")
        print("Count = 0")
        return

    current = front
    count = 0

    while current is not None:
        count += 1
        current = current.next

    print("Queue is not empty.")
    print("Count =", count)


# Show estimated waiting time
def waiting_time():
    if front is None:
        print("No patients waiting.")
        return

    current = front
    count = 0

    print("\nEstimated Waiting Time")

    while current is not None:
        print("Token", current.token, "-", count * 7, "minutes")
        count += 1
        current = current.next


# Free all remaining nodes before exiting
def exit_program():
    global front, rear

    while front is not None:
        front = front.next

    rear = None
    print("All remaining nodes freed.")
    print("Program ended.")


# Main menu
while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Is Empty and Count")
    print("6. Estimated Waiting Time")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        enqueue()

    elif choice == "2":
        dequeue()

    elif choice == "3":
        peek()

    elif choice == "4":
        display()

    elif choice == "5":
        is_empty_count()

    elif choice == "6":
        waiting_time()

    elif choice == "7":
        exit_program()
        break

    else:
        print("Invalid choice.")
