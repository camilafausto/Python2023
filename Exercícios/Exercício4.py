#Exercício 1:
#Utilizando um loop "while", imprima os números de 1 a 10.
num = 1;

while num <= 10:
    print(num);
    num += 1;

print();

#Exercício 2:
#Utilizando um loop "for", imprima os números de 1 a 10.
for num in range(1,11):
    print(num);

print();

#Exercício 3:
#Utilizando um loop "while", calcule a soma dos números de 1 a 100.
num = 1;
soma = 0;

while num <= 100:
    soma += num;
    num += 1;

print("A soma dos números de 1 a 100: ", soma);
print();

#Exercício 4:
#Utilizando um loop "for", calcule a soma dos números de 1 a 100.
soma = 0;

for num in range (1, 101):
    soma += num;

print("A soma dos números de 1 a 100: ", soma);
print();

#Exercício 5:
#Utilizando um loop "while", imprima os números pares de 1 a 20.
num = 1;

while num <= 20:
    if num % 2 == 0:
        print(num);
    num += 1;

print();

#Exercício 6:
#Utilizando um loop "for", imprima os números pares de 1 a 20.
for num in range (1,21):
    if num % 2 == 0:
        print(num);
    num += 1;

print();

#Exercício 7:
#Utilizando um loop "while", inverta uma string digitada pelo usuário.
string = input("Digite uma string: ");
indice = len(string) - 1;
inverta = " ";

while indice >= 0:
    inverta += string[indice];
    indice -= 1;

print("String invertida: ", inverta);
print();

#Exercício 8:
#Utilizando um loop "for", verifique se uma palavra digitada pelo usuário é um palíndromo 
#(lê-se da mesma forma de trás para frente).

palavra = input("Digite uma palavra: ").lower()

palindromo = True;

for indice in range(len(palavra)):
    if palavra[indice] != palavra[-(indice + 1)]:
        palindromo = False;
        break

if palindromo:
    print(f"A palavra {palavra} é um palíndromo.")
else:
    print(f"A palavra {palavra} não é um palíndrmo.")

print();

#Exercício 9:
#Utilizando um loop "while", encontre o menor número inteiro cujo quadrado 
#seja maior do que 1000.

num = 1;

while num ** 2 <= 1000:
    num += 1;

print("O menor número inteiro cujo quadrado seja maior do que 1000: ", num);
print();

#Exercício 10:
#Utilizando um loop "for", imprima os elementos de uma lista em ordem inversa.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

for indice in range(len(lista) - 1, - 1, - 1):
    print(lista[indice]);

print();



