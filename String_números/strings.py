
nome = "Camila"
sobrenome = "Vasconcelos"

print(nome + sobrenome);


frase = "Olá, Mundo!";
print("String original:");
print(frase);
print();

print("Acessando caracteres individuais: ");
print("frase");
print("Primeiro caractere: ", frase[0]);
print("Ultimo caractere ", frase[-1]);


nome = input("Nome:  ");
print(nome);
print()

#Inserindo as variaveis no print com f
print(f" Bem-vindo {nome}");
print("Bem-vindo {}".format(nome))

#Concatenando strings 

print("Concatenado strings:")
outraFrase = "Bem-vindo"
fraseCompleta= frase+ ' '+outraFrase;
print(fraseCompleta);
print();

#Tamanho da string 
tamanho = len(frase);
print("Tamanho :",tamanho);
print();

#Divindo uma string em  sub strings 
print("Divindo a string:");
palavras = fraseCompleta.split();
print(palavras);

#Substituindo partes das string 
print("Substituindo partes das string :");
novaFrase = frase.replace("mundo","python");
print(novaFrase);
print();

#Convertendo para letras maiúsculas e minúsculas
print("Convertendo para letras maiúsculas e minúsculas:");
print("Maiúsculas: ", frase.upper());
print("Minúsculas: ", frase.lower());