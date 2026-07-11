def is_palindrome(text):
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned += char.lower()

    reversed_text = cleaned [::-1]
    return cleaned == reversed_text


def main():
    while True:
        text = input("\nGali erey ama jumlad (ama 'Kabax' si aad ubaxdo)").strip()
        if text.lower() == "Kabax":
            print(f"Macasalaama!")
            break
        elif text.lower() == "":
            print(f"Wax qor saaxiib")
        else:
            result = is_palindrome(text)
            if result:
                print(f"'{text}' Waa palindrome!")
            else:
                print(f"'{text}' Maahan palindrome")

main()