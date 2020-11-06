:warning: -> Informações faltantes
 
 Vivemos em tempos sombrios em que uma simples preferência gastronômica tem causado danos irreparáveis ao planeta. O consumo desenfreado de carne causa desequilíbrio climático, problemas de saúde, aumento da desigualdade social, bem como sofrimento desnecessário a animais. Impactos ambientais da pecuária ocorrem não somente por seu estímulo às queimadas e ao desmatamento de vastas florestas, mas também pelo fato de que essa atividade implica alto consumo de recursos naturais e emissão de gases do efeito estufa.

Diversas ações podem ser realizadas para reduzir esse problema, tanto em nível governamental quanto em nível individual. Uma dessas ações é a substituição de carne por outros alimentos com alto valor proteico. Entre eles estão os cogumelos, que são altamente nutritivos e saborosos. Há uma infinidade de receitas com cogumelos, as quais poderiam se tornar mais populares no Brasil. Além disso, o custo de produção de cogumelos é baixo e seu impacto no meio ambiente é desprezível se comparado com o de carne bovina.

Porém, há um sério problema com cogumelos: muitas espécies são alucinógenas, venenosas ou não são recomendadas para consumo humano por diversas outras razões. Por isso, antes de se decidir produzir cogumelos para consumo, é necessário que eles sejam analisados para verificar se realmente são comestíveis.

O propósito deste projeto é desenvolver um algoritmo que use características dos cogumelos para ajudar a identificar se eles são comestíveis ou não. Essas características são informações como cor, forma, cheiro e outros fatores que podem ajudar na caracterização e classificação de novos cogumelos.  Para tal, será usada a base de dados de cogumelos da UCI, que conta com milhares de amostras de cogumelos, cada um caracterizado por D=22 desses atributos listados na pagina da UCI (vide seção Attribute Information). Ou seja, dado um conjunto de cogumelos para o qual é sabido se eles são comestíveis ou não, seu algoritmo deve inferir se cogumelos de um outro conjunto são comestíveis ou não. Matematicamente, após a conversão de atributos em números, representaremos amostras como vetores  :warning:.

Para esta tarefa, você deve implementar o algoritmo de K-vizinhos mais próximos. Trata-se de um dos classificadores mais simples para aprendizado de máquina (ou reconhecimento de padrões). Como todo classificador supervisionado, ele utiliza um conjunto de treinamento e um conjunto de teste.

  - O conjunto de treinamento é fornecido para permitir que o algoritmo possa modelar o problema. Esse conjunto contém amostras para as quais sabemos tanto seus atributos quanto seus rótulos.
  - Já o conjunto de teste simula uma aplicação do algoritmo (deployment) e contém amostras para as quais sabemos seus atributos mas não sabemos seus rótulo. O objetivo é justamente inferir os rótulos dessas novas amostras.

No classificador de **K**-vizinhos mais próximos, como o próprio nome diz, a inferência de uma amostra de teste é feita baseada no rótulo das **K** amostras de treinamento que são mais próximas a ele. Ou seja, o seguinte algoritmo é aplicado:

   1- Leia o valor de K, um número inteiro.
   
   2- Leia o valor de :warning:, um número inteiro que indica quantas amostras de treinamento serão dadas.
   
   3- Leia o valor de :warning:, um número inteiro que indica quantas amostras de teste serão dadas.
   
   4- Leia todos os vetores de treinamento :warning:, ou seja, leia uma matriz de   linhas (cogumelos) e **D** colunas (atributos), onde cada linha representa uma amostra.
   
   5- No problema deste projeto, os dados são fornecidos como uma sequencia de caracteres separados por espaço. Para usar uma métrica numérica, é necessário converter esses caracteres em números. Para tal, utilize o "vocabulário" de atributos disponível na seção Attribute Information da página da base de dados, de forma que o valor de atributo listado primeiro é convertido ao número 0, o segundo a 1, e assim por diante. Por exemplo, o terceiro atributo de cogumelos (ou seja, a terceira coluna dos dados) se chama cap-color e pode assumir os seguintes valores:

    brown='n', buff='b', cinnamon='c', gray='g', green='r', pink='p', purple='u', red='e', white='w', yellow='y'.

Converta o caractere 'n' para 0, 'b' para 1, 'c' para 2, 'g' para 3 e assim por diante. Faça isso para todos os atributos.

   6- Dada a codificação acima, note que cada atributo poderá terá uma escala diferente da dos outros atributos. Por exemplo, alguns atributos podem assumir somente 2 valores e por isso assumirão no máximo o valor 1, enquanto que outros podem assumir um valor maior que 10. Dada a maneira em que as amostras são comparadas, isso pode injustamente dar mais valor a certos atributos do que outros, sendo que não sabemos qual é a real relevância de cada atributo. Para igualar a relevância dos atributos, os dados devem ser normalizados (ou padronizados). Para tal, é preciso calcular o vetor :warning: de médias e o vetor :warning: de desvios padrão para todos os atributos. 
   
Detalhe importante: ao calcular o desvio padrão, não use a correção de Bessel, ou seja, para cada atributo indexado por j, use a seguinte fórmula:   

:warning: :warning: :warning:

   7- Para cada atributo, subtraia a média e divida o resultado pelo desvio padrão. Caso um atributo não varie no conjunto de treinamento (ou seja, seu desvio padrão é 0), seu valor deve ser atribuído a 0.
   
   8- Leia os rótulos :warning: , de todas as amostras de treinamento, ou seja, leia um vetor que contém :warning: elementos, onde cada linha possui apenas um caractere que indica o rótulo, podendo assumir o valor 'p' ou 'e' (de venenoso/ poisonous e comestível/edible).
   
   9- Leia todos os vetores de teste :warning:, ou seja, leia uma matriz de     linhas e :warning: colunas, onde cada linha representa um cogumelo a ser classificado.
   
   10- Da mesma forma que é feita para o conjunto de treinamento, normalize os dados do conjunto de teste, porém, é importante que ao invés de se calcular a média e o desvio padrão novamente, sejam usados os mesmos vetores :warning: e :warning: calculados usando o conjunto de treinamento.
   
   11- Para cada vetor de teste :warning: :
   
   1. Calcule a distância Euclideana entre esse vetor :warning: e todos os vetores de treinamento :warning:.
        
Nota: para um par de vetores:**a** e **b**, ambos contendo **D** elementos, a distância Euclideana é calculada pela seguinte fórmula:

:warning: :warning: :warning:

   2. Verifique, entre os **K** vizinhos mais próximos de :warning: , se a maioria deles (no conjunto de treinamento) é de cogumelos venenosos ('p') ou comestíveis ('e').
   3. Imprima o rótulo da classe majoritária obtida no passo anterior ('p' ou 'e'). 
