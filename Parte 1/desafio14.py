temp = float(input('Informe a temperatura em °C: '))
convF = (temp * (9/5)) + 32
convK = (temp + 273.15)

print('A temperatura em {:.1f}°C corresponde a {:.2f}°F \nE em Kelvin corresponde a {:.2f}K'.format(temp, convF, convK))

print(' ')

tem = float(input('Informe a temperatura em °F: '))
fc = (tem - 32) * 5/9
fk = (tem - 32) * 5/9 + 273.15

print('A temperatura em {:.1f}°F corresponde a {:.3f}°C \nE em Kelvin corresponde a {:.3f}K'.format(tem, fc, fk))

print(' ')

t = float(input('Informe a temperatura em K: '))
kc = (t - 273.15)
kf = (t - 273.15) * 9/5 + 32

print('A temperatura em {:.1f}K corresponde a {:.2f}°C \nE em Fahrenheit corresponde a {:.1f}°F'.format(t, kc, kf))
