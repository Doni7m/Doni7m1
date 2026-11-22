# -*- coding: utf-8 -*-
"""Conteúdo da semana 23/11 a 29/11/2026 (14 posts): 7 carrosséis (A) + 7 imagens únicas (B)."""
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


def R(filo, obra, link, nota="reflexão autoral inspirada na ideia; sem aspas e sem citação literal"):
    return (f"Filósofo: {filo}.\nObra: {obra}\nLink localizado na pesquisa: {link}\n"
            f"Natureza do texto: {nota}. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.")


# ========================= SEGUNDA 23/11 — Sêneca: tempo =========================
car("2026-11-23", "Sêneca", "tempo e atenção", [
    ("Quanto do seu dia foi realmente seu?", None),
    ("Mensagens sem aviso, pedidos que se acumulam, um minuto aqui e outro ali. No fim da tarde, o dia parece ter escorrido pelos dedos.", None),
    ("Não é só falta de tempo. Muitas vezes o tempo existe, mas vai embora em coisas que ninguém escolheu de verdade.", None),
    ("Sêneca escreveu que a vida não é curta de nascença: o que a encurta é o modo como a gastamos.", "Uma reflexão inspirada em Sêneca"),
    ("Escolha uma hora do dia e entregue-a a uma só coisa. Sem tela ao lado, sem segunda tarefa escondida.", None),
    ("Nem sempre dá para proteger o próprio tempo, e tudo bem. Há dias em que ele pertence a quem precisa de nós.", None),
    ("Um dia não precisa render muito para ter sido seu. Basta uma hora vivida por inteiro.", "Salve para relembrar de escolher sua hora."),
], "r23",
    """Há dias que passam inteiros sem que a gente reconheça nenhuma hora como sua.

Sêneca, em Sobre a brevidade da vida, defende que o tempo não é tão escasso quanto parece: o que o desperdiça é a forma como o gastamos. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Escolher uma única hora e vivê-la com atenção já muda a medida do dia. E quando o tempo não for seu, porque alguém precisa de você, isso também é um jeito de vivê-lo.

Qual hora do seu dia você gostaria de proteger?

Salve para lembrar de escolher essa hora e envie a quem anda sem fôlego.

Reflexão autoral inspirada em Sêneca, De brevitate vitae.

@doni7m""",
    ["#Seneca", "#Estoicismo", "#BrevidadeDaVida", "#TempoDeVida", "#Atencao", "#Estoicos", "#GestaoDoTempo",
     "#SegundaFeira", "#BoaSemana", "#Presenca"], 0,
    R("Lúcio Aneu Sêneca (c. 4 a.C.-65 d.C.)", "De brevitate vitae (Sobre a brevidade da vida), sobre o uso do tempo.",
      "https://www.correiobraziliense.com.br/cbradar/brevidade-da-vida-seneca-tempo/"))

single("2026-11-23", "Epicteto", "o espaço entre o fato e a resposta",
       "Entre o que acontece e o que você faz com isso, existe um pequeno espaço. Habite-o.",
       "Uma reflexão inspirada em Epicteto", "r23b",
       """Nem tudo o que acontece depende de nós. Mas quase sempre sobra um pequeno espaço antes da resposta.

Epicteto, filósofo estoico, abre o Manual (Enquiridião) separando o que está ao nosso alcance do que não está. A frase da imagem é uma reflexão autoral inspirada nessa ideia, e não uma citação.

Habitar esse espaço pode ser só respirar uma vez antes de responder.

Qual é o seu pequeno espaço de hoje?

Salve para voltar a ele quando precisar.

Frase autoral inspirada em Epicteto; não é citação literal.

@doni7m""",
       ["#Epicteto", "#Enquiridiao", "#Estoicismo", "#FilosofiaEstoica", "#Escolha", "#PausaConsciente",
        "#SegundaFeira", "#BomDia", "#Respirar", "#Equilibrio"], 3,
       R("Epicteto (c. 50-135 d.C.)", "Enquiridião (Manual), cap. 1: distinção entre o que depende de nós e o que não depende.",
         "https://standardebooks.org/ebooks/epictetus/short-works/george-long/text/the-enchiridion",
         "frase autoral inspirada na ideia; não é citação literal"))

# ========================= TERÇA 24/11 — Simone Weil: atenção ao outro =========================
car("2026-11-24", "Simone Weil", "atenção como presença", [
    ("Quando foi a última vez que alguém realmente te escutou?", None),
    ("Aquela conversa em que a pessoa olha nos olhos, não mexe no celular e deixa você terminar a frase. Parece pouco, mas quase nunca acontece.", None),
    ("Também falhamos nisso. Ouvimos já preparando a resposta, medindo o tempo, pensando no que vem depois.", None),
    ("Simone Weil via na atenção uma forma rara de generosidade: voltar-se ao outro sem querer nada em troca.", "Uma reflexão inspirada em Simone Weil"),
    ("Hoje, numa conversa, pergunte uma segunda vez: e depois? Espere a resposta inteira antes de falar.", None),
    ("Se ninguém tem escutado você, procurar uma pessoa de confiança ou um profissional também é cuidado. Ser ouvido é uma necessidade, não um luxo.", None),
    ("Atenção é um presente que não custa dinheiro, só custa o que a pressa não deixa.", "Envie a alguém que sabe ouvir."),
], "r24",
    """Ser escutado de verdade é raro. E escutar de verdade também.

Simone Weil, filósofa francesa, escreveu sobre a atenção como uma forma de generosidade: voltar-se ao outro sem querer nada em troca. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Perguntar uma segunda vez e esperar a resposta inteira é um começo. E se faltar quem escute você, buscar uma pessoa de confiança ou ajuda profissional também é cuidado.

Quem escuta você de verdade?

Salve para lembrar de ouvir com calma e envie este post a quem sabe escutar.

Reflexão autoral inspirada em Simone Weil, sobre a atenção.

@doni7m""",
    ["#SimoneWeil", "#Atencao", "#EscutaAtiva", "#Generosidade", "#FilosofiaFrancesa", "#OuvirComCuidado",
     "#ConversaDeVerdade", "#TercaFeira", "#Acolher", "#Presenca"], 1,
    R("Simone Weil (1909-1943)", "Textos e cartas sobre atenção e generosidade (a ideia de atenção como forma rara de generosidade é associada a sua correspondência e a Gravity and Grace).",
      "https://www.themarginalian.org/2015/08/19/simone-weil-attention-gravity-and-grace/"))

single("2026-11-24", "Paulo Freire", "aprender com os outros",
       "Aprender é conversar com o mundo, e a conversa melhora quando há outros na roda.",
       "Uma reflexão inspirada em Paulo Freire", "r24b",
       """Quase tudo o que sabemos veio de alguém: uma avó, uma professora, um vizinho, um livro emprestado.

Paulo Freire, educador e filósofo da educação, defendia em Pedagogia do Oprimido que as pessoas se educam em comunhão, mediadas pelo mundo. A frase da imagem é uma reflexão autoral inspirada nessa ideia, e não uma citação.

Aprender não é só receber: é conversar, perguntar, ensinar de volta.

Quem te ensinou algo que você ainda usa?

Salve para lembrar de agradecer a essa pessoa.

Frase autoral inspirada em Paulo Freire; não é citação literal.

@doni7m""",
       ["#PauloFreire", "#PedagogiaDoOprimido", "#Educacao", "#Aprendizado", "#FilosofiaBrasileira", "#Conversar",
        "#Gratidao", "#TercaFeira", "#BomDia", "#Comunidade"], 4,
       R("Paulo Freire (1921-1997)", "Pedagogia do Oprimido (1968), sobre educação como diálogo e comunhão mediada pelo mundo.",
         "https://edisciplinas.usp.br/mod/resource/view.php?id=2526128",
         "frase autoral inspirada na ideia; não é citação literal"))

# ========================= QUARTA 25/11 — Arendt: recomeço =========================
car("2026-11-25", "Hannah Arendt", "recomeço e natalidade", [
    ("E se recomeçar não fosse um fracasso, mas uma capacidade?", None),
    ("Depois de uma decepção, a sensação de estar de volta ao ponto de partida. Como se tudo o que veio antes tivesse sido em vão.", None),
    ("Mas voltar ao começo não apaga o caminho. Quem recomeça já traz consigo o que aprendeu.", None),
    ("Hannah Arendt chamou de natalidade a capacidade humana de começar algo novo, que ninguém consegue prever por completo.", "Uma reflexão inspirada em Hannah Arendt"),
    ("Escolha um começo pequeno para esta semana: uma conversa adiada, uma caminhada, uma folha em branco.", None),
    ("Nem todo recomeço é voluntário, e alguns doem. Contar com outras pessoas nessa hora também faz parte de recomeçar.", None),
    ("Cada começo é frágil, e é por isso que merece cuidado. Dê ao seu o tempo de criar raiz.", "Salve para quando precisar recomeçar."),
], "r25",
    """Recomeçar pode parecer voltar à estaca zero. Mas quem recomeça já não é a mesma pessoa que começou da primeira vez.

Hannah Arendt, em A Condição Humana, chama de natalidade a capacidade que temos de iniciar algo novo e imprevisível. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Um começo pequeno já conta. E se a vida pediu um recomeço que você não escolheu, contar com outras pessoas, ou com ajuda profissional, também é cuidado.

Qual pequeno começo você poderia tentar esta semana?

Salve para lembrar dele e envie a quem está recomeçando.

Reflexão autoral inspirada em Hannah Arendt, A Condição Humana (natalidade).

@doni7m""",
    ["#HannahArendt", "#Natalidade", "#AcondicaoHumana", "#Recomecar", "#NovoComeco", "#FilosofiaPolitica",
     "#QuartaFeira", "#Recomeco", "#Esperanca", "#Coragem"], 2,
    R("Hannah Arendt (1906-1975)", "A Condição Humana (The Human Condition, 1958), conceito de natalidade e capacidade de começar.",
      "https://thefrailestthing.com/2017/01/02/the-miracle-that-saves-the-world/"))

single("2026-11-25", "Miguel de Unamuno", "a dúvida que importa",
       "Nem toda dúvida é falta de fé. Às vezes é o jeito honesto de continuar procurando.",
       "Uma reflexão inspirada em Unamuno", "r25b",
       """Há dúvidas que incomodam porque a pergunta é importante demais para ser respondida depressa.

Miguel de Unamuno, filósofo espanhol, em Do sentimento trágico da vida, trata a dúvida e o anseio de sentido como parte da experiência humana. A frase da imagem é uma reflexão autoral inspirada nessa ideia, e não uma citação.

Duvidar não é fraqueza: pode ser sinal de que você leva a vida a sério.

Qual pergunta você continua carregando?

Salve para voltar a ela com calma.

Frase autoral inspirada em Unamuno; não é citação literal.

@doni7m""",
       ["#Unamuno", "#MiguelDeUnamuno", "#SentimentoTragico", "#Duvida", "#FilosofiaEspanhola", "#PerguntasQueImportam",
        "#QuartaFeira", "#Sentido", "#BoaNoite", "#Reflexao"], 5,
       R("Miguel de Unamuno (1864-1936)", "Del sentimiento trágico de la vida (1912), sobre dúvida, sentido e anseio humano.",
         "https://revistas.usal.es/index.php/0210-749X/article/viewFile/1780/1836",
         "frase autoral inspirada na ideia; não é citação literal"))

# ========================= QUINTA 26/11 — Kierkegaard: escolha e vertigem =========================
car("2026-11-26", "Kierkegaard", "escolher e a vertigem da liberdade", [
    ("Por que escolher às vezes dá vertigem?", None),
    ("Duas portas abertas, nenhuma garantia. Você pesa, adia, pergunta a todo mundo, e a decisão continua exatamente onde estava.", None),
    ("Quando há muitos caminhos possíveis, a liberdade pesa. O frio na barriga não quer dizer que você escolheu mal.", None),
    ("Kierkegaard descreveu a angústia como a vertigem da liberdade: o susto de perceber que o futuro ainda não está escrito.", "Uma reflexão inspirada em Kierkegaard"),
    ("Reduza a escolha ao próximo passo reversível: marcar a conversa, fazer a inscrição, testar por uma semana.", None),
    ("Se a angústia vira peso demais, falar com alguém de confiança ou com um profissional também é cuidado. Decidir não precisa ser solitário.", None),
    ("Escolher não elimina a vertigem. Ensina a andar com ela sem deixar de dar o passo.", "Salve para a próxima decisão difícil."),
], "r26",
    """Algumas decisões não pesam pelo que são, e sim pelo tanto de futuro que carregam.

Kierkegaard, em O Conceito de Angústia, descreve a angústia como a vertigem da liberdade, o susto de perceber que há possibilidades abertas. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Quando a escolha parecer grande demais, reduza-a ao próximo passo que dá para desfazer. E se a angústia pesar, conversar com alguém de confiança ou com um profissional também é cuidado.

Qual escolha você tem adiado?

Salve para lembrar do próximo passo e envie a quem está indeciso.

Reflexão autoral inspirada em Søren Kierkegaard, O Conceito de Angústia (1844).

@doni7m""",
    ["#Kierkegaard", "#SorenKierkegaard", "#ConceitoDeAngustia", "#Existencialismo", "#Escolhas", "#TomarDecisoes",
     "#Liberdade", "#QuintaFeira", "#Ansiedade", "#CuidarDeSi"], 0,
    R("Søren Kierkegaard (1813-1855)", "O Conceito de Angústia (Begrebet Angest, 1844), angústia como vertigem da liberdade.",
      "https://philosophynow.org/issues/145/Kierkegaard_Young_Free_and_Anxious"))

single("2026-11-26", "Heráclito", "mudança e curiosidade",
       "Nem o rio nem você são os mesmos de ontem. Dá para olhar a mudança com curiosidade.",
       "Uma reflexão inspirada em Heráclito", "r26b",
       """Dá para estranhar o espelho, a rua, a própria voz. A vida muda mesmo quando a gente não percebe.

Heráclito de Éfeso, pensador pré-socrático, é lembrado pelas imagens do rio e do fluxo: tudo se transforma. Os fragmentos que chegaram até nós são poucos e disputados, por isso a frase da imagem é uma reflexão autoral inspirada nessa ideia, e não uma citação.

Mudar não é trair quem se foi: é continuar vivo.

O que em você mudou nos últimos anos e merece um olhar gentil?

Salve para reler quando a mudança assustar.

Frase autoral inspirada em Heráclito; não é citação literal.

@doni7m""",
       ["#Heraclito", "#PreSocraticos", "#FilosofiaGrega", "#TudoMuda", "#Impermanencia", "#Mudanca",
        "#QuintaFeira", "#BoaNoite", "#Curiosidade", "#Transformacao"], 2,
       R("Heráclito de Éfeso (c. 540-480 a.C.)", "Fragmentos (Diels-Kranz B12 e B91, sobre o rio), transmitidos por citações posteriores; tradução e atribuição exata são debatidas.",
         "https://www.worldhistory.org/article/182/heraclitus-fragments/",
         "frase autoral inspirada na ideia; não é citação literal"))

# ========================= SEXTA 27/11 — Epicuro: amizade e simplicidade =========================
car("2026-11-27", "Epicuro", "amizade e mesa simples", [
    ("O que torna um jantar simples tão bom?", None),
    ("Pão, uma sopa quente, uma luz baixa. E alguém do outro lado da mesa com quem não é preciso fingir nada.", None),
    ("Costumamos achar que a felicidade pede mais: mais planos, mais coisas, mais ocasiões especiais.", None),
    ("Epicuro ensinava que muito do que nos faz bem é simples e está ao alcance, sobretudo a companhia de amigos.", "Uma reflexão inspirada em Epicuro"),
    ("Convide alguém para uma refeição sem pretensão. Menos cardápio, mais conversa. Quem chega, chega como está.", None),
    ("Se faltam amigos por perto, procurar companhia também é cuidado: um grupo, um vizinho, um telefonema para quem ficou longe.", None),
    ("O que sustenta um dia bom raramente é grande. Costuma ser uma mesa, uma luz e alguém.", "Envie a quem você gostaria de ter à mesa."),
], "r27",
    """Às vezes o melhor dia da semana é uma mesa simples e uma boa conversa.

Epicuro, na Carta a Meneceu, defende uma vida de prazeres simples e de amizade como uma das maiores fontes de tranquilidade. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Convidar alguém sem pretensão já é um começo. E se faltarem pessoas por perto, procurar companhia também é cuidado.

Quem você gostaria de ter à mesa neste fim de semana?

Salve para lembrar de fazer o convite e envie a esse alguém.

Reflexão autoral inspirada em Epicuro, Carta a Meneceu.

@doni7m""",
    ["#Epicuro", "#Epicurismo", "#CartaAMeneceu", "#Amizade", "#PrazeresSimples", "#MesaPosta",
     "#FilosofiaAntiga", "#SextaFeira", "#BoaSextaFeira", "#Companhia"], 3,
    R("Epicuro (341-270 a.C.)", "Carta a Meneceu, sobre prazeres simples, autossuficiência e amizade.",
      "https://classics.mit.edu/Epicurus/menoec.html"))

single("2026-11-27", "Demócrito", "alegria tranquila",
       "A alegria tranquila cresce quando o desejo cabe no dia.",
       "Uma reflexão inspirada em Demócrito", "r27b",
       """Nem sempre a alegria vem de ter mais. Às vezes vem de querer algo que caiba no dia.

Demócrito de Abdera, pensador grego, escreveu sobre a euthymia, um bom ânimo tranquilo, associado à medida nos desejos. Os escritos chegaram em fragmentos, então a frase da imagem é uma reflexão autoral inspirada nessa ideia, e não uma citação.

Querer com medida não é desistir de nada: é abrir espaço para notar o que já está aqui.

O que cabe no seu dia hoje?

Salve para lembrar dessa medida.

Frase autoral inspirada em Demócrito; não é citação literal.

@doni7m""",
       ["#Democrito", "#Euthymia", "#AlegriaTranquila", "#FilosofiaGrega", "#BomAnimo", "#Medida",
        "#SextaFeira", "#BoaSextaFeira", "#Moderacao", "#Contentamento"], 6,
       R("Demócrito de Abdera (c. 460-370 a.C.)", "Fragmentos e testemunhos sobre euthymia (bom ânimo), transmitidos por Estobeu e outros.",
         "https://plato.stanford.edu/entries/democritus/",
         "frase autoral inspirada na ideia; não é citação literal"))

# ========================= SÁBADO 28/11 — Espinosa: o que aumenta sua força =========================
car("2026-11-28", "Espinosa", "o que dá e o que tira força", [
    ("O que te dá força e o que te tira?", None),
    ("Há pessoas e lugares depois dos quais você volta mais inteiro. E há outros depois dos quais só quer sumir por algumas horas.", None),
    ("Nem sempre dá para escolher tudo. Mas notar o efeito de cada coisa já ajuda a dar nome ao que se sente.", None),
    ("Espinosa afirmou que alegria é a passagem a uma perfeição maior, e tristeza, a uma menor: afetos que aumentam ou diminuem nossa potência.", "Uma reflexão inspirada em Espinosa"),
    ("Esta semana, anote três coisas que te deixaram mais vivo e três que te esvaziaram. Sem julgar, só observar.", None),
    ("Tristezas longas não se resolvem só com observação. Compartilhar com alguém de confiança ou buscar ajuda também é cuidado.", None),
    ("Aumentar a própria força não é virar outra pessoa: é aproximar-se do que te faz bem.", "Salve para repetir o exercício."),
], "r28",
    """Há encontros que nos expandem e há encontros que nos encolhem. Perceber a diferença já é um começo.

Espinosa, na Ética (parte III), define alegria como a passagem a uma maior perfeição e tristeza como a passagem a uma menor, ou seja, afetos que aumentam ou diminuem a nossa potência de agir. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Anotar o que te dá força e o que te tira, sem julgar, pode revelar caminhos. E se a tristeza durar, conversar com alguém de confiança ou com um profissional também é cuidado.

O que te deu força esta semana?

Salve para refazer o exercício e envie a quem precisa de um ânimo.

Reflexão autoral inspirada em Baruch Espinosa, Ética, parte III.

@doni7m""",
    ["#Espinosa", "#Spinoza", "#Etica", "#Afetos", "#Alegria", "#FilosofiaModerna",
     "#PotenciaDeAgir", "#Sabado", "#BomFimDeSemana", "#CuidarDeSi"], 4,
    R("Baruch Espinosa (1632-1677)", "Ética (Ethica, 1677), parte III: sobre os afetos de alegria e tristeza como aumento e diminuição da potência de agir.",
      "https://www.gutenberg.org/cache/epub/948/pg948-images.html"))

single("2026-11-28", "Rabi Hilel", "cuidar de si e dos outros",
       "Cuidar de si e cuidar dos outros não competem. Os dois pedem para começar agora, ainda que pequeno.",
       "Uma reflexão inspirada em Hilel", "r28b",
       """Dá para se perder entre dois extremos: viver só para si ou esquecer-se de si por todos.

Hilel, o Ancião, mestre judeu do século I a.C., é lembrado em Pirkei Avot por perguntas sobre cuidar de si, dos outros e do momento presente. A frase da imagem é uma reflexão autoral inspirada nessas perguntas, e não uma citação.

Um gesto pequeno de cada lado já ajuda a equilibrar a balança.

O que você pode fazer hoje por você e por alguém?

Salve para lembrar dos dois.

Frase autoral inspirada em Hilel; não é citação literal.

@doni7m""",
       ["#Hilel", "#PirkeiAvot", "#EticaJudaica", "#Cuidado", "#Solidariedade", "#AutoCuidado",
        "#Sabado", "#BomFimDeSemana", "#Equilibrio", "#Reflexao"], 5,
       R("Hilel, o Ancião (séc. I a.C.-séc. I d.C.)", "Pirkei Avot 1:14 (Ética dos Pais, Mishná), perguntas atribuídas a Hilel sobre cuidar de si, dos outros e do agora.",
         "https://voices.sefaria.org/sheets/35125",
         "frase autoral inspirada nas perguntas; não é citação literal"))

# ========================= DOMINGO 29/11 — Marco Aurélio: mudança =========================
car("2026-11-29", "Marco Aurélio", "mudança e aceitar o que passa", [
    ("E se a mudança não for inimiga do que você ama?", None),
    ("A casa da infância mudou, os amigos moram longe, a rotina de ontem não volta. Bate uma saudade quieta de como era.", None),
    ("Resistir a toda mudança cansa. Mas aceitá-la não é concordar com tudo nem fingir que não dói.", None),
    ("Marco Aurélio, nas Meditações, lembrou que a mudança é da própria natureza das coisas e que nada de útil nasce sem ela.", "Uma reflexão inspirada em Marco Aurélio"),
    ("Pergunte-se: o que nesta mudança já aconteceu e o que ainda posso decidir? Dedique energia só à segunda parte.", None),
    ("Há mudanças que pedem luto, e luto pede companhia. Procurar quem escute ou ajuda profissional também é cuidado.", None),
    ("Quem aceita que tudo passa descobre que também passa o que pesa, e fica o que importa.", "Salve para os dias de despedida."),
], "r29",
    """Mudar de fase, de casa, de rotina: quase toda mudança traz um pouco de saudade junto.

Marco Aurélio, nas Meditações, escreve sobre a transformação como parte da natureza das coisas. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Separar o que já aconteceu do que ainda dá para decidir ajuda a gastar energia no lugar certo. E se a mudança pedir luto, procurar companhia ou ajuda profissional também é cuidado.

Que mudança você ainda está aprendendo a aceitar?

Salve para reler nos dias de despedida e envie a quem está se despedindo de algo.

Reflexão autoral inspirada em Marco Aurélio, Meditações (livro VII).

@doni7m""",
    ["#MarcoAurelio", "#Meditacoes", "#Estoicismo", "#Mudanca", "#Aceitacao", "#Luto",
     "#Domingo", "#DomingoDeReflexao", "#Impermanencia", "#Recomeco"], 1,
    R("Marco Aurélio (121-180 d.C.)", "Meditações (Ta eis heauton), reflexões sobre mudança e natureza (por ex. livro VII).",
      "https://classics.mit.edu/Antoninus/meditations.7.seven.html"))

single("2026-11-29", "Mestre Eckhart", "soltar com a mão aberta",
       "Soltar não é perder. É abrir a mão para o que realmente cabe.",
       "Uma reflexão inspirada em Mestre Eckhart", "r29b",
       """Segurar com força cansa a mão e deixa pouco espaço para o que chega.

Mestre Eckhart, teólogo e místico medieval alemão, escreveu sobre o desprendimento (Abgeschiedenheit) e o deixar-ser (Gelassenheit). A frase da imagem é uma reflexão autoral inspirada nessa ideia, e não uma citação.

Soltar pode ser pequeno: um rancor, uma tarefa que não é sua, uma ideia fixa do que o dia deveria ser.

O que você poderia soltar hoje?

Salve para lembrar de abrir a mão.

Frase autoral inspirada em Eckhart; não é citação literal.

@doni7m""",
       ["#MestreEckhart", "#Eckhart", "#Gelassenheit", "#Desapego", "#Desprendimento", "#FilosofiaMedieval",
        "#Domingo", "#DomingoDeReflexao", "#Soltar", "#Leveza"], 6,
       R("Meister Eckhart (c. 1260-1328)", "Von abegescheidenheit (Sobre o desprendimento) e sermões, sobre desprendimento e Gelassenheit.",
         "https://german.yale.edu/sites/default/files/meister_eckhart_on_detachment.pdf",
         "frase autoral inspirada na ideia; não é citação literal"))
