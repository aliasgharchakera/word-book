from PyDictionary import PyDictionary #library to be used as dictionary and thesaurus
from translate import Translator #library to be used for translations

dictionary = PyDictionary()

dict_of_languages = {'en':'English','la':'Latin','ja':'Japan','es':'Spanish','ur':'Urdu','ru':'Russian',
'de':'German','fr':'French','tr':'Turkish','fa':'Persian','ms':'Malay','hi':'Hindi','ar':'Arabic',
'it':'Italian'}

#function to get meanings of the word
def meaning(word):
    a = dictionary.meaning(word)
    print("-----MEANING(S)-----")
    if type(a)!=dict: #if the word is not available in the library or is a misspelled word
        print("-----Error: Incorrect word or the word is not available-----")
        return main()
    else:
        for i in a:
            print(i)
            for j in a[i]:
                print(str(a[i].index(j)+1)+". "+j) #formatting the desired output in a numbered list

#function to get synonym(s) of the word
def synonym(word):
    a = dictionary.synonym(word)
    print("-----SYNONYM(S)-----")
    if type(a)!=list: #if the word is not available in the library or is a misspelled word
        print("-----Error: Incorrect word or word not available-----")
        return main()
    else:
        for i in a:
            print(str(a.index(i)+1)+". "+i) #formatting the desired output in a numbered list

#function to get antonym(s) of the word
def antonym(word):
    print("-----ANTONYM(S)-----")
    a = dictionary.antonym(word)
    if type(a)!=list: #if the word is not available in the library or is a misspelled word
        print("-----Error: Incorrect word or word not available-----")
        return main()
    else:
        for i in a:
            print(str(a.index(i)+1)+". "+i) #formatting the desired output in a numbered list

#function to translate the word
def translation123(word="",input1="", language=""):
    translation = Translator(from_lang=input1, to_lang=language)
    a = translation.translate(word)
    print("-----TRANSLATION-----")
    print("Input:",word)
    if language.lower() == "ar" or language.lower() == "ur" or language.lower() == "fa":
        string = ""
        for ch in reversed(a):
            string += ch
        print("Translation:", string,"("+dict_of_languages.get(language)+")") #the outputted value is a custom class of objects'''
    else:
        print("Translation:", a,"("+dict_of_languages.get(language)+")")

#main function to call the code
def main():
    word = str(input("Enter your word: "))
    if type(word) != str: #if the input is not a string
        print("Enter a a proper word again")
        return main() #calling the code again for the user
    else:
        pass
    print("Meaning - M")
    print("Synonym - S")
    print("Antonym - A")
    print("Translation - T")
    funct = input("What type of function do you want the code to perform? ").strip()

    for type1 in funct:
        if type1.lower() == 'm':
            meaning(word)
        elif type1.lower() == "s":
            synonym(word)
        elif type1.lower() == 'a':
            antonym(word)
        elif type1.lower() == "t":
            print("-----LIST OF LANGUAGES AVAILABLE-----")
            for i in dict_of_languages:
                print(dict_of_languages[i]+" - "+i)
            while True: #if the inputted language is not supported or is misspelled, the program will prompt the user for the input again
                source_language = input("Enter the input language: ")
                if source_language.lower() not in dict_of_languages:
                    print("-----Error: Choose from the list of available languages-----")
                else:
                    language = input("Enter the language you want to translate to: ")
                    if language == "":
                        translation123(word,source_language,"en") #if there is no input for language, the default language is english
                        break
                    elif source_language == "":
                        translation123(word,"en",language) #if there is no input for language, the default language is english
                        break
                    elif language.lower() not in dict_of_languages:
                        print("-----Error: Choose from the list of available languages-----")
                    else:
                        translation123(word,source_language, language)
                        break
        else:
            print("Thats not one of the options")
            return main()
    y = input("Do you want to run the program again? y for yes, any other key to end: ")
    if y.lower() == 'y' or y.lower()=='yes':
        return main()
    else:
        for ch in "THANKYOU FOR USING OUR CODE":
            print(ch, end=" ")

for ch in ("WELCOME TO WORDBOOK"):
    print(ch, end=" ")
print()
print("All in one code for meanings, synonyms, antonyms and translations")
main()
#eco-friendly
#100lines