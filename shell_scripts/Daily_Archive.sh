#!/bin/bash
#
# Daily_Archive.sh - Archive designated files & directories
###########################################################
#

#
# Gather Current Date
#
DATE=$(date +%F)
#
# Set Arichive File Name
#
FILE=archive-${DATE}.tar.gz
#
# Set Configuration and Destination File
#
CONFIG_FILE='/home/parallels/test/Files_To_Backup'
DESTINATION='/home/parallels/test/'$FILE
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
#
# Build the name of all the files to backup
#
FILE_NO=1                     # Start on Line 1 of Config File. 
exec < $CONFIG_FILE           # Redirect Std Input to name of Config File
#
read FILE_NAME                # Read 1st record
#
while [ $? -eq 0 ]            # Create list of files to backup
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
