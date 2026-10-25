# -*- coding: utf-8 -*-
"""Conteúdo da semana 26/10 a 01/11/2026 (14 posts): 7 carrosséis (A) + 7 imagens únicas (B)."""
from content_w42 import norm, tags30

POSTS = []


def add(**kw):
    POSTS.append(kw)


def single(date, ph, theme, text, sub, scene, caption, tags, off, ref):
    add(date=date, slot="B", kind="single", philosopher=ph, theme=theme, slides=[(text, sub)], scenes=[scene],
        caption=caption, hashtags=tags30(tags, off), ref=ref)


# ========================= SEGUNDA 26/10 =========================
add(date="2026-10-26", slot="A", kind="carousel", philosopher="John Stuart Mill", theme="felicidade como consequência",
    slides=[
        ("Quanto mais você persegue a felicidade, mais ela parece escapar?", None),
        ("Você olha para a própria vida e pergunta: já estou feliz? A pergunta vira régua, e a régua sempre acusa que falta um pouco.", None),
        ("Quem se vigia o tempo todo raramente está inteiro no que faz. A conversa passa, o café esfria, e a atenção fica no placar.", None),
        ("Mill concluiu, depois de uma fase muito difícil, que a felicidade vem melhor quando o foco está em outra coisa: alguém, uma causa, um ofício.", "Uma reflexão inspirada em John Stuart Mill"),
        ("Escolha algo que mereça atenção por si só: uma receita, uma planta, uma conversa longa. Faça por ela, não para melhorar o humor.", None),
        ("Isso não vale para todo dia. Em fases pesadas, nenhuma ocupação basta, e conversar com alguém de confiança também é cuidado.", None),
        ("A alegria costuma chegar de lado, enquanto estamos ocupados com algo que importa. O que merece a sua atenção hoje?", "Salve ou envie a quem anda se cobrando."),
    ],
    scenes=["e26a1", "e26a2", "e26a3", "e26a4", "e26a5", "e26a6", "e26a7"],
    caption="""Existe uma pergunta que cansa mais do que parece: “será que já estou feliz?”

John Stuart Mill conta, na Autobiografia, que percebeu algo curioso depois de um período muito difícil: quem mantém a mente fixa em algo além da própria felicidade tende a encontrá-la pelo caminho. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Não é regra para todos os dias, nem promessa. Há fases em que o peso é grande demais para uma planta ou uma receita resolverem. Se for o seu caso, procurar companhia ou ajuda também é uma forma de cuidar de si.

O que, hoje, merece a sua atenção só por ser bom de fazer?

Salve para reler quando a cobrança apertar e envie a quem anda medindo a própria alegria.

Reflexão autoral inspirada em John Stuart Mill, Autobiografia (1873).

@doni7m""",
    hashtags=tags30(["#JohnStuartMill", "#Mill", "#Autobiografia", "#Felicidade", "#FilosofiaInglesa", "#Atencao", "#SemCobranca",
                     "#PequenasAlegrias", "#SentidoDaVida", "#FocoNoQueImporta", "#ComecoDeSemana"], 0),
    ref="""Filósofo: John Stuart Mill (1806-1873).
Obra: Autobiografia (Autobiography, 1873), capítulo V (a página consultada não indica o capítulo; é o capítulo da "crise mental", conforme as edições correntes — conferir na edição em mãos).
Passagem consultada (verificada em trecho citado): "Those only are happy (I thought) who have their minds fixed on some object other than their own happiness" e, logo depois, "Aiming thus at something else, they find happiness by the way."
Links: https://elimindset.com/?p=30174 (trecho) e https://gutenberg.org/cache/epub/10378/pg10378-images.html (texto integral, Project Gutenberg).
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal no carrossel nem na legenda.""")

single("2026-10-26", "Emerson", "confiar no próprio juízo",
       "Confiar em si não é achar que nunca erra. É dar ao seu próprio juízo uma cadeira na mesa.",
       "Uma reflexão inspirada em Emerson", "e26b",
       """Tem decisão que a gente já sabe qual é, mas continua perguntando a todo mundo.

Ralph Waldo Emerson, no ensaio Autoconfiança, escreveu que todo coração vibra àquela corda de ferro, e pediu: confie em si mesmo. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Ouvir os outros também é sabedoria. Só que, depois de ouvir, vale dar ao que você pensa um lugar à mesa.

Qual decisão você já sabe qual é, mas ainda não assumiu?

Salve para voltar a esta pergunta numa segunda-feira de dúvidas.

Frase autoral inspirada em Emerson, “Self-Reliance” (1841); não é citação literal.

@doni7m""",
       ["#Emerson", "#RalphWaldoEmerson", "#SelfReliance", "#Autoconfianca", "#ConfieEmVoce", "#Decisoes", "#JuizoProprio",
        "#FilosofiaAmericana", "#Transcendentalismo", "#SegundaFeira"], 5,
       """Filósofo e ensaísta: Ralph Waldo Emerson (1803-1882).
Obra: ensaio "Self-Reliance" (Autoconfiança), em Essays: First Series (1841).
Passagens consultadas (texto integral): "Trust thyself: every heart vibrates to that iron string." e "Nothing is at last sacred but the integrity of your own mind."
Link consultado: https://archive.vcu.edu/english/engweb/eng372/selfrel.htm (a página não informa o ano; o ensaio é de 1841).
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")

# ========================= TERÇA 27/10 =========================
add(date="2026-10-27", slot="A", kind="carousel", philosopher="Ortega y Gasset", theme="circunstância",
    slides=[
        ("Você não é só o que decide. Também é o lugar onde a vida te colocou.", None),
        ("Alguém diz que basta querer. Mas você sabe que idioma, trabalho, distância e dinheiro entram na conta de cada escolha.", None),
        ("Ignorar isso gera uma culpa injusta: a de não ter chegado lá, como se todos largassem do mesmo ponto.", None),
        ("Ortega y Gasset dizia que cada pessoa é ela mesma e também a sua circunstância. Entender o entorno faz parte de entender-se.", "Uma reflexão inspirada em Ortega y Gasset"),
        ("Faça um inventário honesto: o que depende de mim, dos outros e do tempo? Cada coluna pede um esforço diferente.", None),
        ("Nem toda circunstância muda hoje. Mas dá para mexer num canto dela: reorganizar a rotina, pedir ajuda, aproximar-se de alguém.", None),
        ("Você não precisa se culpar pelo que o cenário não permitiu. Que canto da sua circunstância cabe mexer esta semana?", "Salve ou envie a quem se cobra demais."),
    ],
    scenes=["e27a1", "e27a2", "e27a3", "e27a4", "e27a5", "e27a6", "e27a7"],
    caption="""“É só querer.” Quem já ouviu essa frase sabe como ela soa quando a vida real tem endereço, boletos e saudade.

José Ortega y Gasset, nas Meditações do Quixote, de 1914, ligou o eu à sua circunstância: a pessoa não existe solta, existe num mundo concreto, e salvá-lo faz parte de salvar-se. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Reconhecer a circunstância não é desculpa nem derrota. É pôr o peso no lugar certo para decidir o que ainda cabe a você.

Se a culpa ou a distância de casa pesarem, procurar companhia ou uma conversa com alguém de confiança também é cuidado.

Que canto da sua circunstância você pode mexer esta semana?

Salve para reler quando a cobrança apertar e envie a quem se cobra demais.

Reflexão autoral inspirada em Ortega y Gasset, Meditaciones del Quijote (1914).

@doni7m""",
    hashtags=tags30(["#OrtegaYGasset", "#MeditacionesDelQuijote", "#Circunstancia", "#FilosofiaEspanhola", "#SemCulpa", "#NemTudoDependeDeVoce",
                     "#VidaLongeDeCasa", "#Imigracao", "#Realidade", "#Escolhas"], 3),
    ref="""Filósofo: José Ortega y Gasset (1883-1955).
Obra: Meditaciones del Quijote (1914), "Meditación preliminar".
Ideia usada: a frase famosa "Yo soy yo y mi circunstancia, y si no la salvo a ella no me salvo yo" (o eu inseparável do mundo vital em que está imerso: família, cultura, momento histórico, sociedade).
Link consultado: https://extensioneinnovacion.substack.com/p/salvar-las-circunstancias (fonte secundária que confirma a frase e a obra de 1914; conferir a página na edição em mãos antes de qualquer citação com aspas).
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal no carrossel nem na legenda.""")

single("2026-10-27", "Descartes", "expectativas e o que depende de nós",
       "Há coisas que o mundo não muda por mim. Esperar menos delas e fazer mais pelo que posso já é um começo.",
       "Uma reflexão inspirada em Descartes", "e27b",
       """Nem tudo o que dói tem solução ao nosso alcance. Mas quase sempre existe uma parte que é nossa.

René Descartes, no Discurso do Método, descreve entre suas regras provisórias a de procurar vencer antes a si mesmo do que à fortuna, e mudar os próprios desejos antes de querer mudar a ordem do mundo. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Isso não manda aceitar injustiça nem calar o que importa. Só ajuda a separar o que é cansaço de lutar contra o inevitável do que ainda merece o seu esforço.

O que você ainda espera que o mundo faça por você, e talvez possa fazer por si?

Salve para os dias em que as expectativas pesarem.

Frase autoral inspirada em Descartes, Discurso do Método, parte III; não é citação literal.

@doni7m""",
       ["#Descartes", "#ReneDescartes", "#DiscursoDoMetodo", "#Expectativas", "#OQueDependeDeMim", "#FilosofiaFrancesa", "#Racionalismo",
        "#Aceitacao", "#Serenidade", "#TerçaFilosofica".replace("ç", "c")], 8,
       """Filósofo: René Descartes (1596-1650).
Obra: Discurso do Método (Discours de la méthode, 1637), Parte III, terceira máxima da moral provisória.
Passagem consultada (tradução inglesa, tradutor não indicado na página): "to endeavor always to conquer myself rather than fortune, and change my desires rather than the order of the world."
Link consultado: https://www.intratext.com/IXT/ENG1174/_P4.HTM
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")

# ========================= QUARTA 28/10 =========================
add(date="2026-10-28", slot="A", kind="carousel", philosopher="Simone de Beauvoir", theme="liberdade dentro dos limites",
    slides=[
        ("Ser livre não é não ter limites. É decidir o que fazer com eles.", None),
        ("Você tem planos, mas também tem corpo, dinheiro, idade, família, história. Nada disso some quando a vontade aparece.", None),
        ("Há quem diga que tudo depende só de você. Há quem diga que nada depende. Nenhuma das duas frases descreve bem a vida real.", None),
        ("Simone de Beauvoir falava em ambiguidade: somos livres e, ao mesmo tempo, situados no mundo. Assumir isso é o ponto de partida.", "Uma reflexão inspirada em Simone de Beauvoir"),
        ("Pergunte: dentro desta situação, qual é a menor escolha que ainda é minha? Um telefonema, um não, um primeiro passo.", None),
        ("Escolher dentro dos limites não é conformismo. É usar a liberdade que existe, sem esperar a que ainda falta.", None),
        ("Sua liberdade pode ser pequena hoje e, ainda assim, real. Qual é a escolha que continua sendo sua?", "Salve ou envie a quem se sente preso."),
    ],
    scenes=["e28a1", "e28a2", "e28a3", "e28a4", "e28a5", "e28a6", "e28a7"],
    caption="""Tem dias em que “faça o que quiser” soa vazio, porque a vida real tem horários, contas e pessoas que dependem de nós.

Simone de Beauvoir, em Por uma moral da ambiguidade, de 1947, convida a assumir a nossa ambiguidade fundamental: somos livres, mas livres dentro de uma situação. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Isso não diminui a liberdade. Dá a ela um chão. Quando a gente aceita o terreno, enxerga melhor o passo possível.

Se a sensação de estar preso for forte e durar, procurar companhia ou ajuda também é cuidado.

Qual é a escolha pequena que ainda é sua nesta semana?

Salve para reler no próximo dia de aperto e envie a quem se sente sem saída.

Reflexão autoral inspirada em Simone de Beauvoir, Pour une morale de l'ambiguïté (1947).

@doni7m""",
    hashtags=tags30(["#SimoneDeBeauvoir", "#Beauvoir", "#MoralDaAmbiguidade", "#Liberdade", "#Existencialismo", "#FilosofiaFrancesa",
                     "#Escolhas", "#Limites", "#NemTudoDependeDeVoce", "#Autonomia"], 6),
    ref="""Filósofa: Simone de Beauvoir (1908-1986).
Obra: Por uma moral da ambiguidade (Pour une morale de l'ambiguïté, 1947; The Ethics of Ambiguity), capítulo 1, "Ambiguidade".
Passagem consultada (tradução inglesa do texto integral): "Let us try to assume our fundamental ambiguity." e, no mesmo trecho, o ser humano apresentado como sujeito soberano e, ao mesmo tempo, objeto para os outros.
Link consultado: https://www.marxists.org/reference/subject/ethics/de-beauvoir/ambiguity/ch01.htm
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal no carrossel nem na legenda.""")

single("2026-10-28", "Plotino", "tirar o que sobra",
       "Antes de acrescentar mais uma coisa à vida, vale perceber o que sobra. Esculpir também é tirar.",
       "Uma reflexão inspirada em Plotino", "e28b",
       """Quando a vida parece cheia demais, talvez a pergunta não seja o que falta, e sim o que pode sair.

Plotino, nas Enéadas, pede a quem quer ver a própria beleza que faça como o escultor: tire o que é excessivo, endireite o que é torto e nunca deixe de esculpir a própria estátua. A frase da imagem é uma reflexão autoral inspirada nessa imagem.

Tirar não é perder. Pode ser um compromisso que já não cabe, uma conversa que se arrasta, uma exigência herdada de outra pessoa.

O que, na sua vida, já poderia sair sem fazer falta?

Salve para repensar a agenda com calma e envie a quem anda sobrecarregado.

Frase autoral inspirada em Plotino, Enéadas I, 6, 9; não é citação literal.

@doni7m""",
       ["#Plotino", "#Eneadas", "#FilosofiaAntiga", "#Neoplatonismo", "#Menos", "#Essencial", "#Simplificar", "#Escultura",
        "#TirarOExcesso", "#Quarta"], 10,
       """Filósofo: Plotino (c. 204-270).
Obra: Enéadas, I, 6 ("Sobre a beleza"), § 9.
Passagem consultada (tradução inglesa de Stephen MacKenna e B. S. Page): "cut away all that is excessive, straighten all that is crooked, bring light to all that is overcast, labour to make all one glow of beauty and never cease chiselling your statue".
Link consultado: https://www.ellopos.net/elpenor/greek-texts/ancient-Greece/plotinus/enneads-1.asp?pg=79
Natureza do texto: frase autoral inspirada na imagem; não é citação literal.""")

# ========================= QUINTA 29/10 =========================
add(date="2026-10-29", slot="A", kind="carousel", philosopher="Voltaire", theme="cultivar o próprio jardim",
    slides=[
        ("Quando o mundo é grande demais, cultive o seu pedaço de terra.", None),
        ("As notícias chegam todo dia e somam problemas que ninguém resolve sozinho. A cabeça cansa de carregar o planeta nas costas.", None),
        ("A impotência pesa, e a tentação é desligar de tudo ou ficar rolando a tela até de madrugada.", None),
        ("No fim de Cândido, depois de tantas desgraças, ele responde que é preciso cultivar o próprio jardim: trabalho concreto, ao alcance das mãos.", "Uma reflexão inspirada em Voltaire"),
        ("Escolha um canto para cuidar: uma planta, uma gaveta, uma conversa pendente. Uma tarefa que cabe na mão basta por hoje.", None),
        ("Cuidar do próprio jardim não é ignorar o mundo. Quem tem os pés firmes num canto pequeno chega mais inteiro ao que é grande.", None),
        ("Nos poios da Madeira, cada terraço de terra foi feito pedra por pedra. Qual é o seu terraço de hoje?", "Salve ou envie a quem anda sobrecarregado de notícias."),
    ],
    scenes=["e29a1", "e29a2", "e29a3", "e29a4", "e29a5", "e29a6", "e29a7"],
    caption="""Existe um cansaço de mundo: a gente lê, se indigna, se preocupa e, no fim do dia, não sabe o que fazer com tudo isso.

Voltaire termina o Cândido, de 1759, com a resposta de que é preciso cultivar o nosso jardim. Depois de uma sequência de desgraças e teorias, a conclusão é pequena e concreta: trabalhar o que está ao alcance. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Não é mandar ninguém ignorar o mundo. É lembrar que, para ajudar, ajuda ter o chão sob os pés. Aqui na Madeira, os poios, aqueles terraços de pedra, são um bom lembrete de que grandes paisagens se fazem com gestos pequenos.

Se o peso das notícias ou da ansiedade for grande demais, procurar companhia ou ajuda também é cuidado.

Qual é o seu terraço de hoje?

Salve para reler antes de abrir as notícias e envie a quem anda sobrecarregado.

Reflexão autoral inspirada em Voltaire, Candide ou l'optimisme (1759), cap. XXX.

@doni7m""",
    hashtags=tags30(["#Voltaire", "#Candide", "#CultivarOJardim", "#Iluminismo", "#FilosofiaFrancesa", "#Poios", "#TerracosDaMadeira",
                     "#Notícias".replace("í", "i"), "#CansacoDeMundo", "#PequenosGestos"], 12),
    ref="""Filósofo: Voltaire (1694-1778).
Obra: Cândido ou O Otimismo (Candide, ou l'optimisme, 1759), capítulo XXX, "Conclusão".
Passagem consultada (tradução inglesa, edição Modern Library via Standard Ebooks; tradutor não indicado na página): "All that is very well," answered Candide, "but let us cultivate our garden." (no original francês: "il faut cultiver notre jardin").
Link consultado: https://standardebooks.org/ebooks/voltaire/candide/the-modern-library/text/chapter-30
Natureza do texto: reflexão autoral inspirada no desfecho da obra; sem aspas e sem citação literal no carrossel nem na legenda. A referência aos poios da Madeira é do autor do perfil, não de Voltaire.""")

single("2026-10-29", "Diógenes", "pedir pouco",
       "Pedir pouco ao mundo também é uma forma de liberdade. Às vezes, tudo o que se quer é um pouco de sol.",
       "Uma reflexão inspirada em Diógenes", "e29b",
       """Há dias em que a lista de desejos fica enorme, e o corpo só pede uma coisa simples: sol na cara e um pouco de silêncio.

Plutarco conta que Alexandre, o Grande, ofereceu a Diógenes o que ele quisesse. O filósofo pediu apenas que o rei saísse da frente do sol. A frase da imagem é uma reflexão autoral inspirada nesse episódio.

Isso não romantiza a falta: ter pouco por necessidade é dura realidade para muita gente. A ideia é outra, a de perceber quanto do que desejamos vem dos outros.

O que você anda pedindo à vida e que, no fundo, não é seu?

Salve para voltar a esta pergunta num dia de excesso.

Frase autoral inspirada em Diógenes de Sinope, episódio narrado por Plutarco, Vida de Alexandre 14; não é citação literal.

@doni7m""",
       ["#Diogenes", "#DiogenesDeSinope", "#Cinismo", "#FilosofiaAntiga", "#Simplicidade", "#Liberdade", "#SolNaCara",
        "#PedirPouco", "#Plutarco", "#MenosEMais"], 15,
       """Filósofo: Diógenes de Sinope (c. 412-323 a.C.).
Fonte: Plutarco, Vida de Alexandre, 14.2-5 (tradução inglesa de John Dryden/Evelyn via Livius.org). A página dá a fala de Diógenes como "I would have you stand from between me and the sun" e a reação de Alexandre: se não fosse Alexandre, escolheria ser Diógenes. (Diógenes Laércio também registra o episódio.)
Link consultado: https://www.livius.org/sources/content/plutarch/plutarchs-alexander/alexander-and-diogenes/
Natureza do texto: frase autoral inspirada no episódio; não é citação literal. A ressalva sobre a pobreza imposta é do autor do perfil.""")

# ========================= SEXTA 30/10 =========================
add(date="2026-10-30", slot="A", kind="carousel", philosopher="Mêncio", theme="compaixão espontânea",
    slides=[
        ("Antes de pensar, você estendeu a mão. Isso já diz algo sobre você.", None),
        ("Alguém tropeça na rua e o seu corpo reage primeiro: o braço se estica, o peito aperta. Só depois vêm as explicações.", None),
        ("Tantas vezes nos achamos frios, cansados, endurecidos. Mas o impulso de cuidar ainda aparece, mesmo quando tentamos escondê-lo.", None),
        ("Mêncio defendia que ninguém é incapaz de sentir pelo sofrimento alheio. Dava o exemplo de uma criança prestes a cair num poço.", "Uma reflexão inspirada em Mêncio"),
        ("Esse impulso é como uma semente: cresce quando é regada. Um bom-dia, uma carona, uma pergunta sincera já são adubo.", None),
        ("Cuidar dos outros também cansa. Se estiver esgotado, descansar não trai a compaixão. Ela precisa de fôlego para durar.", None),
        ("A bondade pequena costuma ser a que mais se repete. Que gesto de cuidado seu ainda não encontrou ocasião?", "Salve ou envie a quem cuida de alguém."),
    ],
    scenes=["e30a1", "e30a2", "e30a3", "e30a4", "e30a5", "e30a6", "e30a7"],
    caption="""Antes de qualquer raciocínio, o corpo já tinha estendido a mão. Quem nunca teve esse reflexo ao ver alguém prestes a cair?

Mêncio, filósofo chinês seguidor de Confúcio, partia desse tipo de cena: diante de uma criança prestes a cair num poço, qualquer pessoa sente alarme e compaixão. Para ele, esse é o broto de uma bondade que se cultiva. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Nem sempre estamos com energia para cuidar. Cuidar de quem cuida também é parte do jardim, e pedir ajuda, ou aceitar companhia, é cuidado.

Qual gesto pequeno de cuidado você poderia repetir esta semana?

Salve para reler num dia em que o coração estiver cansado e envie a quem cuida de alguém.

Reflexão autoral inspirada em Mêncio (Mencius), livro 2A, capítulo 6.

@doni7m""",
    hashtags=tags30(["#Mencio", "#Mencius", "#FilosofiaChinesa", "#Confucionismo", "#Compaixao", "#Cuidado", "#Empatia",
                     "#GestosPequenos", "#Bondade", "#SextaFeira"], 20),
    ref="""Filósofo: Mêncio (Mengzi, c. 372-289 a.C.).
Obra: Mêncio (Mengzi), livro 2A, passagem 6 (a criança prestes a cair num poço e os "brotos" da compaixão).
Passagens consultadas: na tradução de D. C. Lau, "No man is devoid of a heart sensitive to the sufferings of others"; outra tradução (tradutor não indicado na página): "Even nowadays, if an infant were about to fall into a well, anyone would be upset and concerned."
Link consultado: https://www.wabashcenter.wabash.edu/syllabi/g/gier/308/menselect.htm
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal no carrossel nem na legenda.""")

single("2026-10-30", "Bertrand Russell", "interesses fora de si",
       "Preocupações também fazem prisões. Um interesse fora de si, como uma planta, um assunto ou uma pessoa, abre uma janela.",
       "Uma reflexão inspirada em Bertrand Russell", "e30b",
       """Quando a cabeça só gira em torno do mesmo problema, o mundo parece caber num quarto.

Bertrand Russell, em A Conquista da Felicidade, defende que o interesse por coisas fora de nós, hobbies, estudos, pessoas, guarda um pouco de vida mesmo quando o centro balança. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Não é fugir do problema. É dar a ele um lugar menor na casa, para respirar.

Que interesse seu anda esquecido numa gaveta?

Salve para lembrar de abrir uma janela e envie a quem anda preso nos mesmos pensamentos.

Frase autoral inspirada em Bertrand Russell, A Conquista da Felicidade (1930); não é citação literal.

@doni7m""",
       ["#BertrandRussell", "#Russell", "#ConquistaDaFelicidade", "#FilosofiaBritanica", "#Interesses", "#Hobbies", "#AbrirJanelas",
        "#PensamentosRepetitivos", "#VidaPlena", "#SextaFeira"], 22,
       """Filósofo: Bertrand Russell (1872-1970).
Obra: A Conquista da Felicidade (The Conquest of Happiness, 1930), sobretudo os capítulos sobre o entusiasmo e os interesses impessoais.
Ideia usada (conforme resumo dos capítulos consultado): interesses fora de si guardam uma reserva de interesse pela vida se os pilares centrais falham; as paixões que nos fecham em nós mesmos são das piores prisões.
Links consultados: https://heritage.gurus.org/dougdeb/Courses/Happy/Conquest/outline.html (resumo) e https://gutenberg.org/ebooks/77894 (texto integral; capítulo e frase exata não conferidos no original).
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")

# ========================= SÁBADO 31/10 =========================
add(date="2026-10-31", slot="A", kind="carousel", philosopher="Adam Smith", theme="sentir junto",
    slides=[
        ("Quem sofre quase nunca precisa de conselho. Precisa de quem sinta junto.", None),
        ("Alguém conta um problema e a nossa reação é resolver: sugerir, comparar, dizer que passa. A pessoa se cala.", None),
        ("Muitas vezes o conselho nasce da pressa de aliviar o nosso desconforto ao ouvir. O outro percebe e guarda o resto para si.", None),
        ("Adam Smith abriu um livro lembrando que, por mais egoísta que seja, o ser humano se importa com a sorte alheia.", "Uma reflexão inspirada em Adam Smith"),
        ("Experimente repetir com suas palavras o que ouviu e perguntar: você quer que eu só escute ou quer ideias? Deixe o silêncio trabalhar.", None),
        ("Sentir junto não é carregar a dor do outro nem esquecer de si. É ficar perto o bastante para ele não ficar sozinho.", None),
        ("Às vezes cuidar é só ficar. Quem precisa da sua presença esta semana?", "Salve ou envie a quem sabe ouvir."),
    ],
    scenes=["e31a1", "e31a2", "e31a3", "e31a4", "e31a5", "e31a6", "e31a7"],
    caption="""Um amigo conta que a semana foi pesada. Antes de pensar, já estamos oferecendo soluções.

Adam Smith, na abertura de A Teoria dos Sentimentos Morais, de 1759, escreve que, por mais egoísta que se suponha o homem, há princípios em sua natureza que o fazem interessar-se pela sorte dos outros e tornar a felicidade deles necessária a si, mesmo sem tirar disso nada além do prazer de vê-los felizes. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Acompanhar é diferente de consertar. E quem está sozinho com uma dor pode precisar, antes de tudo, de uma presença.

Se a solidão apertar, procurar companhia ou ajuda também é uma forma de cuidar de si.

Quem merece a sua escuta inteira hoje?

Salve para lembrar de perguntar antes de aconselhar e envie a quem sabe ouvir.

Reflexão autoral inspirada em Adam Smith, A Teoria dos Sentimentos Morais (1759), I.i.1.1.

@doni7m""",
    hashtags=tags30(["#AdamSmith", "#TeoriaDosSentimentosMorais", "#Simpatia", "#Escuta", "#Empatia", "#Iluminismo", "#FilosofiaMoral",
                     "#SentirJunto", "#PresencaQueAcolhe", "#Sabado"], 17),
    ref="""Filósofo: Adam Smith (1723-1790).
Obra: A Teoria dos Sentimentos Morais (The Theory of Moral Sentiments, 1759), Parte I, Seção i, Capítulo 1, parágrafo 1 (I.i.1.1).
Passagem consultada (Online Library of Liberty): "How selfish soever man may be supposed, there are evidently some principles in his nature..." (a página foi lida apenas até este trecho; a continuação é parafraseada com base no conhecimento corrente da obra — conferir na edição em mãos).
Link consultado: https://oll.libertyfund.org/quote/adam-smith-selfishness-sympathy
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal no carrossel nem na legenda.""")

single("2026-10-31", "Dōgen", "o momento inteiro",
       "A lenha vira cinza e não volta a ser lenha. Cada momento é inteiro: não precisa ser ensaio do próximo.",
       "Uma reflexão inspirada em Dōgen", "e31b",
       """A gente passa tanto tempo se preparando para o que vem que esquece de estar no que está.

Dōgen, mestre zen do século XIII, escreveu no Genjōkōan que a lenha se torna cinza e não volta a ser lenha, e que não devemos supor que a cinza é depois e a lenha é antes. A frase da imagem é uma reflexão autoral inspirada nessa imagem.

Nada disso manda abandonar planos. Só lembra que o fim de uma tarde, uma conversa ou um café quente acontece uma única vez.

O que, neste exato momento, merece ser vivido inteiro?

Salve para voltar a esta imagem num dia de pressa.

Frase autoral inspirada em Dōgen, Genjōkōan; não é citação literal.

@doni7m""",
       ["#Dogen", "#Genjokoan", "#Zen", "#FilosofiaOriental", "#MomentoPresente", "#LenhaECinza", "#ViverAgora",
        "#Impermanencia", "#BudismoZen", "#Sabado"], 24,
       """Filósofo: Eihei Dōgen (1200-1253), mestre zen japonês.
Obra: Genjōkōan (em Shōbōgenzō).
Passagem consultada (tradução inglesa de Robert Aitken e Kazuaki Tanahashi): "Firewood becomes ash, and it does not become firewood again." e "Yet, do not suppose that the ash is after and the firewood before." Também: "To study the Buddha Way is to study the self."
Link consultado: https://lionsroar.com/the-genjo-koan/
Natureza do texto: frase autoral inspirada na imagem; não é citação literal.""")

# ========================= DOMINGO 01/11 =========================
add(date="2026-11-01", slot="A", kind="carousel", philosopher="Demócrito", theme="medida e bom ânimo",
    slides=[
        ("Nem todo excesso é de coisa ruim. Às vezes é excesso de tudo que parecia bom.", None),
        ("Mais uma série, mais uma compra, mais uma tarefa, mais um compromisso. O corpo pede pausa e a gente responde com mais.", None),
        ("O prazer em dose demais vira cansaço, e o cansaço pede mais prazer para compensar. É um ciclo que conhecemos bem.", None),
        ("Demócrito falava em euthymia, um bom ânimo que nasceria da moderação nas alegrias e de certo equilíbrio de vida.", "Uma reflexão inspirada em Demócrito"),
        ("Teste: em vez de mais uma coisa, escolha a metade. Meia hora de tela, uma fatia, um compromisso a menos. Observe como o dia fica.", None),
        ("Moderação não é privação nem regra rígida. É perceber o ponto em que o prazer ainda é inteiro, antes de virar peso.", None),
        ("Medida boa é a que deixa vontade de voltar amanhã. Onde você pode escolher a metade hoje?", "Salve ou envie a quem vive no excesso."),
    ],
    scenes=["e01a1", "e01a2", "e01a3", "e01a4", "e01a5", "e01a6", "e01a7"],
    caption="""Um domingo pode ser o dia perfeito para notar a conta: quanto do cansaço vem do que fazemos e quanto vem do quanto fazemos.

Demócrito, filósofo pré-socrático, falava em euthymia, um bom ânimo ou contentamento, que viria da moderação das alegrias e de um equilíbrio de vida. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Moderação aqui não é castigo. É perceber quando o prazer ainda é inteiro, e quando já virou obrigação de aproveitar.

Se o cansaço for constante e vier acompanhado de tristeza, procurar companhia ou um profissional de saúde também é cuidado.

Onde você pode escolher a metade hoje?

Salve para reler antes da próxima semana cheia e envie a quem vive no excesso.

Reflexão autoral inspirada em Demócrito, fragmento B191 (Diels-Kranz).

@doni7m""",
    hashtags=tags30(["#Democrito", "#Euthymia", "#PreSocraticos", "#FilosofiaAntiga", "#Moderacao", "#BomAnimo", "#EquilibrioDeVida",
                     "#MenosEMais", "#Domingo", "#SemExcessos"], 1),
    ref="""Filósofo: Demócrito de Abdera (c. 460-370 a.C.).
Fonte: fragmento B191 (Diels-Kranz), sobre a euthymia.
Passagem consultada (tradução inglesa, no resumo de uma resenha do BMCR sobre o livro de Warren): "Euthymia arises in men through a moderation of joy and a good balance of life."
Link consultado: https://www.epicureanfriends.com/post-pdf-export/26931/ (fonte secundária; conferir o grego e a numeração em Diels-Kranz ou no livro de Warren, 2002).
Natureza do texto: reflexão autoral inspirada na ideia; sem aspas e sem citação literal no carrossel nem na legenda.""")

single("2026-11-01", "Maimônides", "ajudar a ficar de pé",
       "O melhor jeito de ajudar é ajudar alguém a ficar de pé, sem expor, sem cobrar gratidão, sem humilhar.",
       "Uma reflexão inspirada em Maimônides", "e01b",
       """Há ajudas que aliviam o dia e há ajudas que mudam o caminho. As duas importam, mas a segunda costuma pedir mais cuidado.

Maimônides, no Mishné Torá, descreve oito graus de caridade e coloca no mais alto aquele que sustenta a mão de quem empobreceu, antes que precise pedir. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Pode ser uma indicação de trabalho, um empréstimo combinado com respeito, uma parceria. O que importa é preservar a dignidade de quem recebe.

Quem, perto de você, está tentando ficar de pé?

Salve para lembrar de ajudar com delicadeza e envie a quem ajuda em silêncio.

Frase autoral inspirada em Maimônides, Mishné Torá, Leis das Doações aos Pobres 10:7; não é citação literal.

@doni7m""",
       ["#Maimonides", "#MishneTora", "#Caridade", "#Dignidade", "#AjudaComRespeito", "#FilosofiaMedieval", "#Solidariedade",
        "#Generosidade", "#Domingo", "#CuidarDoOutro"], 4,
       """Filósofo: Moisés Maimônides (1138-1204).
Obra: Mishné Torá, Leis das Doações aos Pobres (Matanot Aniyim) 10:7, os oito graus da caridade.
Passagem consultada (tradução não identificada na página): "The highest degree, than which there is none higher, is one who upholds the hand of an Israelite reduced to poverty" (a página lida corta a continuação, sobre ajudar com presente, empréstimo, parceria ou trabalho para que a pessoa não precise pedir).
Link consultado: https://voices.sefaria.org/sheets/8430
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")
