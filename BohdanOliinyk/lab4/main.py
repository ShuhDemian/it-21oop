import random


def generate_number() -> int:
    return random.randint(1, 99)


def get_user_guess() -> int:
    guess = int(input("Ваше число: "))
    if guess < 1 or guess > 99:
        print("Ваше число за межами діапазону, спробуйте ще раз!")
        return get_user_guess()
    return guess


def check_guess(guess: int, target: int) -> bool:
    if guess < target:
        print("Більше!")
    elif guess > target:
        print("Менше!")
    else:
        return True
    return False


def main():
    target = generate_number()
    attempts = 0
    print("Гра вгадай число, ведіть число від 1 до 99!")

    while True:
        guess = get_user_guess()

        if check_guess(guess=guess, target=target):
            break

        attempts += 1

    print(f"Ви вгадали число {target} за {attempts} спроб(и)!")


if __name__ == "__main__":
    main()
