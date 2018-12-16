# Auto Marker

Python script to complie and run C programs and output it to a .txt file. Then compare the output txt file with the solution txt file.

### Prerequisites

- Python 3.x
- C Compiler GCC

### Demo

Files in the cwd:
  HelloWorld.c -> Correct output
  auto_mark.py 
  Hello_World.c	-> Wrong output
  solution.txt -> Contains the correct output to comapre

```
$ Python3 auto_mark.py 
```

Output:

```
Hello_World.txt solution.txt differ: char 11, line 1
Mark: 0.0%
Mark: 100%
```
