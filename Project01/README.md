# CS 1XA3 Project01 - fanh11

## Usage
Execute this script from project root with:
	chmod +x ./CS1XA3/Project01/project_analyze.sh
	./CS1XA3/Project01/project_analyze arg1
With possible arguments arg1: 
* 1 - FIXME Log
* 2 - Checkout Latest Merge
* 3 - File Size List
* 4 - File Type Count
* 5 - Find Tag

## Feature 01; FIXME Log (6.2)
Description: FIXME Log finds every file in the repo that has the word #FIXME in the last line. Then it stores the list of file names in a new file - fixme.log - separated by a newline

Execution: 
1. FIXME Log is executed by inputting 1 as arg1 

Reference: [tail -n 1](https://unix.stackexchange.com/questions/286544/how-to-extract-first-and-last-lines-in-a-file)

## Feature 02; Checkout Latest Merge (6.3)
Description: Checkout Latest Merge finds the most recent commit with the word merge (case insensitive) in the commit message and checkout that commit
 
Execution: 
1. Checkout Latest Merge is executed by inputting 2 as arg1

Reference: [awk '{print $1;}'](https://unix.stackexchange.com/questions/65932/how-to-get-the-first-word-of-a-string)

## Feature 03; File Size List (6.4)
Description: File Size List lists the sorted files (largest to smallest) in the repo and their corresponding sizes in human readable format

Execution: 
1. File Size List is executed by inputting 3 as arg1

Reference: [stat -c%s](https://www.cyberciti.biz/faq/howto-bash-check-file-size-in-linux-unix-scripting/)

## Feature 04; File Type Count (6.5)
Description: File Type Count outputs the number of files in the repo that have the user specified extension

Execution: 
1. File Type Count is executed by inputting 4 as arg1
2. Enter a file extension and press enter 

Reference: [find .. -type f -name](https://mac1xa3.ca/Slides/Week05/1XA3_Lab_Week05.html)

## Feature 05; Find Tag (6.6)
Description: Find Tag creates a log file with the user specified Tag name, which it stores all the lines that
begin with a comment (i.e #) and include Tag for each python file in the repo

Execution: 
1. Find Tag is executed by inputting 5 as arg1
2. Enter a Tag and press enter

Reference: [find .. -type f -name](https://mac1xa3.ca/Slides/Week05/1XA3_Lab_Week05.html)

## Custom Feature 01; Float Division (No Implementation Yet)
Description: Float Division performs and outputs the result of float division on two numbers inputted by the user  

Execution: 
1. Float Division is executed by inputting c1 as arg1
2. Enter two numbers and press enter

## Custom Feature 02; Find Error
Description: Find Error creates a file that stores all the errors in the python files that are in the repo

Execution: 
1. Find Error is executed by inputting c2 as arg1
