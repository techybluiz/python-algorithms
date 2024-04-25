# #set deleta valores duplicados(mas não garantem a ordem)
# s1 = set('Bianca')
# s1 = {1,2,3,2,1,3,4,5,6,7,8,2,3,3}
# print(4 in s1)
# for numero in s1:
#     print(numero)

# s1 = set()
# s1.add('Bianca') 
# s1.add(3)
# s1.discard('B')
# print(s1)
s2 = {1,2,3,4}
s3 = {4,5,6,7}
s4 =s2|s3 # união de dois sets
s4 =s2 & s3 # diferença entre os set
s4 =s2 ^ s3 # ertorna os numeros que não foram repetidos
print(s4)

letras = set()

while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'b' in letras:
        print('Você encontrou a letra misteriosa')
        break
    print(letras)

