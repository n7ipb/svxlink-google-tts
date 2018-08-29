#!/usr/bin/env python

# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Heavily Modified by Ken Koster - N7IPB - August 2018
#   Added options to control speech parameters and output to a specific filename
#   This is to support scripts that generate sound files for the SvxLink Ham Radio
#   repeater software (http://github.com/sm0svx/svxlink)
#   Complete TTS script package can be found at http://github.com/n7ipb/svxlink-google-tts
#
"""Google Cloud Text-To-Speech API sample application .

Example usage:
    python synthesize_text.py --text "hello"
    python synthesize_text.py --ssml "<speak>Hello there.</speak>"
"""

import argparse

# [START tts_synthesize_text]
def synthesize_text(text,lang,name,gender,rate,pitch,srate,ofilename):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)
    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=lang,
        name=name,
        ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
    audio_config = texttospeech.types.AudioConfig(
            speaking_rate=rate,
            pitch=pitch,
            sample_rate_hertz=srate,
        audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open(ofilename, 'wb') as out:
        out.write(response.audio_content)

# [END tts_synthesize_text]


# [START tts_synthesize_ssml]
def synthesize_ssml(ssml,lang,name,gender,rate,pitch,srate,ofilename):
    """Synthesizes speech from the input string of ssml.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/

    Example: <speak>Hello there.</speak>
    """
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(ssml=ssml)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=lang,
        name=name,
        ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
    audio_config = texttospeech.types.AudioConfig(
            speaking_rate=rate,
            pitch=pitch,
            sample_rate_hertz=srate,
        audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open(ofilename, 'wb') as out:
        out.write(response.audio_content)
# [END tts_synthesize_ssml]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--text',
                    help='The text from which to synthesize speech.')
    group.add_argument('--ssml',
                    help='The ssml string from which to synthesize speech.')
    parser.add_argument('--lang',default = 'en_US',
                    help='The language code to use.  (en_US)')
    parser.add_argument('--name',default = 'en-US-Wavenet-B',
                    help='The Voice to use.  (en_US-Wavenet-B)')
    parser.add_argument('--gender',default = 'FEMALE',
                    help='Gender Male/Female.')
    parser.add_argument('--rate',type=float,default = 1.1,
                    help='The speaking rate')
    parser.add_argument('--pitch',type=float,default = -3.0,
                    help='Voice pitch')
    parser.add_argument('--srate',type=int,default = 16000,
                    help='Sample Rate ')
    parser.add_argument('--ofilename',default = 'output.wav',
                    help='Output file name ')
    
    args = parser.parse_args()
#
#   Uncomment to print arguments
#   print(args.text,args.lang,args.name,args.gender,args.rate,args.pitch,args.srate,args.ofilename)
    if args.text:
        synthesize_text(args.text,args.lang,args.name,args.gender,args.rate,args.pitch,args.srate,args.ofilename)
    else:
        synthesize_ssml(args.ssml,args.lang,args.name,args.gender,args.rate,args.pitch,args.srate,args.ofilename)
