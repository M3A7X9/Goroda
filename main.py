from opencage.geocoder import OpenCageGeocode

def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return "Город не найден"

# Пример использования
key = '1828e03833594c74ae77282ddae5ff1c'
city = 'Москва'
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")
