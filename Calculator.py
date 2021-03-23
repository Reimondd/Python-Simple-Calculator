
import time


def main():
    print("Very cool calculator")
    N1 = float(input("\nEnter the first number: "))
    Calc = input("What calculation do you want to preform?: ")
    N2 = float(input("Enter the second number: "))
    if Calc == "+":
        print(N1 + N2)
        print("\n Resetting...")
        time.sleep(1)
        main()
    elif Calc == "-":
        print(N1 - N2)
        print("\nResetting...")
        time.sleep(1)
        main()
    elif Calc == "*":
        print(N1 * N2)
        print("\nResetting...")
        time.sleep(1)
        main()
    elif Calc == "/":
        try:
            print(N1 / N2)
            print("\n Resetting...")
            time.sleep(1)
        except ZeroDivisionError:
            print("\n U cannot divide by zero. Restarting!")
            time.sleep(1)
            main()
    else:
        print("Error, Would you like to restart...")
        time.sleep(1)
        restart = input("Type 'Yes/No': ").lower()
        if restart == "yes" or "y":
            print("Reset!")
            main()
        else:
            exit()
main()
