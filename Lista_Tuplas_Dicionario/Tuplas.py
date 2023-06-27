tupla1 =(1,2,3,4,5,6);
tupla2 = ("a", "b", "c");
tupla3 = (1, "Hello, True");
tupla4 = 1,2,3,4;
print(tupla1);
print(tupla2);
print(type(tupla3));
print(type(tupla4));

#Acessando Itens Individualmente em Tuplas
print(tupla2[1]);
#Exemplo de uma forma errada de acessar um item da tupla
#tupla(tupla2));

#Conceito principal de tuplas: Imutável!!
#tupla2[1] = "d";

#Fatiamento de itens na tupla
print(tupla1[1:4]);

#Concatenando tuplas
tupla5 = 1,2,3;
tupla6 = 4,5,6;
tupla7 = tupla5 + tupla6;

print("Concatenando tuplas: ", tupla7);

#exemplos Criando variaveis novas com os valores de uma tupla
a, b, c = tuplas6;
print();
print("Valores das variáveis: ");
print(a);
print(b);
print(c);


