def main():
    while True:
        user_input = input("Enter your number: ")
        try:
            number = int(user_input)
        except ValueError:
            print("Please enter a valid integer.")
            continue  # prompt the user again if the input is not a valid integer

        result = number * 2
        print("Doubled value:", result)

        if result == 100 or result > 100 :
            print("Result is 100 or above to 100. Stopping the program.")
            break  # exit the loop if the condition is met

if __name__ == "__main__":
    main()
