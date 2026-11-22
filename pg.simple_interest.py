import sys

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def main():
    # Command-line arguments are used if given (handy for Jenkins), else ask the user
    if len(sys.argv) == 4:
        principal, rate, time = map(float, sys.argv[1:4])
    else:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (%): "))
        time = float(input("Enter time (in years): "))

    si = calculate_simple_interest(principal, rate, time)
    print(f"Simple Interest = {si}")

if __name__ == "__main__":
    main()

