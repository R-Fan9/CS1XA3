#!/bin/bash

IFS=$'\n'

if [ "$1" -eq 1 ] ; then
	if [ -f fixme.log ] ; then
		rm fixme.log
	fi

	for file in $(find .. -type f) ; do
		if [ $(tail -n 1 "$file" | egrep ".*#FIXME.*") ] ; then
			echo "$file" >> fixme.log
		fi
	done

elif [ "$1" -eq 2 ] ; then
	for i in $(git log --oneline | grep -i "merge") ; do
		commitID=$(echo "$i" | awk '{print $1;}')
		git checkout "$commitID"
		break
	done

elif [ "$1" -eq 3 ] ; then
	for file in $(cd .. | ls -S | grep -v total) ; do
		if [ -f "$file" ] ; then
			filesize=$(stat -c%s "$file")
			echo "$file has $filesize bytes."
		fi
	done

elif [ "$1" -eq 4 ] ; then
	read -p "Please enter a file extension: " extension
	find .. -type f -name "*$extension" | wc -l

elif [ "$1" -eq 5 ] ; then
	read -p "Please enter a tag: " tag
	if [ -f "$tag".log ] ; then
		rm "$tag".log
	fi

	for file in $(find .. -type f -name "*.py") ; do
		echo $(egrep "^#.*$tag.*" "$file") >> "$tag".log
	done

elif [ "$1" -eq 6 ] ; then
	scripts=$(find .. -type f -name "*.sh")
	read -p "Change or Restore? " ans

	if [[ "$ans" == "Change" ]] ; then
		if [ -f permissions.log ] ; then
			rm permissions.log
		fi

		for s in $scripts ; do
			scriptPm=$(ls -l "$s" | awk '{print $1,$9;}')
			echo "$scriptPm" >> permissions.log
			if [[ ${scriptPm:2:1} == "w" ]] ; then
				chmod u+x "$s"
			else
				chmod u-x "$s"
			fi
			if [[ ${scriptPm:5:1} == "w" ]] ; then
				chmod g+x "$s"
			else
				chmod g-x "$s"
			fi
			if [[ ${scriptPm:8:1} == "w" ]] ; then
				chmod o+x "$s"
			else
				chmod o-x "$s"
			fi
		done

	elif [[ "$ans" == "Restore" ]] ; then
		if [ -f permissions.log ] ; then
			for i in $(less permissions.log) ; do
				pm=${i:0:10}
				script=${i:11}
				if [[ ${pm:2:1} == "w" ]] && [[ ${pm:3:1} == "-" ]] ; then
					chmod u-x "$script"
				elif [[ ${pm:2:1} == "-" ]] && [[ ${pm:3:1} == "x" ]] ; then
					chmod u+x "$script"
				fi

                                if [[ ${pm:5:1} == "w" ]] && [[ ${pm:6:1} == "-" ]] ; then
					chmod g-x "$script"
				elif [[ ${pm:5:1} == "-" ]] && [[ ${pm:6:1} == "x" ]] ; then
					chmod g+x "$script"
				fi

				if [[ ${pm:8:1} == "w" ]] && [[ ${pm:9:1} == "-" ]] ; then
					chmod o-x "$script"
				elif [[ ${pm:8:1} == "-" ]] && [[ ${pm:9:1} == "x" ]] ; then
					chmod o+x "$script"
				fi
			done
		fi
	else
		echo "Sorry, no such option."
 	fi

elif [ "$1" -eq 7 ] ; then
	read -p "Backup or Restore? " ans
	if [[ "$ans" == "Backup" ]] ; then
		if [ -d backup ] ; then
			rm -rf backup
		fi

		mkdir backup
		for file in $(find .. -type f -name "*.tmp") ; do
			echo "$file" >> ./backup/restore.log
			mv "$file" backup
		done

	elif [[ "$ans" == "Restore" ]] ; then
		cd backup
		if [ -f restore.log ] ; then
			for i in $(cat restore.log) ; do
				if [ -f "${i##*/}" ] ; then
					cp "${i##*/}" ../"${i%/*}"
				else
					echo "${i##*/}" has been removed
				fi

			done

		else
			echo "Error, restore.log does not exist."
		fi
	else
		echo "Sorry, no such option."

	fi

elif [ "$1" -eq 8 ] ; then
	read -p "Please enter a value for a: " a
	while [ "$a" -eq 0 ] ; do
		read -p "a can not be 0. Please reenter a value: " a
	done

	read -p "Please enter a value for b: " b
	read -p "Please enter a value for c: " c

	disct=$(($b*$b-4*$a*$c))

if [ "$disct" -lt 0 ] ; then
	echo "This can not be computed since the discriminant is negative."
else
cat >script.py <<'END_SCRIPT'

import sys, math
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])
d=float(sys.argv[4])

v1=(-1*b+math.sqrt(d))/(2*a)
v2=(-1*b-math.sqrt(d))/(2*a)

if v1 == v2:
	print("The root of the quadratic equation is:")
	print(v1)
else:
	print("The roots of the quadratic equation are:")
	print(v1)
	print(v2)

END_SCRIPT

python script.py "$a" "$b" "$c" "$disct"

rm script.py

fi

elif [ "$1" -eq 9 ] ; then

	if [ -f errorZero.log ] ; then
		rm errorZero.log
	fi

	for p in $(find .. -type f -name "*.py") ; do
		filesize=$(stat -c%s "$p")

		if [ "$filesize" -eq 0 ] ; then
			echo  "$p" >> errorZero.log
		else
			python "$p" > error 2>> errorZero.log
		fi
	done

	read -p "Do you want to remove all the python files in the repository that are empty and erroneous? (y/n) " input

	if [[ "$input" == 'y' ]] ; then
		for i in $(egrep "../Project01/.*\.py" errorZero.log) ; do
			file=$(echo "$i" | cut -d '"' -f 2) 
			rm "$file"
		done
	else
		regex='^\..*\.py$'
		regex2='^  .*\"\.\./Project01/.*\.py*'

		if [ $(stat -c%s errorZero.log) -eq 0 ] ; then
			echo $'\n'"Empty Python Files:"$'\n'"None"
			echo $'\n'"Erroneous Python Files:"$'\n'"None"	
		else
			echo $'\n'"Empty Python Files:"$'\n'"None"
			for i in $(cat errorZero.log) ; do
				if [[ "$i" =~ $regex ]] ; then 
					echo "$i"
				fi 
			done

			echo $'\n'"Erroneous Python Files:"
			for l in $(cat errorZero.log) ; do
				if [[ "$l" =~ $regex2 ]] ; then
					echo "$l" | cut -d '"' -f 2
				fi
			done
		fi
	fi

else
	echo "Input Error"
fi
