#Виталий 5.0 Beta
#Разработчик: Глеб Пряхин (почта для отзывов и предложений: glebilic@gmail.com)
#сайт ассисента: виталий.online, либо http://vitaliy.renderforestsites.com/



#Библиотеки____________________________________________________________________________

#    системная информация и консоль
import os
import time
from datetime import datetime
import random
from random import choice
import keyboard
import tkinter as tk
import pyautogui


#    Qt
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QShortcut, QLabel, QApplication, QHBoxLayout, QDesktopWidget
from PyQt5.QtCore import pyqtSlot


#    распознавание речи
import speech_recognition
import pyaudio
import sounddevice as sd

#    синтез речи и музыка
import pyttsx3
import wave

#    библиотеки для функций
import webbrowser
import requests


#Визуал_____________________________________________________________________________________
class mywindow(QtWidgets.QMainWindow):  
    
    def __init__(self):  
        super(mywindow, self).__init__()  
        self.setWindowFlags( QtCore.Qt.WindowCloseButtonHint )
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def location_on_the_screen(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height() - sg.height() - widget.height()
        self.move(x, y)
    def btnClicked(self):
            try:
                system(data)
            except:
                exit()
    def keyPressEvent(self, e):  
        if int(e.modifiers()) == (QtCore.Qt.AltModifier):  
            if e.key() == 86:
                self.btnClicked()
            if e.key() == 1052:
                self.btnClicked()
                

class Ui_MainWindow(object):
    def setupUi(self, V5):
        V5.setObjectName("V5")
        V5.resize(121, 90)
        V5.setMinimumSize(QtCore.QSize(121, 90))
        V5.setMaximumSize(QtCore.QSize(121, 90))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        V5.setWindowIcon(icon)
        V5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton = QtWidgets.QPushButton(V5)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 121, 61))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setText("")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(V5)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(V5)
        QtCore.QMetaObject.connectSlotsByName(V5)

    def retranslateUi(self, V5):
        _translate = QtCore.QCoreApplication.translate
        V5.setWindowTitle(_translate("V5", "Виталий 5"))
        self.label_2.setText(_translate("V5", "<html><head/><body><p align=\"center\">(alt+v)</p></body></html>"))



#Данные из  data.txt_________________________________________________________________________
#    Создаем переменную data из файла data.txt
storage = open("data.txt", "r", encoding="utf-8")
data = storage.read()
storage.close()
#    тут ассистент сохраняет имя пользователя, так сказать его юзернэйм
greeting = data[data.find("greeting<")+9:data.find(">greeting")]
#    достаем из data ссылку на почтовый сервис, которым пользуется юзер-                    
email = data[data.find("email<")+6:data.find(">email")]
#    достаем список сайтов из базы ассистента
sites = data[data.find("sites<")+8:data.find(">sites")]
namesites = data[data.find("namesites<")+12:data.find(">namesites")]
sites = sites.split(" | ")
namesites = namesites.split(" | ")
#    достаем список программ из базы ассистента
programs = data[data.find("programs<")+11:data.find(">programs")]
nameprograms = data[data.find("nameprograms<")+15:data.find(">nameprograms")]
closeprograms = data[data.find("closeprograms<")+11:data.find(">closeprograms")]
programs = programs.split(" | ")
nameprograms = nameprograms.split(" | ")
closeprograms = closeprograms.split(" | ")


#Синтез речи и музыка_______________________________________________________________________
#    синтез речи
tts = pyttsx3.init()
speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
for voice in voices:
    if voice.name == 'Mikhail':
        tts.setProperty('voice', voice.id)
def say(t):
    tts.say(t)
    tts.runAndWait()
#    музыка
def sound(track):
        wf = wave.open(track + '.wav')
        p = pyaudio.PyAudio()
        chunk = 1024
        stream = p.open(format = p.get_format_from_width(wf.getsampwidth()), channels = wf.getnchannels(), rate = wf.getframerate(), output = True)
        data = wf.readframes(chunk)
        a = 0
        while a < 500:
            stream.write(data)
            data = wf.readframes(chunk)
            a = a + 1

#Распознавание речи__________________________________________________________________________
def record_and_recognize_audio(*args: tuple):
    with micro:
        recognized_data = ""

        # тут шумодав шум давит
        recognizer.adjust_for_ambient_noise(micro, duration=2)


        try:
            sound("ok")
            audio = recognizer.listen(micro, 5, 5)

        except speech_recognition.WaitTimeoutError:
            sound("error")
            say("Видимо возникли проблемы с микрофоном... Советую вам проверить подключен-ли микрофон и не отошел-ли штекер из разьема")
            return
                

        # отправка запроса на google 
        try:
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # если нет интернета - пишем ошибку
        except speech_recognition.RequestError:
            sound("error")
            say("Какая-то фигня с интернетом. Проверьте пожалуйста, включен ли вай фай, либо не отошел-ли кабель эзернет")
            exit()
        try:
            return recognized_data
        except:
            sound("error")
            say("Произошла неизвестная ошибка! Я уже решаю проблему.")
if __name__ == "__main__":
    try:
        # Устройства записи
        micro = speech_recognition.Microphone()
        recognizer = speech_recognition.Recognizer()
    except:
        say("Видимо возникли проблемы с микрофоном... Советую вам проверить подключен-ли микрофон и не отошел-ли штекер из разьема")
        exit()

#Функции ассистента___________________________________________________________________________________________________________
#    поиск и открытие сайтов в интернете
def web(search_name):
    if "почт" in search_name:
        search_name = search_name[:search_name.find("почт")+len("почт")]
    for site_name in namesites:
        if site_name in search_name:
            webbrowser.open(sites[namesites.index(site_name)])
            return 
    for startphrase in ("найди", "открой", "включи", "запусти"):   
        if startphrase in search_name:
            search_name = search_name[search_name.find(startphrase)+len(startphrase):]
    webbrowser.open("https://www.google.com/search?q=" + search_name)
    say("Вот результаты по запросу "+search_name)
#    открытие и закрытие пропрамм
def openapp(program_search):
    if "закрой" in program_search:
        for program_site in namesites:
            if program_site in program_search:
                os.system("TASKKILL /IM chrome.exe")
                return        
        for program_name in nameprograms:
            if program_name in program_search:
                os.system(closeprograms[nameprograms.index(program_name)])
                return
    else:
        for program_name in nameprograms:
            if program_name in program_search:
                os.system(programs[nameprograms.index(program_name)])
                return
        web(program_search)
#    чтение вслух
def play():
    root = tk.Tk()
    root.withdraw()
    say(root.clipboard_get())
#    запись
def rec():
    say("Начинаю вас слушать. После окончания записи, текст сам появиться в любом выбраном вами поле ввода. Для остановки записи скажите останови запись")
    recwasused = False
    while True:
        # старт записи речи с последующим выводом распознанной речи 
        rectext = record_and_recognize_audio()
        if recwasused == True:
            if rectext == "":
                continue
            rectext = " "+rectext
        if rectext == None:
            continue
        if "останови запись" in rectext:
            sound("stop")
            break
        elif "ввод" in rectext or "отправ" in rectext or "enter" in rectext:
            pyautogui.press("enter")
            sound("stop")
            break
        command = 'echo ' + rectext + '| clip'
        os.system(command)
        pyautogui.keyDown("ctrl")
        pyautogui.press("v")
        pyautogui.keyUp("ctrl")


        recwasused = True
#    работа со skype
def skype(skypedo):
    if skypedo == "call":
        say("Начинаю вызов")
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.press("k")
        pyautogui.keyUp("ctrl")
        pyautogui.keyUp("shift")
    elif skypedo == "uncall":
        say("Завершаю звонок, до свидания")
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.press("h")
        pyautogui.keyUp("ctrl")
        pyautogui.keyUp("shift")
def power(powerdo):
    if "выкл" in powerdo or "завер" in powerdo and "комп" in powerdo:
        say("Отключаю компьютер через 10 секунд!")
        sound("loading 10 seconds")
        sound("off")
        os.system('shutdown -s')
    elif "спящ" in powerdo:
        sound("off2")
        os.system('rundll32 powrprof.dll,SetSuspendState 0,1,0')
    elif "блок" in powerdo:
        os.system("Rundll32.exe user32.dll,LockWorkStation") 



#Главный цикл___________________________________________________________________________________
def system(data):
    while True:
        now = datetime.now() 
        # старт записи речи с последующим выводом распознанной речи 
        an = record_and_recognize_audio()
        if an == "":
            sound("error")
            return
        elif an == None:
            continue
        else:
            break 


    if "открой" in an or "найди" in an or "включи" in an or "закрой" in an or an in namesites or an in nameprograms:
        sound("stop")
        openapp(an)
        return


    elif "пи" in an:
        sound("stop")
        rec()
        return
    elif "чит" in an:
        sound("stop")
        play()
        return


    elif "врем" in an:
        sound("stop")
        say("Сейчас " + str(now.hour) + " " + str(now.minute))
        return


    elif "звон" in an:
        sound("stop")
        skype("call")
        return
    elif "сброс" in an:
        sound("stop")
        skype("uncall")
        return


    elif "завер" in an and "раб" or "выключ" in an:
        sound("stop")
        power("выкл")
        return
    elif "засни" in an or "спящ" in an:
        sound("stop")
        power("спящ")
        return
    elif "блок" in an:
        sound("stop")
        power("блок")
        return
    elif "пока" in an or "до свидани" in an:
        sound("off2")
        exit()

    elif "возврат в исходное состояние" in an:
        sound("stop")
        say("Возврат в меня в исходное состояние произойдет через 20 секунд! Для отмены откройте и закройте мою программу.")
        sound("loading 10 seconds")
        sound("loading 10 seconds")
        sound("off")
        data = data.replace("familiar", "unfamiliar")
        storage = open("data.txt", "w", encoding="utf-8")
        storage.write(data)
        storage.close()
        sound("on")
        say("Возврат в исходное состояние окончен.")
        exit()


    else:
        sound("problem")
        if "витал" in an:
            say("Ой.. Похоже такой команды не существует, вы можете посмотреть все доступные команды на моём сайте, для этого скажите: открой список команд. Также напоминаю, что команды диалогов больше не поддерживаются.")
            return


if "unfamiliar" in greeting:
    greeting = "familiar"
    webbrowser.open("https://sites.google.com/view/vitaliy5/ассистент-успешно-был-загружен")
    sound("first on")
    say("Виталий 5 был успешно установлен! На этой странице вы найдете много полезной информации.")
    data = data.replace("unfamiliar", "familiar")
    storage = open("data.txt", "w", encoding="utf-8")
    storage.write(data)
    storage.close()
app = QtWidgets.QApplication([])  
application = mywindow()
if keyboard.is_pressed('v') and keyboard.is_pressed('alt'):
    system(data)  
application.location_on_the_screen()
application.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
application.show()    
sys.exit(app.exec())

