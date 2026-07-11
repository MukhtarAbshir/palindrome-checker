def is_palindrome(text):
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned += char.lower()

    reversed_text = cleaned [::-1]
    return cleaned == reversed_text


def main():
    while True:
        text = input("\nEnter a word or sentence (ama 'Quit' to exit)").strip()
        if text.lower() == "Quit":
            print(f"Goodbye!")
            break
        elif text.lower() == "":
            print(f"Please enter something")
        else:
            result = is_palindrome(text)
            if result:
                print(f"'{text}' IS palindrome!")
            else:
                print(f"'{text}' is NOT palindrome.")

main()