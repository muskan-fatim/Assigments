import random

def main():
 Secert = random.randint(1,99)
 guess = int(input("Enter your guess:"))
 try:
    while Secert != guess:
         print("you guess the wrong number")
         if Secert > guess:
            print("your guess is too low")
         elif Secert < guess:
            print("your guess is to high")
         print() # Print an empty line to tidy up the console for new guesses
         guess: int = int(input("Enter a new guess: "))  # Get a new guess from the user
 
 except ValueError:
    print("Please enter you guess")
 print("Congrats! The number was: " + str(Secert))
    
if __name__ == "__main__":
   main()
