from gtts import gTTS
import os 
myText = "Cet édifice emblématique\
            imaginé pour accueillir les services de la nouvelle\
            préfecture du Val d’Oise est l’œuvre d’Henri Bernard,\
            l’architecte de la Maison Ronde, siège de Radio France\
            à Paris. Son originalité réside dans sa forme de pyramide inversée et s’inspire du City Hall de Boston de\
            1959, lui-même inspiré du Palais du gouverneur de\
            Chandigarh réalisé par Le Corbusier"
langage = "fr"
textSpeech = gTTS(text=myText, lang=langage, slow=False)
textSpeech.save("test.mp3")
os.popen("test.mp3")