#!/bin/bash
if [ ! -f $1 ]; then
	echo "No file found"
	exit 1
fi
intregex='^[0-9]+$'
if ! [[ $2 =~ $intregex ]]; then
echo "Second argument must be an integer"
exit 1
fi
echo "Head: " 
head -n $2
echo "Tail: "
tail -n $2
