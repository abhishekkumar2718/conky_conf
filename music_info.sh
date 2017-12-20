#!/bin/bash

if cmus-remote -Q&>/dev/null ; then
	TITLE=$( cmus-remote -Q | grep title | cut -d " " -f 3- )  
	ARTIST=$( cmus-remote -Q | grep "tag artist" | cut -d " " -f 3- )
	ALBUM=$( cmus-remote -Q | grep "tag album " | cut -d " " -f 3- )
	DUR=$( cmus-remote -Q | grep "duration" | cut -d " " -f 2- )
	POS=$( cmus-remote -Q | grep "position" | cut -d " " -f 2- )
	POS_MIN=$(printf %02d $(( POS / 60 )))
	POS_SEC=$(printf %02d $(( POS % 60 )))
	DUR_SEC=$(printf %02d $(( DUR % 60 )))
	DUR_MIN=$(printf %02d $(( DUR / 60 )))
	echo ''
	echo $TITLE
	echo $POS_MIN:$POS_SEC / $DUR_MIN:$DUR_SEC
	echo $ARTIST
	echo $ALBUM
else
	echo ''
	echo ''
	echo 'No Music Playing. Turn on some tunes!!!:)'
	echo ''
	echo ''
fi 
