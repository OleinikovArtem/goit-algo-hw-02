from collections import deque
import re


def is_palindrome(s):
    if len(s) == 0:
        return False

    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    d = deque(s)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


def main():
    test_strings = ["A man, a plan, a canal, Panama", "No lemon, no melon", "Hello, world!", 'else', '']
    results = {s: is_palindrome(s) for s in test_strings}

    # print result
    max_key_length = max(len(key) for key in results.keys())
    print('-' * (max_key_length + 17))
    print(f'{"Phrase":<{max_key_length}} | {"Is Palindrome"}')
    print('-' * (max_key_length + 17))

    for key, value in results.items():
        value_text = 'Yes' if value else 'No'
        print(f'{key:<{max_key_length}} | {value_text}')
    print('-' * (max_key_length + 17))


if __name__ == "__main__":
    main()
