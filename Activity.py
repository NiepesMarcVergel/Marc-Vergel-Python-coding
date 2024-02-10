# Function to convert tuple to list and vice versa
def convert_tuple_to_list_and_back(input_tuple):
    # Here we convert tuple to a list
    input_list = list(input_tuple)
    
    # An error once occured so I just then ask the user if they want to add elements
    add_more = input("Do you want to add more elements? (yes/no): ").lower()
    
    # Continue adding elements until the user says no that shall result in the final list or simply called the tuple
    while add_more == 'yes':
        new_element = input("Enter the new element: ")
        input_list.append(new_element)
        add_more = input("Do you want to add more elements? (yes/no): ").lower()
    
    # Making the  list back to a tuple
    return tuple(input_list)

# Here the user will enter elements separated by commas
user_input = input("Enter elements separated by commas: ")

# Split the input string by commas and strip any extra spaces (a code that I have searched in the web)
elements = [elem.strip() for elem in user_input.split(',')]

# This is the tuple from the items or elements inputed
user_tuple = tuple(elements)

# Here is where it convert tuple to list that shall allow user to add more elements
updated_tuple = convert_tuple_to_list_and_back(user_tuple)

# Print the updated tuple T-T
print("Updated Tuple:", updated_tuple)