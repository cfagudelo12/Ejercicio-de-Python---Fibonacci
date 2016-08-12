numLimString = raw_input("Introduzca el limite para los numeros Fibonacci: ")
numLim = int(numLimString)
num0 = 0
num1 = 1
fib = num0+num1
resultado = str(fib)
while fib < numLim:
    resultado += ", " + str(fib)
    num0 = num1
    num1 = fib
    fib = num0+num1
print(resultado)
