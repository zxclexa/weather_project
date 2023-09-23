import datetime

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from API import weather_api


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon('overcastday_weather_sun_cloudy_4493.png'))
        MainWindow.resize(661, 973)
        MainWindow.setMinimumSize(QtCore.QSize(661, 821))
        MainWindow.setMaximumSize(QtCore.QSize(661, 973))
        MainWindow.setStyleSheet("background-color: #1E90FF;\n"
"border-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 661, 231))
        self.frame.setStyleSheet("background-color: #00BFFF")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.weather_brodcast = QtWidgets.QLabel(self.frame)
        self.weather_brodcast.setGeometry(QtCore.QRect(20, 0, 421, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.weather_brodcast.setFont(font)
        self.weather_brodcast.setObjectName("weather_brodcast")
        self.city = QtWidgets.QLineEdit(self.frame)
        self.city.setGeometry(QtCore.QRect(20, 120, 421, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(20)
        self.city.setFont(font)
        self.city.setStyleSheet("background-color: #ADD8E6;\n"
"border: 2px solid #00008B;\n"
"border-radius: 20;\n"
"color: black")
        self.city.setText("")
        self.city.setAlignment(QtCore.Qt.AlignCenter)
        self.city.setObjectName("city")
        self.weather_pic = QtWidgets.QLabel(self.frame)
        self.weather_pic.setGeometry(QtCore.QRect(440, 20, 101, 91))
        self.weather_pic.setText("")
        self.weather_pic.setPixmap(QtGui.QPixmap("overcastday_weather_sun_cloudy_4493.png"))
        self.weather_pic.setObjectName("weather_pic")
        self.find_button = QtWidgets.QPushButton(self.frame)
        self.find_button.setGeometry(QtCore.QRect(470, 120, 161, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.find_button.setFont(font)
        self.find_button.setStyleSheet("QPushButton {\n"
"    background-color: #1E90FF;\n"
"    border: 2px solid #00008B;\n"
"    border-radius: 20;\n"
"}\n"
"\n"
"QPushButtin:pressed {\n"
"    background-color: #00008B\n"
"}")
        self.find_button.setObjectName("find_button")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 40, 41, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.clear_button = QtWidgets.QPushButton(self.frame)
        self.clear_button.setGeometry(QtCore.QRect(610, 80, 41, 31))
        self.clear_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.clear_button.setObjectName("clear_button")
        self.veter_metric = QtWidgets.QLabel(self.centralwidget)
        self.veter_metric.setGeometry(QtCore.QRect(500, 890, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        self.veter_metric.setFont(font)
        self.veter_metric.setObjectName("veter_metric")
        self.press = QtWidgets.QLabel(self.centralwidget)
        self.press.setGeometry(QtCore.QRect(20, 810, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.press.setFont(font)
        self.press.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.press.setObjectName("press")
        self.temp_ = QtWidgets.QLineEdit(self.centralwidget)
        self.temp_.setGeometry(QtCore.QRect(330, 570, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.temp_.setFont(font)
        self.temp_.setStyleSheet("background-color: #ADD8E6;\n"
"border: 2px solid #00008B;\n"
"border-radius: 15;\n"
"color: black")
        self.temp_.setText("")
        self.temp_.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_.setObjectName("temp_")
        self.veter_ = QtWidgets.QLineEdit(self.centralwidget)
        self.veter_.setGeometry(QtCore.QRect(330, 890, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.veter_.setFont(font)
        self.veter_.setStyleSheet("background-color: #ADD8E6;\n"
"border: 2px solid #00008B;\n"
"border-radius: 15;\n"
"color: black")
        self.veter_.setText("")
        self.veter_.setAlignment(QtCore.Qt.AlignCenter)
        self.veter_.setObjectName("veter_")
        self.date = QtWidgets.QLineEdit(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(330, 410, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.date.setFont(font)
        self.date.setStyleSheet("background-color: #ADD8E6;\n"
"border: 2px solid #00008B;\n"
"border-radius: 15;\n"
"color: black")
        self.date.setText("")
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setObjectName("date")
        self.vlaga = QtWidgets.QLabel(self.centralwidget)
        self.vlaga.setGeometry(QtCore.QRect(20, 730, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.vlaga.setFont(font)
        self.vlaga.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.vlaga.setObjectName("vlaga")
        self.progno_na = QtWidgets.QLabel(self.centralwidget)
        self.progno_na.setGeometry(QtCore.QRect(20, 410, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.progno_na.setFont(font)
        self.progno_na.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progno_na.setObjectName("progno_na")
        self.weather_in_city = QtWidgets.QLabel(self.centralwidget)
        self.weather_in_city.setGeometry(QtCore.QRect(20, 250, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.weather_in_city.setFont(font)
        self.weather_in_city.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.weather_in_city.setObjectName("weather_in_city")
        self.feel_metric = QtWidgets.QLabel(self.centralwidget)
        self.feel_metric.setGeometry(QtCore.QRect(500, 650, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(26)
        self.feel_metric.setFont(font)
        self.feel_metric.setObjectName("feel_metric")
        self.vlaga_ = QtWidgets.QLineEdit(self.centralwidget)
        self.vlaga_.setGeometry(QtCore.QRect(330, 730, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.vlaga_.setFont(font)
        self.vlaga_.setStyleSheet("background-color: #ADD8E6;\n"
"border: 2px solid #00008B;\n"
"border-radius: 15;\n"
"color: black")
        self.vlaga_.setText("")
        self.vlaga_.setAlignment(QtCore.Qt.AlignCenter)
        self.vlaga_.setObjectName("vlaga_")
        self.press_metric = QtWidgets.QLabel(self.centralwidget)
        self.press_metric.setGeometry(QtCore.QRect(500, 810, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        self.press_metric.setFont(font)
        self.press_metric.setObjectName("press_metric")
        self.vlaga_metric = QtWidgets.QLabel(self.centralwidget)
        self.vlaga_metric.setGeometry(QtCore.QRect(500, 730, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        self.vlaga_metric.setFont(font)
        self.vlaga_metric.setObjectName("vlaga_metric")
        self.feel_like = QtWidgets.QLabel(self.centralwidget)
        self.feel_like.setGeometry(QtCore.QRect(20, 650, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.feel_like.setFont(font)
        self.feel_like.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.feel_like.setObjectName("feel_like")
        self.press_ = QtWidgets.QLineEdit(self.centralwidget)
        self.press_.setGeometry(QtCore.QRect(330, 810, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.press_.setFont(font)
        self.press_.setStyleSheet("background-color: #ADD8E6;\n"
"border: 2px solid #00008B;\n"
"border-radius: 15;\n"
"color: black")
        self.press_.setText("")
        self.press_.setAlignment(QtCore.Qt.AlignCenter)
        self.press_.setObjectName("press_")
        self.weath = QtWidgets.QLabel(self.centralwidget)
        self.weath.setGeometry(QtCore.QRect(20, 490, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.weath.setFont(font)
        self.weath.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.weath.setObjectName("weath")
        self.temp = QtWidgets.QLabel(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(20, 570, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.temp.setFont(font)
        self.temp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.temp.setObjectName("temp")
        self.veter = QtWidgets.QLabel(self.centralwidget)
        self.veter.setGeometry(QtCore.QRect(20, 890, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.veter.setFont(font)
        self.veter.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.veter.setObjectName("veter")
        self.city_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.city_2.setGeometry(QtCore.QRect(330, 250, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.city_2.setFont(font)
        self.city_2.setStyleSheet("background-color: #ADD8E6;\n"
"border: 2px solid #00008B;\n"
"border-radius: 15;\n"
"color: black")
        self.city_2.setText("")
        self.city_2.setAlignment(QtCore.Qt.AlignCenter)
        self.city_2.setObjectName("city_2")
        self.temp_metric = QtWidgets.QLabel(self.centralwidget)
        self.temp_metric.setGeometry(QtCore.QRect(500, 570, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(26)
        self.temp_metric.setFont(font)
        self.temp_metric.setObjectName("temp_metr")
        self.temp_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.temp_2.setGeometry(QtCore.QRect(330, 650, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.temp_2.setFont(font)
        self.temp_2.setStyleSheet("background-color: #ADD8E6;\n"
"border: 2px solid #00008B;\n"
"border-radius: 15;\n"
"color: black")
        self.temp_2.setText("")
        self.temp_2.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_2.setObjectName("temp_2")
        self.veter_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.veter_2.setGeometry(QtCore.QRect(330, 1170, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.veter_2.setFont(font)
        self.veter_2.setStyleSheet("background-color: #ADD8E6;\n"
"border: 2px solid #00008B;\n"
"border-radius: 15;\n"
"color: black")
        self.veter_2.setText("")
        self.veter_2.setAlignment(QtCore.Qt.AlignCenter)
        self.veter_2.setObjectName("veter_2")
        self.weath_ = QtWidgets.QLineEdit(self.centralwidget)
        self.weath_.setGeometry(QtCore.QRect(330, 490, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.weath_.setFont(font)
        self.weath_.setStyleSheet("background-color: #ADD8E6;\n"
"border: 2px solid #00008B;\n"
"border-radius: 15;\n"
"color: black")
        self.weath_.setText("")
        self.weath_.setAlignment(QtCore.Qt.AlignCenter)
        self.weath_.setObjectName("weath_")
        self.dolgota_ = QtWidgets.QLineEdit(self.centralwidget)
        self.dolgota_.setGeometry(QtCore.QRect(560, 330, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.dolgota_.setFont(font)
        self.dolgota_.setStyleSheet("background-color: #ADD8E6;\n"
"border: 2px solid #00008B;\n"
"border-radius: 15;\n"
"color: black")
        self.dolgota_.setText("")
        self.dolgota_.setAlignment(QtCore.Qt.AlignCenter)
        self.dolgota_.setObjectName("dolgota_")
        self.location = QtWidgets.QLabel(self.centralwidget)
        self.location.setGeometry(QtCore.QRect(20, 330, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.location.setFont(font)
        self.location.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.location.setObjectName("location")
        self.shirota_ = QtWidgets.QLineEdit(self.centralwidget)
        self.shirota_.setGeometry(QtCore.QRect(390, 330, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.shirota_.setFont(font)
        self.shirota_.setStyleSheet("background-color: #ADD8E6;\n"
"border: 2px solid #00008B;\n"
"border-radius: 15;\n"
"color: black")
        self.shirota_.setText("")
        self.shirota_.setAlignment(QtCore.Qt.AlignCenter)
        self.shirota_.setObjectName("shirota_")
        self.shirota = QtWidgets.QLabel(self.centralwidget)
        self.shirota.setGeometry(QtCore.QRect(310, 330, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.shirota.setFont(font)
        self.shirota.setAlignment(QtCore.Qt.AlignCenter)
        self.shirota.setObjectName("shirota")
        self.dolgota = QtWidgets.QLabel(self.centralwidget)
        self.dolgota.setGeometry(QtCore.QRect(480, 330, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(14)
        self.dolgota.setFont(font)
        self.dolgota.setAlignment(QtCore.Qt.AlignCenter)
        self.dolgota.setObjectName("dolgota")
        self.country = QtWidgets.QLineEdit(self.centralwidget)
        self.country.setGeometry(QtCore.QRect(560, 250, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.country.setFont(font)
        self.country.setStyleSheet("background-color: #ADD8E6;\n"
"border: 2px solid #00008B;\n"
"border-radius: 15;\n"
"color: black")
        self.country.setText("")
        self.country.setAlignment(QtCore.Qt.AlignCenter)
        self.country.setObjectName("country")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WeatherForecast"))
        self.weather_brodcast.setText(_translate("MainWindow", "Прогноз погоды"))
        self.find_button.setText(_translate("MainWindow", "Найти"))
        self.pushButton_3.setText(_translate("MainWindow", "Eng"))
        self.clear_button.setText(_translate("MainWindow", "Чист"))
        self.veter_metric.setText(_translate("MainWindow", "м/с"))
        self.press.setText(_translate("MainWindow", "Давление:"))
        self.vlaga.setText(_translate("MainWindow", "Влажность:"))
        self.progno_na.setText(_translate("MainWindow", "Прогноз на:"))
        self.weather_in_city.setText(_translate("MainWindow", "Погода в городе:"))
        self.feel_metric.setText(_translate("MainWindow", "°C"))
        self.press_metric.setText(_translate("MainWindow", "мм.рт.ст"))
        self.vlaga_metric.setText(_translate("MainWindow", "кг/м³ "))
        self.feel_like.setText(_translate("MainWindow", "Ощущается как:"))
        self.weath.setText(_translate("MainWindow", "Погода:"))
        self.temp.setText(_translate("MainWindow", "Температура:"))
        self.veter.setText(_translate("MainWindow", "Скорость ветра:"))
        self.temp_metric.setText(_translate("MainWindow", "°C"))
        self.location.setText(_translate("MainWindow", "Местоположение:"))
        self.shirota.setText(_translate("MainWindow", "Шир:"))
        self.dolgota.setText(_translate("MainWindow", "Дол:"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

        self.city.setEnabled(True)
        self.city_2.setEnabled(False)
        self.date.setEnabled(False)
        self.weath_.setEnabled(False)
        self.temp_.setEnabled(False)
        self.vlaga_.setEnabled(False)
        self.press_.setEnabled(False)
        self.veter_.setEnabled(False)
        self.country.setEnabled(False)
        self.shirota_.setEnabled(False)
        self.dolgota_.setEnabled(False)
        self.find_button.setEnabled(True)

        self.find_button.clicked.connect(self.find)
        self.clear_button.clicked.connect(self.clear)
        self.pushButton_3.clicked.connect(self.change_lang)

    def find(self):
        try:
            r = requests.get(
                f'http://api.openweathermap.org/data/2.5/weather?q={self.city.text()}&appid={weather_api}&units=metric'
            )
            data = r.json()

            r_2 = requests.get(
                f'http://api.openweathermap.org/data/2.5/weather?q={self.city.text()}&appid={weather_api}'
            )
            data_2 = r_2.json()
            if self.pushButton_3.text() == 'Eng':
                code_to_smile = {
                    "Clear": "Ясно \U00002600",
                    "Clouds": "Облачно \U00002601",
                    "Rain": "Дождь \U00002614",
                    "Drizzle": "Дождь \U00002614",
                    "Thunderstorm": "Гроза \U000026A1",
                    "Snow": "Снег \U0001F328",
                    "Mist": "Туман \U0001F32B"
                }
            elif self.pushButton_3.text() == 'Рус':
                code_to_smile = {
                    "Clear": "Clear \U00002600",
                    "Clouds": "Clouds \U00002601",
                    "Rain": "Rain \U00002614",
                    "Drizzle": "Drizzle \U00002614",
                    "Thunderstorm": "Thunderstorm \U000026A1",
                    "Snow": "Snow \U0001F328",
                    "Mist": "Mist \U0001F32B"
                }

            self.date.setText(f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}')
            if self.pushButton_3.text() == 'Eng':
                self.temp_.setText(f'{data["main"]["temp"]}')
                self.temp_2.setText(f'{data["main"]["feels_like"]}')
            elif self.pushButton_3.text() == 'Рус':
                self.temp_.setText(f'{data_2["main"]["temp"]}')
                self.temp_2.setText(f'{data_2["main"]["feels_like"]}')
            self.vlaga_.setText(f'{data["main"]["humidity"]}')
            self.press_.setText(f'{data["main"]["pressure"]}')
            self.veter_.setText(f'{data["wind"]["speed"]}')
            self.city_2.setText(f'{data["name"]}')
            self.country.setText(f'{data["sys"]["country"]}')
            self.shirota_.setText(f'{data["coord"]["lat"]:.2f}')
            self.dolgota_.setText(f'{data["coord"]["lon"]:.2f}')
            if data["weather"][0]["main"] in code_to_smile:
                self.weath_.setText(code_to_smile[data["weather"][0]["main"]])

        except Exception:
            self.city.clear()
            self.date.clear()
            self.city_2.clear()
            self.weath_.clear()
            self.temp_.clear()
            self.vlaga_.clear()
            self.press_.clear()
            self.veter_.clear()
            self.country.clear()
            self.shirota_.clear()
            self.dolgota_.clear()
            self.temp_2.clear()

            if self.pushButton_3.text() == 'Eng':
                self.city.setText('Усп..Ошибка:(')
            elif self.pushButton_3.text() == 'Рус':
                self.city.setText('Oops..Error:(')

    def clear(self):
        self.city.clear()
        self.date.clear()
        self.city_2.clear()
        self.weath_.clear()
        self.temp_.clear()
        self.vlaga_.clear()
        self.press_.clear()
        self.veter_.clear()
        self.country.clear()
        self.shirota_.clear()
        self.dolgota_.clear()
        self.temp_2.clear()
        self.city.setEnabled(True)

    def change_lang(self):

        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={self.city.text()}&appid={weather_api}&units=metric'
        )
        data = r.json()

        r_2 = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={self.city.text()}&appid={weather_api}'
        )
        data_2 = r_2.json()

        if self.pushButton_3.text() == 'Eng':
            if self.temp_.text() != '':
                self.temp_.setText(f'{data_2["main"]["temp"]}')
            if self.temp_2.text() != '':
                self.temp_2.setText(f'{data_2["main"]["feels_like"]}')
            if self.weath_.text() != '':
                if self.weath_.text() == "Ясно \U00002600":
                    self.weath_.setText("Clear \U00002600")
                elif self.weath_.text() == "Дождь \U00002614":
                    self.weath_.setText("Rain \U00002614")
                elif self.weath_.text() == "Облачно \U00002601":
                    self.weath_.setText("Clouds \U00002601")
                elif self.weath_.text() == "Гроза \U000026A1":
                    self.weath_.setText("Thunderstorm \U000026A1")
                elif self.weath_.text() == "Снег \U0001F328":
                    self.weath_.setText("Snow \U0001F328")
                elif self.weath_.text() == "Туман \U0001F32B":
                    self.weath_.setText("Mist \U0001F32B")
            self.weather_brodcast.setText('Weather Forecast')
            self.find_button.setText('Search')
            self.weather_in_city.setText('Weather in city:')
            self.progno_na.setText('Date:')
            self.weath.setText('Weather:')
            self.temp.setText('Temperature:')
            self.feel_like.setText('Feels like:')
            self.location.setText('Location:')
            self.shirota.setText('Lat:')
            self.dolgota.setText('Lon:')
            self.vlaga.setText('Humidity:')
            self.press.setText('Pressure:')
            self.veter.setText('Wind:')
            self.pushButton_3.setText('Рус')
            self.clear_button.setText('Clr')
            self.temp_metric.setText('°F')
            self.feel_metric.setText('°F')
            self.vlaga_metric.setText('kg/m³')
            self.press_metric.setText('mm Hg')
            self.veter_metric.setText('m/sec')

        elif self.pushButton_3.text() == 'Рус':
            if self.temp_.text() != '':
                self.temp_.setText(f'{data["main"]["temp"]}')
            if self.temp_2.text() != '':
                self.temp_2.setText(f'{data["main"]["feels_like"]}')
            if self.weath_.text() != '':
                if self.weath_.text() == "Clear \U00002600":
                    self.weath_.setText("Ясно \U00002600")
                elif self.weath_.text() == "Rain \U00002614":
                    self.weath_.setText("Дождь \U00002614")
                elif self.weath_.text() == "Drizzle \U00002614":
                    self.weath_.setText("Дождь \U00002614")
                elif self.weath_.text() == "Clouds \U00002601":
                    self.weath_.setText("Облачно \U00002601")
                elif self.weath_.text() == "Thunderstorm \U000026A1":
                    self.weath_.setText("Гроза \U000026A1")
                elif self.weath_.text() == "Snow \U0001F328":
                    self.weath_.setText("Снег \U0001F328")
                elif self.weath_.text() == "Mist \U0001F32B":
                    self.weath_.setText("Туман \U0001F32B")
            self.weather_brodcast.setText('Прогноз погоды')
            self.find_button.setText('Найти')
            self.weather_in_city.setText('Погода в городе:')
            self.progno_na.setText('Прогноз на:')
            self.weath.setText('Погода:')
            self.temp.setText('Температура:')
            self.vlaga.setText('Влажность:')
            self.press.setText('Давление:')
            self.veter.setText('Ветер:')
            self.location.setText('Местоположение:')
            self.shirota.setText('Шир:')
            self.dolgota.setText('Дол:')
            self.feel_like.setText('Ощущается как:')
            self.feel_metric.setText('°C')
            self.pushButton_3.setText('Eng')
            self.clear_button.setText('Чист')
            self.temp_metric.setText('°C')
            self.vlaga_metric.setText('кг/м³')
            self.press_metric.setText('мм.рт.ст')
            self.veter_metric.setText('м/с')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
