# -*- coding: utf-8 -*-
"""Conteúdo da semana 19-25/10/2026 (14 posts): 7 carrosséis (A) + 7 imagens únicas (B)."""
from content_w42 import norm, tags30

POSTS = []


def add(**kw):
    POSTS.append(kw)


# ========================= SEGUNDA 19/10 =========================
add(date="2026-10-19", slot="A", kind="carousel", philosopher="Pascal", theme="silêncio e inquietação",
    slides=[
        ("Quanto tempo você aguenta ficar quieto sem tocar no celular?", None),
        ("Você espera o elevador e já está rolando a tela. Chega em casa e liga a televisão antes mesmo de sentar. O silêncio quase incomoda.", None),
        ("Não é fraqueza. Quando tudo para, aparece o que vinha esperando a vez: uma saudade, uma dúvida, um cansaço que a pressa escondia.", None),
        ("Pascal notou que boa parte da inquietação humana nasce de não sabermos ficar em repouso, sozinhos, dentro de um quarto.", "Uma reflexão inspirada em Pascal"),
        ("Experimente cinco minutos: deixe o celular em outro cômodo, sente-se perto da janela e só observe a respiração. Sem meta e sem aplicativo.", None),
        ("Se o silêncio trouxer algo pesado, você não precisa encarar sozinho. Procurar companhia ou conversar com alguém de confiança também é cuidado.", None),
        ("Ficar quieto não é sumir do mundo. É voltar para dentro por um instante. Quando foi a última vez?", "Salve ou envie a quem vive correndo."),
    ],
    scenes=["d19a1", "d19a2", "d19a3", "d19a4", "d19a5", "d19a6", "d19a7"],
    caption="""Existe um cansaço que não vem do trabalho, e sim de nunca parar.

Blaise Pascal, nos Pensamentos, observou que boa parte dos nossos males vem de não sabermos ficar tranquilos num quarto. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Cinco minutos sem tela não resolvem a vida, mas podem devolver um pouco de chão. E, se o que aparecer no silêncio for pesado demais, procurar companhia ou ajuda também é uma forma de cuidar de si.

Em que momento do dia você mais foge do silêncio?

Salve para tentar esta noite e envie a quem vive correndo.

Reflexão autoral inspirada em Pascal, Pensamentos (fragmento 139, ed. Brunschvicg).

@doni7m""",
    hashtags=tags30(["#Pascal", "#BlaisePascal", "#Pensamentos", "#Silencio", "#Inquietacao", "#DesconectarParaConectar", "#PausaDigital",
                     "#Solitude", "#MomentoDeCalma", "#FilosofiaFrancesa", "#VidaCorrida", "#DetoxDigital"], 0),
    ref="""Filósofo: Blaise Pascal (1623-1662).
Obra: Pensamentos (Pensées), fragmento 139 (ed. Brunschvicg) / 136 (ed. Lafuma): o infortúnio dos homens vem de não saberem ficar em repouso num quarto.
Passagem consultada (tradução inglesa de W. F. Trotter): "all the unhappiness of men arises from one single fact, that they cannot stay quietly in their own chamber."
Link consultado: https://kwize.com/Pens%C3%A9es/216-53 (fonte secundária; conferir a numeração na edição em mãos).
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal no carrossel nem na legenda.""")

add(date="2026-10-19", slot="B", kind="single", philosopher="Agostinho", theme="presente e tempo",
    slides=[("O passado mora na lembrança e o futuro mora na espera. Só o presente cabe nas suas mãos hoje.", "Uma reflexão inspirada em Agostinho")],
    scenes=["d19b"],
    caption="""Quase tudo o que pesa vive em outro tempo: o que já foi ou o que ainda nem chegou.

Agostinho, nas Confissões, notou que passado, presente e futuro existem, de certo modo, dentro de nós: o passado como memória, o presente como atenção, o futuro como expectativa. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Isso não manda ninguém esquecer o que dói nem deixar de planejar. Só lembra que a próxima xícara de café, a próxima conversa e o próximo passo acontecem agora.

O que está ao alcance das suas mãos neste momento?

Salve para voltar a esta pergunta numa semana corrida.

Frase autoral inspirada em Agostinho, Confissões, XI, 20; não é citação literal.

@doni7m""",
    hashtags=tags30(["#Agostinho", "#SantoAgostinho", "#Confissoes", "#Presente", "#Tempo", "#AquiEAgora", "#Memoria", "#Expectativa",
                     "#FilosofiaMedieval", "#VivendoOAgora"], 3),
    ref="""Filósofo: Agostinho de Hipona (354-430).
Obra: Confissões, Livro XI, caps. 14 e 20.
Passagens consultadas (tradução inglesa de J. G. Pilkington): cap. 14, "What, then, is time? If no one ask of me, I know; if I wish to explain to him who asks, I know not"; cap. 20, "present of things past, memory; present of things present, sight; present of things future, expectation."
Links: https://logoslibrary.org/augustine/confessions/1114.html e https://logoslibrary.org/augustine/confessions/1120.html
Natureza do texto: frase autoral inspirada na ideia; não é citação literal. (A tradução consultada usa "sight" para o presente; a leitura como "atenção" é interpretação corrente, não aspas.)""")

# ========================= TERÇA 20/10 =========================
add(date="2026-10-20", slot="A", kind="carousel", philosopher="Laozi", theme="suavidade como força",
    slides=[
        ("Gentileza não é fraqueza. Às vezes é a forma mais resistente de força.", None),
        ("Alguém responde mal, o trânsito não anda, o dia aperta. O corpo pede para endurecer, rebater, fechar a cara.", None),
        ("Endurecer parece proteger, mas costuma gastar energia e deixar o dia ainda mais áspero para quem o carrega por horas.", None),
        ("O Tao Te Ching lembra que nada é mais macio que a água, e nada a supera diante do que é duro.", "Uma reflexão inspirada em Laozi"),
        ("Antes de reagir, solte o maxilar, os ombros e a respiração. Uma resposta calma e curta já muda o clima da conversa.", None),
        ("Suavidade não é aceitar tudo. É escolher o tom, mesmo quando a conversa exige firmeza. A voz baixa também chega longe.", None),
        ("A água segue o caminho que existe e, com o tempo, desfaz o que parecia impossível. Onde você pode ser mais água hoje?", "Salve ou envie a quem anda com o dia pesado."),
    ],
    scenes=["d20a1", "d20a2", "d20a3", "d20a4", "d20a5", "d20a6", "d20a7"],
    caption="""Há dias em que tudo pede dureza: a resposta rápida, o tom seco, a porta fechada.

O Tao Te Ching, atribuído a Laozi, observa que nada no mundo é mais macio que a água e, ainda assim, nada a supera diante do que é duro (capítulo 78). Este carrossel é uma reflexão inspirada nessa imagem, e não uma citação literal.

Suavidade não significa aceitar tudo, nem calar o que importa. Significa escolher o tom, respirar antes de responder e lembrar que firmeza e cuidado podem andar juntos.

Se o dia estiver difícil demais, tudo bem pedir ajuda ou ficar perto de alguém que acalma você. Isso também é cuidado.

Onde você pode ser um pouco mais água esta semana?

Salve para reler antes de uma conversa difícil e envie a quem anda com o dia pesado.

Reflexão autoral inspirada em Laozi, Tao Te Ching, cap. 78.

@doni7m""",
    hashtags=tags30(["#Laozi", "#TaoTeChing", "#Taoismo", "#FilosofiaOriental", "#Agua", "#Suavidade", "#Gentileza", "#ForcaGentil",
                     "#Respirar", "#SabedoriaAntiga", "#Paciencia"], 7),
    ref="""Filósofo: Laozi (tradição: séc. VI-IV a.C.; autoria e datação debatidas).
Obra: Tao Te Ching (Daodejing), capítulo 78.
Passagem consultada (tradução inglesa sem tradutor indicado na página): "Nothing in the world is softer than water, yet nothing surpasses it in overcoming the hard and strong... The weak can overcome the strong, the soft can overcome the hard."
Link consultado: https://en.5000yan.com/tao-te-ching/chapter-78-soft-overcomes-hard.html (conferir também a edição de D. C. Lau).
Natureza do texto: reflexão autoral inspirada na imagem da água; sem aspas e sem citação literal no carrossel nem na legenda.""")

add(date="2026-10-20", slot="B", kind="single", philosopher="William James", theme="atenção e escolha do que notar",
    slides=[("O seu dia é feito, em boa parte, do que você escolhe notar.", "Uma reflexão inspirada em William James")],
    scenes=["d20b"],
    caption="""A mesma manhã pode ser só pressa ou também uma xícara quente, a luz na janela e uma mensagem simpática.

William James, nos Princípios de Psicologia, escreveu que a nossa experiência é aquilo a que concordamos prestar atenção. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Isso não apaga o que é difícil nem exige otimismo à força. Só lembra que a atenção é um pequeno poder que ainda está nas nossas mãos.

O que você quer notar hoje?

Salve para voltar a esta pergunta quando o dia correr depressa.

Frase autoral inspirada em William James, Princípios de Psicologia (1890), cap. XI; não é citação literal.

@doni7m""",
    hashtags=tags30(["#WilliamJames", "#Atencao", "#Pragmatismo", "#Percepcao", "#PrestarAtencao", "#Mindfulness", "#OlharComCuidado",
                     "#PequenosPrazeres", "#ManhaTranquila", "#FilosofiaAmericana"], 10),
    ref="""Filósofo e psicólogo: William James (1842-1910).
Obra: Os Princípios de Psicologia (The Principles of Psychology, 1890), capítulo XI, "Attention".
Passagem consultada: "My experience is what I agree to attend to. Only those items which I notice shape my mind - without selective interest, experience is an utter chaos."
Link consultado: https://psychclassics.yorku.ca/James/Principles/prin11.htm
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")

# ========================= QUARTA 21/10 =========================
add(date="2026-10-21", slot="A", kind="carousel", philosopher="Zhuangzi", theme="valor além da produtividade",
    slides=[
        ("Quem disse que tudo o que existe precisa ser útil?", None),
        ("Você olha para a agenda e mede o dia em entregas. Descansar vira desperdício, e um passeio sem motivo parece perda de tempo.", None),
        ("Aos poucos, o seu valor passa a depender do que você produz. E quando não rende, a culpa aparece mesmo sem ninguém cobrar.", None),
        ("Zhuangzi conta de uma árvore tão torta que nenhum carpinteiro a quis. O amigo a achava inútil; ele sugeriu descansar debaixo dela.", "Uma reflexão inspirada em Zhuangzi"),
        ("Reserve uma hora sem finalidade: caminhar sem destino, olhar o mar, conversar sem pauta. Não precisa render, só precisa ser sua.", None),
        ("Isso não é desculpa para largar tudo. Trabalho e responsabilidade existem. Mas você é mais do que a lista do que entrega.", None),
        ("Há partes de você que valem por existir, e não por servir. Qual é a sua hora inútil favorita?", "Salve ou envie a quem vive em modo produtivo."),
    ],
    scenes=["d21a1", "d21a2", "d21a3", "d21a4", "d21a5", "d21a6", "d21a7"],
    caption="""Uma agenda cheia pode ser sinal de vida boa, mas também pode esconder uma pergunta silenciosa: se eu não render hoje, ainda valho?

Zhuangzi, no primeiro capítulo, conta de uma árvore enorme e torta demais para virar tábua. O amigo diz que ela não serve para nada; Zhuangzi responde que ela poderia ser plantada num campo vasto, e que se poderia descansar ao lado dela. Este carrossel é uma reflexão inspirada nessa história, e não uma citação literal.

Nem toda hora precisa ter finalidade. Isso não apaga as responsabilidades de ninguém, mas lembra que somos mais do que a soma das entregas.

Se a culpa por descansar pesar demais, vale conversar com alguém de confiança. Pedir ajuda também é cuidado.

Qual é a sua hora inútil favorita?

Salve para reler quando a agenda apertar e envie a quem vive em modo produtivo.

Reflexão autoral inspirada em Zhuangzi, cap. 1 ("Passeio livre e fácil").

@doni7m""",
    hashtags=tags30(["#Zhuangzi", "#Chuangtzu", "#Taoismo", "#FilosofiaChinesa", "#Descanso", "#Produtividade", "#SemPressa",
                     "#TempoLivre", "#ValorProprio", "#ArvoreTorta", "#Ocio"], 13),
    ref="""Filósofo: Zhuangzi (séc. IV a.C.).
Obra: Zhuangzi, capítulo 1, "Passeio livre e fácil" (Xiaoyao you), história da árvore inútil (Hui Shi e Zhuangzi).
Passagem consultada (tradução inglesa de Burton Watson): "Why don't you plant it in Not-Even-Anything Village, or the field of Broad-and-Boundless, relax and do nothing by its side, or lie down for a free and easy sleep under it? Axes will never shorten its life, nothing can ever harm it."
Link consultado: https://theanarchistlibrary.org/library/chuang-tzu-zuangzi-burton-watson-the-complete-works-of-chuang-tzu
Natureza do texto: reflexão autoral inspirada na história; sem aspas e sem citação literal no carrossel nem na legenda.""")

add(date="2026-10-21", slot="B", kind="single", philosopher="Paulo Freire", theme="aprender em comunidade",
    slides=[("Ninguém aprende sozinho. A gente se ensina junto, trocando o que sabe e o que ainda não sabe.", "Uma reflexão inspirada em Paulo Freire")],
    scenes=["d21b"],
    caption="""Quem vive longe de casa sabe: o vizinho que explica o ônibus, a colega que ensina uma palavra nova, a senhora do mercado que indica a fruta certa. Muita coisa a gente aprende assim.

Paulo Freire, na Pedagogia do Oprimido, defendia que as pessoas se educam umas às outras, mediadas pelo mundo. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Perguntar não diminui ninguém. E quem ensina também aprende no caminho.

O que alguém já ensinou a você sem perceber?

Salve para lembrar de agradecer e envie a quem te ensinou algo.

Frase autoral inspirada em Paulo Freire, Pedagogia do Oprimido (1968), cap. 2; não é citação literal.

@doni7m""",
    hashtags=tags30(["#PauloFreire", "#PedagogiaDoOprimido", "#Educacao", "#AprenderJuntos", "#Comunidade", "#TrocaDeSaberes",
                     "#Gratidao", "#BrasileirosNoExterior", "#Imigrantes", "#FilosofiaBrasileira"], 16),
    ref="""Educador e filósofo: Paulo Freire (1921-1997).
Obra: Pedagogia do Oprimido (1968), capítulo 2 (capítulo conferir na edição em mãos; a página consultada não o indica).
Passagem consultada (reproduzida em matéria de imprensa): "Ninguém educa ninguém, ninguém educa a si mesmo, os homens se educam entre si, mediatizados pelo mundo."
Link consultado: https://oantagonista.com.br/ladooa/entretenimento/paulo-freire-os-homens-se-educam-entre-si-mediatizados-pelo-mundo-o-livro-mais-citado-do-brasileiro-mais-citado-nas-ciencias-sociais/ (fonte secundária)
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")

# ========================= QUINTA 22/10 =========================
add(date="2026-10-22", slot="A", kind="carousel", philosopher="Bergson", theme="mudança e identidade",
    slides=[
        ("Você já não é a pessoa que era há cinco anos.", None),
        ("Às vezes alguém lembra de você como era, e a descrição já não encaixa. Gostos, medos e prioridades foram mudando sem aviso.", None),
        ("A mudança incomoda porque deixa saudade de quem fomos e dúvida sobre quem estamos nos tornando.", None),
        ("Bergson via a vida como duração: existir é mudar, e mudar é amadurecer, criando a si mesmo aos poucos.", "Uma reflexão inspirada em Bergson"),
        ("Pergunte-se: o que mudou em mim e eu ainda não admiti? Escreva três linhas sobre quem você é hoje, e não sobre quem foi.", None),
        ("Mudar não apaga o que veio antes. A pessoa que você foi continua guiando de longe, com as lições que deixou.", None),
        ("Você ainda está em obra, e isso é sinal de vida. O que em você já mudou e merece ser reconhecido?", "Salve ou envie a quem está se reinventando."),
    ],
    scenes=["d22a1", "d22a2", "d22a3", "d22a4", "d22a5", "d22a6", "d22a7"],
    caption="""Em algum momento, você percebe que já não pensa como pensava, nem quer o que queria. Ninguém avisou quando aconteceu.

Henri Bergson tratava a vida como duração: um fluxo em que o passado se carrega no presente e a pessoa se transforma enquanto vive. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Mudar pode trazer saudade e dúvida. Pode também trazer alívio. As duas coisas cabem no mesmo dia, e nenhuma delas é erro.

Se a mudança estiver pesando e você se sentir perdido, procurar companhia ou uma conversa com alguém de confiança também é cuidado.

O que em você mudou e ainda não foi reconhecido?

Salve para reler num dia de dúvida e envie a quem está se reinventando.

Reflexão autoral inspirada em Henri Bergson, A Evolução Criadora (1907), cap. 1.

@doni7m""",
    hashtags=tags30(["#Bergson", "#HenriBergson", "#Duracao", "#EvolucaoCriadora", "#Mudanca", "#Identidade", "#Transformacao",
                     "#Amadurecer", "#NovasFases", "#FilosofiaFrancesa", "#EmConstrucao"], 19),
    ref="""Filósofo: Henri Bergson (1859-1941).
Obra: A Evolução Criadora (L'Évolution créatrice, 1907), capítulo 1; noção de duração (durée).
Fonte consultada: Project Gutenberg #26163, "Creative Evolution" (trad. Arthur Mitchell): https://gutenberg.org/ebooks/26163 (a página consultada só traz metadados). A frase corrente "Pour un être conscient, exister consiste à changer, changer à se mûrir, se mûrir à se créer indéfiniment soi-même" aparece em sites de citações (https://www.dicocitations.com/citations/citation-115911.php), mas NÃO foi conferida no texto da obra nesta rodada.
Natureza do texto: reflexão autoral inspirada na ideia de duração; sem aspas e sem citação literal no carrossel nem na legenda. Antes de citar a frase com aspas, conferir na edição.""")

add(date="2026-10-22", slot="B", kind="single", philosopher="Cícero", theme="plantar para quem vem depois",
    slides=[("Algumas das melhores coisas que fazemos hoje só darão sombra a quem vier depois.", "Uma reflexão inspirada em Cícero")],
    scenes=["d22b"],
    caption="""Quem planta uma árvore de crescimento lento sabe que talvez nunca se sente debaixo dela. Planta mesmo assim.

Cícero, em Sobre a Velhice, cita o verso de que o lavrador planta árvores que beneficiarão outra geração, e põe um velho camponês a responder que planta para os deuses imortais, que quiseram que ele recebesse esses bens dos antepassados e também os transmitisse aos que vêm depois. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Pode ser uma árvore, uma receita passada adiante, uma palavra de incentivo ou um hábito gentil. O gesto pequeno de hoje também faz sombra amanhã.

O que você gostaria de deixar plantado para alguém?

Salve para voltar a esta pergunta e envie a quem planta sem esperar aplauso.

Frase autoral inspirada em Cícero, Cato Maior de Senectute, §§ 24-25; não é citação literal.

@doni7m""",
    hashtags=tags30(["#Cicero", "#SobreAVelhice", "#Legado", "#PlantarArvores", "#Geracoes", "#Generosidade", "#FilosofiaRomana",
                     "#Sombra", "#AtosSilenciosos", "#Heranca"], 22),
    ref="""Filósofo: Marco Túlio Cícero (106-43 a.C.).
Obra: Cato Maior de Senectute (Sobre a Velhice), §§ 24-25.
Passagem consultada (latim, Project Gutenberg #14945): § 24, "serit arbores, quae alteri saeclo prosint"; § 25, "Nec vero dubitat agricola, quamvis sit senex, quaerenti cui serat respondere: dis immortalibus, qui me non accipere modo haec a maioribus voluerunt, sed etiam posteris prodere."
Link consultado: https://gutenberg.org/cache/epub/14945/pg14945-images.html
Natureza do texto: frase autoral inspirada na passagem (o verso citado por Cícero é de Cecílio Estácio); sem aspas na imagem nem na legenda.""")

# ========================= SEXTA 23/10 =========================
add(date="2026-10-23", slot="A", kind="carousel", philosopher="Martin Buber", theme="ver a pessoa por trás do papel",
    slides=[
        ("Quando foi a última vez que você olhou o caixa, o motorista ou o vizinho como pessoas inteiras?", None),
        ("Passamos o dia cercados de papéis: atendente, entregador, colega, chefe. Quase sem perceber, tratamos cada um como parte de uma tarefa.", None),
        ("E nós também somos reduzidos a papéis. Ninguém gosta de ser visto como função, nem quando a pressa é grande.", None),
        ("Martin Buber distinguia dois modos de relação: tratar o outro como coisa útil, o “isso”, ou encontrá-lo como pessoa inteira, o “tu”.", "Uma reflexão inspirada em Martin Buber"),
        ("Comece pequeno: olhe nos olhos, diga o nome quando souber, pergunte como foi o dia e espere a resposta.", None),
        ("Isso não exige intimidade nem tempo extra. Um instante de presença já devolve à outra pessoa o que o ritmo do dia tirou.", None),
        ("Para Buber, viver de verdade passa por encontros. Quem você pode encontrar de verdade hoje?", "Salve ou envie a quem trata todos com respeito."),
    ],
    scenes=["d23a1", "d23a2", "d23a3", "d23a4", "d23a5", "d23a6", "d23a7"],
    caption="""O sorriso de quem atende, o bom-dia do vizinho, o olhar do motorista no retrovisor: tanta gente passa pelo nosso dia e quase não vemos.

Martin Buber, em Eu e Tu, distingue a relação com o outro como “isso”, algo útil e manejável, e como “tu”, uma pessoa inteira que encontramos. Para ele, a vida real é encontro. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Ninguém consegue ser inteiramente presente o tempo todo, e tudo bem. Mas um olhar, um nome e uma pergunta feita com calma já devolvem humanidade a um momento comum.

Para quem vive longe de casa, um cumprimento sincero na rua pode pesar muito. Se a solidão apertar, procurar companhia ou uma conversa também é cuidado.

Quem você vai encontrar de verdade hoje?

Salve para lembrar e envie a quem trata todos com respeito.

Reflexão autoral inspirada em Martin Buber, Eu e Tu (1923).

@doni7m""",
    hashtags=tags30(["#MartinBuber", "#EuETu", "#Encontro", "#Relacoes", "#Empatia", "#Presenca", "#Respeito", "#Humanidade",
                     "#OlharParaOOutro", "#FilosofiaDoDialogo", "#Convivencia"], 25),
    ref="""Filósofo: Martin Buber (1878-1965).
Obra: Eu e Tu (Ich und Du, 1923); distinção entre as palavras-princípio Eu-Isso e Eu-Tu.
Passagem consultada (tradução inglesa de R. Gregory Smith, 1958, citada em artigo): "All real living is meeting." (Buber 1958: 25, segundo a página consultada.)
Link consultado: https://infed.org/mobi/?p=747 (fonte secundária; conferir paginação na edição em mãos).
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal no carrossel nem na legenda.""")

add(date="2026-10-23", slot="B", kind="single", philosopher="Emmanuel Levinas", theme="o rosto do outro",
    slides=[("Antes de qualquer palavra, o rosto de alguém já nos pede um pouco de atenção.", "Uma reflexão inspirada em Emmanuel Levinas")],
    scenes=["d23b"],
    caption="""Às vezes a pessoa não diz nada, mas está tudo ali: o olhar baixo, o cansaço, a pressa de quem não quer incomodar.

Emmanuel Levinas pensou o encontro com o rosto do outro como um chamado que vem antes de qualquer regra: alguém que aparece diante de nós e, sem poder, já nos convoca à responsabilidade. A frase da imagem é uma reflexão autoral, mais suave e cotidiana, inspirada nessa ideia.

Atenção não exige resolver o problema do outro. Às vezes basta notar, perguntar e ficar um instante.

Quem merece que você pare e olhe de verdade hoje?

Salve para lembrar de perguntar como a pessoa está e envie a quem sabe olhar.

Frase autoral inspirada em Emmanuel Levinas, Ética e Infinito (1982); não é citação literal.

@doni7m""",
    hashtags=tags30(["#Levinas", "#EmmanuelLevinas", "#RostoDoOutro", "#Etica", "#Responsabilidade", "#Atencao", "#Empatia",
                     "#OlharComCuidado", "#FilosofiaContemporanea", "#Cuidado"], 28),
    ref="""Filósofo: Emmanuel Levinas (1906-1995).
Obra: Ética e Infinito (Éthique et Infini, 1982, entrevistas com Philippe Nemo; trad. inglesa de R. A. Cohen, 1985) e Totalidade e Infinito (1961).
Ideia usada: o rosto do outro como apelo que convoca à responsabilidade. Passagem citada em artigo secundário: "The face orders and ordains me" (Levinas, 1985).
Link consultado: https://www.mtai.org/?p=2183 (fonte secundária; conferir a página na edição em mãos antes de qualquer citação).
Natureza do texto: frase autoral e mais branda do que o original, inspirada na ideia; sem aspas e sem citação literal.""")

# ========================= SÁBADO 24/10 =========================
add(date="2026-10-24", slot="A", kind="carousel", philosopher="Confúcio", theme="o prazer de aprender",
    slides=[
        ("Aprender também pode ser um prazer, e não só uma obrigação.", None),
        ("Faz tempo que você aprende só o que é exigido: o sistema novo do trabalho, o formulário, a regra que mudou.", None),
        ("Aprender por pura vontade ficou para depois, como se fosse luxo de quem tem tempo sobrando.", None),
        ("Nas Analectas, Confúcio abre perguntando se não é agradável aprender e, no tempo certo, praticar o que se aprendeu.", "Uma reflexão inspirada em Confúcio"),
        ("Escolha algo pequeno e sem nota: dez palavras de uma língua nova, uma receita, um acorde, o nome de uma planta da ilha.", None),
        ("Errar faz parte e ninguém está avaliando. Praticar um pouco, no seu ritmo, é mais bonito do que esperar o momento perfeito.", None),
        ("Curiosidade é uma forma de carinho consigo mesmo. O que você gostaria de aprender só por prazer?", "Salve ou envie a quem está aprendendo algo novo."),
    ],
    scenes=["d24a1", "d24a2", "d24a3", "d24a4", "d24a5", "d24a6", "d24a7"],
    caption="""Existe o aprender que cansa, porque vem de cobrança, e o aprender que alimenta, porque vem de curiosidade. O segundo costuma ficar para depois.

Confúcio, na primeira passagem das Analectas, pergunta se não é agradável aprender e praticar, no tempo certo, aquilo que se aprendeu. Este carrossel é uma reflexão inspirada nessa abertura, e não uma citação literal.

Começar pequeno basta: dez palavras, uma receita, uma música. O prazer de aprender não precisa de diploma, e quem recomeça fora da própria terra sabe como cada palavra nova pode soar como uma pequena conquista.

Se a vontade de aprender parecer ter sumido e isso durar muito, conversar com alguém de confiança também é cuidado.

O que você aprenderia hoje só por prazer?

Salve para lembrar e envie a quem está aprendendo algo novo.

Reflexão autoral inspirada em Confúcio, Analectas, I, 1.

@doni7m""",
    hashtags=tags30(["#Confucio", "#Analectas", "#FilosofiaChinesa", "#Aprender", "#Curiosidade", "#AprendizadoContinuo", "#PequenosPrazeres",
                     "#NuncaEraTardeDemais", "#EstudarPorPrazer", "#ComecarDeNovo", "#Pratica"], 1),
    ref="""Filósofo: Confúcio (551-479 a.C.).
Obra: Analectas (Lunyu), Livro I, cap. 1 (Xue Er).
Passagem consultada (tradução inglesa de James Legge, Project Gutenberg #3330): "Is it not pleasant to learn with a constant perseverance and application?"
Link consultado: https://gutenberg.org/cache/epub/3330/pg3330-images.html
Natureza do texto: reflexão autoral inspirada na abertura das Analectas; sem aspas e sem citação literal no carrossel nem na legenda.""")

add(date="2026-10-24", slot="B", kind="single", philosopher="Boécio", theme="altos e baixos passam",
    slides=[("A roda gira. Nem a alegria nem o peso moram em nós para sempre.", "Uma reflexão inspirada em Boécio")],
    scenes=["d24b"],
    caption="""Quem já viveu uma semana boa seguida de uma ruim sabe: nada fica no mesmo lugar por muito tempo.

Boécio, na Consolação da Filosofia, escreve da prisão e coloca a Fortuna em cena: a sua própria natureza é a inconstância, e a roda sempre volta a girar. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Isso não diminui o que dói hoje. Só lembra que o dia difícil também tem prazo, e que o bom costuma voltar em pedaços pequenos.

Se o peso demorar a passar, procurar companhia ou ajuda também é uma forma de cuidar de si.

O que, neste momento, está girando na sua vida?

Salve para os dias pesados e envie a quem está atravessando um.

Frase autoral inspirada em Boécio, A Consolação da Filosofia, Livro II; não é citação literal.

@doni7m""",
    hashtags=tags30(["#Boecio", "#ConsolacaoDaFilosofia", "#RodaDaFortuna", "#Impermanencia", "#TempoDeEsperanca", "#FilosofiaMedieval",
                     "#DiasDificeis", "#Resiliencia", "#TudoPassa", "#Consolo"], 4),
    ref="""Filósofo: Anício Mânlio Severino Boécio (c. 477-524).
Obra: A Consolação da Filosofia (De consolatione philosophiae), Livro II (caps. I e II).
Ideia usada (segundo o resumo de Standard Ebooks, trad. H. R. James): a natureza da Fortuna é a inconstância, e os seus dons são dela para dar e tirar.
Link consultado: https://standardebooks.org/ebooks/boethius/the-consolation-of-philosophy/h-r-james/text/book-2 (página de resumo; não traz o texto traduzido, por isso não há citação).
Natureza do texto: frase autoral inspirada na ideia; sem aspas e sem citação literal.""")

# ========================= DOMINGO 25/10 =========================
add(date="2026-10-25", slot="A", kind="carousel", philosopher="Merleau-Ponty", theme="ouvir o corpo",
    slides=[
        ("Seu corpo não é um detalhe. É por onde você vive o dia.", None),
        ("A cabeça empurra: mais uma tarefa, mais um café, mais uma hora. O corpo avisa baixinho com costas tensas, olhos pesados e ombros duros.", None),
        ("Muitas vezes tratamos o corpo como veículo que precisa aguentar, e só prestamos atenção quando ele para de colaborar.", None),
        ("Merleau-Ponty defendia que o corpo não é um objeto ao nosso lado: é o nosso modo de estar no mundo.", "Uma reflexão inspirada em Merleau-Ponty"),
        ("Faça uma escuta de um minuto: onde há tensão? Solte a mandíbula, desça os ombros, beba água. Um pequeno gesto já conta.", None),
        ("Nem sempre dá para parar quando precisamos. Ainda assim, pausas pequenas e honestas valem mais do que aguentar em silêncio.", None),
        ("Cuidar do corpo é cuidar de quem vive nele. Qual sinal seu corpo vem tentando te dar?", "Salve ou envie a quem anda no limite."),
    ],
    scenes=["d25a1", "d25a2", "d25a3", "d25a4", "d25a5", "d25a6", "d25a7"],
    caption="""Domingo costuma ser o dia em que o corpo finalmente consegue falar: o cansaço da semana aparece, o pescoço pesa, o sono cobra.

Maurice Merleau-Ponty, na Fenomenologia da Percepção, defendia que o corpo não é um objeto entre outros, mas o nosso modo de estar no mundo. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Ouvir o corpo não é diagnosticar nada, e não substitui acompanhamento de saúde. É só prestar um pouco de atenção: soltar os ombros, beber água, fazer uma pausa curta. Se algum sinal persistir, vale conversar com um profissional de saúde.

Qual sinal seu corpo vem tentando te dar?

Salve para o próximo dia corrido e envie a quem anda no limite.

Reflexão autoral inspirada em Merleau-Ponty, Fenomenologia da Percepção (1945).

@doni7m""",
    hashtags=tags30(["#MerleauPonty", "#Fenomenologia", "#Corpo", "#OuvirOCorpo", "#Descanso", "#Pausa", "#Autocuidado",
                     "#CorpoEMente", "#Domingo", "#FilosofiaFrancesa", "#CuidarDeSi"], 7),
    ref="""Filósofo: Maurice Merleau-Ponty (1908-1961).
Obra: Fenomenologia da Percepção (Phénoménologie de la perception, 1945).
Ideia usada: o corpo vivido não é objeto entre objetos, mas o modo de ser-no-mundo. Segundo a Stanford Encyclopedia of Philosophy: o corpo é experimentado de modo que o distingue de todas as outras coisas, não está "em" o espaço mas o habita, e é um "terceiro gênero de ser entre o puro sujeito e o objeto".
Link consultado: https://plato.stanford.edu/entries/merleau-ponty/ (seções 3 e 4; fonte secundária, sem citação literal da obra).
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal no carrossel nem na legenda.""")

add(date="2026-10-25", slot="B", kind="single", philosopher="Iris Murdoch", theme="o outro é real",
    slides=[("Amar também é lembrar que o outro é real: tem pressa, medo e história que não são os nossos.", "Uma reflexão inspirada em Iris Murdoch")],
    scenes=["d25b"],
    caption="""Cada janela acesa numa encosta guarda uma vida inteira: manhãs difíceis, saudades, pequenas alegrias que ninguém vê.

Iris Murdoch escreveu, em um ensaio de 1959, que o amor é a realização extremamente difícil de que algo além de nós mesmos é real. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Lembrar disso muda o tom: com quem demora, com quem erra, com quem pensa diferente. Não é aceitar tudo, é ver a pessoa antes da nossa versão dela.

De quem você quer se aproximar com um olhar mais real esta semana?

Salve para começar a semana com mais atenção e envie a quem você quer olhar melhor.

Frase autoral inspirada em Iris Murdoch, “The Sublime and the Good” (1959); não é citação literal.

@doni7m""",
    hashtags=tags30(["#IrisMurdoch", "#Amor", "#Atencao", "#Empatia", "#VerOOutro", "#Relacoes", "#FilosofiaMoral",
                     "#Cuidado", "#OlharMaisReal", "#ComecoDeSemana"], 10),
    ref="""Filósofa e escritora: Iris Murdoch (1919-1999).
Obra: ensaio "The Sublime and the Good", Chicago Review, vol. 13 (1959), p. 51 (segundo a página consultada); ideia retomada em A Soberania do Bem (1970).
Passagem consultada: "Love is the extremely difficult realization that something other than oneself is real."
Link consultado: https://footnotes2plato.com/2011/10/26/iris-murdoch-on-love-and-otherness/ (fonte secundária; a própria página diz não ter verificado o original).
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")
