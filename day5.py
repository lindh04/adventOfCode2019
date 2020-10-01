from intcodeComputer import IntcodeComputer


def part1(inData: str):
    comp = IntcodeComputer(inData, separatorIfString=",")()


def part2(inData: str):
    pass


if __name__ == "__main__":
    with open("in.txt") as f:
        inData = f.read()

    part1(inData)
