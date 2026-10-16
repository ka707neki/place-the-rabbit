print("Welcome to Place the Rabbit!")

# Main game loop
while True:
    # Reset/Create the field (3x3 grid) at the start of each round
    field = [["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"]]

    print("\nCurrent Field:")
    print(f"{' '.join(field[0])}\n{' '.join(field[1])}\n{' '.join(field[2])}")

    user_input = (
        input(
            "\nWhere should the rabbit go? (RowCol e.g., 11, 32) or 'q' to quit: "
        )
        .strip()
        .lower()
    )

    # Check for exit command
    if user_input in ["q", "quit", "exit"]:
        print("Thanks for playing! Goodbye!")
        break

    # Validate input format (must be 2 digits)
    if len(user_input) != 2 or not user_input.isdigit():
        print("Invalid input! Please enter exactly two digits (e.g., 12).")
        continue

    row = int(user_input[0])
    column = int(user_input[1])

    # Validate range (1 to 3)
    if row < 1 or row > 3 or column < 1 or column > 3:
        print(
            f"Invalid position ({row},{column})! Please stay within the 3x3 field (1-3)."
        )
    else:
        # Place the rabbit (convert 1-based index to 0-based index)
        field[row - 1][column - 1] = "🐇"

        print("\nSuccess!")
        print(f"{' '.join(field[0])}\n{' '.join(field[1])}\n{' '.join(field[2])}")