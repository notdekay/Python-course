import random

def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    print("Guess my number (1-100)!")
    while True:
        try:
            guess = int(input("> "))
            attempts += 1       
            if guess == secret:
                print(f"Correct! Attempts: {attempts}")
                break
            elif guess < secret:
                print("Higher")
            else:
                print("Lower")           
        except ValueError:
            print("Enter a number")

def main():
    while True:
        play_game()
        play_again = input("\nPlay again? (y/n): ").lower().strip()
        if play_again not in ['y' , 'yes']:
            print("Thanks for playing!")
            break
        print("\n" + "="*30 + "\n")
if __name__ == "__main__":
    main()