# b - c < a < b + c == princípio para formar um triângulo e vice-versa
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('O segmentos acima NÃO PODEM FORMAR um triângulo')
