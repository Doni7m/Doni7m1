# -*- coding: utf-8 -*-
"""Conteúdo da semana 09/11 a 15/11/2026 (14 posts): 7 carrosséis (A) + 7 imagens únicas (B)."""
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


# ========================= SEGUNDA 09/11 =========================
car("2026-11-09", "Heidegger", "soltar o controle (serenidade)", [
    ("Você já tentou controlar tudo e só ficou mais cansado?", None),
    ("Planeja o dia, antecipa respostas, ensaia conversas que talvez nunca aconteçam. A cabeça trabalha mesmo quando o corpo já parou.", None),
    ("Controlar parece proteção. Mas muita coisa não responde ao seu esforço: o tempo dos outros, o resultado, o que vão pensar.", None),
    ("Heidegger chamava de serenidade uma atitude de deixar as coisas serem, sem tentar dominar tudo o tempo todo.", "Uma reflexão inspirada em Heidegger"),
    ("Separe o que é fazer do que é esperar. Cumpra a sua parte com cuidado e permita que o resto aconteça no ritmo dele.", None),
    ("Soltar não é desistir nem ficar indiferente. É cansar menos de segurar o que nunca coube nas suas mãos.", None),
    ("O que você poderia soltar hoje sem perder o cuidado?", "Salve para reler quando o controle apertar."),
], "q09",
    """Tem dia em que a cabeça segue trabalhando horas depois de o corpo ter parado: planos, respostas ensaiadas, cenários que talvez nunca aconteçam.

Heidegger, em Serenidade (Gelassenheit), fala de uma atitude de deixar as coisas serem, sem a pretensão de dominar tudo. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Soltar não é desistir. É fazer a sua parte com cuidado e aceitar que o resto tem outro ritmo.

O que você poderia soltar hoje, sem deixar de cuidar?

Salve para reler quando o controle apertar e envie a quem anda carregando coisa demais.

Reflexão autoral inspirada em Heidegger, Serenidade (Gelassenheit).

@doni7m""",
    ["#Heidegger", "#MartinHeidegger", "#Serenidade", "#Gelassenheit", "#SoltarOControle", "#FilosofiaAlema",
     "#Desapego", "#Ansiedade", "#SegundaFeira", "#PausaNoDia", "#VidaLeve"], 0,
    """Filósofo: Martin Heidegger (1889-1976).
Obra: Serenidade (Gelassenheit), 1959; edição inglesa Discourse on Thinking (trad. J. Anderson e E. Freund, 1966), onde a serenidade (Gelassenheit) é apresentada como atitude de “deixar ser” frente às coisas e ao pensamento calculante.
Link consultado (localizado na pesquisa): https://archive.org/download/discourseonthink00heid/discourseonthink00heid_bw.pdf
Natureza do texto: reflexão autoral inspirada no conceito; sem aspas e sem citação literal no carrossel nem na legenda. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

single("2026-11-09", "Abraham Joshua Heschel", "descanso como lugar no tempo",
       "Nem todo refúgio é feito de pedra. Alguns são feitos de uma tarde inteira sem pressa.",
       "Uma reflexão inspirada em Heschel", "q09b",
       """Existem refúgios que não ocupam espaço nenhum: duram uma tarde.

Abraham Joshua Heschel, no livro O Shabat, descreve o descanso semanal como uma espécie de catedral construída no tempo, e não na pedra. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Reservar um pedaço do dia sem pressa e sem tarefa é uma forma de morar melhor na própria vida.

Que tarde, ou que hora, você poderia proteger esta semana?

Salve para lembrar de reservá-la.

Frase autoral inspirada em Heschel, The Sabbath (1951); não é citação literal.

@doni7m""",
       ["#Heschel", "#AbrahamJoshuaHeschel", "#OShabat", "#Descanso", "#TempoLivre", "#FilosofiaJudaica",
        "#SemPressa", "#Pausa", "#SegundaFeira", "#BomDia"], 3,
       """Filósofo e teólogo: Abraham Joshua Heschel (1907-1972).
Obra: The Sabbath (1951; O Shabat), tese do Shabat como “palácio no tempo”, santuário que se constrói no tempo, e não no espaço.
Link consultado (localizado na pesquisa): https://breakingmatzo.com/philosophy/a-palace-in-time-rabbi-abraham-joshua-heschel-on-the-sabbath/
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")

# ========================= TERÇA 10/11 =========================
car("2026-11-10", "Edith Stein", "ser compreendido (empatia)", [
    ("E se ser compreendido for mais raro do que ser ouvido?", None),
    ("Muita gente escuta esperando a vez de falar. Você conta como se sente e volta com um conselho, uma comparação, uma pressa.", None),
    ("Ser compreendido não é receber concordância. É sentir que o outro tentou ver a situação do lugar onde você está.", None),
    ("Edith Stein estudou a empatia como esse ato de perceber a vivência do outro sem confundi-la com a nossa.", "Uma reflexão inspirada em Edith Stein"),
    ("Na próxima conversa, experimente uma pergunta antes da opinião: “Como foi isso para você?” Depois, apenas fique.", None),
    ("Você não precisa resolver o que o outro sente. Muitas vezes basta mostrar que ele não está sozinho nisso.", None),
    ("Quem já te compreendeu de verdade? Essa pessoa sabe disso?", "Envie esta imagem a ela."),
], "q10",
    """Ser ouvido e ser compreendido não são a mesma coisa. Dá para ser ouvido por alguém que já preparava a resposta.

Edith Stein dedicou sua tese ao problema da empatia (Einfühlung): como percebemos a vivência do outro sem confundi-la com a nossa. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Na próxima conversa, tente uma pergunta antes da opinião. E deixe o silêncio fazer a parte dele.

Quem já te compreendeu de verdade? Conta aqui nos comentários.

Salve e envie a essa pessoa, só para ela saber.

Reflexão autoral inspirada em Edith Stein, Sobre o problema da empatia (1917).

@doni7m""",
    ["#EdithStein", "#Empatia", "#Fenomenologia", "#Einfuhlung", "#EscutaAtiva", "#FilosofiaAlema",
     "#Compreensao", "#Relacoes", "#TercaFeira", "#Conversa", "#Afeto"], 5,
    """Filósofa: Edith Stein (1891-1942).
Obra: Zum Problem der Einfühlung (Sobre o problema da empatia), tese de 1917, estudo fenomenológico da empatia como percepção da vivência alheia.
Link consultado (localizado na pesquisa): https://philarchive.org/archive/SHUESA-2
Natureza do texto: reflexão autoral inspirada no conceito; sem aspas e sem citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

single("2026-11-10", "Walter Benjamin", "o tédio fértil",
       "O tédio de uma tarde sem planos pode estar chocando a ideia que você ainda não sabe que tem.",
       "Uma reflexão inspirada em Walter Benjamin", "q10b",
       """Nem todo vazio é falta. Às vezes é espaço de sobra para algo nascer.

Walter Benjamin, no ensaio O Narrador (1936), liga o tédio ao descanso profundo em que a experiência amadurece. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Deixar uma tarde livre, sem tela e sem tarefa, pode ser mais produtivo do que parece.

Quando foi a última vez que você se deixou entediar de propósito?

Salve para tentar nesta semana.

Frase autoral inspirada em Walter Benjamin, O Narrador; não é citação literal.

@doni7m""",
       ["#WalterBenjamin", "#ONarrador", "#Tedio", "#TempoLivre", "#Criatividade", "#FilosofiaAlema",
        "#SemTela", "#Ocio", "#TercaFeira", "#PausaNoDia"], 8,
       """Filósofo: Walter Benjamin (1892-1940).
Obra: O Narrador (Der Erzähler, 1936), ensaio em que o tédio é associado ao descanso profundo em que a experiência amadurece.
Link consultado (localizado na pesquisa): https://www.prospectmagazine.co.uk/other/flights-of-the-dream-bird
Natureza do texto: frase autoral inspirada na ideia; não é citação literal (a imagem de Benjamin sobre o tédio e o “pássaro do sonho” não foi reproduzida).""")

# ========================= QUARTA 11/11 =========================
car("2026-11-11", "Byung-Chul Han", "autoexigência e cansaço", [
    ("Quando foi que você virou o chefe mais exigente da própria vida?", None),
    ("Ninguém manda você produzir no domingo, mas a culpa aparece quando descansa. A voz que cobra parece ser a sua.", None),
    ("Quando a cobrança vem de dentro, não há a quem reclamar. Você se cansa e ainda se culpa por estar cansado.", None),
    ("Byung-Chul Han chama isso de sociedade do cansaço: um tempo em que cada um se cobra e confunde pressão com liberdade.", "Uma reflexão inspirada em Byung-Chul Han"),
    ("Experimente, no fim do dia, anotar uma coisa que foi suficiente. Não a melhor, não a máxima. Suficiente.", None),
    ("O cansaço também pede escuta, não só descanso. Às vezes ele pergunta o que, exatamente, você está tentando provar.", None),
    ("Hoje, o suficiente já basta?", "Salve para lembrar nos dias de cobrança."),
], "q11",
    """Tem uma voz que cobra, compara e não deixa o domingo ser domingo. E ela costuma falar com a sua própria voz.

Byung-Chul Han, em A Sociedade do Cansaço, descreve um tempo em que cada pessoa se explora acreditando ser livre. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Anotar uma coisa que foi suficiente já muda um pouco o clima do fim do dia. E, se o cansaço persistir, procurar ajuda também é uma forma de cuidar de si.

O que foi suficiente para você hoje?

Salve para lembrar nos dias de cobrança e envie a quem anda se exigindo demais.

Reflexão autoral inspirada em Byung-Chul Han, Sociedade do Cansaço (2010).

@doni7m""",
    ["#ByungChulHan", "#SociedadeDoCansaco", "#Autoexigencia", "#Cansaco", "#Suficiente", "#FilosofiaContemporanea",
     "#Descanso", "#Produtividade", "#QuartaFeira", "#SaudeEmocional", "#Limites"], 11,
    """Filósofo: Byung-Chul Han (n. 1959).
Obra: Müdigkeitsgesellschaft (A Sociedade do Cansaço), 2010, tese do “sujeito de desempenho” que se explora a si mesmo acreditando ser livre.
Link consultado (localizado na pesquisa): https://philosophybreak.com/articles/byung-chul-han-burnout-society-our-only-imperative-is-to-achieve/
Natureza do texto: reflexão autoral inspirada no conceito; sem aspas e sem citação literal. Não é conselho clínico; a legenda indica buscar ajuda se o cansaço persistir.""")

single("2026-11-11", "Wang Yangming", "conhecer e agir",
       "Entender de verdade passa por começar. O primeiro passo também faz parte do saber.",
       "Uma reflexão inspirada em Wang Yangming", "q11b",
       """Tem coisa que a gente “sabe” há meses e ainda não fez. Talvez falte um passo para o saber ficar completo.

Wang Yangming, filósofo chinês do século XVI, defendia a unidade entre conhecer e agir. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

O passo pode ser mínimo: uma mensagem, uma pasta aberta, dez minutos.

Qual é o seu primeiro passo de hoje?

Salve para lembrar de dá-lo.

Frase autoral inspirada em Wang Yangming e na unidade entre conhecer e agir; não é citação literal.

@doni7m""",
       ["#WangYangming", "#FilosofiaChinesa", "#Neoconfucionismo", "#ComecarAgora", "#PrimeiroPasso", "#Acao",
        "#Coragem", "#Decisao", "#QuartaFeira", "#Recomecar"], 14,
       """Filósofo: Wang Yangming (1472-1529).
Tema: unidade de conhecer e agir (zhi xing he yi), central em suas conversas reunidas em Instruções para a prática da vida (Chuanxilu).
Link consultado: https://plato.stanford.edu/entries/wang-yangming/ (Stanford Encyclopedia of Philosophy)
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")

# ========================= QUINTA 12/11 =========================
car("2026-11-12", "John Dewey", "hábitos e ajustes de cenário", [
    ("Você muda de ideia com facilidade e de hábito com dificuldade?", None),
    ("Sabe que dormiria melhor sem o celular na cama. Concorda que deveria ligar para os pais. E a rotina continua igual.", None),
    ("Hábito não é só vontade fraca. É um caminho percorrido tantas vezes que o corpo segue sozinho, mesmo contra o que você pensa.", None),
    ("Dewey via o hábito como a marca que a experiência deixa em nós. Mudar a conduta pede mudar também as condições.", "Uma reflexão inspirada em John Dewey"),
    ("Mude o cenário: carregue o celular longe da cama, deixe o livro sobre o travesseiro, ponha o contato dos pais no topo da lista.", None),
    ("Não exija perfeição. Cada vez que você repete o caminho novo, ele fica um pouco mais largo.", None),
    ("Que pequeno ajuste de cenário você faria esta semana?", "Salve para decidir com calma."),
], "q12",
    """A gente entende uma coisa e continua fazendo outra. Isso não quer dizer que falte caráter. Quer dizer que o hábito é um caminho muito pisado.

John Dewey, em Natureza Humana e Conduta, trata o hábito como a marca que a experiência deixa em nós e lembra que o ambiente conta tanto quanto a intenção. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Às vezes mudar o cenário é mais fácil do que mudar a si mesmo: o celular longe da cama, o livro à vista.

Que ajuste pequeno você faria esta semana?

Salve para decidir com calma e envie a quem está tentando mudar uma rotina.

Reflexão autoral inspirada em John Dewey, Human Nature and Conduct (1922).

@doni7m""",
    ["#JohnDewey", "#Dewey", "#Habitos", "#Rotina", "#MudarDeHabito", "#FilosofiaAmericana",
     "#Pragmatismo", "#Mudanca", "#QuintaFeira", "#PequenosPassos", "#Constancia"], 17,
    """Filósofo: John Dewey (1859-1952).
Obra: Human Nature and Conduct (Natureza Humana e Conduta), 1922, sobre hábito, impulso e inteligência na conduta.
Link consultado (localizado na pesquisa): https://www.gutenberg.org/ebooks/41386
Natureza do texto: reflexão autoral inspirada no conceito; sem aspas e sem citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

single("2026-11-12", "Mozi", "cuidar sem lista de favoritos",
       "Cuidar de quem está perto é natural. Ampliar um pouco o círculo é o exercício.",
       "Uma reflexão inspirada em Mozi", "q12b",
       """Cuidar de quem a gente ama vem fácil. O desafio é o círculo ao redor.

Mozi, filósofo chinês do século V a.C., defendia o chamado cuidado imparcial (jian ai): estender atenção e consideração para além do círculo próximo. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Pode ser pouco: cumprimentar o vizinho, agradecer quem atende, ceder o lugar.

A quem você poderia dedicar um gesto de cuidado hoje, fora do seu círculo habitual?

Salve para lembrar do exercício.

Frase autoral inspirada em Mozi e no cuidado imparcial; não é citação literal.

@doni7m""",
       ["#Mozi", "#Mohismo", "#CuidadoImparcial", "#FilosofiaChinesa", "#Gentileza", "#Comunidade",
        "#Vizinhanca", "#Empatia", "#QuintaFeira", "#Solidariedade"], 20,
       """Filósofo: Mozi (Mo Di), séculos V-IV a.C.
Tema: cuidado imparcial ou preocupação com todos (jian ai), núcleo da ética moísta.
Link consultado: https://iep.utm.edu/mozi/ (Internet Encyclopedia of Philosophy)
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")

# ========================= SEXTA 13/11 =========================
car("2026-11-13", "Paul Ricoeur", "a história que contamos sobre nós", [
    ("A história que você conta sobre si mesmo é a única possível?", None),
    ("Um erro antigo vira “eu sempre estrago tudo”. Uma fase difícil vira o retrato inteiro. De tanto repetir, a versão parece fato.", None),
    ("Contar a própria vida é escolher o que entra, o que fica de fora e o que liga um acontecimento a outro.", None),
    ("Ricoeur falava em identidade narrativa: nos reconhecemos ao contar nossa vida, e uma narrativa pode ser recontada.", "Uma reflexão inspirada em Paul Ricoeur"),
    ("Reescreva um episódio difícil incluindo o que você fez para atravessá-lo. Não maquie. Complete.", None),
    ("Recontar não apaga o que doeu. Só impede que um capítulo ocupe o livro inteiro.", None),
    ("Que capítulo seu merece ser lido com mais justiça?", "Salve ou envie a quem escreve a vida com você."),
], "q13",
    """“Eu sempre faço isso.” “Comigo nunca dá certo.” Frases assim viram a história oficial da nossa vida sem ninguém perceber.

Paul Ricoeur desenvolveu a ideia de identidade narrativa: nos reconhecemos ao contar a nossa vida, e a narrativa pode ser recontada com mais inteireza. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Recontar não é negar o que doeu. É lembrar também do que você fez para atravessar.

Que capítulo seu merece ser lido com mais justiça?

Salve para reescrever com calma e envie a quem escreve a vida ao seu lado.

Reflexão autoral inspirada em Paul Ricoeur, Tempo e Narrativa e O Si-mesmo como um Outro.

@doni7m""",
    ["#PaulRicoeur", "#Ricoeur", "#IdentidadeNarrativa", "#Hermeneutica", "#ContarAHistoria", "#FilosofiaFrancesa",
     "#Recomecar", "#Autoconhecimento", "#SextaFeira", "#Memoria", "#Narrativa"], 23,
    """Filósofo: Paul Ricoeur (1913-2005).
Obras: Temps et récit (Tempo e Narrativa, 1983-85) e Soi-même comme un autre (O Si-mesmo como um Outro, 1990), onde se desenvolve a identidade narrativa.
Link consultado (localizado na pesquisa): https://ojs.unica.it/index.php/ecch/article/view/6960
Natureza do texto: reflexão autoral inspirada no conceito; sem aspas e sem citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

single("2026-11-13", "Nagarjuna", "interdependência e gratidão",
       "Nada do que você tem veio só de você. Agradecer é reconhecer a rede que sustenta cada dia.",
       "Uma reflexão inspirada em Nagarjuna", "q13b",
       """O pão da manhã, o café, a rua limpa, a mensagem que chegou na hora certa. Pouca coisa na nossa vida surgiu sozinha.

Nagarjuna, filósofo budista dos séculos II-III, desenvolveu a ideia de origem dependente: as coisas existem em relação umas com as outras. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Agradecer, nesse sentido, é olhar a rede que sustenta o dia.

Quem entrou nessa rede hoje, mesmo sem saber?

Salve para lembrar de agradecer.

Frase autoral inspirada em Nagarjuna e na origem dependente; não é citação literal.

@doni7m""",
       ["#Nagarjuna", "#OrigemDependente", "#FilosofiaBudista", "#Gratidao", "#Interdependencia", "#Agradecer",
        "#Budismo", "#Presenca", "#SextaFeira", "#Conexao"], 26,
       """Filósofo: Nagarjuna (séculos II-III d.C.).
Obra: Mūlamadhyamakakārikā (Versos Fundamentais do Caminho do Meio), onde a origem dependente e a vacuidade são discutidas.
Link consultado (localizado na pesquisa, bibliografia da SEP): https://philpapers.org/sep/nagarjuna/
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")

# ========================= SÁBADO 14/11 =========================
car("2026-11-14", "Karl Popper", "errar e revisar", [
    ("Estar errado dói. Continuar errado por orgulho costuma doer mais.", None),
    ("Você defende uma opinião por inércia. Muda de assunto quando percebe a falha. Prefere parecer certo a parecer alguém que aprende.", None),
    ("Admitir um erro parece perder terreno. Na prática, é o único jeito de voltar a pisar em chão firme.", None),
    ("Karl Popper defendia que o conhecimento avança quando aceitamos testar nossas ideias e corrigi-las.", "Uma reflexão inspirada em Karl Popper"),
    ("Na próxima discordância, pergunte: “O que eu estaria perdendo se estivesse errado?” E escute a resposta até o fim.", None),
    ("Rever uma ideia não é fraqueza. É dar a si mesmo a chance de não repetir a mesma volta.", None),
    ("Qual convicção sua merece uma segunda leitura?", "Salve para ler de novo com calma."),
], "q14",
    """Admitir um erro costuma parecer derrota. Mas manter uma ideia só por orgulho tem um custo, e quase sempre é maior.

Karl Popper defendia que aprendemos testando nossas ideias e corrigindo o que falha, no que ficou conhecido como falibilismo. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Um bom exercício para a próxima discordância: “o que eu estaria perdendo se estivesse errado?”

Qual convicção sua merece uma segunda leitura?

Salve para reler com calma e envie a quem sabe mudar de ideia.

Reflexão autoral inspirada em Karl Popper, Conjecturas e Refutações (1963).

@doni7m""",
    ["#KarlPopper", "#Popper", "#Falibilismo", "#PensamentoCritico", "#AprenderComOsErros", "#FilosofiaDaCiencia",
     "#Humildade", "#MudarDeIdeia", "#Sabado", "#Aprendizado", "#Dialogo"], 29,
    """Filósofo: Karl Popper (1902-1994).
Obra: Conjectures and Refutations (Conjecturas e Refutações, 1963), sobre conhecimento como correção de erros por conjectura e crítica (falibilismo).
Link consultado (localizado na pesquisa): https://en.unav.edu/web/ciencia-razon-y-fe/the-ethical-roots-of-karl-poppers-epistemology
Natureza do texto: reflexão autoral inspirada no conceito; sem aspas e sem citação literal. Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

single("2026-11-14", "María Zambrano", "razão poética",
       "Algumas coisas só se entendem devagar, com a razão e o sentimento sentados à mesma mesa.",
       "Uma reflexão inspirada em María Zambrano", "q14b",
       """Há perguntas que não se resolvem só com argumentos nem só com sentimento. Pedem os dois, e tempo.

María Zambrano, filósofa espanhola, propôs a chamada razão poética: um modo de pensar que não separa a razão da sensibilidade. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Para as decisões difíceis, talvez ajude escrever, caminhar, deixar a ideia descansar uma noite.

Que decisão sua pede mais tempo do que pressa?

Salve para voltar a esta imagem.

Frase autoral inspirada em María Zambrano e na razão poética; não é citação literal.

@doni7m""",
       ["#MariaZambrano", "#RazaoPoetica", "#FilosofiaEspanhola", "#Sensibilidade", "#PensarDevagar", "#Poesia",
        "#Decisao", "#Escrita", "#Sabado", "#TempoParaPensar"], 2,
       """Filósofa: María Zambrano (1904-1991).
Tema: razão poética (razón poética), proposta de um pensar que integra razão e sensibilidade, presente em obras como Claros del bosque (1977).
Link consultado (localizado na pesquisa): https://revistas.javeriana.edu.co/index.php/vniphilosophica/article/view/24000
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")

# ========================= DOMINGO 15/11 =========================
car("2026-11-15", "Ernst Bloch", "esperança e o ainda-não", [
    ("Esperar algo melhor é ingenuidade ou uma forma de coragem?", None),
    ("Depois de tantas decepções, esperar parece arriscado. É mais seguro não querer muito para não se frustrar.", None),
    ("Mas viver sem nada a desejar também cansa. Quem não imagina o que falta mal enxerga o que poderia mudar.", None),
    ("Ernst Bloch chamou de “ainda-não” aquilo que existe como possibilidade e pede passos concretos para acontecer.", "Uma reflexão inspirada em Ernst Bloch"),
    ("Escolha um desejo pequeno e dê a ele um passo real esta semana: uma ligação, uma inscrição, um espaço na agenda.", None),
    ("Esperança não é garantir que dará certo. É manter a porta entreaberta enquanto você faz a parte que cabe a você.", None),
    ("O que ainda não existe, mas você gostaria que existisse?", "Salve para começar a semana com isso em mente."),
], "q15",
    """Domingo à noite costuma trazer um balanço: o que deu certo, o que ficou pendente, o que a gente já não espera mais.

Ernst Bloch, em O Princípio Esperança, pensa o “ainda-não”: aquilo que existe como possibilidade e pede passos concretos para acontecer. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Esperança, aqui, não é promessa de que dará certo. É manter a porta entreaberta e fazer a parte que cabe a você.

O que ainda não existe, mas você gostaria que existisse?

Salve para começar a semana com isso em mente e envie a quem anda precisando de uma porta aberta.

Reflexão autoral inspirada em Ernst Bloch, O Princípio Esperança (1954-59).

@doni7m""",
    ["#ErnstBloch", "#PrincipioEsperanca", "#Esperanca", "#AindaNao", "#FilosofiaAlema", "#Sonhar",
     "#DomingoNoite", "#Recomeco", "#NovaSemana", "#Possibilidades", "#Desejo"], 5,
    """Filósofo: Ernst Bloch (1885-1977).
Obra: Das Prinzip Hoffnung (O Princípio Esperança, 1954-1959), sobre a esperança, o sonho diurno e o “ainda-não” (Noch-Nicht).
Link consultado (localizado na pesquisa): https://www.marxists.org/archive/bloch/hope/introduction.htm
Natureza do texto: reflexão autoral inspirada no conceito; sem aspas e sem citação literal (as aspas em “ainda-não” indicam apenas o termo). Fonte localizada por busca web; o texto integral não foi lido nesta rodada.""")

single("2026-11-15", "Alain", "humor e vontade",
       "O humor muda sozinho. Começar a semana com gentileza já é uma decisão sua.",
       "Uma reflexão inspirada em Alain", "q15b",
       """Tem dias em que o humor está pesado sem motivo claro. Ele passa. Mas o jeito de tratar a própria semana ainda é uma escolha.

Alain (Émile Chartier), nos Propos sur le bonheur, associa o pessimismo ao humor e o otimismo à vontade, ideia a ele atribuída. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Escolher gentileza não é negar o cansaço. É decidir como atravessá-lo.

Que gentileza você promete à sua semana?

Salve para voltar a esta frase na segunda-feira.

Frase autoral inspirada em Alain, Propos sur le bonheur (1928); não é citação literal.

@doni7m""",
       ["#Alain", "#EmileChartier", "#ProposSurLeBonheur", "#FilosofiaFrancesa", "#Gentileza", "#NovaSemana",
        "#Vontade", "#Humor", "#DomingoNoite", "#Felicidade"], 8,
       """Filósofo: Alain (Émile Chartier, 1868-1951).
Obra: Propos sur le bonheur (Reflexões sobre a felicidade, 1928); a ideia “o pessimismo é de humor, o otimismo é de vontade” é atribuída a ele em fontes secundárias.
Link consultado (localizado na pesquisa): https://philosophe-alain.fr/propos/make-a-vow/
Natureza do texto: frase autoral inspirada na ideia; não é citação literal. A atribuição exata da fórmula ao texto original não foi confirmada nesta rodada, por isso não há aspas.""")
