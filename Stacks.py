# Initialize an empty stack and flags for stack creation and stack name
custom_stack = []
is_stack_created = False
custom_stack_name = None

# Function to create a stack
def create_stack():
    global is_stack_created, custom_stack_name
    # Check if the stack has not been created yet
    if not is_stack_created:
        custom_stack_name = input("Input a name for your stack: ")
        is_stack_created = True  # Set the flag to indicate stack creation
        print("Stack created!")
    else:
        print("You have already created a stack!")

# Function to append an element to the stack
def append_element():
    global is_stack_created
    # Check if the stack has been created
    if not is_stack_created:
        print("Create a stack first before adding elements!")
    else:
        element = input("Enter an element to add: ")
        custom_stack.append(element)  # Add the element to the stack
        print(f"{element} added to the stack.")

# Function to remove an element from the stack
def remove_element():
    global is_stack_created
    # Check if the stack has been created and is not empty
    if not is_stack_created:
        print("Create a stack first before removing elements!")
    elif custom_stack:
        element = custom_stack.pop()  # Remove and retrieve the top element from the stack
        print(f"Removed: {element}")
    else:
        print("The stack is empty.")

# Function to peek at the top element of the stack
def peek_element():
    global is_stack_created
    # Check if the stack has been created and is not empty
    if not is_stack_created:
        print("Create a stack first before peeking!")
    elif custom_stack:
        print(f"Top element: {custom_stack[-1]}")
    else:
        print("The stack is empty.")

# Function to display the elements in the stack
def show_stack():
    global is_stack_created
    # Check if the stack has been created and is not empty
    if not is_stack_created:
        print("Create a stack first before displaying elements!")
    elif custom_stack:
        print("Stack content:", custom_stack)
    else:
        print("The stack is empty.")

# Main loop for stack operations
while True:
    print("\nChoose a stack operation:")
    print("[C] - Create Stack")
    print("[A] - Append element to Stack")
    print("[D] - Remove element from Stack")
    print("[P] - Peek the top element of Stack")
    print("[S] - Show the Stack Element")
    print("[Q] - Quit")

    choice = input("Enter your choice: ").upper()

    # Perform operations based on user's choice
    if choice == 'C':
        create_stack()
    elif choice == 'A':
        append_element()
    elif choice == 'D':
        remove_element()
    elif choice == 'P':
        peek_element()
    elif choice == 'S':
        show_stack()
    elif choice == 'Q':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose from the options.")

