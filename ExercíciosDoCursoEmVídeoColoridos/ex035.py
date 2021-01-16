# a < b + c, b < a + c, c < a + b
a = float(input('\033[31mPrimeira reta:\033[m '))
b = float(input('\033[32mSegunda reta:\033[m '))
c = float(input('\033[33mTerceira reta:\033[m '))
if a < b + c and b < a + c and c < a + b:
    print('Essas retas \033[34;4;1mPODEM FORMAR TRIÂNGULO\033[m')
else:
    print('Essas retas \033[1;4;31mNÃO PODEM FORMAR TRIÂNGULO\033[m')
