import customtkinter as ctk
from googletrans import Translator as GoogleTranslator
from customtkinter import *
import pyttsx3
import pyperclip


languages = {'afrikaans': 'af', 'albanian': 'sq', 
'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 
'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 
'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 
'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 
'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 
'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 
'danish': 'da', 'dutch': 'nl', 'english': 'en', 
'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 
'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 
'galician': 'gl', 'georgian': 'ka', 'german': 'de', 
'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 
'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 
'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 
'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 
'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 
'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 
'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 
'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 
'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 
'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 
'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 
'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 
'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 
'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 
'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 
'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 
'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 
'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 
'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 
'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 
'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 
'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 
'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 
'yoruba': 'yo', 'zulu': 'zu'}
_languages = {'af': 'afrikaans', 'sq': 'albanian', 
'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 
'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 
'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 
'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 
'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 
'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 
'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 
'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 
'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 
'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 
'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 
'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 
'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 
'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 
'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 
'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 
'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 
'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 
'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 
'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 
'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 
'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 
'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 
'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 
'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 
'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 
'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 
'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 
'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 
'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 
'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 
'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 
'zu': 'zulu'}
lang_list = ['english','spanish','afrikaans', 'albanian', 'amharic', 'arabic', 
'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 
'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 
'chinese (simplified)', 'chinese (traditional)', 'corsican', 
'croatian', 'czech', 'danish', 'dutch', 'esperanto', 
'estonian', 'filipino', 'finnish', 'french', 'frisian', 
'galician', 'georgian', 'german', 'greek', 'gujarati', 
'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 
'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 
'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 
'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 
'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 
'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 
'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 
'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 
'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 
'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 
'slovenian', 'somali', 'sundanese', 'swahili', 
'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 
'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 
'xhosa', 'yiddish', 'yoruba', 'zulu']



# Color options
color1 = "white"
color2 = "dodger blue"
color3 = "gray95"
color4 = "green2"
# Font options
font1 = "times new roman"
font2 = "Kokila"
font3 = "Helvetica"

root= ctk.CTk()

window=root
window.geometry("540x600")
window.title('SHITTY translator')
window.resizable(width=False, height=False)

frame_input = ctk.CTkFrame(window, width=500, height=250)
frame_input.place(x=20, y=20)
frame_output = ctk.CTkFrame(window, width=500, height=270)
frame_output.place(x=20, y=300)

#=====================================================================#

currLang = StringVar()
currLang.set("Not Detected")

detectedLang = CTkLabel(frame_input, 
        textvariable=currLang, font=(font3, 20))
        

detectedLang.place(x=10, y=0)


opcions = ctk.CTkComboBox(frame_output,
        font=(font1, 15),
        values=lang_list)

opcions.set("Choose language")
opcions.place(x=0, y=0)


fromText_Box = ctk.CTkTextbox(frame_input, font=(font1, 15), height=220, width=500)
fromText_Box.place(x=0, y=40)

toText_Box= ctk.CTkTextbox(frame_output, font=(font1, 15), height=230, width=500)
toText_Box.place(x=0, y=40)

def run_translation():
    try:
        fromText = fromText_Box.get("1.0", "end-1c")
        translator_instance = GoogleTranslator()
        dest_lang = opcions.get()  # Opcions es el idioma destino (código, supongo)
        
        if dest_lang == '':
            print("Nothing has been chosen!", "Please Select a Language")
        else:
            if fromText != '':
                langType = translator_instance.detect(fromText)
                detected_lang_code = langType.lang.lower()
                
                # Mostrar el idioma detectado en tu label/entry
                currLang.set(_languages[detected_lang_code])
                
                result = translator_instance.translate(fromText, dest=dest_lang)
                
                toText_Box.delete("1.0", END)
                toText_Box.insert(INSERT, result.text)
    except Exception as es:
        print("error", es)

translateBtn = ctk.CTkButton(window, text="Translate", 
        font=(font2, 14, "bold"),
        command=run_translation)
translateBtn.place(x=200, y=290)

def copy_output_text():
    output_text = toText_Box.get("1.0", "end-1c")
    pyperclip.copy(output_text)
    

def speak_output_text():
    output_text = toText_Box.get("1.0", "end-1c")
    if output_text.strip() != "":
        engine = pyttsx3.init()
        engine.say(output_text)
        engine.runAndWait()
    else:
        print("No hay texto para leer")

copyBtn = ctk.CTkButton(window, text="Copy", 
                        font=(font2, 12), width=80, command=copy_output_text)
copyBtn.place(x=350, y=570)

speakBtn = ctk.CTkButton(window, text="listen it", 
                        font=(font2, 12), width=80, command=speak_output_text)
speakBtn.place(x=450, y=570)

root.mainloop()
