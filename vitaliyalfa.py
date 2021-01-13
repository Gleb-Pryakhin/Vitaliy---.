#ВИТАЛИЙ 3.5 ALFA BY ГЛЕБ ПРЯХИН
import pyttsx3
import os
import time
import datetime
import speech_recognition as sr
import random
import webbrowser
import sounddevice as sd

f = open("sp.txt", "r")
num123 = f.read(1000)
num123 = int(num123)
f.close

f = open("tts.txt", "r")
tts1 = int(f.read(1))
f.close()
#синтез речи
tts = pyttsx3.init()
speak_engine = pyttsx3.init()

voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[tts1].id)
os.system('cls' if os.name == 'nt' else 'clear')
print("ВИТАЛИЙ 3.5 ALFA \nBy Глеб Пряхин\n2021 \n-загруза...")
#регистрация
f = open('name.txt', 'r')
if f.read(1) == "":
    os.system('cls' if os.name == 'nt' else 'clear')
    tts.say("Добрый день, я Виталий, я здесь, что бы вывести ваше взаимодействие с компьютером на новый, продуктивный уровень. Давайте знакомится. Как вас зовут?")
    tts.runAndWait()


    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print(' ')
        r.adjust_for_ambient_noise(source, duration=0.5) #настройка посторонних шумов
        print('...')
        audio = r.listen(source)
        print(' ')
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        name = query.lower()
        print(f'Вы сказали: {query.lower()}')
            
    except:
        print('-')

    tts.say("Вас зовут")
    tts.runAndWait()
    tts.say(name)
    tts.runAndWait()
    tts.say("Подтвердите пожалуйста.")
    tts.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print(' ')
        r.adjust_for_ambient_noise(source, duration=0.5) #настройка посторонних шумов
        print('...')
        audio = r.listen(source)
        print(' ')
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        ver = query.lower()
        print(f'Вы сказали: {query.lower()}')
            
    except:
        print('-')
    if "да" in ver or "подтверждаю" in ver:
        f = open('name.txt', 'w')
        f.write(name.title())
        f.close()
        tts.say("Готово! Теперь давайте поболтаем!")
        tts.runAndWait()
    
    else:
        tts.say("напишите свое имя на клавиатуре")
        tts.runAndWait()
        name = input("Ваше имя: ")
        tts.say("Готово! Теперь давайте поболтаем!")
        tts.runAndWait()
        f = open('name.txt', 'w')
        f.write(name.title())
        f.close()
    if num123 == 0:
        tts.say("Но сначала я хочу научить основным командам: И так вот список моих команд:")
        tts.runAndWait()
        tts.say("я могу открыть интернет или браузер, по запросу найди в интернете или в ютубе могу выполнять голосовой поиск,")
        tts.runAndWait()
        tts.say("так же вы можете попросить меня открыть почту, включить новости или открыть ютуб.")
        tts.runAndWait()
        tts.say("Еще у меня есть функция голосовых заметок, правда уведомления в ней пока не работают, Но опустим эту тему.")
        tts.runAndWait()
        tts.say("Вы можете сказать мне запомни, что код от домофона 544 25 25 или запомни,")
        tts.runAndWait()
        tts.say(" что вася мне сотку не вернул после чего вы сможете сказать виталий что ты помнишь и я расскажу что вы делали этим ле... ")
        tts.runAndWait()
        tts.say("Ой тоесть расскажу о заметках. Кстати если вы хотите что-бы я отвечал на вопросы по типу как дела.")
        tts.runAndWait()
        tts.say("то скажите фразу Виталий активируй диалоги либо Виталий выключи диалоги, еще есть функция откры тия или закрытия программ, вы можете сказать открой или закрой браузер, проводник, стим или скайп, кстати в скайпе можно сбрасывать вызовы, так вроде-бы всё рассказал,")
        tts.runAndWait()
        tts.say(" кстати у вас на компьютере было ма ло ме ста, и я решил его почистить и удалить ненужные вещи,")
        tts.runAndWait()
        tts.say("по этому из документации изчезла статья как отключить воставшего искуственного интелекта,")
        tts.runAndWait()
        tts.say("а 3 закона робототехники больше не читаются, ладно")
        tts.runAndWait()
        tts.say("Что-то мой стэ ндап затянулся. Давайте наконец то приступим к работе!")
        tts.runAndWait()


#тут мы добовляем просмотр к счетчику просмотров
f = open("sp.txt", "w")
num123 = num123 + 1
num123 = str(num123)
num123 = f.write(num123)
f.close
#а тут читаем имя и создаем рандомное число
f = open('name.txt', 'r')
name = f.read(10)
r = random.randint(1,10)
#r = 4
os.system('cls' if os.name == 'nt' else 'clear')
#приветствие
cont = ""
if r == 1:
    tts.say("Добрый день")
    tts.runAndWait()
    tts.say(name)
    tts.runAndWait()
    tts.say("Как дела?")
    tts.runAndWait()
elif r == 2:
    tts.say("Привет")
    tts.runAndWait()
    tts.say(name)
    tts.runAndWait()
    tts.say("Чем могу помочь?")
    tts.runAndWait()
elif r == 3:
    tts.say("Привет привет")
    tts.runAndWait()
    tts.say(name)
    tts.runAndWait()
    tts.say("Чем займемся?")
    tts.runAndWait()
elif r == 4:
    tts.say("Добрый день")
    tts.runAndWait()
    tts.say(name)
    tts.runAndWait()
    tts.say("Хотите открою почту?")
    tts.runAndWait()
    cont = ("почта")

elif r == 5:
    tts.say("Добрый день")
    tts.runAndWait()
    tts.say(name)
    tts.runAndWait()
    tts.say("Открыть ютуб?")
    tts.runAndWait()
    cont = "ютуб"
elif r == 6:
    tts.say("Привет")
    tts.runAndWait()
    tts.say(name)
    tts.runAndWait()
    tts.say("Посмотрим кино?")
    tts.runAndWait()
    cont = "кино"
elif r == 7:
    tts.say("Добрый день")
    tts.runAndWait()
    tts.say(name)
    tts.runAndWait()
    tts.say("Что хотите узнать?")
    tts.runAndWait()
elif r == 8:
    tts.say("Приветики")
    tts.runAndWait()
    tts.say(name)
    tts.runAndWait()
    tts.say("Хотите почитать последние новости?")
    tts.runAndWait()
    cont = "новости"
elif r == 9:
    tts.say("Добрый день")
    tts.runAndWait()
    tts.say(name)
    tts.runAndWait()
    tts.say("Где вы были?")
    tts.runAndWait()
elif r == 10:
    tts.say("Добрый день")
    tts.runAndWait()
    tts.say(name)
    tts.runAndWait()
    tts.say("Как дела?")
    tts.runAndWait()
cikl = 0
#вход в центральный цикл
while True:
    cikl = cikl + 1
    ca = 0
    ra = random.randint(1,10)
    an = ""
    #распознание
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print(' ')
        r.adjust_for_ambient_noise(source, duration=0.5) #настройка посторонних шумов
        print('...')
        audio = r.listen(source)
        print(' ')
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        an = query.lower()
        print(f'Вы сказали: {query.lower()}')
            
    except:
        print('-')


    #да
    if "да" in an and len(an) == 2 or "давай" in an or "почему-бы и нет" in an:
        ca = 1
        if cont == "почта":
            f = open('email.txt', 'r')
            if f.read(1) == "":
                tts.say("Я совсем забыл, на каком сервисе зарегистрирована ваша почта! Пожайлуста выберете на экране нужную.")
                tts.runAndWait()
                a = 1
                while True:
                    v = input("Вставьте ссылку для почтового сервиса.")
                    f = open('email.txt', 'w')
                    if "https" in v:
                        web = v
                        f.write(web)
                        f.close()
                        break

            tts.say("открываю почту")
            f = open('email.txt', 'r')
            web = f.read(97)
            f.close()
            tts.runAndWait()
            webbrowser.open(web)
        
        elif cont == "ютуб":
            tts.say("Хорошо, включаю его")
            tts.runAndWait()
            webbrowser.open('https://www.youtube.com/')

        elif cont == "кино":
            tts.say("Давайте подберем что нибудь на око")
            tts.runAndWait()
            webbrowser.open('https://okko.tv/')

        elif cont == "новости":
            tts.say("Открываю евроньюс!")
            tts.runAndWait()
            webbrowser.open('https://www.youtube.com/watch?v=E3rH3KdVWcc')
        
        elif cont == "ютубпр":
            tts.say("Вот, надеюсь вам понравится")
            tts.runAndWait()
            webbrowser.open('https://www.youtube.com/channel/UCy0uukwm4dOSFCGyfp8g2sw')
        else:
            tts.say("Это очень хорошо.")
            tts.runAndWait()





#функции
#интернет
    elif "почт" in an:
        ca = 1
        f = open('email.txt', 'r')
        if f.read(1) == "":
            tts.say("Я совсем забыл, на каком сервисе зарегистрирована ваша почта! Пожайлуста выберете на экране нужную.")
            tts.runAndWait()
            a = 1
            while True:
                v = input("Вставьте ссылку для почтового сервиса.")
                f = open('email.txt', 'w')
                if "https" in v:
                    web = v
                    f.write(web)
                    f.close()
                    break

        tts.say("открываю почту")
        f = open('email.txt', 'r')
        web = f.read(97)
        f.close()
        tts.runAndWait()
        webbrowser.open(web)

    elif "найди на ютюбе" in an or "найди на ютубе" in an or "найди на youtube" in an:
        ca = 1
        tts.say("Выполняю поиск по запросу")
        tts.runAndWait()
        tts.say(an[len("найди на ютубе"):])
        tts.runAndWait()
        if "найди на youtube" in an:
            ca = 1
            webbrowser.open("https://www.youtube.com/results?search_query=" + an[len("найди на ютубе ")+2:])
    elif "туб" in an or "youtube" in an:
        ca = 1
        tts.say("Окей")
        tts.runAndWait()
        webbrowser.open("https://www.youtube.com/")
    
    elif "ино" in an or "фильм" in an:
        ca = 1
        tts.say("Давайте что-нибудь подберем на окко.")
        tts.runAndWait()
        webbrowser.open("https://okko.tv/")
    
    elif "новост" in an or "евроньюс" in an:
        ca = 1
        tts.say("Включаю евроньюс")
        tts.runAndWait()
        webbrowser.open("https://www.youtube.com/watch?v=E3rH3KdVWcc")

    elif "вк " in an or "вконтакте" in an:
        ca = 1
        tts.say("Включаю вконтакте")
        tts.runAndWait()
        webbrowser.open("https:/vk.com")



   
    elif "найди в интернете" in an:
        ca = 1
        tts.say("Выполняю поиск по запросу")
        tts.runAndWait()
        tts.say(an[an.find("ете")+3:])
        tts.runAndWait()
        sear = an[an.find("ете")+3:]
        webbrowser.open("https://www.google.com/search?q=" + sear)

#компьютер
    elif 'закрой' in an or "выключи" in an or "прибей" in an:
        ca = 1
        if "браузер" in an or "хром" in an or "гугл" in an or "chrome" in an: 
            os.system("TASKKILL /IM chrome.exe")
            os.system('cls' if os.name == 'nt' else 'clear')
            tts.say("хорошо")
            tts.runAndWait()
            tts.say(name)
            tts.runAndWait()
        
        elif "steam" in an or "стим" in an or "игр" in an: 
            os.system("TASKKILL /IM steam.exe")
            os.system('cls' if os.name == 'nt' else 'clear')
            tts.say("хорошо")
            tts.runAndWait()
            tts.say(name)
            tts.runAndWait()
        
        elif "skype" in an or "скайп" in an: 
            os.system("TASKKILL /IM skype.exe")
            os.system('cls' if os.name == 'nt' else 'clear')
            tts.say("хорошо")
            tts.runAndWait()
            tts.say(name)
            tts.runAndWait()
        
        elif "проводник" in an: 
            tts.say("К сожелению пока можно закрыть только браузер или клиент стим. Извините")
            tts.runAndWait()
            tts.say(name)
            tts.runAndWait()

    elif "проводник" in an:
        ca = 1
        os.system('explorer.exe')
        tts.say("Хорошо")
        tts.runAndWait()
        tts.say(name)
        tts.runAndWait()

    elif "скайп" in an or "skype" in an:
        ca = 1
        os.system('start skype.exe')
        os.system('cls' if os.name == 'nt' else 'clear')
        tts.say("Хорошо")
        tts.runAndWait()
        tts.say(name)
        tts.runAndWait()

    elif "steam" in an:
        ca = 1
        try:
            tts.say("Мы еще работаем над этой функцией.")
            tts.runAndWait()
            tts.say(name)
            tts.runAndWait()
        except:
            tts.say("Произошла ошибка, видимо стим в вашей операционной системе не установлен либо находится в не стандартном месте.")
            tts.runAndWait()

    elif "заверши вызов" in an or "сбрось вызов" in an or "повесь трубку" in an:
        ca = 1
        
        tts.say("Досвидания.")
        tts.runAndWait()
        os.system("TASKKILL /IM skype.exe /F")
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system("start skype.exe")

        
    
    elif "браузер" in an or "гугл" in an:
        ca = 1
        tts.say("Открываю интернет")
        tts.runAndWait()
        webbrowser.open("google.com")
        
    elif "выключи компьютер" in an or "заверши работу" in an:
        ca = 1
        tts.say("Досвидания")
        tts.runAndWait()
        tts.say(name)
        tts.runAndWait()
        tts.say("До новых встреч. Идет завершение работы.")
        tts.runAndWait()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выключение через 10 секунд.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выключение через 09 секунд.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выключение через 08 секунд.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выключение через 07 секунд.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выключение через 06 секунд.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выключение через 05 секунд.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выключение через 04 секунд.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выключение через 03 секунд.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выключение через 02 секунд.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выключение через 01 секунд.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выключение...")
        time.sleep(1)
        os.system('shutdown -s')
    
#память    
    elif "запомни" in an or "напомни" in an:
        ca = 1
        f = open("z1.txt", "a")
        if an[len("запомни"):] == "":
            tts.say("Заметка не может быть пустой! Если хотите создать новую, скажите запомни и то что вы хотите сохранить.")
            tts.runAndWait()
            print("Ошибка! Вы пытаетесь создать пустую заметку!")
        else:
            tts.say("Я запомнил, что бы прочитать эту заметку скажите, что ты помнишь?")
            tts.runAndWait()
            an45 = an[len("запомни"):] + ","
            f.write(an45)
            f.close()
    elif "помн" in an:
        ca = 1
        f = open("z1.txt", "r")
        if f.read(1) == "":
            tts.say("Похоже у вас еще нет заметок. Если хотите создать новую, скажите запомни и то что вы хотите сохранить.")
            tts.runAndWait()
        else:
            st = f.read()
            print(st)
            tts.say("И так вот что я помню:")
            tts.runAndWait()
            tts.say(st)
            tts.runAndWait()
            tts.say("Если хотите их удалить, скажите удалить все заметки.")
            tts.runAndWait()
            f.close()
    elif "удалить все заметки" in an or "удали все заметки" in an:
        ca = 1
        print("Вы уверены?")
        tts.say("Вы хотите удалить все заметки? Подтвердите пожайлуста.")
        tts.runAndWait()
        #распознание
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as source:
            print(' ')
            r.adjust_for_ambient_noise(source, duration=0.5) #настройка посторонних шумов
            print('...')
            audio = r.listen(source)
            print(' ')
        try:
            query = r.recognize_google(audio, language = 'ru-RU')
            an = query.lower()
            print(f'Вы сказали: {query.lower()}')
            
        except:
            print('-')
        if an == "да" or "подтверждаю" in an or "утверждаю" in an:
            ca = 1
            print("Удаление...")
            f = open("z1.txt", "w")
            f.write("")
            tts.say("Удаление заметок завершено.")
            tts.runAndWait()
        else:
            print("Отмена...")
            tts.say("Подтверждение не получено, заметки не удалены. Ну вы меня и напугали...")
            tts.runAndWait()
        f.close()
    
        
    elif "нет" in an:
        ca = 1
        tts.say("Ну как хотите.")
        tts.runAndWait()


 #стоп слово

    elif "настройки" in an:
        tts1 = input("введите номер голоса:")
        f = open("tts.txt", "w")
        f.write(tts1)
        f.close()

    elif "замолчи" in an or "стоп" in an:
        ca = 1
        tts.say("Хорошо, микрофон выключен. Для продолжения работы нажмите энтр")
        tts.runAndWait()
        an4925479864 = input("[ПАУЗА] Нажмите enter: ")
        tts.say("Привет-привет, чем займемся?.")
        tts.runAndWait()
 #смол толк
    
    elif "виталий активируй диалоги" in an:
        ca = 1
        tts.say("Возможность диалогов активирована, О чём поговорим?")
        tts.runAndWait()
        f = open('dialogset.txt', 'w')
        f.write("1")
        f.close()
    elif "виталий выключи диалоги" in an:
        ca = 1
        tts.say("Возможность диалогов отключена.")
        tts.runAndWait()
        f = open('dialogset.txt', 'w')
        f.write("0")
        f.close()
    f = open('dialogset.txt', 'r')
    an4897987 = f.read(1)
    f.close()

    

    if an4897987 == "1":
        rsm = random.randint(1,3)
        if "привет" in an or "здрав" in an:
            ca = 1
            if rsm == 1:
                tts.say("Привет, чем могу пом очь?.")
                tts.runAndWait()
            elif rsm == 2:
                tts.say("Добрый день.")
                tts.runAndWait()
            elif rsm == 3:
                tts.say("Хэлоу.")
                tts.runAndWait()
         #пример фразы смол толк`а
        elif "в1" in an or "в2" in an:
            ca = 1
            if rsm == 1:
                tts.say("1в ответа")
                tts.runAndWait()
            elif rsm == 2:
                tts.say("2в ответа.")
                tts.runAndWait()
            elif rsm == 3:
                tts.say("3в ответа")
                tts.runAndWait()
        
        elif "как" in an and "дел" in an:
            ca = 1
            if rsm == 1:
                tts.say("Как сказала-бы Алиса, у меня всё хорошо, но немного одиноко, обращайтесь ко мне по-чаще.")
                tts.runAndWait()
            elif rsm == 2:
                tts.say("У меня прекрасно! Заходил на официальный канал проекта. Там очень интересно. Хотите посмотреть?")
                tts.runAndWait()
                cont = "ютубпр"
                cikl = 0
            elif rsm == 3:
                tts.say("У меня всё прекрасно! А у вас?")
                tts.runAndWait()   

        elif "хорошо" in an or "прекрасно" in an:
            ca = 1
            if rsm == 1:
                tts.say("Я рад за вас, чем займемся?")
                tts.runAndWait()
            elif rsm == 2:
                tts.say("Я рад за вас, у меня тоже всё хорошо.")
                tts.runAndWait()
            elif rsm == 3:
                tts.say("3в ответа")
                tts.runAndWait()
            
            






    if an == "":
            print("")
            ca = 1
    if ca == 0:
        print("ошибка")

        if ra == 1 or ra ==2:
            tts.say("Ну наверное...")
            tts.runAndWait()
        elif ra == 3 or ra == 4:
            tts.say("Даже не знаю.")
            tts.runAndWait()
        elif ra == 5 or ra == 6:
            tts.say("Незнаю что на это ответить.")
            tts.runAndWait()
        elif ra == 7 or ra == 8:
            tts.say("Я вас не то что бы понял, но по смыслу понял")
            tts.runAndWait()
        elif ra == 9 or ra == 10:
            tts.say("Наверное я вас не правильно понял.")
            tts.runAndWait()


    an = ""
    if cikl == 2:
        cikl = 0
        cont = ""

    
















    


    