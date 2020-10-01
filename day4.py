def checkPasswordPart1(password) -> bool:
    if len(str(password)) != 6 or any(str(password)[i] > str(password)[i+1] for i in range(5)):
        return False
    groups = [str(password).count(char) for char in set(str(password))]
    if any(x >= 2 for x in groups):
        return True
    else:
        return False


def part1(inData):
    count = 0
    for x in range(382345, 843167):
        if checkPasswordPart1(x):
            count += 1
    print(count)


def checkPasswordPart2(password) -> bool:
    if len(str(password)) != 6 or any(str(password)[i] > str(password)[i+1] for i in range(5)):
        return False
    groups = [str(password).count(char) for char in set(str(password))]
    if any(x == 2 for x in groups):
        return True
    else:
        return False


def part2(inData):
    count = 0
    for x in range(382345, 843167):
        if type(checkPasswordPart2(x)) == int:
            print(checkPasswordPart2(x))
        if checkPasswordPart2(x):
            count += 1
    print(count)


if __name__ == "__main__":
    with open("in.txt") as f:
        inData = f.read()

    print("\n\nPart1:")
    part1(inData)

    print("\n\nPart1:")
    part2(inData)
    print("\n\n")
