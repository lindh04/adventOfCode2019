from typing import Tuple


class IntcodeComputer:
    def __init__(self, intcode, separatorIfString=False) -> None:
        if separatorIfString:
            self.intcode = list(
                map(int, intcode.split(separatorIfString)))
        else:
            self.intcode = intcode

    def __call__(self, noun: int = None, verb: int = None):
        data = list(self.intcode)
        counter = 0

        if noun:
            data[1] = noun
        if verb:
            data[2] = verb

        for x in range(len(data)):
            if counter != 0:
                counter -= 1
                continue
            else:
                counter, done, data = self.runOpCode(data[x], x, data)
                if done:
                    return data[0]

    def runOpCode(self, opcode: int, index: int, dataList: list) -> Tuple[int, bool, list]:
        if opcode not in [1, 2, 3, 4, 5, 6, 7, 8]:
            ogOpcode = int(opcode)
            opcode = int(str(opcode)[-2:])
            modes = list(map(int, [i for i in str(ogOpcode)[:-2]]))
            if len(modes) != 3:
                for x in range(3 - len(modes)):
                    modes.insert(0, 0)
        else:
            modes = None
        return {
            1: self.code1,
            2: self.code2,
            3: self.code3,
            4: self.code4,
            5: self.code5,
            6: self.code6,
            7: self.code7,
            8: self.code8,
            99: self.code99,
        }.get(opcode)(index, dataList, modes)

    def findFromOutput(self, target: int, nounRange: range = range(0, 99), verbRange: range = range(0, 99)):
        for x in nounRange:
            for y in verbRange:
                if self.__call__(x, y) == target:
                    return x, y
        raise Exception("Unable to find correct values")

    def code1(self, i, dataList, modes) -> Tuple[int, bool, list]:
        data = list(dataList)
        if not modes:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        else:
            _, b, c = modes
            b = data[i+2] if b != 0 else data[data[i+2]]
            c = data[i+1] if c != 0 else data[data[i+1]]
            data[data[i+3]] = b + c
        return 3, False, data

    def code2(self, i, dataList, modes) -> Tuple[int, bool, list]:
        data = list(dataList)
        if not modes:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        else:
            _, b, c = modes
            b = data[i+2] if b != 0 else data[data[i+2]]
            c = data[i+1] if c != 0 else data[data[i+1]]
            data[data[i+3]] = b * c
        return 3, False, data

    def code3(self, i, dataList, modes) -> Tuple[int, bool, list]:
        data = list(dataList)
        if not modes:
            data[data[i+1]] = int(input("Opcode 3 (Requesting Input): "))
        else:
            raise Exception("Modes given to opcode 3")
        return 1, False, data

    def code4(self, i, dataList, modes) -> Tuple[int, bool, list]:
        data = list(dataList)
        if not modes:
            print("Opcode 4 (Sending Output): ", data[data[i+1]])
        else:
            _, _, c = modes
            if c == 0:
                print("Opcode 4 (Sending Output): ", data[data[i+1]])
            else:
                print("Opcode 4 (Sending Output): ", data[i+1])
        return 1, False, data

    def code5(self, i, dataList, modes) -> Tuple[int, bool, list]:
        data = list(dataList)
        if not modes:
            if data[data[i+1]] != 0:
                counter = data[data[i+2]] - i - 1
        else:
            _, b, c = modes
            b = data[i+2] if b != 0 else data[data[i+2]]
            c = data[i+1] if c != 0 else data[data[i+1]]

            if c != 0:
                counter = b - i

        return counter, False, data

    def code6(self, i, dataList, modes) -> Tuple[int, bool, list]:
        data = list(dataList)
        if not modes:
            if data[data[i+1]] == 0:
                counter = data[data[i+2]] - i - 1
            else:
                counter = 2
        else:
            _, b, c = modes
            b = data[i+2] if b != 0 else data[data[i+2]]
            c = data[i+1] if c != 0 else data[data[i+1]]

            if c == 0:
                counter = b - i
            else:
                counter = 2

        return counter, False, data

    def code7(self, i, dataList, modes) -> Tuple[int, bool, list]:
        data = list(dataList)
        if not modes:
            if data[data[i+1]] < data[data[i+2]]:
                data[data[i+3]] = 1
            else:
                data[data[i+3]] = 0
        else:
            _, b, c = modes
            b = data[i+2] if b != 0 else data[data[i+2]]
            c = data[i+1] if c != 0 else data[data[i+1]]

            if c < b:
                data[data[i+3]] = 1
            else:
                data[data[i+3]] = 0

        return 3, False, data

    def code8(self, i, dataList, modes) -> Tuple[int, bool, list]:
        data = list(dataList)
        if not modes:
            if data[data[i+1]] == data[data[i+2]]:
                data[data[i+3]] = 1
            else:
                data[data[i+3]] = 0
        else:
            _, b, c = modes
            b = data[i+2] if b != 0 else data[data[i+2]]
            c = data[i+1] if c != 0 else data[data[i+1]]

            if c == b:
                data[data[i+3]] = 1
            else:
                data[data[i+3]] = 0

        return 3, False, data

    def code99(self, i, dataList, modes) -> Tuple[int, bool, list]:
        data = list(dataList)
        return 0, True, data
