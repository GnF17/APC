Dada uma imagem conte quantos pixels tem valor maior do que metade do valor máximo que um pixel pode assumir na imagem.

Essa operação é muito simples e bastante útil. Por exemplo, dada uma imagem contendo apenas um número escrito à mão, tal como nas caixinhas do campo de código postal em envelopes do correio, é possível distinguir o número 1 do número 8 usando essa simples contagem.

Nesta questão, a imagem é fornecida no formato [NetPBM]( http://netpbm.sourceforge.net/) ASCII, ou seja, um arquivo PNM do tipo P1, P2 ou P3. Trata-se de um formato que permite que imagens sejam editadas em qualquer editor de texto, pois além da imagem não ser comprimida, os dados são salvos em formato de texto e com uma estrutura muito simples. Além disso, o formato é altamente disseminado, qualquer visualizador de imagens padrão no Linux é capaz de exibi-las.

A documentação completa desse formato encontra-se em seu site oficial.

Essencialmente, o arquivo possui um cabeçalho contendo 3 ou 4 itens (dependendo do tipo de imagem), o qual é seguido por uma sequência de números que indica o valor de cada pixel. A seguir, fornecemos mais detalhes.
Cabeçalho

    O arquivo das imagens sempre começa com um magic_number, que tem esse nome por convenção, mas na realidade não é apenas um número. Trata-se do caractere 'P' seguido por um número.
    Esse magic_number pode ser uma das strings abaixo:
        "P1" no caso de imagens em preto e branco (binárias), ou seja, imagens em que seus pixels assumem somente valor 0 ou 1. Ao contrário de outros padrões de imagem, o valor 0 indica branco e o valor 1 indica preto.
        "P2", no caso de imagens de tons de cinza, ou seja, imagens em que seus pixels podem assumir um valor maior ou igual a zero, sendo que quanto maior o valor, mais claro é o pixel.
        "P3", no caso de imagens coloridas, ou seja, imagens em que a cor de cada pixel é definida por uma tripla de números, indicando, nesta ordem, a quantia de vermelho, verde e azul. Esses valores são chamados de sub-pixels.
    Nota: o formato NetPBM aceita outros tipos (P4, P5 e P6), mas neste exercício usaremos apenas imagens dos 3 formatos acima.
    Após o magic_number os próximos itens relevantes do cabeçalho informam o tamanho da imagem:
        Largura da imagem em pixels.
        Altura da imagem em pixels.
    Posteriormente, somente se a imagem não for em preto e branco (P1), o cabeçalho tem mais um número, o qual chamaremos de max_val que indica qual é o maior valor assumido por qualquer pixel (ou sub-pixel no caso de imagens coloridas). No caso de imagens em preto e branco (P1), este item não ocorre no cabeçalho pois max_val seria sempre 1.

Corpo do arquivo

Após o cabeçalho, os arquivos tem uma sequencia de números que indicam o valor de cada (sub-)pixel.

    No caso de arquivos preto e branco (P1), as imagens são definidas por uma sequência de números que assumem o valor 0 ou 1, podendo ou não ser separados por espaços em branco. No mesmo arquivo, é possível que haja sequencias de números com e sem separadores, por exemplo "010101 00 01 1 00 1" é uma sequência válida de 14 pixels.
    No caso de arquivos de tons de cinza (P2) ou coloridos (P3), há sempre um separador entre o valor de cada (sub-)pixel.
    No caso de imagens coloridas (P3), cada pixel é definido por uma sequencia de 3 números, definindo a quantia de vermelho, verde e azul.

Outros detalhes importantes

    Após o magic_number, o arquivo pode (ou não) ter comentários em qualquer lugar. Comentários se iniciam com o caractere "#" e são delimitados pelo final (quebra) da linha. Ao carregar os dados do arquivo, seu programa deve ignorar o conteúdo desses comentários e prosseguir com o que vier a partir da linha seguinte.
    Todos os dados numéricos das imagens são valores dos conjuntos Naturais (i.e., inteiros não negativos).
    Com exceção do corpo das imagens em preto e branco (padrão P1, conforme discutido acima), todos os valores numéricos (inclusive do cabeçalho) devem ser separados por um ou mais espaços em branco, quebras de linha ou caracteres de tabulação. Seu programa deve ser robusto aos diversos tipos de separadores. Partes diferentes de um mesmo arquivo podem ter dados separados por quebras de linha e por espaços em branco.
    Para se resolver este exercício, seu algoritmo deve comparar o valor dos pixels com a metade de max_val, ou seja, a comparação é feita com o valor definido pelo cabeçalho, e não o valor observado no corpo da imagem. Por exemplo, uma imagem de tons de cinza (P2) pode ter max_val=100, sendo que todos os pixels presentes em seu corpo tem valor menor que 70. Nesse caso, a ideia é contar quantos pixels tem valor maior que 50 (e não 35). 
    No caso de imagens coloridas (P3, que possuem 3 valores por pixel), use a média entre esses 3 valores para fazer a comparação com a metade de max_val. 

Entrada

A entrada para o seu programa é apenas uma string

nome_do_arquivo.pnm

o qual é fornecido pela entrada padrão, indicando qual é o nome do arquivo de imagem a ser analisado. Esse arquivo é fornecido em formato PNM ASCII, do NetPBM, i.e., tipos P1, P2 ou P3.

Saída

A saída é um número inteiro, contendo a contagem de pixels cujo valor (ou média das 3 cores) é maior que a metade do maior valor que essa imagem pode conter (max_val/2).

Testes

Arquivos dos casos de teste abaixo podem ser obtidos seguindo este [link](https://github.com/GnF17/APC/tree/main/Trabalho%203%20-%20Contagem%20de%20pixels%20com%20valores%20mais%20altos%20em%20imagens%20NetPBM/Arquivos%20NetPBM%20-%20Exemplo).

Você pode converter imagens de outros formatos (JPG, PNG etc.) para formatos do tipo NetPBM, usando Gimp, ImageMagick ou outros programas, tais como os listados na página do NetPBM.
