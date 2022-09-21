def TempConversion(kind, temp):
    if kind == "f":
        print((temp-32)*(5/9))
    else:
        print((temp*1.8)+32)

numeric = (input('type f or c '))
temp = int(input(f'temperature in {numeric} '))
TempConversion(numeric, temp)
