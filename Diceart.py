import random

rolling = True
dice_art = {1: ("┌───────────┐",
                "│           │",
                "│     ●     │",
                "│           │",
                "└───────────┘"),
            2: ("┌───────────┐",
                "│  ●        │",
                "│           │",
                "│        ●  │",
                "└───────────┘"),
            3: ("┌───────────┐",
                "│  ●        │",
                "│     ●     │",
                "│        ●  │",
                "└───────────┘"),
            4: ("┌───────────┐",
                "│  ●     ●  │",
                "│           │",
                "│  ●     ●  │",
                "└───────────┘"),
            5: ("┌───────────┐",
                "│  ●     ●  │",
                "│     ●     │",
                "│  ●     ●  │",
                "└───────────┘"),
            6: ("┌───────────┐",
                "│  ●     ●  │",
                "│  ●     ●  │",
                "│  ●     ●  │",
                "└───────────┘")
            }

while rolling:
    print("---------------------------")
    dice = []
    total = 0
    num_of_dice = int(input("How many dice?: "))

    for die in range(num_of_dice):
        dice.append(random.randint(1,6))

    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()

    for die in dice:
        total +=die

    print(f"total: {total}")
    if not input("Do you want to roll again?(y/n)").lower() == "y":
        rolling = False

print("---------------------------")
print("Bye bye!")
