# Exc.1: Crie uma lista chamada "frutas" contendo as seguintes frutas:
#maçã, banana, laranja, abacaxi e melancia. Em seguida, exiba a
#lista completa na tela.

print ("Frutas");

Frutas = ["maça", "banana", "laranja", "abacaxi", "melancia"];


#Exc.2: Adicione a fruta "uva" à lista "frutas" utilizando o método
#append(). Exiba a lista atualizada na tela.

Frutas = { 

    'Uva' : 1
}
Frutas.append("Uva");
print(Frutas)

#Exc.3: Remova a fruta "banana" da lista "frutas" utilizando o método
#remove(). Exiba a lista atualizada na tela.

FrutasrutaRemovida = Frutas.remove("banana");
FrutasRemovida = Frutas.pop(2);
print(Frutas);
print(FrutasRemovida);

#Exc.4:Acesse o segundo elemento da lista "frutas" e armazene-o em uma variável chamada "fruta_selecionada". 
# Em seguida, exiba o valor armazenado na variável.

Frutas_Selecionada = Frutas.Selecionada("banana");
Frutas_Selecionada = Frutas.pop(2);
print(Frutas);
print(Frutas_Selecionada);

#Exc.5:Crie uma tupla chamada "cores" contendo as seguintes cores:Vermelho, azul, verde, amarelo e roxo. Em seguida, exiba a tupla
#completa na tela

Cores = ["Vermelho", "Azul", "Verde", " Amarelo", "Roxo"]
print();

#exc.6:Acesse o terceiro elemento da tupla "cores" e armazene-o em uma variável chamada "cor_selecionada". Em seguida, exiba o
#valor armazenado na variável.

Cores = ["Vermelho", "Azul", "Verde", " Amarelo", "Roxo"]
print();

Cores_Selecionada = Cores("Verde");
Cores_Selecionada = Cores.pop(3);
print(Cores);
print(Cores_Selecionada);

#Exc.7:Tente adicionar a cor "laranja" à tupla "cores" e observe o resultado. Explique o motivo pelo qual ocorreu um erro fazendo
#um comentário no código.

Cores("laranja");





#Exc.8:Crie um dicionário chamado "aluno" contendo as seguintes informações: nome, idade e cidade. Utilize as chaves "nome",
#"idade" e "cidade" para representar cada informação. Em seguida, exiba o dicionário completo na tela.

Aluno = {
  'nome'      : 'Joana', 
  'Idade' : '20',
  'Cidade'      : 'São Paulo'
}

print(Aluno);

#Exc.9:Acesse a idade do aluno no dicionário "aluno" e armazene-o em uma variável chamada "idade_aluno". Em seguida, exiba o valor
#armazenado na variável

Idade_aluno = {
'idade' : '20',

}
 
print(Aluno);

#Exc.10: Adicione a informação do gênero do aluno ao dicionário "aluno" utilizando a chave "gênero" e o valor correspondente. Exiba
#o dicionário atualizado na tela.

Gênero = {

# fiquei com dúvidas?

}

print(Aluno);


#Exc.11:Remova a informação da cidade do dicionário "aluno" utilizando o método pop() e a chave correspondente. Exiba o
#dicionário atualizado na tela.

elementoRemovido = Aluno.pop("São Paulo");

print(elementoRemovido);
print();
print("Dicionário atualizado: ", Aluno);