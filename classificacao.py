#3 variaveis que estamos cadastrando: eh gordinho? Tem perna curta? Faz au au? 
from sklearn.naive_bayes import MultinomialNB


porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, 
cachorro1, cachorro2, cachorro3]

# as marcacoes sao utilizadas para definir a classificacao dos itens, neste caso, se sao porcos ou cachorros
marcacoes = [1, 1, 1, -1, -1, -1] #1 = porco e -1 = cachorro o -1 e utilizado somente para dar enfase, mas
#funciona igual ao 0

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]
teste = [misterioso1, misterioso2, misterioso3]

#os codigos abaixo sao para treinar o algoritmo
modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

# os dados abaixo sao os dados de marcacoes de teste
marcacoes_teste = [-1, 1, -1]
resultado = modelo.predict(teste)
print(resultado)

#o print abaixo é usado para definir as diferenças encontradas
diferencas = resultado - marcacoes_teste

#o loop abaixo é utilizado para apurar quantas vezes foram apresentadas diferenças no teste
acertos = [d for d in diferencas if d==0]
total_de_acertos = len(acertos)

total_de_elementos = len(teste)

taxa_de_acerto = 100.0 * (total_de_acertos / total_de_elementos)
print(f'A taxa de acerto deste teste é de: {taxa_de_acerto}') #com interpolação de string


