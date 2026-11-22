import sys

def is_palindrome(text):
    # keep only letters and digits, ignore case, spaces and punctuation
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    # Use a command-line argument if given (handy for Jenkins), else ask the user
    s = sys.argv[1] if len(sys.argv) > 1 else input("Enter a string: ")
    if is_palindrome(s):
        print(f"'{s}' is a palindrome")
    else:
        print(f"'{s}' is not a palindrome")