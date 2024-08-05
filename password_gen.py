import random
import string


def generate_password(totalchars, inc_upper=True, inc_digits=True, inc_special=True):
    # init char sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if inc_upper else ""
    digits = string.digits if inc_digits else ""
    special = string.punctuation if inc_special else ""

    # combine char sets
    allChars = lower + upper + digits + special

    # return user password
    user_password = "".join(random.choice(allChars) for i in range(totalchars))
    return user_password


def main():
    totalchars = int(input("Total Characters: "))
    inc_upper = input("Include Uppercase?(y/n): ").lower() == "y"
    inc_digits = input("Include Digits? (y/n): ").lower() == "y"
    inc_special = input("Include Special Characters? (y/n): ").lower() == "y"

    # print password
    try:
        user_password = generate_password(
            totalchars, inc_upper, inc_digits, inc_special
        )
        print("Your Unique Password: " + user_password)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
