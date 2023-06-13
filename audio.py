from gtts import gTTS
import os 
myText = "Descendre les marches du chemin de l’Ivraie pour \
profiter du magnifique panorama sur les coteaux \
et la boucle de l’Oise. S’ouvre l’extraordinaire pers- \
pective de l’Axe Majeur , œuvre magistrale de l’ar- \
tiste Dani Karavan. Cité dans d’innombrables revues \
d’art contemporain, ce parcours urbain long de 3 kilo- \
mètres rehausse la beauté naturelle de la boucle de \
l’Oise. Par temps clair, la vue porte sur une autre pers- \
pective célèbre, celle reliant le Jardin des Tuileries à \
l’Arche de la Défense."
langage = "fr"
textSpeech = gTTS(text=myText, lang=langage, slow=False)
textSpeech.save("test.mp3")
os.popen("test.mp3")