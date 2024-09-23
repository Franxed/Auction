# Imported Libraries.

import random

# These are the npc's that will bid against you.
users = ['James',
         'John',
         'Peter',
         'Oliver',
         'John',
         'Mikael',
         'Marinette',
         'Simon',
         'Phillip',
         'Fiona',
         'Martin',
         'Stacy',
         'Olivia']

# These are the items that the npc's will offer to trade.

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

print(f"Auction item : {item[0]}. \nThe staring price is R{item[1]}!\n")

# User's bid.
new_price = item[1] + random.randint(100, 1000)
print(f"{user} bids R{new_price} for the {item[0]}.")

while True:
    try:
        query = input("Bid? (Y/N) : ").lower()

        # If user agrees to bid.
        if query == "y" or query == "yes":
            name = str(input("What is your name? : ")).title()               # Require name.
            bid = int(input(f"How many would you like to bid? : "))     # Require amount.

            # If the user bid is bigger than competitor.
            if bid > new_price:
                print(f"{name} bids {bid}!")
                new_price = new_price + random.randint(100, 1000)       # Competitor rebid. ('thinking')

                # If the competitor bid is bigger than user's bid, print it.
                if new_price > bid:
                    print(f"{user} bid R{new_price} for {item[0]}!")

                    new_query = str(input("Continue bid? (Y/N) : ")).lower()

                    if new_query == "y" or new_query == "yes":
                        new_bid = int(input(f"How many would you like to bid? : "))
                        print(f"{name} bids {new_bid}!.")

                        new_price = new_price + random.randint(100, 1000)  # Competitor rebid. ('thinking')
                        print(f"{user} bids R{new_price} for the {item[0]}.")

                        if new_price > new_bid:
                            print(f"{user} won this auction with the {item[0]} for R{new_price}!")
                            break

                        else:
                            print(f"Cannot bid under or equal to R{new_price}!")
                            continue

                    elif new_query == "n" or new_query == "no":
                        print(f"{user} won this auction with the {item[0]} for R{new_price}!")
                        break

                    else:
                        print("Incorrect input.")
                        continue

                else:
                    print(f"{name} won this auction with the {item[0]} for R{bid}!")
                    break
            elif bid < new_price:
                print(f"Cannot bid under or equal to R{new_price}!")
                continue

            else:
                print(f"{user} won this auction with the {item[0]} for R{new_price}!")

        elif query == "n" or query == "no":
            print(f"{user} won this auction with the {item[0]} for R{new_price}!")

        else:
            print("Incorrect input. Input either 'yes/y' or 'no/n'.")






    except ValueError as ve:
        print(f"Error : {ve}")
