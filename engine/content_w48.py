# -*- coding: utf-8 -*-
"""Conteúdo da semana 16/11 a 22/11/2026 (14 posts): 7 carrosséis (A) + 7 imagens únicas (B)."""
from content_w42 import norm, tags30

POSTS = []


def add(**kw):
    POSTS.append(kw)


def single(date, ph, theme, text, sub, scene, caption, tags, off, ref):
    add(date=date, slot="B", kind="single", philosopher=ph, theme=theme, slides=[(text, sub)], scenes=[scene],
        caption=caption, hashtags=tags30(tags, off), ref=ref)


def car(date, ph, theme, slides, prefix, caption, tags, off, ref):
    add(date=date, slot="A", kind="carousel", philosopher=ph, theme=theme, slides=slides,
        scenes=[f"{prefix}a{i}" for i in range(1, 8)], caption=caption, hashtags=tags30(tags, off), ref=ref)


# ========================= SEGUNDA 16/11 =========================
car("2026-11-16", "Lucrécio", "medo do escuro e do desconhecido", [
    ("Por que o medo cresce tanto quando a luz se apaga?", None),
    ("A casa em silêncio, o quarto escuro, a mensagem sem resposta. O que não se vê logo ganha forma, quase sempre pior.", None),
    ("Imaginar é rápido; conferir é lento. Por isso o medo costuma chegar antes dos fatos e ficar mais tempo que eles.", None),
    ("Lucrécio, poeta epicurista, via no entendimento das coisas a luz que dissolve o medo, e não em mais escuridão.", "Uma reflexão inspirada em Lucrécio"),
    ("Acenda uma luz pequena: escreva numa frase o que você teme e, ao lado, o que de fato sabe. Compare as duas.", None),
    ("Nem todo medo cede assim, e está tudo bem. Alguns pedem companhia: contar a alguém também é acender uma luz.", None),
    ("Entender o medo não o apaga num instante, mas devolve contorno ao que a noite tinha inchado.", "Salve para reler quando a noite pesar."),
], "r16",
    """Tem noite em que o quarto escuro parece maior do que é, e a cabeça preenche o silêncio com o pior que consegue imaginar.

Lucrécio, no poema De rerum natura, defende que o medo se dissolve com a compreensão da natureza das coisas, e não com a fuga. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Escrever o que se teme e o que de fato se sabe é um jeito simples de dar contorno ao medo. E quando ele for grande demais para carregar sozinho, contar a alguém ou buscar ajuda também é cuidado.

Qual medo seu diminuiu quando você o disse em voz alta?

Salve para reler quando a noite pesar e envie a quem anda assustado com o escuro de dentro.

Reflexão autoral inspirada em Lucrécio, De rerum natura.

@doni7m""",
    ["#Lucrecio", "#DeRerumNatura", "#Epicurismo", "#MedoDoEscuro", "#Ansiedade", "#FilosofiaAntiga",
     "#BoaNoite", "#CuidarDeSi", "#SegundaFeira", "#Coragem"], 0,
    """Filósofo e poeta: Tito Lucrécio Caro (c. 99-55 a.C.).
Obra: De rerum natura (Da natureza das coisas), poema epicurista; a tese de que o terror e as trevas do espírito se dissipam pelo conhecimento da natureza (livros I e III).
Links localizados na pesquisa: https://www.poetryintranslation.com/PITBR/Latin/LucretiusDeRerumNaturaBkII.php e https://www.gutenberg.org/cache/epub/785/pg785-images.html
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

single("2026-11-16", "Jan Patočka", "cuidar da alma",
       "Cuidar da alma é perguntar com calma o que em você merece ser protegido.",
       "Uma reflexão inspirada em Patočka", "r16b",
       """Entre tantas urgências, vale uma pergunta mais quieta: o que em mim merece ser protegido?

Jan Patočka, filósofo tcheco, retomou de Platão a ideia de cuidar da alma como tarefa permanente: viver examinando o que importa. A frase da imagem é uma reflexão autoral inspirada nessa ideia, e não uma citação.

Cuidar da alma não exige nada grandioso. Cabe numa pausa, numa conversa honesta, num limite dito com gentileza.

O que em você merece mais cuidado esta semana?

Salve para voltar a esta pergunta.

Frase autoral inspirada em Patočka; não é citação literal.

@doni7m""",
       ["#Patocka", "#JanPatocka", "#CuidarDaAlma", "#FilosofiaTcheca", "#Platao", "#Fenomenologia",
        "#SegundaFeira", "#AutoCuidado", "#Pausa", "#BomDia"], 3,
       """Filósofo: Jan Patočka (1907-1977).
Obra: Ensaios heréticos sobre a filosofia da história (Heretical Essays in the Philosophy of History), onde retoma o cuidado da alma (epimeleia tes psyches) de Sócrates e Platão.
Link localizado na pesquisa: https://en.wikipedia.org/wiki/Jan_Pato%C4%8Dka
Natureza do texto: frase autoral inspirada na ideia; não é citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

# ========================= TERÇA 17/11 =========================
car("2026-11-17", "Georg Simmel", "solidão no meio da multidão", [
    ("Dá para se sentir sozinho justamente no meio de muita gente?", None),
    ("A rua cheia, o café barulhento, o grupo de mensagens ativo. Tanta presença, e ninguém que pergunte como você está de verdade.", None),
    ("Estar perto não é estar com. A multidão oferece companhia em quantidade, mas nem sempre em qualidade.", None),
    ("Georg Simmel observou que, nas grandes cidades, a proximidade dos corpos convive com uma distância íntima entre as pessoas.", "Uma reflexão inspirada em Simmel"),
    ("Escolha uma pessoa e ofereça algo pequeno e concreto: um café marcado, uma ligação curta, uma pergunta que espere a resposta.", None),
    ("Se a solidão pesa, procurar companhia ou ajuda também é cuidado. Pedir presença não incomoda; é um jeito honesto de existir perto de alguém.", None),
    ("Presença não se mede em quantidade de gente, mas na atenção de quem está perto.", "Envie a alguém de quem você sente falta."),
], "r17",
    """Dá para estar cercado de gente e, mesmo assim, sentir que ninguém chegou perto.

Georg Simmel, no ensaio A metrópole e a vida mental, descreve como a vida nas grandes cidades aproxima os corpos e, ao mesmo tempo, cria uma reserva entre as pessoas. Este carrossel é uma reflexão inspirada nessa leitura, e não uma citação literal.

Se você anda se sentindo só, procurar companhia, ou conversar com alguém de confiança ou com um profissional, também é cuidado. Pedir presença não é incômodo.

De quem você sente falta hoje?

Salve para lembrar de escrever a essa pessoa e envie este post a quem merece uma mensagem sua.

Reflexão autoral inspirada em Georg Simmel, A metrópole e a vida mental (1903).

@doni7m""",
    ["#Simmel", "#GeorgSimmel", "#Solidao", "#Sociologia", "#VidaNaCidade", "#CompanhiaImporta",
     "#SaudadeDeGente", "#CuidarDeSi", "#TercaFeira", "#Conexao"], 1,
    """Filósofo e sociólogo: Georg Simmel (1858-1918).
Obra: Die Großstädte und das Geistesleben (A metrópole e a vida mental, 1903), sobre a reserva e a distância interior na vida urbana.
Link localizado na pesquisa: https://sociologiac.net/2026/01/27/metropolis-and-mental-life-georg-simmel/
Natureza do texto: reflexão autoral inspirada na leitura do ensaio; sem aspas e sem citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

single("2026-11-17", "Musônio Rufo", "filosofia como prática",
       "Pensar bonito é pouco. O que conta é repetir, devagar, o pouco de bom que você já sabe.",
       "Uma reflexão inspirada em Musônio Rufo", "r17b",
       """Muita gente sabe o que lhe faz bem e adia por anos. Entre saber e fazer cabe uma vida inteira.

Musônio Rufo, mestre estoico do século I, insistia que a filosofia vale pelo que se pratica no dia a dia, e não apenas pelo que se discursa. A frase da imagem é uma reflexão autoral inspirada nessa ideia, e não uma citação.

Uma pequena prática repetida pesa mais do que uma grande intenção guardada.

Qual pequena prática você poderia repetir hoje?

Salve para lembrar dela.

Frase autoral inspirada em Musônio Rufo; não é citação literal.

@doni7m""",
       ["#MusonioRufo", "#Estoicismo", "#FilosofiaPratica", "#Habitos", "#PequenosPassos", "#FilosofiaRomana",
        "#TercaFeira", "#Constancia", "#Rotina", "#BomDia"], 4,
       """Filósofo estoico: Gaio Musônio Rufo (c. 30-c. 101 d.C.).
Obra: Preleções (Lectures), reunidas por Lúcio; a ideia de que a filosofia é prática de vida.
Link localizado na pesquisa: https://booktopia.com.au/that-one-should-disdain-hardships-musonius-rufus/book/9780300261547.html (That One Should Disdain Hardships, trad. Cynthia King, introdução de Gretchen Reydams-Schils; Yale University Press, 2020)
Natureza do texto: frase autoral inspirada na ideia; não é citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

# ========================= QUARTA 18/11 =========================
car("2026-11-18", "Alasdair MacIntyre", "pedir ajuda e depender dos outros", [
    ("Pedir ajuda é fraqueza ou parte de ser humano?", None),
    ("Você resolve sozinho, adia o pedido, diz que depois vê. Ajudar o outro parece natural; precisar dele, constrangedor.", None),
    ("Só que ninguém nasceu pronto. Mãos alheias nos alimentaram, ensinaram e cuidaram, e em algum momento voltarão a ser necessárias.", None),
    ("Alasdair MacIntyre defende que somos animais racionais e dependentes: a vulnerabilidade faz parte da vida humana, não é falha dela.", "Uma reflexão inspirada em MacIntyre"),
    ("Comece pequeno: peça uma informação, uma carona, meia hora de atenção. Um pedido simples já exercita a confiança.", None),
    ("Aceitar ajuda também dá ao outro a chance de ser útil. Muita gente só se sente parte quando é chamada.", None),
    ("Depender não diminui ninguém. É o fio que mantém a vida de pé.", "Salve para lembrar disso na próxima vez que hesitar."),
], "r18",
    """Pedir ajuda costuma custar mais do que oferecer. Parece que precisar do outro é um defeito a esconder.

Alasdair MacIntyre, no livro Dependent Rational Animals, argumenta que a vulnerabilidade e a dependência marcam a vida humana do começo ao fim, e que reconhecê-las é parte de viver bem. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Se o peso está grande, pedir ajuda a alguém de confiança, ou a um profissional, também é cuidado.

A quem você poderia pedir uma pequena ajuda esta semana?

Salve para lembrar e envie a quem tem dificuldade de pedir.

Reflexão autoral inspirada em Alasdair MacIntyre, Dependent Rational Animals (1999).

@doni7m""",
    ["#MacIntyre", "#AlasdairMacIntyre", "#PedirAjuda", "#Vulnerabilidade", "#Interdependencia", "#EticaDasVirtudes",
     "#CuidarDosOutros", "#QuartaFeira", "#Comunidade", "#Apoio"], 2,
    """Filósofo: Alasdair MacIntyre (1929-2025).
Obra: Dependent Rational Animals: Why Human Beings Need the Virtues (1999; Paul Carus Lectures), sobre vulnerabilidade, dependência e as virtudes do reconhecimento mútuo.
Link localizado na pesquisa: https://www.delibris.org/en/dependent-rational-animals
Natureza do texto: reflexão autoral inspirada na tese do livro; sem aspas e sem citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

single("2026-11-18", "Gottfried Wilhelm Leibniz", "pequenas coisas somadas",
       "O mar que você ouve é feito de ondas que ninguém ouve sozinhas. Os dias bons também.",
       "Uma reflexão inspirada em Leibniz", "r18b",
       """Existem dias bons que ninguém anota: um cumprimento, um café quente, a luz numa parede.

Leibniz, nos Novos ensaios sobre o entendimento humano, usa a imagem do mar: o rumor das ondas é feito de pequenas percepções que, uma a uma, passam despercebidas. A frase da imagem é uma reflexão autoral inspirada nessa ideia, e não uma citação.

Talvez a vida boa seja mais soma de pequenas ondas do que uma grande onda.

Que pequena onda de hoje merece a sua atenção?

Salve para reparar nelas.

Frase autoral inspirada em Leibniz; não é citação literal.

@doni7m""",
       ["#Leibniz", "#GottfriedLeibniz", "#PequenasPercepcoes", "#Racionalismo", "#SomDoMar", "#PequenosPrazeres",
        "#QuartaFeira", "#Gratidao", "#Atencao", "#BomDia"], 5,
       """Filósofo: Gottfried Wilhelm Leibniz (1646-1716).
Obra: Nouveaux essais sur l'entendement humain (Novos ensaios sobre o entendimento humano, escrito c. 1704, publicado em 1765), Prefácio: as "pequenas percepções" e a imagem do rumor do mar composto de ondas.
Link localizado na pesquisa: https://www.gutenberg.org/ebooks/40957 (e https://philopedia.org/works/new-essays-on-human-understanding/)
Natureza do texto: frase autoral inspirada na imagem; não é citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

# ========================= QUINTA 19/11 (teste do slot A às 09:00) =========================
car("2026-11-19", "Thich Nhat Hanh", "caminhar sem pressa", [
    ("Quando foi a última vez que você caminhou sem estar indo a lugar nenhum?", None),
    ("A gente anda de olho no celular, pensando no próximo compromisso, chegando antes de chegar. O corpo está aqui; a cabeça, adiante.", None),
    ("O trajeto vira só um intervalo a vencer, e boa parte do dia passa sem ser vivida.", None),
    ("Thich Nhat Hanh, mestre zen e escritor, ensinava a caminhada atenta: cada passo pode ser uma chegada, e não só um meio.", "Uma reflexão inspirada em Thich Nhat Hanh"),
    ("Num trajeto curto, guarde o telefone e sinta o chão. Conte cinco passos. Perceba cheiro, luz e som, sem tentar mudar nada.", None),
    ("Não é técnica para render mais. É devolver um pedaço do dia a quem o vive.", None),
    ("O lugar aonde você vai pode esperar um pouco. O caminho também faz parte da vida.", "Salve para lembrar de andar mais devagar."),
], "r19",
    """Tem trajeto que a gente faz tantas vezes que deixa de ver. Do portão ao ponto de ônibus, da porta ao mar.

Thich Nhat Hanh, mestre zen e autor de Peace Is Every Step, propunha a caminhada atenta: perceber o passo, a respiração, o chão. Este carrossel é uma reflexão inspirada nessa prática, e não uma citação literal.

Não precisa de tempo extra. Basta guardar o telefone num trecho curto e deixar o caminho existir.

Que trajeto do seu dia você poderia fazer mais devagar?

Salve para lembrar e envie a quem anda sempre com pressa.

Reflexão autoral inspirada em Thich Nhat Hanh, Peace Is Every Step (1991).

@doni7m""",
    ["#ThichNhatHanh", "#PeaceIsEveryStep", "#Zen", "#CaminhadaAtenta", "#Mindfulness", "#AndarDevagar",
     "#SemPressa", "#QuintaFeira", "#Presenca", "#PausaNoDia"], 3,
    """Mestre zen, escritor e ativista pela paz: Thich Nhat Hanh (1926-2022). Entra aqui como referência de tradição contemplativa, não como filósofo acadêmico.
Obra: Peace Is Every Step (1991) e How to Walk (2015), sobre a meditação andando.
Links localizados na pesquisa: https://plumvillage.org/courses/how-to-walk e https://dhammatalks.net/Books2/Thich_Nhat_Hanh_A_Guide_to_Walking_Meditation.htm
Natureza do texto: reflexão autoral inspirada na prática; sem aspas e sem citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

single("2026-11-19", "Xunzi", "pequenos passos acumulados",
       "Nenhum caminho longo se faz de uma vez. Faz-se de um passo pouco notado, repetido.",
       "Uma reflexão inspirada em Xunzi", "r19b",
       """Quase tudo que importa foi construído por passos que ninguém aplaudiu.

Xunzi, filósofo confuciano do século III a.C., abre o capítulo Exortação ao aprendizado com a ideia de que o saber e o caráter se formam por acúmulo, pouco a pouco. A frase da imagem é uma reflexão autoral inspirada nessa ideia, e não uma citação literal.

Se o caminho parece longo demais, olhe só para o próximo passo.

Qual pequeno passo você pode repetir amanhã?

Salve para lembrar dele.

Frase autoral inspirada em Xunzi; não é citação literal.

@doni7m""",
       ["#Xunzi", "#FilosofiaChinesa", "#Confucionismo", "#PassoAPasso", "#Constancia", "#Aprendizado",
        "#QuintaFeira", "#PequenosPassos", "#Persistencia", "#BomDia"], 6,
       """Filósofo: Xunzi (Xun Kuang, c. 310-235 a.C.).
Obra: Xunzi, capítulo 1, Quan xue (Exortação ao aprendizado), sobre o acúmulo gradual de aprendizado e caráter.
Link localizado na pesquisa: https://ctext.org/xunzi/quan-xue
Natureza do texto: frase autoral inspirada na ideia; não é citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

# ========================= SEXTA 20/11 =========================
car("2026-11-20", "Sor Juana Inés de la Cruz", "pensar no cotidiano (cozinha)", [
    ("E se o pensamento também morasse na cozinha?", None),
    ("Há quem ache que refletir exige silêncio, livros e tempo de sobra. A vida real tem panela no fogo e roupa por lavar.", None),
    ("Então pensar vira luxo de quem tem folga, e a gente se acostuma a viver no piloto automático.", None),
    ("Sor Juana Inés de la Cruz, poeta e filósofa do século XVII, dizia com humor que, se Aristóteles tivesse cozinhado, teria escrito mais.", "Uma reflexão inspirada em Sor Juana"),
    ("Faça de uma tarefa comum um pequeno laboratório: observe o alho na panela, o vapor, o ponto da massa. Pergunte por quê.", None),
    ("Pensar bem não pede lugar especial. Pede atenção ao que já está diante de você.", None),
    ("A sabedoria também mora nas mãos ocupadas.", "Salve para lembrar na próxima vez que for à cozinha."),
], "r20",
    """A gente costuma imaginar o pensamento como coisa de escritório, biblioteca ou madrugada. Mas boa parte da vida acontece entre panelas, panos e horários.

Sor Juana Inés de la Cruz, freira, poeta e pensadora do México colonial, escreveu na Resposta a Sor Filotea que, nos segredos da cozinha, também se descobre natureza, e brincou que Aristóteles teria escrito mais se tivesse cozinhado. Este carrossel é uma reflexão inspirada nessa passagem, e não uma citação literal.

Observar o cotidiano com curiosidade já é uma forma de filosofar.

O que você já descobriu sem querer enquanto fazia algo comum?

Salve para lembrar e envie a quem cozinha com amor.

Reflexão autoral inspirada em Sor Juana Inés de la Cruz, Resposta a Sor Filotea de la Cruz (1691).

@doni7m""",
    ["#SorJuana", "#SorJuanaInesDeLaCruz", "#Cozinha", "#FilosofiaDoCotidiano", "#PequenosPrazeres", "#MulheresFilosofas",
     "#CozinharComAmor", "#SextaFeira", "#Curiosidade", "#Presenca"], 4,
    """Filósofa, poeta e freira: Sor Juana Inés de la Cruz (c. 1648-1695).
Obra: Respuesta a Sor Filotea de la Cruz (1691), onde observa que também se filosofa entre as panelas e remata que, se Aristóteles tivesse cozinhado, teria escrito mais.
Link localizado na pesquisa: https://www.columbia.edu/cu/spanish/courses/spanish3349/07crisisimperio/sorjuanarespuesta.html
Natureza do texto: reflexão autoral; a passagem sobre Aristóteles é parafraseada, sem aspas. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

single("2026-11-20", "Watsuji Tetsurō", "o lugar nos molda",
       "O lugar onde vivemos também nos escreve: vento, luz e gente entram no nosso jeito de ser.",
       "Uma reflexão inspirada em Watsuji", "r20b",
       """Quem muda de lugar costuma descobrir que muda um pouco também.

Watsuji Tetsurō, filósofo japonês, escreveu em Fūdo (Clima e cultura) que o ser humano se forma em relação ao seu meio: clima, paisagem e convivência fazem parte de quem somos. A frase da imagem é uma reflexão autoral inspirada nessa ideia, e não uma citação.

Quem vive numa ilha entende bem: o mar vira hábito, o vento vira conversa.

O que do lugar onde você vive mora em você?

Salve para lembrar de onde vem o seu jeito.

Frase autoral inspirada em Watsuji; não é citação literal.

@doni7m""",
       ["#Watsuji", "#WatsujiTetsuro", "#Fudo", "#FilosofiaJaponesa", "#Pertencimento", "#Paisagem",
        "#SextaFeira", "#VidaNaIlha", "#Lugar", "#BomDia"], 7,
       """Filósofo: Watsuji Tetsurō (1889-1960).
Obra: Fūdo (1935; Clima e cultura / Climate and Culture), estudo do meio (clima, paisagem, convivência) como parte da existência humana.
Link localizado na pesquisa: https://plato.stanford.edu/entries/watsuji-tetsuro/
Natureza do texto: frase autoral inspirada na ideia; não é citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

# ========================= SÁBADO 21/11 =========================
car("2026-11-21", "Vilém Flusser", "viver entre dois lugares", [
    ("É possível pertencer a dois lugares ao mesmo tempo?", None),
    ("Você cozinha com o tempero daqui e ouve a música de lá. Num lugar sente falta do outro; ao voltar, já não se encaixa inteiro.", None),
    ("Ficar entre dois lugares cansa. Sempre parece haver uma explicação a dar, uma saudade a justificar.", None),
    ("Vilém Flusser, filósofo nascido em Praga e que viveu décadas no Brasil, pensou o desenraizamento do migrante como uma condição que também pode criar.", "Uma reflexão inspirada em Flusser"),
    ("Em vez de escolher um lugar, deixe os dois conversarem: a receita da mãe, a palavra de lá, o hábito daqui. É casa em construção.", None),
    ("A saudade não prova que você errou de lugar. Prova que houve algo que valeu a pena levar consigo.", None),
    ("Pertencer talvez seja menos um endereço e mais o conjunto de pessoas e hábitos que você carrega.", "Envie a quem também vive longe de casa."),
], "r21",
    """Quem vive longe de onde nasceu conhece essa sensação: um pé em cada lugar, e às vezes nenhum chão inteiro.

Vilém Flusser, filósofo tcheco-brasileiro, refletiu sobre o exílio e a migração em obras como Bodenlos e Da liberdade do migrante, e viu no desenraizamento uma condição que também pode criar. Este carrossel é uma reflexão inspirada nessas ideias, e não uma citação literal.

Se a saudade aperta, conversar com quem entende essa distância, ou com alguém de confiança, também é cuidado.

O que você trouxe de casa e não largaria por nada?

Salve para lembrar e envie a quem também mora longe.

Reflexão autoral inspirada em Vilém Flusser, Bodenlos (1992) e Da liberdade do migrante.

@doni7m""",
    ["#Flusser", "#VilemFlusser", "#Migrante", "#Saudade", "#Exilio", "#BrasileirosNoExterior",
     "#VidaLongeDeCasa", "#Pertencimento", "#Sabado", "#Raizes"], 5,
    """Filósofo: Vilém Flusser (1920-1991), nascido em Praga, viveu no Brasil de 1940 a 1972.
Obra: Bodenlos: uma autobiografia filosófica (1992) e o ensaio sobre a condição do migrante (Da liberdade do migrante / Von der Freiheit des Migranten).
Links localizados na pesquisa: https://seer.ufrgs.br/index.php/intexto/article/view/102846 e https://revistalanda.ufsc.br/PDFs/vol5n1/01.%20CHAMADARafael%20Alonso%20Vil%C3%A9m%20Flusser,%20um%20migrante%20pluril%C3%ADngue.pdf
Natureza do texto: reflexão autoral inspirada nas ideias; sem aspas e sem citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

single("2026-11-21", "Vladimir Jankélévitch", "o que foi vivido permanece",
       "O que foi vivido nunca deixa de ter sido. Nenhum tempo apaga um dia bom.",
       "Uma reflexão inspirada em Jankélévitch", "r21b",
       """Há dias que acabaram, mas não passaram: continuam existindo como fato.

Vladimir Jankélévitch, filósofo francês, pensou a irreversibilidade do tempo e sustentou que ter vivido algo é um fato que nada desfaz. A frase da imagem é uma reflexão autoral inspirada nessa ideia, e não uma citação.

Isso consola quem teme perder as boas lembranças: elas não se apagam, mesmo quando o dia já foi embora.

Que dia bom você carrega consigo?

Salve para lembrar dele.

Frase autoral inspirada em Jankélévitch; não é citação literal.

@doni7m""",
       ["#Jankelevitch", "#VladimirJankelevitch", "#FilosofiaFrancesa", "#Tempo", "#Memoria", "#Saudade",
        "#Sabado", "#Lembrancas", "#Irreversivel", "#BoaNoite"], 8,
       """Filósofo: Vladimir Jankélévitch (1903-1985).
Obra: L'irréversible et la nostalgie (1974), sobre a irreversibilidade do tempo e o fato de ter sido.
Link localizado na pesquisa: https://encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/jankelevitch-vladimir-1903-1985
Natureza do texto: frase autoral inspirada na ideia; não é citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

# ========================= DOMINGO 22/11 =========================
car("2026-11-22", "Karl Jaspers", "o que fica de pé quando os planos caem", [
    ("O que ainda fica de pé quando os planos caem?", None),
    ("Um trabalho que acaba, uma relação que muda, uma notícia sem aviso. De repente, o roteiro combinado já não serve.", None),
    ("Primeiro vem o choque; depois, a pressa de consertar tudo. Mas há perdas que não se resolvem: se atravessam.", None),
    ("Karl Jaspers chamou de situações-limite os momentos em que a fragilidade da vida não se contorna, e viu neles a chance de olhar o essencial.", "Uma reflexão inspirada em Jaspers"),
    ("Faça duas listas curtas: o que mudou e o que continua. Pessoas, valores e hábitos pequenos que seguem de pé merecem ser vistos.", None),
    ("Nem todo recomeço é escolhido. Mas dá para escolher um primeiro passo pequeno e alguém com quem dividi-lo.", None),
    ("Quando tudo balança, o que ainda fica de pé mostra onde você pode se apoiar.", "Salve para reler em dia difícil."),
], "r22",
    """Tem dia em que o chão muda sem pedir licença, e os planos feitos com tanto cuidado ficam sem lugar.

Karl Jaspers, em Filosofia, chamou de situações-limite os momentos como a perda, o sofrimento e a culpa, que não dá para contornar e que podem abrir um olhar mais honesto para o que importa. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Se o peso for grande, conversar com alguém de confiança ou procurar ajuda profissional também é cuidado.

O que ainda está de pé na sua vida hoje?

Salve para reler em dia difícil e envie a quem está atravessando um.

Reflexão autoral inspirada em Karl Jaspers, Filosofia (1932) e a noção de situações-limite.

@doni7m""",
    ["#Jaspers", "#KarlJaspers", "#SituacoesLimite", "#Existencialismo", "#Recomecos", "#Resiliencia",
     "#ApoioMutuo", "#Domingo", "#Perdas", "#Esperanca"], 6,
    """Filósofo: Karl Jaspers (1883-1969).
Obra: Philosophie (1932), em particular a noção de situações-limite (Grenzsituationen): morte, sofrimento, luta e culpa como situações que não se contornam.
Links localizados na pesquisa: https://www.newworldencyclopedia.org/entry/Karl_Jaspers e https://en.wikipedia.org/wiki/Limit_situation
Natureza do texto: reflexão autoral inspirada na noção; sem aspas e sem citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

single("2026-11-22", "John Mbiti", "somos pelos outros",
       "Ninguém é uma ilha: somos porque alguém nos vê, nos chama e nos espera.",
       "Uma reflexão inspirada em Mbiti", "r22b",
       """Existir também é ser esperado: alguém que olha a porta, guarda um lugar, pergunta se chegamos bem.

John Mbiti, filósofo e teólogo queniano, resumiu em African Religions and Philosophy uma visão de comunidade em que a pessoa se constitui na relação com os outros. A frase da imagem é uma reflexão autoral inspirada nessa ideia, e não uma citação literal.

E você também pode ser esse alguém para outra pessoa.

Quem espera por você hoje? E quem você poderia esperar?

Salve para lembrar de escrever a alguém.

Frase autoral inspirada em Mbiti; não é citação literal.

@doni7m""",
       ["#Mbiti", "#JohnMbiti", "#FilosofiaAfricana", "#Ubuntu", "#Comunidade", "#Pertencimento",
        "#Domingo", "#Amizade", "#Familia", "#BomDomingo"], 9,
       """Filósofo e teólogo: John S. Mbiti (1931-2019).
Obra: African Religions and Philosophy (1969), sobre a visão comunitária da pessoa na filosofia africana tradicional.
Link localizado na pesquisa: https://unisapressjournals.co.za/index.php/Phronimon/article/view/12205
Natureza do texto: frase autoral inspirada na ideia; não é citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")
