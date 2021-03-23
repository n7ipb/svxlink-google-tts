# svxlink-google-tts
### Tools to create SvxLink sound files using Googles Cloud TTS


This is the README file for generating SvxLink sound clips using the Google
text to speech system (https://cloud.google.com/text-to-speech). 

Google Cloud Text-to-Speech enables developers to synthesize natural-sounding 
speech with more than 250 voices, available in multiple languages and variants. It creates
extremely high quality speech and can easily be used to add additional messages 
to SvxLink.

You have to have a Google Cloud account and an API key to use this code.  

Start by following the directions found here:

https://cloud.google.com/text-to-speech/docs/quickstart-protocol

Install the API key .json file in ~/.google/<your key filename.json>
NOTE: The svxlink-google-tts script assumes the key name is key.json
Change the script if your key name is different.

Make sure you have python and pip installed.   
Then install the python virtualenv with 'pip install virtualenv'

To generate sound files start by checking out the code.

    git clone http://gitub.com/n7ipb/svxlink-google-tts
    cd svxlink-google-tts

The 'English' directory contains all the text files that will be converted.  
The directory tree and files match those of the current SVXLink 'heather' release
plus a 'Custom' directory for your own customizations.  The default Custom
directory contains the strings used by pnw220.net.  Feel free to use them or create your own.

The configs directory contains config files for US Male and a US Female voice. Use the
-L option to list available voices and create your own configs as needed.

The scripts directory has the scripts needed to contact the Google servers and to generate
all the wave files from the .txt files found in 'English'.

    svxlink-google-tts.sh - the main program that traverses the English directory and creates 
    all the .wav files. 

Usage: svxlink-google-tts.sh [-L] [-T <source text dir>] [-D <destination dir>] <config file>

  -L -- List available Voices
  -T -- Direcory of text files to convert
  -D -- Destination Direcory for sound files


# Example config file:

```

###############################################################################
#
# Default configuration file for svxlink-google-tts.sh 
#
# Modify this or create your own custom config file with a different name
#
###############################################################################
# Set which subdirectories to search through for text files to convert
# 
SUBDIRS="Custom,Core,DtmfRepeater,Parrot,SelCallEnc,Trx,Default,EchoLink,Frn,Help,MetarInfo,PropagationMonitor,TclVoiceMail"

#
#
# Customizations for the synthesis
#
# For full descriptions of the following see;
# https://cloud.google.com/text-to-speech/docs/reference/rpc/google.cloud.texttospeech.v1beta1#google.cloud.texttospeech.v1beta1.TextToSpeech.SynthesizeSpeech
# 
LANGUAGE="en_US"
# run the script with the -L option to obtain a list of available names
# ./svxlink-google-tts.sh -L
NAME="en-US-Wavenet-C"
# Gender is often overridden by the choices available for a given name
# so this may have no noticable effect
GENDER="FEMALE"
# Speaking rate - 0.25 to 4.0, 1.0 is normal rate
RATE="1.0"
# Speaking pitch - -20.0,20.0, each step is a semitone up or down
PITCH="-2.0"
# Samplerate for the audio synthesis.   Use 16000 for svxlink
SAMPLERATE="16000"
#
# Type of text files - Ascii text (text),  Synthesized Speech Markup Language (ssml)
# at the moment it's all files as text or all as ssml.   By default all the existing SvxLink text 
# files are not using ssml.
TEXTTYPE="text"

```

# To use:
    Make sure you have an API .json key installed in ~/.google
    
    cd to the repository.
    
    build:
	scripts/svxlink-google-tts -T English -D us_male configs/US_Male.cfg

	This creates .wav files for all the entries found in the English directory. Places them
	in a directory called us_male and creates an archive called svxlink-sounds.tar.bz2 in
	that same directory. You can then transfer that to your target system.  Upon unpacking you
	will have a local directory called us_male with all the sound files. Place that where your
	sound files are stored.
 
    
    Test sound samples with 'aplay <path to wave file>'
    
