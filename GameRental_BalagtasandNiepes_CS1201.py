#Balagtas, Michaella and Niepes, Marc Vergel
#CS-1201

game_library = {
    "Donkey Kong" : {"quantity": 3, "cost": 2},
    "Super Mario Bros" : {"quantity": 5, "cost": 3},
    "Tetris" : {"quantity": 2 , "cost":1},
}

user_accounts = {}

admin_username = "admin"
admin_password = "adminpass"



# Functions to display available games with number and rental cost Main 1
def display_available_games():
    print(game_library)

# new user MAin 2
def register_user():
    print("Sign up")

    while True:
        try:
            username = input("Enter Username (or leave blank to go back): ")
            balance = 0
            points = 0
            if not username:
                main()
            if username in user_accounts:
                print("The username that you enter already exist. Please enter a new one.")
                continue
            while True:
                try: 
                    password = input("Enter password: ")
                    if len(password) < 8:
                        print("Password is not at least 8 characters")
                        continue
                    if len(password) > 8:
                        user_accounts[username] = {"password" : password, "balance" : balance, "points" : points}  
                        print("Sign Up successful")
                        main()
                    else:
                        print("Invalid input.")
                        continue 
                except ValueError as e:
                    print(e)
                    register_user()
        except ValueError as e:
            print(e)
            register_user()


def log_in(): #Gateway to main 3 :)
    while True:
        try:
            username = input("Enter username (or leave blank to go back): ")
            if not username:
                main()
            password = input("Enter password: ")
            if user_accounts.get(username) and user_accounts[username]['password'] == password:
                print("Login Successful")
                login_menu(username)
            else:
                print("Invalid account username or password")
        except ValueError as e:
            print(e)
            main()


def login_menu(username):
    while True:
     print("Logged in")
     print("1. Rent a Game")
     print("2. Return a Game")
     print("3. Top-up Account")
     print("4. Display Inventory")
     print("5. Redeem Free Rental Game")
     print("6. Check Points")
     print("7. Log out")

     userchoice = (input("Enter your choice: "))
    
     if userchoice == "1":
          rent_game(username)
     elif userchoice == "2":
          return_game(username)
     elif userchoice == "3":
          top_up_account(username)
     elif userchoice == "4":
          display_inventory(username)
     elif userchoice == "5":
          redeem_free_game_rental(username)
     elif userchoice == "6":
          check_points(username)
     elif userchoice == "7":
          main()
          return
     else:
         print("Invalid Input")

def admin_log_in(): #main 4
    admin_username_input = input("Enter admin username: ")
    admin_password_input = input("Enter admin password: ")

    if admin_username_input == admin_username and admin_password_input == admin_password:
        print("Admin login successful.")
        admin_login_menu()
    else:
        print("Incorrect admin username or password.")
        main()

def admin_login_menu():
    while True: 
        try:
            print("Welcome to Admin Control")
            print("1. Add Quantity")
            print("2. Increase Price")
            print("3. Go back to Main Menu")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                admin_add_quantity()
            if choice == 2:
                increase_price()
            if choice == 3:
                main()
            else:
                print("Invalid Input.")
        except ValueError as e:
            main()

#an exclusive control for admin to add quantity to each game has
def admin_add_quantity():
    def admin_add_quantity():
        print("Add Quantity to Games")
    for game, details in game_library.items():
        print(f"{game}: Quantity - {details['quantity']}")
    
    game_to_add = input("Enter the name of the game to add quantity (or leave blank to go back): ")
    if not game_to_add:
        admin_login_menu()
    
    try:
        quantity_to_add = int(input("Enter the quantity to add: "))
        if quantity_to_add <= 0:
            print("Quantity to add must be a positive integer.")
            admin_add_quantity()
        else:
            game_library[game_to_add]['quantity'] += quantity_to_add
            print(f"Quantity of '{game_to_add}' updated successfully! New quantity: {game_library[game_to_add]['quantity']}")
            admin_add_quantity()  # Option to add quantity to another game
    except ValueError:
        print("Invalid input. Please enter a valid quantity.")
        admin_add_quantity()

# a control exclusive to admin to add price rise to games
def increase_price():
    print("Increase Price of Games")
    for game, details in game_library.items():
        print(f"{game}: Cost - {details['cost']}")
    
    game_to_increase_price = input("Enter the name of the game to increase price (or leave blank to go back): ")
    if not game_to_increase_price:
        admin_login_menu()
    
    try:
        new_price = float(input("Enter the new price: "))
        if new_price <= 0:
            print("New price must be a positive number.")
            increase_price()
        else:
            game_library[game_to_increase_price]['cost'] = new_price
            print(f"Price of '{game_to_increase_price}' updated successfully! New price: {game_library[game_to_increase_price]['cost']}")
            increase_price()  # Option to increase price of another game
    except ValueError:
        print("Invalid input. Please enter a valid price.")
        increase_price()

# rent a game
def rent_game(username):
    print("Available Games:")
    for game, details in game_library.items():
        print(f"{game}: Quantity - {details['quantity']}, Cost - {details['cost']}")
    
    # Code to handle the process of renting a game
    gamename = input("Select Game (or leave blank to go back): ")
    if not gamename:
        login_menu(username)
    elif gamename not in game_library:
        print("Invalid game name. Please select a game from the list.")
        rent_game(username)
    elif game_library[gamename]['quantity'] <= 0:
        print("Sorry, this game is out of stock.")
        rent_game(username)
    else:
        print(f"Selected Game: {gamename}")
        print("1. Pay using Balance")
        print("2. Pay using points")
        pay_option = input("Choose how to pay: ")

        if pay_option == "1":
            if user_accounts[username]['balance'] < game_library[gamename]['cost']:
                print("Not enough balance to rent this game. Please top up your account.")
            else:
                user_accounts[username]['balance'] -= game_library[gamename]['cost']
                game_library[gamename]['quantity'] -= 1
                user_accounts[username]['points'] += 1
                print(f"Game '{gamename}' rented successfully! Remaining balance: {user_accounts[username]['balance']}, Points: {user_accounts[username]['points']}")
        elif pay_option == "2":
            if user_accounts[username]['points'] < game_library[gamename]['cost']:
                print("Not enough points to rent this game.")
            else:
                user_accounts[username]['points'] -= game_library[gamename]['cost']
                game_library[gamename]['quantity'] -= 1
                print(f"Game '{gamename}' rented successfully! Points deducted: {game_library[gamename]['cost']}")
        else:
            print("Invalid input.")
            rent_game(username)

# return a game function that will help user put back what they game they currently have 
def return_game(username):
    print("Return Game")
   
    for game, details in game_library.items():
        print(f"{game}: Quantity - {details['quantity']}")
    
    return_game_name = input("Enter the name of the game you want to return (or leave blank to go back): ")
    if not return_game_name:
        login_menu(username)
    elif return_game_name not in game_library:
        print("Invalid game name. Please select a game from the list.")
        return_game(username)
    else:
        return_quantity = int(input("Enter the quantity of the game to return: "))
        if return_quantity <= 0:
            print("Invalid quantity. Please enter a valid number.")
            return_game(username)
        elif return_quantity > game_library[return_game_name]['quantity']:
            print("You can't return more copies than you have rented.")
            return_game(username)
        else:
            game_library[return_game_name]['quantity'] += return_quantity
            print(f"Successfully returned {return_quantity} copy/copies of '{return_game_name}'.")
            login_menu(username)

#this is the top up code that will enable the user to add something in their balance.
def top_up_account(username):
    try:
        top_up_amount = float(input("Enter the amount you want to top up: "))
        if top_up_amount <= 0:
            print("Invalid amount. Please enter a positive number.")
            top_up_account(username)
        else:
            user_accounts[username]['balance'] += top_up_amount
            print(f"Successfully topped up ${top_up_amount}. New balance: ${user_accounts[username]['balance']}")
            login_menu(username)
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        top_up_account(username)
        
#just a display what the user possession function
def display_inventory(username):
    print(f"Inventory for user '{username}':")
    for game, details in game_library.items():
        if details['quantity'] > 0:
            print(f"{game}: Quantity - {details['quantity']}")
    login_menu(username)

#I forgot what should I put in here so...
def redeem_free_game_rental(username):

    print("Sorry but the Rent a Game has currently no free games to offer.")
    login_menu(username)

def check_points(username):

    points = user_accounts[username]['points']
    print(f"You have {points} points.")
    login_menu(username)

def main():
    while True:
       print("Welcome to the Game Rental System")
       print("1. Display Available Games")
       print("2. Register User")
       print("3. Log In")
       print("4. Admin Login")
       print("5. Exit")

       choice = input("Enter your choice: ")

       if choice == "1":
          display_available_games()
       elif choice == "2":
          register_user()
       elif choice == "3":
          log_in()
       elif choice == "4":
          admin_log_in()
       elif choice == "5":
          print("Exiting Game Rental System")
          break
       else:
         print("Invalid Input")

if __name__ == "__main__":
    main()