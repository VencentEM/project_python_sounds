from gtts import gTTS

#data
txt  = "Welcome here, i was there for you "
langue = 'en'

#pass data as parameter
resultat = gTTS(text= txt, lang = langue)  
#when this fonction take the parameters (text and langue), it return to us a result

resultat.save("audio.mp3")