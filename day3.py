def addToCoords(wirePath: list):
    coords = []
    x, y = 0, 0
    for v in wirePath:
        if v[0] == "U":
            y += 1
            y2 = y + v[1]
            for i in range(y, y2):
                coords.append((x, i))
            y = int(y2) - 1
        if v[0] == "D":
            y2 = y - v[1]
            for i in reversed(range(y2, y)):
                coords.append((x, i))
            y = int(y2)
        if v[0] == "R":
            x += 1
            x2 = x + v[1]
            for i in range(x, x2):
                coords.append((i, y))
            x = int(x2) - 1
        if v[0] == "L":
            x
            x2 = x - v[1]
            for i in reversed(range(x2, x)):
                coords.append((i, y))
                x = int(x2)
        return coords


def findCrossing(wireCoords1, wireCoords2, returnClosest=False):
    crossing = list(set(wireCoords1).intersection(set(wireCoords2)))

    if returnClosest:
        absCoords = [(abs(x), abs(y)) for (x, y) in crossing]
        distance = [x + y for (x, y) in absCoords]
        distance.sort()
        return distance[0]

    else:
        return crossing


def part1(inData):
    wire1, wire2 = inData.split("\n")
    wire1 = [[x[0], int(x[1:])] for x in "".join(wire1).split(",")]
    wire2 = [[x[0], int(x[1:])] for x in "".join(wire2).split(",")]

    coords1 = addToCoords(wire1)
    coords2 = addToCoords(wire2)

    print(findCrossing(coords1, coords2, returnClosest=True))


def part2(inData):
    wire1, wire2 = inData.split("\n")
    wire1 = [[x[0], int(x[1:])] for x in "".join(wire1).split(",")]
    wire2 = [[x[0], int(x[1:])] for x in "".join(wire2).split(",")]

    coords1 = addToCoords(wire1)
    coords2 = addToCoords(wire2)

    crossing = findCrossing(coords1, coords2)

    steps = []

    for coord in crossing:
        index1 = coords1.index(coord) + 1
        index2 = coords2.index(coord) + 1
        steps.append(index1 + index2)

    print(sorted(steps)[0])


if __name__ == "__main__":
    with open("in.txt") as f:
        inData = f.read()

    print("\n\nPart1:")
    part1(inData)

    print("\n\nPart1:")
    part2(inData)
    print("\n\n")
