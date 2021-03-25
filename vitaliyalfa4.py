#ВИТАЛИЙ 4.0 ALFA BY ГЛЕБ ПРЯХИН
"""
                                           -ДОКУМЕНТАЦИЯ-

ФАЙЛЫ-
Для работы нужны эти файлы: email.txt (хранит ссылку на почтовый сервис), name.txt (хранит имя пользователя), sp.txt (кол-во просмотров),
tts.txt (хранит индификатор голоса), z1.txt (хранит заметки), dialogset.txt (Устарел, может остатся от старых версий, если у вас он есть - удалите).

ПЕРЕМЕННЫЕ-
В коде есть такие переменные: an (хранит фразы пользователя), name (хранит имя пользователя, задается файлом name.txt), views (хранит кол-во просмотров, задается файлом sp.txt),
f (используется для работы с файлами), rec1 и rec2 (используется для работы с кортежами и циклами for), error (каждое действие ассистента приравнивает error к 0, если действия не было, то срабатывает elif в конце кода.)

Остальные комментарии будут встречатся по ходу кода
"""
#модули
import pyttsx3
import os
import time
from datetime import datetime
import speech_recognition as sr
import random
import webbrowser
import sounddevice as sd
import pyowm 
import requests


os.system("color 70")

#шапка
os.system('cls' if os.name == 'nt' else 'clear')
print("ВИТАЛИЙ 4.0 ALFA -загрузка... \n Автор проекта: Глеб Пряхин \n Автор 3д модели: Юрий Москвин \n В работе заимствуется команда на принудительное закрытие файлов у YT канала MIXANIGEN. \n ------------------------ \n НАШ САЙТ: http://vitaliy.renderforestsites.com")

#просмотры
f = open("sp.txt", "r")
views = f.read(1000)
views = int(views)
f.close()
f = open("sp.txt", "w")
views = views + 1
views = str(views)
views = f.write(views)
f.close()

#синтез речи
f = open("tts.txt", "r")
tts1 = int(f.read(1))
f.close()
text = ""
tts = pyttsx3.init()
speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[tts1].id)
def run():
    tts.say(t)
    tts.runAndWait()
    print("Виталий:", t)

#функция на быстрое открытие веб страниц
def runweb():
    webbrowser.open(web)
    tts.say("открываю веб страницу")
    tts.runAndWait()


os.system('cls' if os.name == 'nt' else 'clear')

#функция на сброс вызова в скайпе
def falcall():
    os.system("TASKKILL /IM skype.exe /F")
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system("start skype.exe")

#читаем файл smalltalk и делаем 2 списка: 1 - с ключевыми словами, 2 - с ответами ассистента
f = open("smalltalk.txt", "r", encoding="utf-8")
smalltalkdialog = f.read()

asksmalltalk = smalltalkdialog[len("мопросы: "):smalltalkdialog.find(" | [конецстроки1]")].split(" | ")

answersmalltalk = smalltalkdialog[smalltalkdialog.find("ответы: ") + len("ответы: "):smalltalkdialog.find(" | [конецстроки2]")].split(" | ")

#читаем файл customdialog и делаем 2мсписка: 1 - с ключевыми словами, 2 - с ответами ассистента
f = open("customdialog.txt", "r", encoding="utf-8")
customdialog = f.read()

askdialog = customdialog[len("вопросы: "):customdialog.find(" | [конецстроки1]")].split(" | ")

answerdialog = customdialog[customdialog.find("ответы: ") + len("ответы: "):customdialog.find(" | [конецстроки2]")].split(" | ")

#имя
f = open('name.txt', 'r')
if f.read(1) == "":
    t = "Привет меня зовут Виталий, давайте приступим к регистрации. Как вас зовут? напишите своё имя на клавиатуре"
    run()
    name = input("Меня зовут: ").title()
    f = open('name.txt', 'w')
    f.write(name.title())
    f.close()
    
    t = "Очень приятно " + name + " все готово к работе. Как вы уже знаете я Виталий, проект ученика школы 14 09 Глеба Пряхина. На данном этапе разработки я могу открывать и закрывать приложения, поддержать не сложный диалог и еще несколько интересных фишек. И так процесс регистрации завершен. перезапускаю программу."
    run()
    f.close
f = open('name.txt', 'r')
name = f.read(10)
f.close


#приветствия
greeting = ("Добрый день", "приветствую вас", "Здравствуйте, как прошел ваш день", "Здравствуйте, чем могу помочь", "Добрый день, рад вас видеть", "Добрый день, слушаю вас", "Как сказал бы Кеша, добрый день повелитель, слушаю вас", "Чем могу по мочь", "Привет, чем могу помочь?", "Здравствуйте, чем могу по мочь?")
t = greeting[random.randint(1,9)] + " " + name
run()

#рандомные предложения
recomend = ("Открой браузер", "Найди в интернете стихи А. Пушкина.", "Как дела?", "Что ты умеешь?", "Запомни код от домофона 495 544.", "Найди на ютубе котиков.")


#тут кортеж с фразами, которые произносятся в случае ошибки.
randomdialog = ("Я вас не понял, но по смыслу понял", "Вы знаете, иногда люди просто не могут найти общий язык. Давайте вы перефразируете ваш вопрос, а я попробую найти более подходящий ответ.", "Нуу наверное, я честно говоря не знаю, что на это ответить, но давайте я попробую предположить... Наверное... Да, или нет...", "Чем занимаетесь?", "Моя твоя не понимать", "Чем займемся?", "Для меня это слишком сложно, попробуйте сказать это другими словами.")


timer = 100
rec = 0
rectext = ""
#вход в цикл (в начале форматируем переменную an(отвечает за прием ответов) и переменную error (актиирует сообщения в случае ошибки) )
while True:
    now = datetime.now()
    an = "я ничего не сказал"
    error = 1

    #распознование (и не просите, в функцию не добавлю)
    rec1 = len(recomend) - 1
    rec2 = recomend[random.randint(0, rec1)]
    print('-------------------')
    r = sr.Recognizer()
    with sr.Microphone() as source:
	    print("Скажите что нибудь, например:", rec2)
	    r.pause_threshold = 1
	    #r.adjust_for_ambient_noise(source, duration=1)
	    audio = r.listen(source)
    try:
	    an = r.recognize_google(audio, language="ru-RU").lower()
	    print("Вы сказали: " + an)
    except sr.UnknownValueError:
        t = "Я вас не слышу, говорите громче!"
        print("Сбой системы распознования речи. ")

    #тут будут действия ассистента (разговоры в цикле for дальше)
    if "почт" in an:
            error = 0
            f = open('email.txt', 'r')
            if f.read(1) == "":
                t = "я забыл адресс вашего почтового сервиса вставьте ссылку на сайт почтового сервиса в мою программу"
                run()
                a = 1
                while True:
                    v = input("Вставьте ссылку для почтового сервиса.")
                    f = open('email.txt', 'w')
                    if "https" in v:
                        web = v
                        f.write(web)
                        f.close()
                        break

            t = "Хорошо " + name + "."
            f = open('email.txt', 'r')
            web = f.read(97)
            f.close()
            webbrowser.open(web)

    #поиск
    elif "найди" in an:
        error = 0
        if "в интернете" in an:
            t = "Начинаю поиск в интернете" + an[an.find("ете")+3:]
            run()
            sear = an[an.find("ете")+3:]
            webbrowser.open("https://www.google.com/search?q=" + sear)

        elif "youtube" in an:
            sear = an[an.find("be")+2:]
            t = "Начинаю поиск в ютубе " + sear
            run()
            webbrowser.open("https://www.youtube.com/results?search_query=" + sear)

        else:
            t = "Вы дали мало данных, скажите найди в интернете, либо найди в ютубе и ваш вопрос."
            run()
        continue
    #функция на закрытие Тут мы берем 2 кортежа, в кортеже "listprogram" у нас ключевые слова, а в "listprogram2" команды.
    elif "закрой" in an:
        listprogram = ("steam", "skype", "браузер")
        listprogram2 = ("TASKKILL /IM steam.exe", "TASKKILL /IM skype.exe", "TASKKILL /IM chrome.exe")
        for net in range(len(listprogram)):
            if listprogram[net] in an:
                program = listprogram2[net]
                os.system(program)
                os.system('cls' if os.name == 'nt' else 'clear')
                t = "Закрываю " + listprogram[net] 
                run()
                error = 0
        continue

    #синтезатор речи
    elif "текст" in an:
        error = 0
        t = "Вставьте сюда текст, который надо синтезировать. в конце текста напишите команду стопсинтез"
        run()
        t = ""
        while True:
            t = t + " " + str(input("Вставьте сюда текст > "))
            if "стопсинтез" in t:
                break
                t = t[:t.find("стопсинтез")]
        run()
         

    #интернет Тут мы берем 2 кортежа, в кортеже "fordefweb" у нас ключевые слова, а в "fordefweb" ссылки.
    fordefweb = ("youtube", "вконтакте", "браузер", "google", "новости", "окко", "хабр", "facebook", "wifmedia", "свой сайт")
    fordefweb2 = ("https://www.youtube.com/", "https:/vk.com", "https://www.google.ru/", "https://www.google.ru/", "https://lenta.ru/", "https://okko.tv/", "https://habr.com/ru/feed/", "https://www.facebook.com/", "https://wifmedia.com/", "http://vitaliy.renderforestsites.com")
    for net in range(len(fordefweb)):
        if fordefweb[net] in an:
            web = fordefweb2[net]
            runweb()
            error = 0


    #программы Тут мы берем 2 кортежа, в кортеже "listprogram" у нас ключевые слова, а в "listprogram2" команды.
    listprogram = ("проводник", "skype")
    listprogram2 = ("explorer.exe", "start skype.exe")
    for net in range(len(listprogram)):
        if listprogram[net] in an:
            program = listprogram2[net]
            os.system(program)
            t = "Открываю " + listprogram[net] 
            run()
            error = 0
    
    #команды на выключения. переменная start безполезна и нужна только для приостановки программы
    if "замолчи" in an or "выключи микрофон" in an:
        error = 0
        t = "нажмите энтэр для продолжения диалога"
        run()
        start = input("нажмите тут enter")
        t = "С возвращением " + name + " в систему!"
        run()
    elif "сбрось вызов" in an or "сбросить вызов" in an or "повесь трубку" in an or "повесить трубку" in an or "положь трубку" in an:
        t = ("Досвидания!", "До новых встреч!", "Чао.", "Завершаю вызов.")[random.randint(0,3)]
        run()
        error = 0
        falcall()  
    elif "выключи компьютер" in an or "заверши работу" in an or "завершить работу" in an:
        error = 0
        t = "Начинаю отключения компьютера. Выключение через:"
        run()
        timer = 10
        for i in range(10):
            timer = timer - 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Выключение через", timer, "секунд.")
            time.sleep(1)
            t = str(timer) + " секунд."
            run()
        print("Выключение...")
        t = "Досвидания " + name
        run()
        os.system("color 07")
        time.sleep(1)
        os.system('shutdown -s')  
    elif "пока" in an or "до свидания" in an or "выключись" in an:
        t = "До скорых встреч " + name + "!"
        run()
        os.system("color 07")
        exit()
        



    elif "брось" in an:
        error = 0
        t = ("орел", "решка")[random.randint(0, 1)]
        run()
 
    #память    тут происходит работа с файлом z1.txt
    elif "запомни" in an or "напомни" in an:
        error = 0
        f = open("z1.txt", "a")
        if an[len("запомни"):] == "":
            t = "Заметка не может быть пустой! Скажите запомни и то, что вы хотите сохранить."
            run()
            print("Ошибка! Вы пытаетесь создать пустую заметку!")
        else:
            t = "Я запомнил, что бы прочитать эту заметку скажите, что ты помнишь?"
            run()
            note = an[len("запомни"):] + ","
            f.write(note)
            f.close()

    elif "помн" in an:
        error = 0
        f = open("z1.txt", "r")
        if f.read(1) == "":
            t = ("Похоже у вас еще нет заметок. Если хотите создать новую, скажите запомни и то что вы хотите сохранить.")
            run()
        else:
            notes = f.read()
            print(notes)
            t = "И так вот что я помню: " + notes + " Если хотите их удалить, скажите удалить все заметки."
            run()
            f.close()

            

    elif "удали" in an and "заметки" in an:
        error = 0
        print("Удаление...")
        f = open("z1.txt", "w")
        f.write("")
        f.close()
        t = "Все заметки удалены."
        run()


    #время
    elif "врем" in an:
        error = 0
        t = name + ", сейчас " + str(now.hour) + " " + str(now.minute)
        run()
    
    #кастомный диалог.
    for word in range(len(askdialog)):
        if askdialog[word] in an:
            error = 0
            t = answerdialog[word]
            run()
            break

    #small talk 
    for word in range(len(asksmalltalk)):
        if asksmalltalk[word] in an:
            error = 0
            t = answersmalltalk[word]
            run()
            break
    


    
    #ошибка, если error = 1, то ассистент не знает что ответить, и мы берем рандомную фразу
    if error == 1:
        if an == "я ничего не сказал":
            print("Команда не отправлена.")
        else:
            rec1 = len(randomdialog) -1
            t = randomdialog[random.randint(0, rec1)]
            run()



    

