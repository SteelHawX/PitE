# This repository is used to store my solutions to weekly PitE course assignments 

## First homework assignment: PyWordCount


### Description

**PyWordCount** is a script that can be used to count number of characters, words or lines of given file.
It resembles WordCount known to UNIX users and also uses same option symbols.

### Installation and use

To use **PyWordCount** it is necessary to have installed interpreter for python3. To run
script you need open console in scripts directory and write:
>python wc.py [-l] [-w] [-c] filename

you can also use -h or --help for further information

## Second homework assignment: TicTacToeGame

### Description

**TicTacToeGame** is a simple program emulating TicTacToe in terminal

### Installation and use

To use **TicTacToeGame** it is necessary to have installed interpreter for python3. To run
script you need open console in scripts directory and write:
>python3 TicTacToe.py

To run unit tests for **TicTacToeGame** write to console:
>python3 test_TicTacToe.py

### Code review

#### General overwiew
Only half of the code is documented, however all of the function names are pretty descriptive, so it's not that bad. Classes seem to divide projects well into two parts, but for such a simple game it doesn't seem necessary. Some of the code looks really messy, particularly checking win conditions. 

#### Is it working?
Game is working as intended. No inputs other then allowed integers are possible, and game checks winning or losing conditions correctly. 

#### Optimization
Game seems pretty well optimized, however there are quite a few functions that could be shorter, more information in comments that I put into code. 

Checking victory conditions always has to look at all fields in the column/row/diagonal which could be optimized better. 

#### Problems and errors
Board is being drawn twice for every move for some reason, which definitely makes the game look messy. 

Very wierd typo/gramatical error when comunicating with the user: "Now is a player O has a turn". Seems to not be proof read.

#### Testing
Tests cover a lot of problems that could arise and are written well. I can't find any flaws in the way their code is written.

## Third homework assignment: TicTacToeGame + Tcp

### Description

Simple program using tcp communication. Game is running on the server and users send just moves to server.

### Installation and use

To use the program it is necessary to have installed interpreter for python3. To run server
script you need open console in scripts directory and write:
>python3 Server.py

To run client script you need open console in scripts directory and write:
>python3 Client.py
