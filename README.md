# pyBrainFuck

---

This is a small Brainfuck interpreter written with Python3 with simple error check

+ author:archie2k16 me@archie.cc
# Brief introduction of Brainfuck
Brainfuck is a **fully Turing complete** programming language with only **EIGHT** simple commands 


| Character | Meaning |implementation method in the source code |
| --- | --- | ------ |
|>| Increment the data pointer by 1 |**.moveRight()**|
|<|Decrement the data pointer by 1 |**.moveLeft()**|
|+|Increment the byte at the data pointer by 1|**.plusOne()**|
|-|	Decrement the byte at the data pointer by 1|**.minusOne()**|
|.|Output the byte at the data pointer|**.outPut()**|
|,|Accept one byte of input, storing its value in the byte at the data pointer.|**.inPut()**|
|[|	If the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.|**.loopBegin()**|
|]|	If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.|**.loopEnd()**|
## How to use:

``python pyBF.py 
``
