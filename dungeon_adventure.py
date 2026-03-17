import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input() 
        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        # TODO: Return the dictionary
        user_name = input(str(f"Hello hero, what is your name? "))
        user = {
            'name': user_name,
            'health': 10,
            'inventory': []
                }
        return user
        
        

    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        # TODO: Return the dictionary
        treasures = {
            "gold coin": 5,
            "ruby": 10,
            "ancient scroll": 7,
            "emerald": 9,
            "silver ring": 4,
            "slightly wonky sword": 2,
            "picture of a painter painting a picture of a differet painter": 4,
            "rock that looks like it might be worth something": 0,
            "signed autobiography of famous dungeon raider": 1
        }
        return treasures

    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TODO: Print the room number and the 4 menu options listed above
        print(f"You are in room {room_number}. What would you like to do?\n1. Search for treasure \n2. Move to the next room \n3. Check health and inventory.\n4. Quit")
        return 
        


    def search_room(player, treasures):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"]) - check
        # TODO: Write an if/else to handle treasure vs trap outcomes-
        # TODO: Update player dictionary accordingly
        # TODO: Print messages describing what happened
        search = random.choice(["treasure", "trap"])
        if search == "treasure":
            item = random.choice(list(treasures.keys()))
            player["inventory"].append(item)
            print(f"You for a {item}!")
        else: 
            player["health"] -= 2
            print("You hit a trap! You lose 2 health.")
        print(f"Your current health is {player['health']}")







    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health
        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”
        print(f"Your health is {'health'}")
        if player["inventory"]  >= 1:
             print(f"Your inventory is contains: ",{['inventory']})
        else:
             print("You have nothing currently in your inventory.")

    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        # TODO: Print final health, items, and total value
        # TODO: End with a message like "Game Over! Thanks for playing."
        total_value = sum(treasures[item] for item in player["inventory"] if item in treasures)
        print("\n--- Game Summary ---")
        print(f"Final Health: {player['health']}")
        if player["inventory"]:
            print("Collected items:", ", ".join(player["inventory"]))
        else:
            print("No treasures collected.")
        print(f"Total Score (Treasure Value): {total_value}")
        print("\nGame Over! Thanks for playing, adventurer!")

    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        # TODO: Inside each room, prompt player choice using input()
        # TODO: Use if/elif to handle each choice (1–4)
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored
        for room in range(1,6):
            while True:
                display_options(room)
                choice = int(input("Enter your choice: 1-4: "))
                if choice == 1:
                    search_room(player, treasures)
                    if player['health'] < 1:
                        print(f"You died {player['name']}... you will be greatly missed.")
                        end_game(player, treasures)
                        return
                elif choice == 2:
                    if room <= 4:
                        print(f"The floor creaks as you move as you slowly move onto the next room. {room+1}")
                        room += 1 
                    else:
                        print(f"You have defeated the dungeon {player['name']}.\n You will always be revered.")
                        break
                elif choice == 3: 
                    check_status(player)
                elif choice == 4:
                    print(f"{player['name']}, you shall henceforth be known as a coward. To you, I bid ado.")
                    end_game(player, treasures)
                    return
                else:
                    print("You really need to only choose 1 - 4.")

        end_game(player,treasures)
    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
