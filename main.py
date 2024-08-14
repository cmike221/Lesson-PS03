from bs4 import BeautifulSoup
import requests
from googletrans import Translator


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
    #    print(response.text)
        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div",id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        translator = Translator()
        rus_word = translator.translate(word, dest="ru").text
        rus_definition = translator.translate(word_definition, dest="ru").text
        print(f"Значение слова - {rus_definition}")
        user = input("Что это за слово ?")
        if user == rus_word:
            print("Все верно!")
        else:
            print(f"Ответ не верный, было загадано слово - {rus_word}")

        play_again = input("Хотите сыграть еще раз? д/н")
        if play_again != "д":
            print("Спасибо за игру!")
            break

word_game()

