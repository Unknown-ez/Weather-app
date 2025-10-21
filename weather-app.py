import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family:calibri;           
                           }
            QLabel#city_label{
                font-size: 40pt;
                font-style: italic;               
                           }
            QLineEdit#city_input{
                font-size: 40pt;           
                           }
            QPushButton#get_weather_button{
                font-size: 30pt;
                font-weight: bold;       
                           }
            QLabel#temp_label{
                font-size: 75px;         
                           }
            QLabel#emoji_label{
                 font-size: 100px;
                 font-family: Segoe UI emoji;          
                           }
            QLabel#description_label{
                 font-size: 50px;          
                           }             
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        
        api_key = "da9fb65036da8799fe4f04818d5d9a75"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
 
    try:
        response = requests.get(url=url)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") == 200:
            self.display_weather(data)
        else:
            self.display_error(data)

    except requests.exceptions.HTTPError as http_error:
        match response.status_code:
            case 400:
                print("Bad Request — Please check your input.")
            case 401:
                print("Unauthorized — Invalid API key.")
            case 403:
                print("Forbidden — Access denied.")
            case 404:
                print("Not Found — City not found.")
            case 500:
                print("Internal Server Error — Please try again later.")
            case 502:
                print("Bad Gateway — Invalid response from the server.")
            case 503:
                print("Service Unavailable — Server is down.")
            case 504:
                print("Gateway Timeout — No response from the server.")
            case _:
                print(f"HTTP Error: {http_error}")

    except requests.exceptions.RequestException:
                pass

    def display_error(self, message):
        pass

    def display_weather(self, data):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
