import random

answers = [
    "Бесспорно",
    "Мне кажется - да",
    "Пока неясно, попробуй снова",
    "Даже не думай",
    "Предрешено",
    "Вероятнее всего",
    "Спроси позже",
    "Мой ответ - нет",
    "Никаких сомнений",
    "Хорошие перспективы",
    "Лучше не рассказывать",
    "По моим данным - нет",
    "Можешь быть уверен в этом",
    "Да",
    "Сконцентрируйся и спроси опять",
    "Весьма сомнительно",
]
print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
name = input("Как тебя зовут?")
print("Привет,", name)


def input_phrase():
    print("Какой вопрос ты хочешь задать?")
    phrase = input()
    print(random.choice(answers))
    print("Хочешь задать еще один вопрос?")
    input1 = input("Введи:да/нет?:")
    if input1.lower() == "да":
        input_phrase()
    else:
        print("Возвращайся если возникнут вопросы!")


input_phrase()
