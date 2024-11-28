from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser

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

            # Получаем URL для OpenStreetMap
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lng}"

            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return {
                    "coordinates": f"Широта: {lat}, Долгота: {lng}\nСтрана: {country}\nРегион: {region}",
                    "map_url": osm_url
                }
            else:
                return {
                    "coordinates": f"Широта: {lat}, Долгота: {lng}\nСтрана: {country}.",
                    "map_url": osm_url
                }
        else:
            return {"coordinates": "Город не найден", "map_url": None}
    except Exception as e:
        return f"Общая ошибка: {e}"

def show_coordinates(event=None):
    city = entry.get()
    result  = get_coordinates(city, key)
    label.config(text=result["coordinates"])
    # Сохраняем URL в глобальной переменной для доступа из другой функции
    global map_url
    map_url = result["map_url"]

def show_map():
    if map_url:
        webbrowser.open(map_url)


# Интерфейс
window = Tk()
window.title("Поиск координат города")
window.geometry("400x150")

key = '1828e03833594c74ae77282ddae5ff1c'
map_url = None

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

map_button = Button(text="Показать карту", command=show_map)
map_button.pack()

# Запуск приложения
window.mainloop()
