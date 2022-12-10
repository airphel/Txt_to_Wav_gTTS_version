#
#Conversion TXT message to WAV file for Beacon radio
#
#2022 airphel
#
# msg-wav.sh
Script réalisé à partir du celui de F8ASB.
Générateur de message d'information pour serveur HBLink, FreeDMR, ...
Ce programme permet de générer automatiquement un fichier son au format Wav depuis une saisie de texte dans un fichier .txt. 

Le programme utilise la synthèse vocale de Google Text to Speech. 
 
### Installation nécessaire pré-requise :

`pip install gTTS`

`apt-get install ffmpeg`

`apt-get install mpg321`


### Création du fichier :

1 - Dans le fichier gtts.py, choisir la langue de conversion.

2 - Définir le contenu à convertir dans le fichier message.txt.

3 - Le texte sera ensuite automatiquement transformer en voix et au format Wav. 
Remarque : La ponctuation peut changer l'intonation de la voix.

4 - Le programme réalise le fichier son, avec le bon format Wav 8k.


### Comment fonctionne le script Python :

Le script msg-wav.py s'occupe de transformer un fichier texte en son mp3 `output.mp3` avec les modules gTTS et mpg321 puis en wav avec le module ffmpeg.
Le fichier de sortie s'appellera `message.wav`

La commande d'utilsation est :
`Python3 msg-wav.py <nomdufichiertexte>`

Si vous le transformez en executable la commande ./ remplacera python3.
(chmod +x msg-wav.py)
