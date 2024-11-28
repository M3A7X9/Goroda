from opencage.geocoder import OpenCageGeocode

def get_coordinates(city, key):
    """ Получает координаты города, используя библиотеку OpenCage. """
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city)

        if results:
            # Возвращает первый результат
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return "Город не найден"
    except Exception as e:
        return f"Общая ошибка: {e}"

# Пример использования
key = '1828e03833594c74ae77282ddae5ff1c'
city = 'Москва'
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")
