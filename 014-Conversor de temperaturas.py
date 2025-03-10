# Faça um programa que converta uma temperatura em graus celsius para graus fahrenheit.

temp_celsius = int(input('Digite um valor em graus celsius para conversão: '))
temp_fahrenheit = (temp_celsius * 1.8 + 32)
print(f'Graus Celsius: {temp_celsius:.2f}°C'
      f'\nGraus Fahrenheit: {temp_fahrenheit:.2f}°F')
