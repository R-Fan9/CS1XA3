# CS 1XA3 Project01 - fanh11

## Usage
Execute this script from project root with: 
``` 
chmod +x ./CS1XA3/Project01/project_analyze.sh 
./CS1XA3/Project01/project_analyze arg1 
``` 
With possible arguments arg1: 
* 1 - FIXME Log 
* 2 - Checkout Latest Merge 
* 3 - File Size List 
* 4 - File Type Count 
* 5 - Find Tag
* 6 - Switch to Executable
* 7 - Backup and Delete/Restore
* 8 - Calculate Roots
* 9 - Remove or Display

## Feature 01; FIXME Log (6.2)
Description: FIXME Log finds every file in the repo that has the word #FIXME in the last line. Then it stores 
the list of file names in a new file - fixme.log - separated by a newline
 
Execution: 
1. FIXME Log is executed by inputting 1 as arg1
 
Reference: [tail -n 1](https://unix.stackexchange.com/questions/286544/how-to-extract-first-and-last-lines-in-a-file)

## Feature 02; Checkout Latest Merge (6.3)
Description: Checkout Latest Merge finds the most recent commit with the word merge (case insensitive) in the 
commit message and checkout that commit 

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
1. Find Tag is executed by inputting 5 as arg1 e
2. Enter a Tag and press enter

Reference: [find .. -type f -name](https://mac1xa3.ca/Slides/Week05/1XA3_Lab_Week05.html)

## Feature 06; Switch to Executable (6.7)
Description: Switch to Executable finds all the shell scripts in the repo and allows the user to change or restore
the permissions of each shell script. If the user decides to change the permissions, then only people who have write
permissions of that shell script will also have executable permissions. If the user decides to restore the permissions,
then the original permissions of the shell scripts will be restored.

Execution:
1. Switch to Executable is executed by inputting 6 as arg1
2. Input 'Change' or 'Restore' and press enter

Reference: [${scriptPm:2:1}](https://unix.stackexchange.com/questions/303960/index-a-string-in-bash)

## Feature 07; Backup and Delete/Restore (6.8)
Description: Backup and Delete/Restore allows the users to back up or restore all the files with the .tmp extension. 
If the user decides to back up the files, the files will be moved to a new directory called 'backup' and a file
called 'restore.log' will be created to store the files' original paths. If the user decides to restore, all the files
in the 'backup' directory will be restored to their original locations.  

Execution:
1. Backup and Delete/Restore is executed by inputting 7 as arg1
2. Input 'Backup' or 'Restore' and press enter

Reference: ["${i##*/}"](https://www.tldp.org/LDP/abs/html/string-manipulation.html)

## Custom Feature 01; Calculate Roots
Description: Calculate Roots allows the user to calculate the root(s) of a quadratic equation (ax^2+bx+c). It prompts 
the user to input the values for a, b and c. It will continue to ask the user to input a value for 'a' if 0 is 
entered. If the discriminant of that quadratic equation is negative, an error message will be displayed. Otherwise, an 
embedded python script will be used to calculate and display the root(s) of that quadratic equation.

Execution:  
1. Float Division is executed by inputting 8 as arg1
2. Input a value for 'a' (Do not enter 0) and press enter
3. Input a value for 'b' and press enter
4. Input a value for 'c' and press enter

Reference: [cat >script.py <<'END_SCRIPT'](https://unix.stackexchange.com/questions/184726/how-to-include-python-script-inside-a-bash-script)

## Custom Feature 02; Remove or Display
Description: Remove or Display finds all the empty and erroneous python files in the repository. Then, it creates a
file called 'errorZero.log' to store the paths of empty python files and the error messages of the erroneous python 
files. Afterward, it allows the user to decide whether or not to remove these python files. If the user decides to 
remove these files, they will be removed from the repository. Otherwise, all the empty and erroneous python files' 
paths will be displayed separately 

Execution:
1. Remove or Display is executed by inputting 9 as arg1
2. Input 'y' or 'n' and press enter

Reference: [python "$p" > error 2>> errorZero.log](https://mac1xa3.ca/Slides/Week04/1XA3_Lecture_Week04.html)
