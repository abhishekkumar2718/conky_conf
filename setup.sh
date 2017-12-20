#!/bin/bash

if [ -d ~/.conky ] ; then
	echo ".conky already exists. Please delete before trying again."
	exit
else
 	mkdir ~/.conky
fi
if [ -d ~/bin ] ; then
	echo "bin/ does not exist. Creating one..."
else
	echo "bin/ exists. Proceeding to copy..."
fi

echo Copying Files...
cp * ~/.conky/
echo Done.

echo Creating executables...
rm ~/.conky/conky_start
cp conky_start ~/bin/
chmod u+x ~/bin/conky_start
echo Done.

echo Running configuration...
conky_start

