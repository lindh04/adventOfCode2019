from intcodeComputer import IntcodeComputer


def part1(inData: str):
    comp = IntcodeComputer(inData, separatorIfString=",")(inputList=[1])


def part2(inData: str):
    comp = IntcodeComputer(inData, separatorIfString=",")(inputList=[5])


if __name__ == "__main__":
    with open("in.txt") as f:
        inData = f.read()

    print("\n\nPart1:")
    part1(inData)

    print("\n\nPart1:")
    part2(inData)
    print("\n\n")
