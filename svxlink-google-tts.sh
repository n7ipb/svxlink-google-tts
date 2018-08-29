
shopt -s nullglob
SRC_DIR="."

create_virt_env() {
    virtualenv env
    source env/bin/activate
    pip -q install -r $SRC_DIR/requirements.txt
    export GOOGLE_APPLICATION_CREDENTIALS=~/.google/PLACE_YOUR_API_KEY_FILENAME_HERE
}

list_voices() {
    create_virt_env
    python ${SRC_DIR}/list_voices.py
}

# Print a usage message and then exit
print_usage_and_exit()
{
    echo "Usage: svxlink-google-tts.sh [-L] <config file> "
    echo
    echo "  -L -- List available Voices"
    exit 1
}

# Default config file
CONFIG_FILE="google_tts.cfg"

while getopts "L" opt; do
    case $opt in
        L)
            list_voices
            exit 1
        ;;
    esac
done

if [ $# -eq 1 ]; then
    CONFIG_FILE=$1
fi

create_virt_env

# Check if the filter_sounds.cfg config file exists and source it in if it does
if [ ! -r "${SRC_DIR}/$CONFIG_FILE" ]; then
    echo -e "\n*** ERROR: Configuration file $CONFIG_FILE is missing"
    print_usage_and_exit
fi

. "${SRC_DIR}/$CONFIG_FILE"

# Check if the SUBDIRS config variable is set
if [ -z "$SUBDIRS" ]; then
    echo -e "\n*** ERROR: Configuration variable SUBDIRS not set."
    print_usage_and_exit
fi

# Loop through each subdirectory specified in SUBDIRS
for subdir in $SUBDIRS; do
    echo "Entering $SRC_DIR/$subdir"
    for file in $subdir/*.txt; do
        echo -e "\t$file"
        tts_text=$(cat $file)
        filename=$(basename "$file")
        filename="${filename%.*}"
        # Call synthesize_text to produce the sound file
        python ${SRC_DIR}/synthesize_text.py --$TEXTTYPE "$tts_text" --lang $LANGUAGE --name $NAME --gender $GENDER --rate $RATE --pitch  $PITCH --srate $SAMPLERATE --ofilename $subdir/$filename.wav

    done
done
shopt -u nullglob
