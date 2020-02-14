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
fi
