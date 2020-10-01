from intcodeComputer import IntcodeComputer


def part1(inData: str):
    print(IntcodeComputer(inData, separatorIfString=",")(12, 2))


def part2(inData: str):
    comp = IntcodeComputer(inData, separatorIfString=",")
    noun, verb = comp.findFromOutput(19690720)
    print(100 * noun + verb)


if __name__ == "__main__":
    with open("in.txt") as f:
        inData = f.read()

    part1(inData)
    part2(inData)
