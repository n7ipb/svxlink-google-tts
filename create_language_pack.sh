#!/bin/sh
#
# Copyright (C) 2018 Ken Koster - N7IPB
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#
# 
# Simple script to grab configuration info from a tts config file
# and create a compressed archive of all the associated
# wave files
#
# Usage: ./create_langauge_pack.sh <config file>
#
shopt -s nullglob

# Print a usage message and then exit
print_usage_and_exit()
{
    echo "Usage: create_language_pack <config file> "
    exit 1
}

SRC_DIR="."
# Default config file
CONFIG_FILE="google_tts.cfg"
#
# Grab an optional config file if present
if [ $# -eq 1 ]; then
    CONFIG_FILE=$1
fi

# Check if the filter_sounds.cfg config file exists and source it in if it does
if [ ! -r "${SRC_DIR}/$CONFIG_FILE" ]; then
    echo -e "\n*** ERROR: Configuration file $CONFIG_FILE is missing"
    print_usage_and_exit
fi

. "${SRC_DIR}/$CONFIG_FILE"

# Create the list of SUBDIRS to pull .wav files from
for subdir in $SUBDIRS; do
    tarlist="$tarlist $SRC_DIR/$subdir/*.wav"
    echo "Processing $SRC_DIR/$subdir"
done
#
# Build the tar file
    tar -zcvf svxlink_sounds_$NAME\_$GENDER\_$RATE\_$PITCH.tgz $tarlist $CONFIG_FILE
