print()
print('Wind Chill Table')
print('\tTemperature')
print('   ', end = '')
for temp in range(-20, 61, 10):
    print(format(temp, '8d'), end = '')
print()

# Print y values of table.
print('Speed  ', end = '')
for temp in range(-20, 61, 10):
    print('_______', end = '')
print('_________')

# Print calculations inside table.
for speed in range(10, 61, 5):
    print(speed, '|', end = '    ')
    for temp in range(-20, 61, 10):
        wind_chill = 35.74 + 0.6215 * temp \
                     - speed ** 0.16 * (35.75 \
                     - 0.4275 * temp)
        print(format(wind_chill, '6.2f'), end = '  ')
print()