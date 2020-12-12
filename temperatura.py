temperatura = float(input('Informe a temperatura em °C: '))
convF = (temperatura * (9/5)) + 32
convK = (temperatura + 273.15)

print(f'A temperatura de {temperatura :.1f}°C corresponde a {convF :.2f}°F \nE em Kelvin corresponde a {convK :.2f}K')

print(' ')

temperatura2 = float(input('Informe a temperatura em °F: '))
fc = (temperatura2 - 32) * 5/9
fk = (temperatura2 - 32) * 5/9 + 273.15

print(f'A temperatura de {temperatura2 :.1f}°F corresponde a {fc :.3f}°C \nE em Kelvin corresponde a {fk :.3f}K')

print(' ')

temperatura3 = float(input('Informe a temperatura em K: '))
kc = (temperatura3 - 273.15)
kf = (temperatura3 - 273.15) * 9/5 + 32

print(f'A temperatura de {temperatura3 :.1f}K corresponde a {kc :.1f}°C \nE em Fahrenheit corresponde a {kf :.1f}°F')
