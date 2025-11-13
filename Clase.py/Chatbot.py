import random

while True:
    start = input("Do you want to generate random numbers? (yes/no): ").strip().lower()
    if start == "yes":
        # Generate a random integer between 1 and 9 (inclusive)
        random_int = random.randint(1, 9)
        print(f"Random integer: {random_int}")

        # Generate a random floating-point number between 0 and 1
        random_float = random.random()
        print(f"Random float: {round(random_float, 1)}")
    elif start == "no":
        print("Exiting program.")
        break
    else:
        print("Please enter 'yes' or 'no'.")
