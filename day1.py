def part1(inData: str):
    print(sum(list(map(lambda x: (int(x) // 3) - 2, inData.split("\n")))))


def part2(inData: str):
    def calcCost(mass):
        ans = 0
        mass = mass//3 - 2

        while mass > 0:
            ans += mass
            mass = mass//3 - 2

        return ans

    print(sum(list(map(lambda x: calcCost(int(x)), inData.split("\n")))))


if __name__ == "__main__":
    with open("in.txt") as f:
        inData = f.read()

    part1(inData)
    part2(inData)
