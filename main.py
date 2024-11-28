from opencage.geocoder import OpenCageGeocode
from tkinter import *


def get_coordinates(city, key):
    """ Получает координаты города, используя библиотеку OpenCage. """
    try:
        geocoder = OpenCageGeocode(key)
        #results = geocoder.geocode(city, language='ru')
        results = geocoder.geocode(city, language='ru')

        if results:
            # Возвращает первый результат
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return f"Широта: {lat}, Долгота: {lng}\n Страна: {country}. Регион: {region}"
            else:
                return f"Широта: {lat}, Долгота: {lng}\n Страна: {country}"
        else:
            return "Город не найден"
    except Exception as e:
        return f"Общая ошибка: {e}"

def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=coordinates)

# Интерфейс
window = Tk()
window.title("Поиск координат города")
window.geometry("400x150")

key = '1828e03833594c74ae77282ddae5ff1c'
city = 'Москва'
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")

# Элементы интерфейса
entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)  # Привязка события нажатия Enter

button = Button(text="Поиск", command=show_coordinates)
button.pack()

label = Label(text="Введите город и нажмите Поиск")
label.pack()

# Запуск приложения
window.mainloop()
