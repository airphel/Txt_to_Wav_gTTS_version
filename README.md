#
#Conversion TXT message to WAV file for Beacon radio
#
#2022 airphel
#
# msg-wav.sh
Script made from that of F8ASB.

Information message generator for HBLink server, FreeDMR, ...
This program automatically generates a sound file in Wav format from a text entry in a .txt file.

The program uses speech synthesis from Google Text to Speech.
 
### Necessary installation prerequisites:

`pip install gTTS`

`apt-get install ffmpeg`

`apt-get install mpg321`


### File creation:

1 - In the gtts.py file, choose the conversion language.

2 - Define the content to convert in the message.txt file.

3 - The text will then automatically transform into voice and Wav format.
Note: Punctuation can change the intonation of the voice.

4 - The program produces the sound file, with the correct Wav 8k format.


### How the Python script works:

The msg-wav.py script tranforms a text file into its mp3 `output.mp3` with the gTTS and mpg321 modules then into wav with the ffmpeg module.
The output file will be called `message.wav`

The command to use is:
`Python3 msg-wav.py <textfilename>`

If you turn it into an executable the ./ command will replace python3.
(chmod +x msg-wav.py)
