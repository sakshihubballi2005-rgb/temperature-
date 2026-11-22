import sys

def get_scores():
    # Command-line arguments are used if given (handy for Jenkins), else ask the user
    if len(sys.argv) > 1:
        return [float(x) for x in sys.argv[1:]]
    return [float(x) for x in input("Enter scores separated by space: ").split()]

def main():
    scores = get_scores()
    if not scores:
        print("No scores entered.")
        return
    total = sum(scores)
    print("Scores :", scores)
    print("Sum    :", total)
    print("Average:", total / len(scores))

if __name__ == "__main__":
    main()