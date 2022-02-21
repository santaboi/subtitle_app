#simple translation package powered by googletrans
from googletrans import Translator
from googletrans import LANGUAGES as LG
import os
src = "en"
dest = 'zh-tw'
file_name = "text1.txt"

translator_dir = os.path.dirname(__file__) #absolute path of this code
rel_path = "lyrics/" + file_name
out_rel_path = "output_lyrics/" + file_name
lyrics_path = os.path.join(translator_dir , rel_path)
out_path = os.path.join(translator_dir , out_rel_path)


lyrics = open( lyrics_path , "r")

try :
    with open(out_rel_path , "w") as fo :
        translator = Translator()
        for text_per_line in lyrics :
            """translation = translator.translate(text_per_line , dest ="zh-tw")
            print(text_per_line)
            print(translation.text)"""
            translator = Translator()
            translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest="en")
            print(translation.text)
            #fo.write(text_per_line)
            #fo.write(translation.text)
except FileNotFoundError:
    print("The 'docs' directory does not exist")
