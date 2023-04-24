# pip install googletrans==4.0.0-rc1
from googletrans import Translator
translator = Translator()
language = {
    "bn":"Bangla",
    "en":"English",
    "ko":"Koren",
    "fr":"French",
    "de":"German",
    "he":"Hebrew",
    "hi":"Hindi",
    "it":"Italian",
    "ja":"Japanese",
    "la":"Latin",
    "ms":"Malay",
    "ne":"Nepali",
    "ru":"Russian",
    "ar":"Arabic",
    "zh":"Chinese",
    "es":"Spanish"
}
allow = True #variable to control correct language code input
while allow:# allow: #checking if language code is valid
    user_code = input("Enter a desired langauge code. To see the langauge code list enter 'options' \n")
    if user_code=="options":
        print("Code:Language")
        for item in language.items(): #("bn","Bangla")
            print(f"{item[0]} => {item[1]}") #"bn" >= "Bangla"
        print()
    else:
        for lan_code in language.keys():
            if lan_code == user_code:
                print(f"You have selected {language[lan_code]}")
                allow= False
        if allow:
            print("Its not a valid language code")

while True: #Translation
    string  = input("Write the text you want to translate: \nTo exit the program write 'close'\n")
    if string == 'close':
        print(f'\nHave a nice day')
        break
    #translating method from googletrans
    translated  = translator.translate(string,dest=user_code)
    print(f"\n{language[user_code]} translation:{translated.text} ")
    print(f'Pronunciation : {translated.pronunciation}')

    for item in language.items():
        #checking if source language is listed in language dictionary
        if translated.src == item[0]:
            print(f'Translated from : {item[1]}')
