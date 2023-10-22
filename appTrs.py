
#for creating app of translation we need to install two things
#translator and translate
#pip install translator - translate

''' 
Translator : tell us from which language to which language, 
translator we give it in her parameter a language where we want to be translated to.
Translate : we give it a sentence or words that we want to translate
'''
import translate 
from translate import Translator 
data = Translator(from_lang = "English", to_lang = "Spanish")
#data c est que un variable qu on a cree pour stock ca
resultat = data.translate("i don't like that. Please leave, i am not happy anymore")
# resulat est variable qu on a cree pour stocke le resulat de la traduction de mot/phrase
print(resultat)
