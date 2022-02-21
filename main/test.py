from googletrans import Translator
from googletrans import LANGUAGES as LG

translator = Translator()
translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest="en")
print(translation.text)