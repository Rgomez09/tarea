import requests

def obtener_temperatura(ciudad, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"
    respuesta = requests.get(url)
    datos = respuesta.json()

    if datos["cod"] != "404":
        temperatura_actual = datos["main"]["temp"]
        temperatura_maxima = datos["main"]["temp_max"]
        temperatura_minima = datos["main"]["temp_min"]

        # Convertir las temperaturas de Kelvin a Celsius
        temperatura_actual_celsius = temperatura_actual - 273.15
        temperatura_maxima_celsius = temperatura_maxima - 273.15
        temperatura_minima_celsius = temperatura_minima - 273.15

        return temperatura_maxima_celsius, temperatura_minima_celsius
    else:
        return None, None

ciudad = input("London")
api_key = "670de0091ad9b9989a1dea901457aadf"  # Reemplaza con tu propia API key de OpenWeatherMap

temperatura_max, temperatura_min = obtener_temperatura(ciudad, api_key)

if temperatura_max is not None and temperatura_min is not None:
    print(f"Temperatura máxima: {temperatura_max}°C")
    print(f"Temperatura mínima: {temperatura_min}°C")
else:
    print("No se pudo obtener la temperatura para la ciudad especificada.")
