import os


def main():
    number = input("Please enter a number: ")
    while not number.isnumeric():
        print("Entered value is not numeric")
        number = input("Please enter a number: ")

    if not os.path.exists("total.txt"):
        open("total.txt", "w")

    with open("total.txt", "r") as file:
        line = file.readline()
        if not line:
            total = 0
        else:
            total = int(line)

    with open("total.txt", "w") as file:
        total += int(number)
        if total > 152:
            total -= 152
        print("Total number: " + str(total))
        file.write(str(total))


if __name__ == '__main__':
    main()
