temp = input("Input the temperature you'd want to convert?: (eg: 45F, 23C etc)")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == 'C':
    result = int(round((9 * degree) / 5 + 32))
    o_convention = 'Fahrenheit'
elif i_convention.upper() == 'F':
    result = int(round((degree - 32) * 5 / 9))
    o_convention = 'Celsius'
else:
    print('Input proper unit')
    quit()

print('THe temperature in', o_convention, 'is', result, 'degrees.')
