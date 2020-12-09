#!/bin/bash
#
# Hourly_Archive.sh - Archive designated files & directories
# make dirtory by month/day and rename file by hourmin
###########################################################
#

#
MONTH=$(date +%m)
DAY=$(date +%d)
TIME=$(date +%k%M)
#
mkdir -p /home/parallels/Archive/$MONTH/$DAY
#
# Set Arichive File Name
#
FILE=archive-${TIME}.tar.gz
#
# Set Configuration and Destination File
#
CONFIG_FILE='/home/parallels/test/Files_To_Backup'
DESTINATION='/home/parallels/Archive/'$MONTH/$DAY/$FILE
#
#################  Main Script ###########################
#
# Check Backup Config file exists
#
if [ -f $CONFIG_FILE ]
then
    echo
else
    echo
    echo "$CONFIG_FILE does not exits."
    echo "Backup not completed due to missing Configuration File"
    echo 
    exit
fi

FILE_NO=1
exec < $CONFIG_FILE
read FILE_NAME
while [ $? -eq 0 ]
do
    # Make sure the file or directory exists.
    # The mean of the -o is or.
    if [ -f $FILE_NAME -o -d $FILE_NAME ]
    then
        FILE_LIST="$FILE_LIST $FILE_NAME"
    else
        echo
        echo "$FILE_NAME, does not exist."
        echo "Obviously, I will not include it in this archive."
        echo "It is listed on line $FILE_NO of the config file."
        echo "Continuing to build archive list..."
        echo
    fi
    FILE_NO=$[$FILE_NO + 1]
    read FILE_NAME
done

echo "Starting archive..."
echo
#
##########################################################
#
# Backup the files and Compress Archive
#
tar -zcf $DESTINATION $FILE_LIST 2> /dev/null
#
echo "Archive completed"
echo
exit
