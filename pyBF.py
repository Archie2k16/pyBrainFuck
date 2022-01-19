# pyBF.py
# @author:archie2k16 me@archie.cc

class pyBF:
    def __init__(s, code):
        s.symbols = ['>', '<', '+', '-', '.', ',', '[', ']']
        s.pipLine = [0]
        s.pointer = 0
        s.pos = 0
        s.braceStack = []
        s.braceMap = {}
        s.errors = [
            (0, 'Unexpected symbol'),
            (1, 'Unexpected "]" at position {}'),
            (2, 'Unexpected "[" at position {}'),
            (3, 'Pointer should not be Negative'),
        ]
        s.code = code
        s.outBuffer = bytearray()

    def showError(s, n, *prompt):
        code, txt = s.errors[n]
        print(f'Error {code}:', txt.format(*prompt))
        quit()

    def moveRight(s):  # implement >
        s.pointer += 1
        if len(s.pipLine) < s.pointer + 1:
            s.pipLine.extend([0] * (s.pointer + 1 - len(s.pipLine)))

    def moveLeft(s):  # implement <
        if s.pointer > 0:
            s.pointer -= 1
        else:
            s.showError(3)

    def plusOne(s):  # implement +
        s.pipLine[s.pointer] += 1

    def minusOne(s):  # implement -
        s.pipLine[s.pointer] -= 1

    def outPut(s):  # implement .
        s.outBuffer.append(s.pipLine[s.pointer])

    def inPut(s):  # implement ,
        x = input()[0]
        s.pipLine[s.pointer] = x

    def loopBegin(s):  # implement [
        if not s.pipLine[s.pointer]:
            s.pos = s.braceMap[s.pos]

    def loopEnd(s):  # implement ]
        if s.pipLine[s.pointer]:
            s.pos = s.braceMap[s.pos]

    def run(s):
        commands = dict(
            zip(s.symbols, [s.moveRight, s.moveLeft, s.plusOne, s.minusOne, s.outPut, s.inPut, s.loopBegin, s.loopEnd]))
        for key, x in enumerate(s.code):
            if x == '[':
                s.braceStack.append(key)
            elif x == ']':
                if s.braceStack:
                    val = s.braceStack.pop()
                    s.braceMap[val] = key
                    s.braceMap[key] = val
                else:
                    s.showError(1, key + 1)
        if s.braceStack:
            s.showError(2, s.braceStack.pop())

        while s.pos < len(code):
            cmd = code[s.pos]
            if commands.get(cmd, False):
                commands[cmd]()
            else:
                s.showError(0)
            s.pos += 1
        return s.outBuffer.decode()


if __name__ == '__main__':
    code = input()
    a = pyBF(code)
    print(a.run())
