# -*- coding: utf-8 -*-
"""Conteúdo da semana 02/11 a 08/11/2026 (14 posts): 7 carrosséis (A) + 7 imagens únicas (B)."""
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


# ========================= SEGUNDA 02/11 =========================
car("2026-11-02", "Montaigne", "um canto só seu (solitude)", [
    ("Mesmo cercado de gente, você tem um canto só seu?", None),
    ("Há dias em que você atende todo mundo: mensagens, pedidos, opiniões. Quando a noite chega, já nem sabe o que pensa.", None),
    ("Estar só por escolha não é o mesmo que ficar sozinho sem querer. Um acolhe, o outro pesa.", None),
    ("Montaigne propunha guardar, dentro da vida cheia, um fundo de loja só seu: um espaço livre para conversar consigo.", "Uma reflexão inspirada em Montaigne"),
    ("Dez minutos bastam: caminhar sem fone, escrever três linhas, olhar o mar pela janela. Sem produzir nada. O canto é seu.", None),
    ("Esse canto não substitui as pessoas. Se a solidão estiver mais pesada do que silenciosa, procurar companhia ou ajuda também é cuidado.", None),
    ("Quem tem um canto só seu volta aos outros mais inteiro. Qual é o seu?", "Salve para lembrar de visitá-lo."),
], "n02",
    """Tem dia em que você responde a todo mundo e, quando a noite chega, não sobra ninguém para conversar com você mesmo.

Montaigne, no ensaio Da solidão, sugere reservar “um fundo de loja” só nosso, um canto livre dentro da vida cheia. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Ter um canto assim não é fugir das pessoas. É voltar a elas com mais inteireza. E, se a solidão estiver mais pesada do que silenciosa, procurar companhia ou ajuda também é uma forma de cuidar de si.

Onde fica o seu canto: uma caminhada, um caderno, uma janela?

Salve para lembrar de visitá-lo e envie a quem anda sem tempo para si.

Reflexão autoral inspirada em Montaigne, Ensaios, “Da solidão” (Livro I).

@doni7m""",
    ["#Montaigne", "#MichelDeMontaigne", "#Ensaios", "#Solitude", "#TempoParaSi", "#CantoSeu", "#FilosofiaFrancesa",
     "#Renascimento", "#PausaNoDia", "#SegundaFeira", "#Silencio"], 0,
    """Filósofo e ensaísta: Michel de Montaigne (1533-1592).
Obra: Ensaios (Essais), Livro I, capítulo 39, “Da solidão” (De la solitude).
Passagem consultada (tradução inglesa citada na página): "We must reserve a back shop all our own, entirely free" (“devemos reservar um fundo de loja todo nosso, inteiramente livre”). A página não indica livro e capítulo; o ensaio aparece ali como o de número 39, e o capítulo 39 do Livro I corresponde a “Da solidão” nas edições correntes.
Link consultado: https://hermitary.com/solitude/montaigne.html
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal no carrossel nem na legenda (apenas a expressão “fundo de loja”).""")

single("2026-11-02", "Foucault", "cuidado de si",
       "Cuidar de si não é egoísmo. É um exercício diário de ficar à altura da própria vida.",
       "Uma reflexão inspirada em Foucault", "n02b",
       """Cuidar de si costuma ser a última coisa da lista, logo depois de todo mundo.

Michel Foucault dedicou o curso A Hermenêutica do Sujeito (Collège de France, 1981-1982) ao cuidado de si na Antiguidade, a partir de Sócrates. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Cuidar de si pode ser pequeno: regar o vaso, dormir melhor, dizer não a mais uma tarefa.

O que você poderia cuidar hoje, só porque faz bem?

Salve para voltar a esta pergunta quando a semana apertar.

Frase autoral inspirada em Foucault, A Hermenêutica do Sujeito (curso de 1981-1982); não é citação literal.

@doni7m""",
       ["#Foucault", "#MichelFoucault", "#CuidadoDeSi", "#HermeneuticaDoSujeito", "#Autocuidado", "#FilosofiaFrancesa",
        "#RotinaGentil", "#VidaDiaria", "#BomDia", "#PequenosCuidados"], 3,
       """Filósofo: Michel Foucault (1926-1984).
Obra: A Hermenêutica do Sujeito (L'herméneutique du sujet), curso no Collège de France, 1981-1982.
Fonte consultada: a página da editora descreve o curso como um exame de como o “cuidado de si” (epimeleia heautou) foi pensado na Antiguidade, a partir de Sócrates.
Link consultado: https://academic.macmillan.com/academictrade/9780312425708/thehermeneuticsofthesubject
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")

# ========================= TERÇA 03/11 =========================
car("2026-11-03", "Sartre", "ainda em construção", [
    ("Quem disse que você já está pronto, definido e sem chance de mudar?", None),
    ("Alguém colou uma etiqueta em você há anos: “tímido”, “sem jeito”, “o que nunca termina”. De tanto ouvir, você repete.", None),
    ("A etiqueta descreve o que você fez até aqui. Ela não conhece o que ainda vai fazer.", None),
    ("Para Sartre, a existência vem antes da essência: ninguém nasce com um destino escrito, e cada pessoa se faz pelo que escolhe fazer.", "Uma reflexão inspirada em Sartre"),
    ("Escolha um gesto pequeno que não combine com a etiqueta: ligar para alguém, recusar um pedido, voltar a tocar. Um gesto já abre uma fresta.", None),
    ("Isso não apaga o que pesa. Idade, dinheiro, saúde e lugar de origem entram na conta. Liberdade é o espaço que sobra depois deles.", None),
    ("Você ainda está se fazendo. Que gesto seu desmentiria a etiqueta hoje?", "Salve ou envie a quem se subestima."),
], "n03",
    """Algumas etiquetas grudam cedo e a gente carrega por anos, como se fossem parte do corpo.

Para Jean-Paul Sartre, em O existencialismo é um humanismo, a existência precede a essência: não nascemos com uma natureza pronta, e cada pessoa vai se fazendo pelo que faz de si. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Isso não significa que tudo dependa só de vontade. Idade, dinheiro, saúde e lugar de origem pesam, e reconhecer isso também é honestidade. Ainda assim, quase sempre sobra um espaço pequeno de escolha.

Qual etiqueta antiga você gostaria de desmentir com um gesto?

Salve para reler quando a dúvida bater e envie a quem se subestima.

Reflexão autoral inspirada em Jean-Paul Sartre, O existencialismo é um humanismo (1946).

@doni7m""",
    ["#Sartre", "#JeanPaulSartre", "#Existencialismo", "#ExistencialismoEUmHumanismo", "#Escolhas", "#Liberdade",
     "#SemEtiquetas", "#Recomecar", "#FilosofiaFrancesa", "#TercaFeira", "#Autonomia"], 6,
    """Filósofo: Jean-Paul Sartre (1905-1980).
Obra: O existencialismo é um humanismo (L'existentialisme est un humanisme), conferência de 1946.
Passagens consultadas (tradução inglesa): "What do we mean by saying that existence precedes essence?"; "Man is nothing else but that which he makes of himself."; "man is condemned to be free" e "We are left alone, without excuse."
Link consultado: https://www3.nd.edu/~afreddos/courses/264/sartre.htm
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal no carrossel nem na legenda. A ressalva sobre limites (idade, dinheiro, saúde) é do texto autoral, para não sugerir que tudo dependa de vontade.""")

single("2026-11-03", "Gabriel Marcel", "presença e disponibilidade",
       "Estar presente é mais do que estar no mesmo lugar. É ficar disponível para o outro.",
       "Uma reflexão inspirada em Gabriel Marcel", "n03b",
       """Dá para estar na mesma sala e continuar ausente. E dá para estar longe e se fazer presente.

Gabriel Marcel chamava de disponibilidade a abertura de uma pessoa ao outro, e dizia que alguém na mesma sala pode estar ausente enquanto outro, a quilômetros, está presente. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Às vezes, ficar disponível é só deixar a porta aberta e a luz acesa.

Para quem você pode estar mais disponível esta semana?

Salve para lembrar de dar um oi.

Frase autoral inspirada em Gabriel Marcel; não é citação literal.

@doni7m""",
       ["#GabrielMarcel", "#Marcel", "#Disponibilidade", "#Presenca", "#Relacoes", "#Amizade", "#FilosofiaFrancesa",
        "#Existencialismo", "#AtencaoAoOutro", "#Acolher"], 9,
       """Filósofo: Gabriel Marcel (1889-1973).
Fonte consultada: verbete da Encyclopaedia Britannica (seção “The broken world”): descreve a disponibilidade (disponibilité) como o grau de abertura de uma pessoa ao outro e contrasta quem está na mesma sala e “ausente” com quem está a quilômetros e “presente”.
Link consultado: https://www.britannica.com/biography/Gabriel-Honore-Marcel/The-broken-world
Observação: a obra específica não foi consultada diretamente; a atribuição é à ideia geral descrita na fonte.
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")

# ========================= QUARTA 04/11 (teste A às 12:00 Madeira) =========================
car("2026-11-04", "Plutarco", "comparação", [
    ("Por que olhar para quem tem mais faz o que você tem parecer pouco?", None),
    ("Você abre o celular e vê a viagem, a casa nova, a promoção do outro. Em segundos, a sua semana boa encolhe.", None),
    ("Plutarco notava esse costume: muita gente sofre mais com o que os outros possuem do que se alegra com o que tem.", "Uma reflexão inspirada em Plutarco"),
    ("Ele sugeria também olhar para quem vive com menos, sem comemorar a falta de ninguém, apenas para enxergar o próprio quinhão.", None),
    ("Escreva três coisas que você já tem e que, há alguns anos, pediria como um favor: uma chave, uma carta, uma xícara quente.", None),
    ("Comparar às vezes informa. Mas se a régua só sobe e nunca chega, o problema é a régua, não você.", None),
    ("O que da sua vida já bastaria para quem você foi um dia?", "Salve para reler quando a vitrine pesar."),
], "n04",
    """A vitrine dos outros tem um truque: ela mostra o melhor ângulo e esconde o resto, e a sua vida inteira entra na comparação.

Plutarco, em Sobre a tranquilidade da alma, observa que muita gente se aflige mais com o que os outros têm do que goza do que possui, e sugere olhar também para quem vive com menos. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

A ideia não é se consolar com a falta alheia, e sim enxergar com mais justiça o que já está nas suas mãos.

O que você tem hoje que o você de alguns anos atrás pediria como um favor?

Salve para reler quando a vitrine pesar e envie a quem anda se comparando demais.

Reflexão autoral inspirada em Plutarco, Sobre a tranquilidade da alma (De tranquillitate animi), Moralia.

@doni7m""",
    ["#Plutarco", "#Moralia", "#TranquilidadeDaAlma", "#Comparacao", "#Gratidao", "#FilosofiaAntiga", "#MenosVitrine",
     "#ValorProprio", "#QuartaFeira", "#Suficiencia", "#PazInterior"], 12,
    """Filósofo e moralista: Plutarco (c. 46-120 d.C.).
Obra: Sobre a tranquilidade da alma (Peri euthymias / De tranquillitate animi), em Moralia, seções 9 a 12.
Passagens consultadas (tradução inglesa, Loeb, via Thayer/LacusCurtius): observar “persons of inferior fortune, and not, as most people do, compare oneself with those who are superior” (§10); “does not rejoice so much in our own blessings as it is pained by those which other men possess” (§11); “not to overlook whatever we have that is pleasant and attractive” (§8).
Link consultado: https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Moralia/De_tranquillitate_animi*.html
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal no carrossel nem na legenda. A ressalva “sem comemorar a falta de ninguém” é do texto autoral.""")

single("2026-11-04", "Kitarō Nishida", "experiência inteira do presente",
       "Antes de pensar sobre o pôr do sol, houve o pôr do sol. Volte a ele, de vez em quando.",
       "Uma reflexão inspirada em Kitarō Nishida", "n04b",
       """A gente passa tanto tempo comentando a vida que esquece de simplesmente vivê-la.

O filósofo japonês Kitarō Nishida chamou de experiência pura a percepção direta, anterior a pensamentos, julgamentos e reações, em Uma investigação sobre o bem (1911). A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Hoje, por alguns minutos, olhe para uma coisa só (o céu, a xícara, o rosto de alguém) antes de comentá-la por dentro.

O que você vai olhar sem comentar?

Salve para lembrar de olhar.

Frase autoral inspirada em Nishida, Uma investigação sobre o bem (1911); não é citação literal.

@doni7m""",
       ["#Nishida", "#KitaroNishida", "#ExperienciaPura", "#FilosofiaJaponesa", "#PorDoSol", "#Presenca", "#OlharComCalma",
        "#EscolaDeKyoto", "#UmaInvestigacaoSobreOBem", "#MomentoPresente"], 15,
       """Filósofo: Kitarō Nishida (1870-1945).
Obra: Uma investigação sobre o bem (Zen no kenkyū, 1911).
Fonte consultada: verbete da EBSCO Research Starters: a “experiência pura” é a percepção direta dos fenômenos antes de pensamentos, juízos e sentimentos, sem separação entre sujeito e objeto (“mere constructions abstracted from a unified experience”).
Link consultado: https://www.ebsco.com/research-starters/literature-and-writing/inquiry-good-kitaro-nishida
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")

# ========================= QUINTA 05/11 =========================
car("2026-11-05", "Josef Pieper", "lazer e pequenos prazeres", [
    ("Descansar só para voltar a render ainda é descansar?", None),
    ("Você tira a tarde livre e, no meio dela, já planeja a próxima semana. O corpo parou, mas a cabeça segue no escritório.", None),
    ("Vivemos como se o valor do dia fosse medido pelo que ele produz. Até o descanso vira tarefa: dormir direito, relaxar direito.", None),
    ("Pieper chamava de lazer outra coisa: uma atitude aberta, de quem se deixa tocar pelo mundo sem exigir resultado.", "Uma reflexão inspirada em Josef Pieper"),
    ("Experimente uma hora sem utilidade: cozinhar devagar, ouvir um disco inteiro, ver a chuva cair. Sem foto, sem meta.", None),
    ("Se a culpa aparecer, deixe passar. Ela vem de um costume antigo de só se achar digno quando se é útil.", None),
    ("Que prazer pequeno você merece só por existir?", "Salve e envie a quem não se permite parar."),
], "n05",
    """Descansar para voltar a produzir mais não é bem descansar, é manutenção.

Josef Pieper, em Lazer, a base da cultura, defende o lazer como uma atitude de abertura, uma condição da alma que capacita a perceber a realidade, e alerta que o trabalho total ameaça essa capacidade. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Não é elogio à preguiça, nem regra que caiba em todas as rotinas. É um convite a reservar, de vez em quando, um tempo que não precise render nada.

Qual prazer pequeno você anda adiando por achar que não tem utilidade?

Salve para reler antes do fim de semana e envie a quem não se permite parar.

Reflexão autoral inspirada em Josef Pieper, Lazer, a base da cultura (Leisure: The Basis of Culture).

@doni7m""",
    ["#JosefPieper", "#Pieper", "#LazerEFilosofia", "#PequenosPrazeres", "#Descanso", "#SemCulpa", "#TempoLivre",
     "#FilosofiaAlema", "#Pausa", "#QuintaFeira", "#VidaLeve"], 18,
    """Filósofo: Josef Pieper (1904-1997).
Obra: Lazer, a base da cultura (Leisure: The Basis of Culture).
Passagens consultadas (descrição da editora Liberty Fund): leisure como “an attitude of mind and a condition of the soul that fosters a capacity to perceive the reality of the world”; “in our bourgeois Western world total labor has vanquished leisure”.
Link consultado: https://www.libertyfund.org/?p=12260
Observação: a página é uma apresentação da editora, não o texto integral.
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal no carrossel nem na legenda.""")

single("2026-11-05", "Martha Nussbaum", "fragilidade do que é bom",
       "O que é bom na vida é frágil. Talvez por isso mereça tanto cuidado.",
       "Uma reflexão inspirada em Martha Nussbaum", "n05b",
       """Quase tudo o que mais importa depende de coisas que não controlamos: saúde, tempo, gente.

Em A Fragilidade da Bondade, Martha Nussbaum examina como muitos dos componentes de uma vida boa são vulneráveis a fatores fora do nosso controle. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Perceber a fragilidade não precisa trazer medo. Pode trazer cuidado.

O que, na sua vida, você gostaria de cuidar melhor por ser frágil?

Salve para lembrar de cuidar do que é raro.

Frase autoral inspirada em Nussbaum, A Fragilidade da Bondade (1986); não é citação literal.

@doni7m""",
       ["#MarthaNussbaum", "#Nussbaum", "#FragilidadeDaBondade", "#Vulnerabilidade", "#Cuidado", "#FilosofiaMoral",
        "#TragediaGrega", "#ValorDasPequenasCoisas", "#CuidarDoQueImporta", "#Resiliencia"], 21,
       """Filósofa: Martha C. Nussbaum (n. 1947).
Obra: A Fragilidade da Bondade: sorte e ética na tragédia e na filosofia gregas (The Fragility of Goodness), 1986.
Fonte consultada (descrição do livro): “many of the valued constituents of a well-lived life are vulnerable to factors outside a person's control”. A página consultada não confirma o ano; a data de 1986 é a da primeira edição, conforme as edições correntes (conferir na edição em mãos).
Link consultado: https://www.labyrinthbooks.com/the-fragility-of-goodness
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")

# ========================= SEXTA 06/11 (teste B às 20:30 Madeira) =========================
car("2026-11-06", "Paul Tillich", "coragem de ser", [
    ("Coragem não é ausência de medo. É continuar sendo você apesar dele.", None),
    ("Você quer dizer algo difícil, mudar de rumo ou assumir um gosto que ninguém por perto compartilha. E o medo sussurra: melhor não.", None),
    ("Esperamos o dia em que o medo vá embora para agir. Esse dia raramente chega, e a vida segue esperando na porta.", None),
    ("Paul Tillich via a coragem como uma afirmação do próprio ser apesar da ansiedade: dizer “eu sou” mesmo com o chão tremendo.", "Uma reflexão inspirada em Paul Tillich"),
    ("Escolha uma afirmação pequena para hoje: pedir o que precisa, dizer não, mostrar um trabalho. Com medo, mesmo assim.", None),
    ("Coragem também é pedir apoio. Ninguém afirma o próprio ser sozinho o tempo todo, e pedir ajuda faz parte.", None),
    ("O que você faria hoje, com medo mesmo, por ser quem é?", "Salve ou envie a quem está juntando coragem."),
], "n06",
    """Quase ninguém age quando o medo vai embora. A maioria age com ele ao lado.

Paul Tillich, em A coragem de ser (1952), descreve a coragem como a afirmação de si mesmo apesar da ansiedade do não ser. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Isso não é um chamado para se forçar além do que dá. Coragem também inclui dizer não, descansar e pedir apoio. Se o medo estiver pesado demais, conversar com alguém de confiança ou com um profissional também é um jeito de ser corajoso.

Que pequena afirmação de quem você é pode caber no seu dia de hoje?

Salve para reler antes de uma conversa difícil e envie a quem anda juntando coragem.

Reflexão autoral inspirada em Paul Tillich, A coragem de ser (The Courage to Be, 1952).

@doni7m""",
    ["#PaulTillich", "#Tillich", "#ACoragemDeSer", "#TheCourageToBe", "#Coragem", "#Medo", "#SerVoceMesmo",
     "#FilosofiaExistencial", "#SextaFeira", "#PedirApoio", "#Autenticidade"], 24,
    """Filósofo e teólogo: Paul Tillich (1886-1965).
Obra: A coragem de ser (The Courage to Be), 1952; versão ampliada das Terry Lectures dadas em Yale no outono de 1950.
Fonte consultada (verbete EBSCO Research Starters): a coragem como “the universal and essential self-affirmation of one's being”, “in spite of the anxiety of nonbeing”. A frase literal “courage is self-affirmation in spite of” não consta na página; a ideia, sim.
Link consultado: https://www.ebsco.com/research-starters/literature-and-writing/tillich-examines-modern-anxiety-courage-be
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal no carrossel nem na legenda (as aspas em “eu sou” são do texto autoral, não de Tillich).""")

single("2026-11-06", "Pierre Hadot", "filosofia como modo de viver",
       "Filosofar não é só pensar bonito. É praticar, aos poucos, um jeito de viver.",
       "Uma reflexão inspirada em Pierre Hadot", "n06b",
       """Muita ideia boa fica só no caderno. A diferença está no que a gente pratica em silêncio.

Pierre Hadot, em Exercícios espirituais e filosofia antiga e em O que é a filosofia antiga?, mostrou que, na Antiguidade, a filosofia era um modo de ver e de estar no mundo, praticado com exercícios, e não só teoria. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Um degrau por vez já é caminho.

Que pequena prática você levaria desta semana para a próxima?

Salve para lembrar de praticar.

Frase autoral inspirada em Hadot, Philosophy as a Way of Life (edição inglesa de 1995); não é citação literal.

@doni7m""",
       ["#PierreHadot", "#Hadot", "#FilosofiaComoModoDeVida", "#ExerciciosEspirituais", "#FilosofiaAntiga", "#Pratica",
        "#UmDegrauPorVez", "#HabitosGentis", "#SextaNoite", "#FilosofiaPratica"], 27,
       """Filósofo e historiador da filosofia antiga: Pierre Hadot (1922-2010).
Obras: Exercícios espirituais e filosofia antiga; O que é a filosofia antiga?; edição inglesa Philosophy as a Way of Life (Blackwell, 1995).
Fonte consultada (página da editora da edição inglesa): a filosofia antiga praticada como exercícios espirituais que moldavam o modo de viver, “a way of seeing and of being in the world”.
Link consultado: https://www.wiley-vch.de/en/areas-interest/humanities-social-sciences/philosophy-as-a-way-of-life-978-0-631-18033-3
Natureza do texto: frase autoral inspirada na ideia; não é citação literal. Os títulos em português acima são os conhecidos das edições brasileiras e portuguesas; a página consultada trata da edição inglesa.""")

# ========================= SÁBADO 07/11 =========================
car("2026-11-07", "Gadamer", "conversar de verdade", [
    ("Algumas conversas nos levam para onde nem pensávamos ir.", None),
    ("Você chega querendo provar um ponto. Sai pensando em outra coisa, e a conversa já não é a que você planejou.", None),
    ("Muitas vezes ouvimos só esperando a nossa vez. A conversa vira dois monólogos educados.", None),
    ("Gadamer dizia que caímos numa conversa mais do que a conduzimos: ela tem espírito próprio, e quem entra de verdade pode sair mudado.", "Uma reflexão inspirada em Gadamer"),
    ("Hoje, faça uma pergunta a mais antes de responder. Escute até o fim da frase, sem ensaiar o que dirá.", None),
    ("Isso exige abrir mão de ter razão o tempo todo. Em troca, a pessoa à sua frente deixa de ser plateia.", None),
    ("Com quem vale a pena ter uma conversa sem pressa neste fim de semana?", "Salve ou envie a essa pessoa."),
], "n07",
    """Já aconteceu de você começar uma conversa de cinco minutos e terminar duas horas depois, pensando outra coisa?

Hans-Georg Gadamer, em Verdade e Método, escreve que, em geral, “caímos em conversação”, e que uma conversa tem um espírito próprio. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Ouvir de verdade dá trabalho: pede abrir mão, por alguns minutos, da necessidade de ter razão.

Quem seria a pessoa certa para uma conversa sem pressa neste sábado?

Salve para lembrar de perguntar mais e envie a essa pessoa.

Reflexão autoral inspirada em Hans-Georg Gadamer, Verdade e Método (1960).

@doni7m""",
    ["#Gadamer", "#HansGeorgGadamer", "#VerdadeEMetodo", "#Hermeneutica", "#Conversa", "#EscutaAtiva", "#Dialogo",
     "#FilosofiaAlema", "#Sabado", "#ConversaSemPressa", "#Amizade"], 0,
    """Filósofo: Hans-Georg Gadamer (1900-2002).
Obra: Verdade e Método (Wahrheit und Methode), 1960; tradução inglesa Truth and Method.
Passagens consultadas (tradução inglesa, parte III, cap. 1): “it is generally more correct to say that we fall into conversation, or even that we become involved in it”; “a conversation has a spirit of its own, and that the language in which it is conducted bears its own truth within it”.
Link consultado: https://www.zukunftsphilologie.de/fileadmin/pdf/zukunftsphilologie/lecture-cum-seminar/2014-01-16_Gadamer_Truth_and_Method______Part_III_Chpt_1.pdf
Observação: a legenda traz, entre aspas, apenas a expressão “caímos em conversação”, tradução livre do trecho verificado; o restante é interpretação autoral. A ideia de “sair mudado” é interpretação nossa, não consta no trecho consultado.
Natureza do texto: reflexão autoral inspirada na ideia.""")

single("2026-11-07", "Shantideva", "peso e passo",
       "Se há o que fazer, dê um passo. Se não há, deixe o peso descansar um pouco.",
       "Uma reflexão inspirada em Shantideva", "n07b",
       """Nem todo peso tem solução hoje. Mas quase todo peso aceita uma pausa.

O mestre budista Shantideva, no Bodhicaryāvatāra (cap. 6, verso 10), pergunta, em várias traduções: se há remédio, por que se abater? E, se não há, de que serve abater-se? A frase da imagem é uma reflexão autoral inspirada nesse verso, com um cuidado a mais: sentir o que pesa é humano, e dividir o peso com alguém também ajuda.

Que peso você pode apoiar no banco, só por esta noite?

Salve para lembrar de descansar.

Frase autoral inspirada em Shantideva, Bodhicaryāvatāra 6.10; não é citação literal.

@doni7m""",
       ["#Shantideva", "#Bodhicaryavatara", "#FilosofiaBudista", "#CaminhoDoBodisatva", "#Descansar", "#PesoNasCostas",
        "#PausaNecessaria", "#SabadoNoite", "#Serenidade", "#Compaixao"], 3,
       """Filósofo e monge budista: Shantideva (séc. VIII).
Obra: Bodhicaryāvatāra (O caminho do bodisatva), capítulo 6, verso 10.
Passagens consultadas (várias traduções): “If there's a remedy when trouble strikes, / What reason is there for dejection? / And if there is no help for it, / What use is there in being glum?” (Padmakara Translation Group, 2007); “If it can be remedied, / Why be displeased about it?” (Kalsang Gyaltsen e Kunga Chodron, 2019).
Link consultado: https://bodhicitta.tsadra.org/index.php/Texts/Bodhicary%C4%81vat%C4%81ra/Verses/6.10
Natureza do texto: frase autoral inspirada no verso; não é citação literal. O acréscimo sobre sentir o que pesa e dividir o peso é do texto autoral, para não soar como pedido de que a pessoa deixe de sentir.""")

# ========================= DOMINGO 08/11 =========================
car("2026-11-08", "Tomás de Aquino", "tristeza e companhia", [
    ("Nem toda tristeza precisa ser resolvida. Algumas só pedem companhia.", None),
    ("Há dias em que o peito pesa sem motivo claro. E logo aparece a cobrança: por que você não reage? Por que não anima?", None),
    ("Vencer a tristeza à força costuma gastar a energia que já faltava. Ela também precisa de lugar, de tempo e de gente por perto.", None),
    ("Tomás de Aquino listou o que costuma aliviar a dor: o choro, o apoio dos amigos, o sono e até um bom banho.", "Uma reflexão inspirada em Tomás de Aquino"),
    ("Hoje, escolha o cuidado mais simples ao alcance: um banho quente, uma noite de sono cedo, uma mensagem a quem você confia.", None),
    ("Falar com alguém não é fraqueza. Se o peso durar muito ou ficar grande demais, procurar ajuda profissional também é cuidado.", None),
    ("Quem não está só costuma carregar o peso com mais jeito. Quem você pode chamar hoje?", "Salve ou envie a quem anda carregando peso."),
], "n08",
    """Nem toda tristeza é um problema a resolver. Às vezes ela só quer lugar, tempo e alguém por perto.

Tomás de Aquino, na Suma Teológica (I-II, questão 38), examina o que costuma aliviar a dor da tristeza: o choro, a compaixão dos amigos, o sono e os banhos, entre outros remédios. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Não é conselho clínico, nem promessa de cura. Se o peso durar muito ou parecer grande demais, procurar companhia e ajuda profissional também é uma forma de cuidar de si.

Quem você pode chamar hoje, ainda que só para sentar ao lado?

Salve para reler quando o dia pesar e envie a quem anda carregando peso.

Reflexão autoral inspirada em Tomás de Aquino, Suma Teológica, I-II, q. 38.

@doni7m""",
    ["#TomasDeAquino", "#SumaTeologica", "#FilosofiaMedieval", "#Tristeza", "#Companhia", "#Amizade", "#CuidadoComSi",
     "#PedirAjuda", "#Domingo", "#SaudeEmocional", "#Acolhimento"], 6,
    """Filósofo e teólogo: Tomás de Aquino (1225-1274).
Obra: Suma Teológica (Summa Theologiae), I-II, questão 38, “Dos remédios da dor ou tristeza”.
Passagens consultadas (tradução inglesa, New Advent): art. 2: “Tears and groans naturally assuage sorrow”; art. 3: “when a man's friends condole with him, he sees that he is loved by them, and this affords him pleasure”; art. 5: “whatever restores the bodily nature to its due state of vital movement, is opposed to sorrow and assuages it” (sono e banhos).
Link consultado: https://www.newadvent.org/summa/2038.htm
Natureza do texto: reflexão autoral inspirada nas ideias; sem aspas e sem citação literal no carrossel nem na legenda. Texto de acolhimento, sem conselho clínico; inclui a ressalva sobre procurar ajuda profissional.""")

single("2026-11-08", "Hegel", "reconhecimento",
       "A gente só se vê inteiro quando alguém nos reconhece. E reconhecer o outro também é um presente.",
       "Uma reflexão inspirada em Hegel", "n08b",
       """Ser visto de verdade por alguém muda o jeito como a gente se vê.

Na Fenomenologia do Espírito (§178), Hegel escreve que a autoconsciência existe em si e para si ao existir para outra autoconsciência, isto é, apenas sendo reconhecida. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Hoje, um reconhecimento simples já conta: “eu vi o que você fez”.

Quem merece ouvir isso de você?

Salve para lembrar de agradecer a quem te viu.

Frase autoral inspirada em Hegel, Fenomenologia do Espírito, §178; não é citação literal.

@doni7m""",
       ["#Hegel", "#FenomenologiaDoEspirito", "#Reconhecimento", "#Dialetica", "#FilosofiaAlema", "#Gratidao",
        "#SerVisto", "#Relacoes", "#DomingoNoite", "#Agradecer"], 6,
       """Filósofo: Georg Wilhelm Friedrich Hegel (1770-1831).
Obra: Fenomenologia do Espírito (Phänomenologie des Geistes, 1807), seção A, “Independência e dependência da autoconsciência” (§178).
Passagem consultada (tradução inglesa, marxists.org): “Self-consciousness exists in itself and for itself, in that, and by the fact that it exists for another self-consciousness; that is to say, it is only by being acknowledged or ‘recognized’.”
Link consultado: https://www.marxists.org/reference/archive/hegel/works/ph/phba.htm
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")
