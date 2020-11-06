T
N
NU_ANO_INGRESSO NU_DIA_NASCIMENTO NU_MES_NASCIMENTO NU_ANO_NASCIMENTO TP_SEXO TP_SITUACAO
      ...
      .
      .

Onde:

    T é um número inteiro que indica qual tarefa seu programa deve desempenhar. A lista de tarefas está descrita posteriormente.
    N indica quantas linhas de dados serão fornecidas para o seu programa (i.e., dados de quantos alunos). 

Da terceira linha em diante, o arquivo possui 6 números inteiros por linha (separados por espaço em branco) e cada linha se refere
 aos dados de um estudante. As colunas tem este significado:

    NU_ANO_INGRESSO: ano em que ano o aluno ingressou na UnB.
    NU_DIA_NASCIMENTO: dia de nascimento, expresso com até 2 dígitos.
    NU_MES_NASCIMENTO: mês de nascimento, expresso numericamente, com até 2 dígitos.
    NU_ANO_NASCIMENTO: ano de nascimento, expresso com 4 dígitos.
    TP_SEXO: indicador de sexo do(a) aluno(a), podendo assumir estes valores:
        o número 1 indica feminino
        o número 2 indica masculino
    TP_SITUACAO: indica qual é a situação do(a) aluno(a) no curso, podendo assumir esses valores numéricos:
        2: Cursando
        3. Matrícula trancada
        4. Desvinculado do curso
        5. Transferido para outro curso da mesma IES
        6. Formado
        7. Falecido
    Isso indica que alunos considerados como casos atuais de alunos regulares apresentam o número 2 ou 6 nesse campo.

Seu programa deve ler os dados no formato acima e executar uma entre 7 tarefas, dependendo do valor do primeiro número que é lido 
(T). A seguir está lista de tarefas, todas se referem a ler os dados, calcular e imprimir alguma informação.

  1  Imprima a porcentagem de alunos regulares e não regulares. Como dito acima, alunos considerados regulares são aqueles
     cujo estado atual é "cursando" ou "formado". A saída deve ter este formato:

    matriculados ou formados:XXX.X
    alunos em outras situacoes:XXX.X

  2  Imprima a porcentagem de alunos do sexo masculino e alunos do sexo feminino seguindo este formato:

    sexo masculino:XXX.X
    sexo feminino:XXX.X

  3  Imprima o tempo médio, em anos, desde que o aluno ingressou no curso. Para tal, assuma que o ano atual é (início de)
     2019, i.e., se um aluno iniciou seu curso em 2018, considere que ele está no curso há 1 ano. Seu programa deve imprimir 
     resultado neste formato:

    media de anos desde ingresso:XXX.X

  4  Imprima o histograma percentual de dia da semana em que os alunos nasceram, neste formato:

    domingo:XXX.X
    segunda:XXX.X
    terca:XXX.X
    quarta:XXX.X
    quinta:XXX.X
    sexta:XXX.X
    sabado:XXX.X

  5  Note que para esta tarefa, a soma dos números impressos deve normalmente resultar no valor 100.0.
    Combinação das tarefas 2 e 1, i.e., imprima os percentuais de alunos regulares e não-regulares, separados em alunos 
    masculinos e posteriormente dentre alunos femininos, neste formato:

    dentre masculinos:
    matriculados ou formados:XXX.X
    alunos em outras situacoes:XXX.X
    dentre femininos:
    matriculados ou formados:XXX.X
    alunos em outras situacoes:XXX.X

  6  Combinação das tarefas 1 e 3, i.e, imprima o tempo no curso, separado em alunos regulares e alunos não-regulares, 
    neste formato:

    entre matriculados ou formados:
    media de anos desde ingresso:XXX.X
    dentre alunos em outras situacoes:
    media de anos desde ingresso:XXX.X

  7  Combinação das tarefas 2 e 4, i.e., dentre alunos do sexo masculino (e posteriormente dentre alunos do sexo feminino), 
    imprima o histograma percentual do dia da semana em que eles nasceram no formato abaixo:

    dentre masculinos:
    domingo:XXX.X
    segunda:XXX.X
    terca:XXX.X
    quarta:XXX.X
    quinta:XXX.X
    sexta:XXX.X
    sabado:XXX.X
    dentre femininos:
    domingo:XXX.X
    segunda:XXX.X
    terca:XXX.X
    quarta:XXX.X
    quinta:XXX.X
    sexta:XXX.X
    sabado:XXX.x

Recomendamos que seu programa use f-strings para imprimir a saída de dados e que todos os dados numéricos de saída são números 
decimais devendo ser impressos com uma casa decimal. O número deve ocupar um espaço de 5 caracteres (incluindo o ponto).
Note nos casos de teste (tanto na entrada quanto na saída) não há o uso de acentos, cedilhas nem letras maiúsculas.
