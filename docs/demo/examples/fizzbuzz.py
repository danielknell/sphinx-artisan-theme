"""
I can haz job plz?
"""


def main() -> None:
    """
    Entry point
    """

    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        elif i % 3 == 0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")

        else:
            print(str(i))


if __name__ == "__main__":
    main()
