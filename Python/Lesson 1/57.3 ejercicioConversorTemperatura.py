celcius = float(input('Ingrese una temperatura en °C: '))
fahrenheit = float(input('Ingrese una temperatura en °F: '))

def conversorCelciusAFahrenheit (celcius, fahrenheit):
    fahrenheit =  ((celcius*9)/5) + 32
    return fahrenheit

def conversorFarenheitACelcius (fahrenheit, celcius):
    celcius = ((fahrenheit-32)*5) / 9
    return celcius

fahrenheitConvertido = conversorCelciusAFahrenheit(celcius, fahrenheit)
print(f'La conversión de °C a °F da un total de: {fahrenheitConvertido} °F')

celciusConvertido = conversorFarenheitACelcius(celcius, fahrenheit)
print(f'La conversión de °F a °C da un total de: {celciusConvertido} °C')


