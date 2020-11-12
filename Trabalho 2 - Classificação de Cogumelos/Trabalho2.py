'''Trabalho/projeto 2 - classificação de cogumelos
Segredo da Realidade : Cogumelo azul

Leia atentamente este enunciado. A compreensão do enunciado faz parte da avaliação.

Vivemos em tempos sombrios em que uma simples preferência gastronômica tem causado danos irreparáveis ao planeta. O consumo desenfreado de carne causa desequilíbrio climático, problemas de saúde, aumento da desigualdade social, bem como sofrimento desnecessário a animais. Impactos ambientais da pecuária ocorrem não somente por seu estímulo às queimadas e ao desmatamento de vastas florestas, mas também pelo fato de que essa atividade implica alto consumo de recursos naturais e emissão de gases do efeito estufa.

Diversas ações podem ser realizadas para reduzir esse problema, tanto em nível governamental quanto em nível individual. Uma dessas ações é a substituição de carne por outros alimentos com alto valor proteico. Entre eles estão os cogumelos, que são altamente nutritivos e saborosos. Há uma infinidade de receitas com cogumelos, as quais poderiam se tornar mais populares no Brasil. Além disso, o custo de produção de cogumelos é baixo e seu impacto no meio ambiente é desprezível se comparado com o de carne bovina.

Porém, há um sério problema com cogumelos: muitas espécies são alucinógenas, venenosas ou não são recomendadas para consumo humano por diversas outras razões. Por isso, antes de se decidir produzir cogumelos para consumo, é necessário que eles sejam analisados para verificar se realmente são comestíveis.

O propósito deste projeto é desenvolver um algoritmo que use características dos cogumelos para ajudar a identificar se eles são comestíveis ou não. Essas características são informações como cor, forma, cheiro e outros fatores que podem ajudar na caracterização e classificação de novos cogumelos.  Para tal, será usada a base de dados de cogumelos da UCI, que conta com milhares de amostras de cogumelos, cada um caracterizado por D=22 desses atributos listados na pagina da UCI (vide seção Attribute Information). Ou seja, dado um conjunto de cogumelos para o qual é sabido se eles são comestíveis ou não, seu algoritmo deve inferir se cogumelos de um outro conjunto são comestíveis ou não. Matematicamente, após a conversão de atributos em números, representaremos amostras como vetores    

.

Para esta tarefa, você deve implementar o algoritmo de K-vizinhos mais próximos. Trata-se de um dos classificadores mais simples para aprendizado de máquina (ou reconhecimento de padrões). Como todo classificador supervisionado, ele utiliza um conjunto de treinamento e um conjunto de teste.

    O conjunto de treinamento é fornecido para permitir que o algoritmo possa modelar o problema. Esse conjunto contém amostras para as quais sabemos tanto seus atributos quanto seus rótulos.
    Já o conjunto de teste simula uma aplicação do algoritmo (deployment) e contém amostras para as quais sabemos seus atributos mas não sabemos seus rótulo. O objetivo é justamente inferir os rótulos dessas novas amostras.

No classificador de  
-vizinhos mais próximos, como o próprio nome diz, a inferência de uma amostra de teste é feita baseada no rótulo das  

amostras de treinamento que são mais próximas a ele. Ou seja, o seguinte algoritmo é aplicado:

    Leia o valor de  

, um número inteiro.
Leia o valor de  
, um número inteiro que indica quantas amostras de treinamento serão dadas.
Leia o valor de  
, um número inteiro que indica quantas amostras de teste serão dadas.
Leia todos os vetores de treinamento    
, ou seja, leia uma matriz de   linhas (cogumelos) e  
colunas (atributos), onde cada linha representa uma amostra.
No problema deste projeto, os dados são fornecidos como uma sequencia de caracteres separados por espaço. Para usar uma métrica numérica, é necessário converter esses caracteres em números. Para tal, utilize o "vocabulário" de atributos disponível na seção Attribute Information da página da base de dados, de forma que o valor de atributo listado primeiro é convertido ao número 0, o segundo a 1, e assim por diante. Por exemplo, o terceiro atributo de cogumelos (ou seja, a terceira coluna dos dados) se chama cap-color e pode assumir os seguintes valores:
brown='n', buff='b', cinnamon='c', gray='g', green='r', pink='p', purple='u', red='e', white='w', yellow='y'.
Converta o caractere 'n' para 0, 'b' para 1, 'c' para 2, 'g' para 3 e assim por diante. Faça isso para todos os atributos.
Dada a codificação acima, note que cada atributo poderá terá uma escala diferente da dos outros atributos. Por exemplo, alguns atributos podem assumir somente 2 valores e por isso assumirão no máximo o valor 1, enquanto que outros podem assumir um valor maior que 10. Dada a maneira em que as amostras são comparadas, isso pode injustamente dar mais valor a certos atributos do que outros, sendo que não sabemos qual é a real relevância de cada atributo. Para igualar a relevância dos atributos, os dados devem ser normalizados (ou padronizados). Para tal, é preciso calcular o vetor  
de médias e o vetor   de desvios padrão para todos os atributos.
Detalhe importante: ao calcular o desvio padrão, não use a correção de Bessel, ou seja, para cada atributo indexado por  , use a seguinte fórmula:                                       
.
Para cada atributo, subtraia a média e divida o resultado pelo desvio padrão. Caso um atributo não varie no conjunto de treinamento (ou seja, seu desvio padrão é 0), seu valor deve ser atribuído a 0.
Leia os rótulos    
, de todas as amostras de treinamento, ou seja, leia um vetor que contém  
elementos, onde cada linha possui apenas um caractere que indica o rótulo, podendo assumir o valor 'p' ou 'e' (de venenoso/ poisonous e comestível/edible).
Leia todos os vetores de teste    
, ou seja, leia uma matriz de     linhas e  
colunas, onde cada linha representa um cogumelo a ser classificado.
Da mesma forma que é feita para o conjunto de treinamento, normalize os dados do conjunto de teste, porém, é importante que ao invés de se calcular a média e o desvio padrão novamente, sejam usados os mesmos vetores  
e  
calculados usando o conjunto de treinamento.
Para cada vetor de teste     
:

    Calcule a distância Euclideana entre esse vetor     

e todos os vetores de treinamento    .
Nota: para um par de vetores:   e  , ambos contendo   elementos, a distância Euclideana é calculada pela seguinte fórmula:
                         
.
Verifique, entre os  
vizinhos mais próximos de     

        , se a maioria deles (no conjunto de treinamento) é de cogumelos venenosos ('p') ou comestíveis ('e').
        Imprima o rótulo da classe majoritária obtida no passo anterior ('p' ou 'e').

Entrada

Os dados de entrada são fornecidos desta maneira:

K
Ntrain Ntest
x1,1 x1,2  x1,3 ... x1,D 
x2,1 x2,2  x2,3 ... x2,D  
.
.
.
xNtrain,1  xNtrain,2  xNtrain,3  ... xNtrain,D 
y1
y2
y3
.
.
.
yNtrain
x1,1 x1,2  x1,3 ... x1,D 
x2,1  x2,2  x2,3 ... x2,D  
.
.
.
xNtest,1  xNtest,2  xNtest,3  ... xNtest,D 

Onde:

    K é um número inteiro, maior que zero e impar.
    Ntrain é um número inteiro maior que zero que informa quantas amostras de treinamento serão fornecidas.
    Ntest é um número inteiro maior que zero que informa quantas amostras de teste serão fornecidas.
    xi,j são caracteres separados por um espaço em branco. Cada coluna j assume um valor ditado pela lista presente na página da base de dados (seção Attribute Information).
    D tem valor 22, ou seja, há sempre 22 atributos.
    yi é o rotulo do cogumelo i, e assume valor 'p' ou 'e' (venenoso/poisonous ou comestível/edible).

Note que os rótulos são fornecidos para o conjunto de treinamento mas devem ser inferidos pelo algoritmo para o conjunto de teste.

Saída

A saída gerada deve conter Ntest linhas, onde cada linha possui o valor 'p' ou 'e' (venenoso/poisonous ou comestível/ edible).
Testes

Como de costume, a seguir há alguns casos de teste visíveis. Além deles, há vários outros casos ocultos e sua nota é proporcional ao número de casos em que seu programa passa. Estamos exibindo somente casos com poucas amostras para que esta página não fique muito poluída, porém os casos de teste ocultos possuem muito mais amostras. Para permitir que os alunos façam testes com um conjunto grande, estamos disponibilizando um arquivo ZIP que contem um arquivo de entrada e um de saída. Esse caso de teste é diferente do todos usados para avaliar seu programa no Moodle, porém, ele possui características que, se seu programa funcionar nele, podemos com um grande grau de certeza dizer que seu programa passará em todos os casos ocultos contidos aqui.

Faça download do arquivo e descompacte-o no mesmo diretório onde fica seu programa. Para testar seu programa num terminal Linux (assumindo que seu programa se chama solution.py), sugerimos os seguintes comandos:

python solution.py < big_in.txt > big_res.txt
diff big_res.txt big_out.txt

Seja paciente. Para o arquivo big_in.txt, é esperado que uma solução desse problema demore mais de um minuto de processamento. Porém, se seu programa demorar muito mais que isso (por exemplo, 5 minutos), é melhor investigar e tentar melhorar a eficiência dele para evitar problemas com o CodeRunner.
O segundo comando compara seu resultado (big_res.txt) com o gabarito. Se houver alguma diferença, ele vai listar as linhas onde erros ocorrem. Caso contrário, ele não imprime nada na tela, o que indica que seu código passou no teste. Clique aqui para mais informações sobre o método acima.

For example:
Input 	Result

1
33 11
f s g t f f c b w t b f s w w p w o p h v g
x f g t n f c b p t b s s w w p w o p k y d
f y n t n f c b u t b s s g w p w o p k y d
x s y t l f c b k e c s s w w p w o p k s g
b f w f n f w b g e ? s s w w p w t p w s g
s f n f n f c n g e e s s w w p w o p n v u
x f g f n f w b g e ? k s w w p w t p w s g
x s w t p f c n p e e s s w w p w o p n v g
f f e t n f c b p t b s s g g p w o p n v d
f s b t n f c b e e ? s s w e p w t e w c w
f y n t l f c b n e r s y w w p w o p k y p
x f g f c f c n n e b s s w w p w o p k v d
x y g f f f c b h e b k k p b p w o l h y g
f s b t f f c b p t b f f w w p w o p h s g
k y n f y f c n b t ? k s w w p w o e w v p
f s b t f f c b p t b f f w w p w o p h v g
x s w t p f c n n e e s s w w p w o p n v u
f y y f f f c b g e b k k n b p w o l h y p
s f n f n f c n g e e s s w w p w o p n y u
x y e t n f c b u t b s s p w p w o p n y d
f y p t n f c b g e b s s w w p w t p r v g
f s e f f f c n b t ? s s w w p w o e w v d
x s b t n f c b e e ? s s e e p w t e w c w
x y g t n f c b u t b s s g w p w o p k v d
x y y t a f c b n e r s y w w p w o p n s g
f y y f f f c b g e b k k p n p w o l h y g
f y n f y f c n b t ? s s w p p w o e w v p
x s b t f f c b p t b f s w w p w o p h v u
f y n f n f c b w e b y y n n p w t p w y p
x y n t a f c b n e r s y w w p w o p n s g
f s g f n f w b n t e f f w w p w o e k s g
f f g t n f c b w t b s s g w p w o p k y d
x y e f y f c n b t ? s s w w p w o e w v l
p
e
e
e
e
e
e
p
e
e
e
p
p
p
p
p
p
p
e
e
p
p
e
e
e
p
p
p
e
e
e
e
p
f f g f f f c b p e b k k n b p w o l h v d
b s y t l f c b w e c s s w w p w o p k n g
f f n t n f c b n t b s s w w p w o p n y d
x s w t a f w n p t b s s w w p w o p u v d
k y n f f f c n b t ? k k p p p w o e w v l
f y e f s f c n b t ? s s w w p w o e w v p
x y e t n f c b u t b s s p g p w o p k v d
f f n t n f c b p t b s s w w p w o p k y d
x s n t p f c n k e e s s w w p w o p n s u
f y w t p f c n w e e s s w w p w o p k s u
x f n t n f c b u t b s s w g p w o p k v d

	

p
e
e
e
p
p
e
e
p
p
e

9
33 12
f s e f f f c n b t ? s k w p p w o e w v d
x f p f c f w n n e b s s w w p w o p n v d
k s n f f f c n b t ? k s p p p w o e w v l
f y b t n f c b g e b s s w w p w t p r v g
f f w f n f w b p t e f s w w p w o e k s g
f f n f n f w b h t e s f w w p w o e k a g
x y n f n f c b w e b y y n n p w t p w y p
f y g f f f c b g e b k k p n p w o l h y g
f y g f f f c b p e b k k p p p w o l h v d
f y n f y f c n b t ? s k w p p w o e w v p
f s n f n f w b n t e s s w w p w o e k s g
x y n f f f c n b t ? k s p p p w o e w v p
f s w f n f w b n t e s f w w p w o e n s g
f f n t n f c b w t b s s p g p w o p n y d
f f g f f f c b g e b k k n n p w o l h v g
x s g f n f w b n t e f f w w p w o e n s g
x y e t n f c b n t b s s w p p w o p n y d
f s y t a f w n n t b s s w w p w o p u v d
f y g t n f c b p t b s s g g p w o p k v d
x f w f n f w b p t e s s w w p w o e n a g
f y g t n f c b w t b s s w g p w o p k v d
f s n f n a c b o e ? s s o o p n o p y c l
f y g f f f c b p e b k k p n p w o l h v d
b s n f n a c b o e ? s s o o p o o p o c l
f f y f f f c b p e b k k p b p w o l h y d
x s w f n f w b k t e s f w w p w o e k s g
f f n t n f c b p t b s s g w p w o p n y d
f y p t n f c b r e b s s w w p w t p r v g
k y n f f f c n b t ? k k w p p w o e w v l
f y y f f f c b g e b k k b p p w o l h y d
x f n t n f c b w t b s s g g p w o p n v d
x f e t n f c b w t b s s p w p w o p n v d
x f y f f f c b h e b k k n p p w o l h y p
p
p
p
p
e
e
e
p
p
p
e
p
e
e
p
e
e
e
e
e
e
e
p
e
p
e
e
p
p
p
e
e
p
f y g f f f c b g e b k k p b p w o l h y p
x s n f y f c n b t ? k s p p p w o e w v d
x y w t a f c b n e c s s w w p w o p n n g
f y g f f f c b h e b k k p b p w o l h y p
k y e f s f c n b t ? k s w p p w o e w v p
k s g f n f w b w e ? s k w w p w t p w s g
x y e f f f c n b t ? k k w w p w o e w v p
x s n f n a c b n e ? s s o o p n o p b c l
x s e f s f c n b t ? s k w w p w o e w v d
k y p t n f c b e e ? s s e e p w t e w c w
f f g f f f c b g e b k k n p p w o l h y d
x f g f f f c b p e b k k p n p w o l h y g

	

p
p
p
p
p
p
p
p
p
p
p
p

15
36 12
s f g f n f c n g e e s s w w p w o p k v u
f y w t p f c n w e e s s w w p w o p k v g
x f n t n f c b n t b s s g g p w o p k v d
f y g t n f c b u t b s s w g p w o p k y d
f y e t n f c b w t b s s g p p w o p n v d
x s p f c f w n u e b s s w w p w o p k s d
f s n t p f c n n e e s s w w p w o p k s g
f f g t n f c b w t b s s p g p w o p n y d
k y n f n f c n w e ? k y w n p w o e w v d
k s n f n a c b o e ? s s o o p n o p n c l
f y e t n f c b u t b s s w g p w o p n v d
x s e f s f c n b t ? k s w p p w o e w v l
x f g f n f w b h t e f s w w p w o e k a g
f s g t f f c b h t b s s w w p w o p h v u
x y y t l f c b n e r s y w w p w o p n y g
k y e f f f c n b t ? k s p w p w o e w v d
x f g t n f c b w t b s s w g p w o p k y d
f s n f s f c n b t ? s k p p p w o e w v l
f y p t n f c b w e ? s s w e p w t e w c w
f y w t p f c n k e e s s w w p w o p n v u
x s n t p f c n k e e s s w w p w o p k s u
f f g t n f c b n t b s s g w p w o p k y d
x y n t n f c b w e ? s s w w p w t e w c w
x y y t l f c b w e c s s w w p w o p n s g
f y g f f f c b h e b k k p b p w o l h v d
x f g t n f c b p t b s s p p p w o p k y d
b f g f n f w b p e ? s k w w p w t p w n g
x s n t p f c n n e e s s w w p w o p k s g
x s y t l f c b k e c s s w w p w o p k n m
x y n f s f c n b t ? s k w w p w o e w v l
x f e t n f c b w t b s s p g p w o p k y d
b s g f n f w b g e ? k k w w p w t p w s g
x s w t a f c b n e c s s w w p w o p k s g
f y w f n f c n p e ? s f w w p w o f h y d
f y n f s f c n b t ? s s w w p w o e w v p
f f e t n f c b p t b s s p g p w o p k y d
e
p
e
e
e
p
p
e
p
e
e
p
e
p
e
p
e
p
e
p
p
e
e
e
p
e
e
p
e
p
e
e
e
e
p
e
x s w f n f w b n t e f f w w p w o e k s g
x f n t n f c b p t b s s w w p w o p k v d
x s w t f f c b h t b f f w w p w o p h s g
x f y f f f c b g e b k k p n p w o l h y p
k f w f n f w b p e ? k k w w p w t p w s g
f y n f f f c n b t ? s k w w p w o e w v p
x y g f f f c b p e b k k p n p w o l h y g
b f g f n f w b g e ? k s w w p w t p w s g
x y w t a f c b g e c s s w w p w o p n n g
f y y f f f c b h e b k k p p p w o l h y g
f y n t n f c b p t b s s w w p w o p k y d
x s e f y f c n b t ? s s w w p w o e w v p

	

p
e
e
e
e
p
e
p
e
e
e
p
'''

d = 22
k = input()
nTrain, nTest = input().split(" ")
xTrain = []
cap-shape = {"b":0, "c": 1, "x":2, "f":3, "k":4, "s":5}
cap-surface = {"f": 0, "g":1, "y":2, "s":3}
cap-color = {"n":0, "b":1, "c":2, "g":3, "r":4, "p":5, "u":6, "e":7, "w":8, "y":9}
bruises = {"t":0, "f":1}
odor = {"a":0, "l":1, "c":2, "y":3, "f":4, "m":5, "n":6, "p":7, "s":8}
gill-attachment = {"a":0, "d":1, "f":2, "n":3}
gill-spacing = {"c":0, "w":1, "d":2}
gill-size = {"b":0, "n":1}
gill-color = {"k":0, "n":1, "b":2, "h":3, "g":4, "r":5, "o":6, "p":7, "u":8, "e":9, "w":10, "y":11}
stalk-shape = {"e":0, "t":1}
stalk-root = {"b":0, "c":1, "u":2, "e":3, "z":4, "r":5, "?":6}
stalk-surface-above-ring = {"f":0, "y":1, "k":2, "s":3}
stalk-surface-below-ring = {"f":0, "y":1, "k":2, "s":3}
stalk-color-above-ring = {"n":0, "b":1, "c":2, "g":3, "o":4, "p":5, "e":6, "w":7, "y":8}
stalk-color-below-ring = {"n":0, "b":1, "c":2, "g":3, "o":4, "p":5, "e":6, "w":7, "y":8}
veil-typee = {"p":0, "u":1}
veil-color =  {"n":0, "o":1, "w":2, "y":3}
ring-number = {"n":0, "o":1, "t":2}
ring-typee = {"c":0, "e":1, "f":2, "l":3, "n":4, "p":5, "s":6, "z":7}
spore-print-color = {"k":0, "n":1, "b":2, "h":3, "r":4, "o":5, "u":6, "w":7, "y":8}
population = {"a":0, "c":1, "n":2, "s":3, "v":4, "y":5}
habitat = {"g":0, "l":1, "m":2, "p":3, "u":4, "w":5, "d":6}

for i in range (int(nTrain)):

