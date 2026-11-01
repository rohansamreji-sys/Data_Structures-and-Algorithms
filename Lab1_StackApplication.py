# Set the maximum number of pages the stack can store
MAX_SIZE = 5

# Created an empty stack
stack = []

# Set top to -1 because the stack is initially empty
top = -1


# Function to visit a new webpage
def visit_page():
    global top

    # To Check if the stack is full
    if top == MAX_SIZE - 1:
        print("Stack Overflow! History is full.")
        return

    # Take the webpage name from the user
    page = input("Enter webpage: ")

    # Add the webpage to the top of the stack
    stack.append(page)

    # Move top one position up
    top += 1

    # Display the visited page
    print("Visited:", page)


# Function to go back to the previous webpage
def go_back():
    global top

    # Check if the stack is empty
    if top == -1:
        print("Stack Underflow! No previous page.")
        return

    # Remove and display the top webpage
    print("Removed:", stack.pop())

    # Move top one position down
    top -= 1


# Function to display the current webpage
def current_page():

    # Check if there is no webpage in the stack
    if top == -1:
        print("No page is currently open.")

    # Display the top webpage without removing it
    else:
        print("Current Page:", stack[top])


# Function to display all visited webpages
def display_history():

    # Check if the stack is empty
    if top == -1:
        print("History is empty.")
        return

    # Display the history heading
    print("Browser History:")

    # Display pages from top to bottom
    for i in range(top, -1, -1):
        print(stack[i])


# Function to clear the complete browser history
def clear_history():
    global top

    # Remove all pages from the stack
    stack.clear()

    # Reset top because the stack is now empty
    top = -1

    # Display confirmation
    print("History cleared.")


# Keep showing the menu until the user chooses Exit
while True:

    # Display the available options
    print("\n1. Visit Page")
    print("2. Go Back")
    print("3. Current Page")
    print("4. Display History")
    print("5. Clear History")
    print("6. Exit")

    # Ask the user to select an option
    choice = input("Enter choice: ")

    # Option 1: Visit a webpage
    if choice == "1":
        visit_page()

    # Option 2: Go back to the previous webpage
    elif choice == "2":
        go_back()

    # Option 3: Display the current webpage
    elif choice == "3":
        current_page()

    # Option 4: Display browser history
    elif choice == "4":
        display_history()

    # Option 5: Clear the browser history
    elif choice == "5":
        clear_history()

    # Option 6: Exit the program
    elif choice == "6":
        print("Exiting...")
        break

    # Handle an invalid menu choice
    else:
        print("Invalid choice.")
