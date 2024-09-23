# Imported Libraries.
import random

# These are the NPCs that will bid against you.
users = [
    'James', 'John', 'Peter', 'Oliver', 'Mikael', 'Marinette', 'Simon',
    'Phillip', 'Fiona', 'Martin', 'Stacy', 'Olivia'
]

# These are the items that the NPCs will offer to trade.
auction_items = {
    "Antique vase": 5000,
    "Vintage car": 30000,
    "Diamond necklace": 15000,
    "Rare painting": 20000,
    "Luxury watch": 10000,
    "Signed sports memorabilia": 2500,
    "Gold coins": 1200,
    "Estate jewelry": 8000,
    "Collectible stamps": 1500,
    "Classic guitar": 4000,
    "Exclusive artwork": 10000,
    "Fine wine collection": 5000,
    "Luxury handbag": 2500,
    "Rare book": 3000,
    "Sculpture": 7000,
    "Antique furniture": 6000,
    "Designer clothing": 1000,
    "Limited edition sneakers": 1200,
    "Historical artifact": 15000,
    "Rare comic book": 2000
}

# Choose a user and item randomly.
item = random.choice(list(auction_items.items()))
user = random.choice(users)

print(f"Auction item: {item[0]}.\nThe starting price is R{item[1]}!\n")

# NPC's initial bid.
new_price = item[1] + random.randint(100, 1000)
print(f"{user} bids R{new_price} for the {item[0]}.")


while True:
    try:
        query = input("Bid? (Y/N): ").lower()

        # If user agrees to bid.
        if query == "y" or query == "yes":
            name = input("What is your name?: ").title()  # Require name.

            # Loop until user enters a valid bid.
            while True:
                bid = int(input(f"How much would you like to bid? (Current bid is R{new_price}): "))

                # If the user bid is bigger than competitor.
                if bid > new_price:
                    print(f"{name} bids R{bid}!")

                    # NPC decides whether to continue bidding.
                    npc_decision = random.choice([True, False])
                    if npc_decision:
                        new_price = bid + random.randint(100, 1000)  # Competitor rebid.
                        user = random.choice(users)
                        print(f"{user} bids R{new_price} for the {item[0]}!")

                        # Ask user if they want to continue bidding.
                        continue_query = input("Continue bidding? (Y/N): ").lower()
                        if continue_query == "y" or continue_query == "yes":
                            continue  # Go back to the bid input loop.
                        elif continue_query == "n" or continue_query == "no":
                            print(f"{user} won this auction with the {item[0]} for R{new_price}!")
                            break  # Exit the bid input loop.
                        else:
                            print("Incorrect input. Please enter 'Y' or 'N'.")
                            continue
                    else:
                        print(f"{name} won this auction with the {item[0]} for R{bid}!")
                        break  # Exit the bid input loop.
                else:
                    print(f"Cannot bid under or equal to R{new_price}! Please enter a higher bid.")
                    continue  # Prompt for the bid again.

            break  # Exit the main auction loop after the auction is over.

        elif query == "n" or query == "no":
            print(f"{user} won this auction with the {item[0]} for R{new_price}!")
            break

        else:
            print("Incorrect input. Please enter 'Y' or 'N'.")

    except ValueError as ve:
        print(f"Error: Please enter a valid number. {ve}")
