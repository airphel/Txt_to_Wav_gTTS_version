# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os
import sys

message = sys.argv[1]
print(message)

fh = open(message, "r")
myText = fh.read().replace("\n", " ")

# Language we want to use 
language = 'fr'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")
fh.close()

