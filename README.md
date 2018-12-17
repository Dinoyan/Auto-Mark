# Auto Marker

Python script to complie and run C programs and output it to a .txt file. Then compare the output txt file with the solution txt file. This script could be used in programming classes to automatically mark bunch of C exercises at once!

### Prerequisites

- Python 3.x
- C Compiler GCC

### Installing

Download this repo to get started.

### Demo

Files in the cwd:
  - student_1.c -> Correct output
  - auto_mark.py 
  - student_2.c	-> Wrong output
  - solution.txt -> Contains the correct output to comapre

```
$ Python3 auto_mark.py 
```

Output:

```
student_1 Mark: 100%
student_2.txt solution.txt differ: char 11, line 1
student_2 Mark: 0.0%
```
