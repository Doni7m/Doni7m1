# -*- coding: utf-8 -*-
"""Conteúdo da semana 12-18/10/2026 (14 posts)."""
import unicodedata

BASE_TAGS = ["#Reflexao", "#FilosofiaDeVida", "#Filosofia", "#Autoconhecimento", "#FrasesParaRefletir", "#TextosAutorais",
             "#IlustracaoAutoral", "#Aquarela", "#Guache", "#IlhaDaMadeira", "#Madeira", "#Portugal", "#BrasileirosNaMadeira",
             "#BrasileirosEmPortugal", "#Funchal", "#Atlantico", "#CarrosselReflexivo", "#ReflexaoDoDia", "#PensamentoDoDia",
             "#Acolhimento", "#Gentileza", "#Presenca", "#Serenidade", "#Calma", "#CuidadoComSi", "#VidaSimples",
             "#PensarDevagar", "#FilosofiaParaTodos", "#Doni7m", "#LeituraDoDia"]


def norm(t):
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()


def tags30(theme, offset=0):
    out, seen = [], set()
    for t in theme + BASE_TAGS[offset:] + BASE_TAGS[:offset]:
        k = norm(t)
        if k not in seen:
            seen.add(k)
            out.append(t)
        if len(out) == 30:
            break
    assert len(out) == 30, (len(out), theme)
    return out


FOOT = "@doni7m"

POSTS = []


def add(**kw):
    POSTS.append(kw)


# ========================= SEGUNDA 12/10 =========================
add(date="2026-10-12", slot="A", kind="carousel", philosopher="Epicuro", theme="amizade e relações",
    slides=[
        ("Quase ninguém planeja a vida em torno das pessoas de quem mais precisa.", None),
        ("Você deixa a mensagem para amanhã, adia o convite, promete uma visita. A agenda enche, e as pessoas continuam esperando em silêncio.", None),
        ("Não é falta de afeto. É que o urgente grita, e o importante costuma falar baixo.", None),
        ("Epicuro via a amizade como a coisa mais valiosa que a sabedoria oferece para uma vida feliz.", "Uma reflexão inspirada em Epicuro"),
        ("Hoje, escolha uma pessoa. Mande um áudio, marque um café, pergunte como ela está de verdade. Um gesto simples já é começo.", None),
        ("Amizade não pede grandes discursos. Pede constância, atenção e um pouco de tempo reservado só para isso.", None),
        ("Quem você anda querendo ver e ainda não chamou?", "Salve ou envie a quem veio à sua cabeça."),
    ],
    scenes=["mon_a1", "mon_a2", "mon_a3", "mon_a4", "mon_a5", "mon_a6", "mon_a7"],
    caption="""Quase ninguém decide deixar de ver as pessoas importantes. Elas só vão ficando para depois, entre a agenda cheia e o cansaço do fim do dia.

Epicuro dizia, em uma de suas máximas, que de tudo o que a sabedoria prepara para uma vida feliz, nada é maior do que a amizade. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Ninguém precisa de grandes gestos. Um áudio, um convite simples ou uma pergunta feita com calma já mantêm uma ponte de pé.

Se a semana estiver pesada, tudo bem escolher um único nome e começar por ele.

Quem você anda querendo ver e ainda não chamou?

Salve para lembrar de escrever e envie a quem veio à sua cabeça.

Reflexão autoral inspirada em Epicuro, Máximas Principais, XXVII.

@doni7m""",
    hashtags=tags30(["#Amizade", "#Amizades", "#Epicuro", "#Epicurismo", "#FilosofiaAntiga", "#Relacionamentos", "#Conexao",
                     "#Saudade", "#TempoDeQualidade", "#PessoasImportantes", "#Afeto", "#Companhia"], 0),
    ref="""Filósofo: Epicuro (341-270 a.C.).
Obra: Máximas Principais (Kyriai Doxai), XXVII, preservada em Diógenes Laércio, Vidas dos Filósofos Ilustres, X.
Passagem consultada (tradução inglesa de R. D. Hicks): "Of all the means which are procured by wisdom to ensure happiness throughout the whole of life, by far the most important is the acquisition of friends."
Link: https://classics.mit.edu/Epicurus/princdoc.html
Natureza do texto: interpretação autoral inspirada na máxima; não há citação literal no carrossel nem na legenda.""")

add(date="2026-10-12", slot="B", kind="single", philosopher="Marco Aurélio", theme="expectativas e julgamentos",
    slides=[("Às vezes o que pesa não é só o acontecimento, mas a conclusão que tiramos dele. Vale reler essa conclusão com calma.", "Uma reflexão inspirada em Marco Aurélio")],
    scenes=["b_mon"],
    caption="""Um imprevisto acontece, e em poucos minutos já temos uma história inteira sobre ele: o que significa, quem errou, o que vem depois.

Marco Aurélio, nas Meditações, lembrava que muito do que nos perturba nasce do nosso juízo sobre as coisas. Reler o próprio juízo, com calma, às vezes alivia um pouco.

Isso não nega o que é difícil de verdade. Só abre espaço para outras leituras.

Que conclusão apressada você poderia reler hoje?

Salve para voltar a esta pergunta.

Frase autoral inspirada em Marco Aurélio, Meditações, VIII, 47; não é citação literal.

@doni7m""",
    hashtags=tags30(["#MarcoAurelio", "#Estoicismo", "#Estoico", "#Meditacoes", "#Expectativas", "#Perspectiva", "#MudarOlhar",
                     "#MenteCalma", "#FilosofiaEstoica", "#ReleituraDeSi"], 5),
    ref="""Filósofo: Marco Aurélio (121-180 d.C.).
Obra: Meditações, Livro VIII, 47.
Passagem consultada (tradução inglesa de George Long): "If thou art pained by any external thing, it is not this thing that disturbs thee, but thy own judgement about it."
Link: https://classics.mit.edu/Antoninus/meditations.8.eight.html
Natureza do texto: frase autoral inspirada na passagem; sem citação literal na imagem nem na legenda.""")

# ========================= TERÇA 13/10 =========================
add(date="2026-10-13", slot="A", kind="carousel", philosopher="Sêneca", theme="tempo",
    slides=[
        ("Talvez o problema não seja ter pouco tempo.", None),
        ("Meia hora aqui, uma tarde ali, uma manhã inteira entre notificações. O dia some em pedaços que ninguém escolheu.", None),
        ("O tempo quase nunca é roubado de uma vez. Vai escorrendo pelo cansaço, pelo hábito e pela dificuldade de dizer não.", None),
        ("Sêneca observava que não temos pouco tempo de vida; desperdiçamos muito dele sem perceber.", "Uma reflexão inspirada em Sêneca"),
        ("Escolha uma hora da semana e dê a ela um dono: uma caminhada, uma conversa, uma leitura. Sem ter que provar nada.", None),
        ("Nem todo tempo perdido é preguiça. Às vezes é excesso de tarefas, falta de escolha ou simples cansaço. Olhar com honestidade já ajuda.", None),
        ("O tempo que importa raramente grita. Reserve um pedaço dele para o que é seu.", "Salve para revisitar no fim da semana."),
    ],
    scenes=["tue_a1", "tue_a2", "tue_a3", "tue_a4", "tue_a5", "tue_a6", "tue_a7"],
    caption="""Há dias em que a pergunta não é o que fazer, e sim para onde o tempo foi.

Sêneca, em Sobre a brevidade da vida, notava que não temos pouco tempo, mas deixamos muito dele escorrer. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Nem sempre dá para escolher tudo. Trabalho, cansaço e obrigações pesam de verdade. Ainda assim, uma pequena hora com dono pode mudar o clima da semana.

Qual hora da sua semana você gostaria de ter só para si?

Salve para revisitar no fim da semana e compartilhe com quem anda sem tempo.

Reflexão autoral inspirada em Sêneca, De Brevitate Vitae, 1.1.

@doni7m""",
    hashtags=tags30(["#Seneca", "#Estoicismo", "#Tempo", "#GestaoDoTempo", "#BrevidadeDaVida", "#FilosofiaEstoica", "#Rotina",
                     "#Prioridades", "#TempoParaSi", "#VidaCorrida", "#Escolhas", "#Desacelerar"], 10),
    ref="""Filósofo: Lúcio Aneu Sêneca (c. 4 a.C.-65 d.C.).
Obra: De Brevitate Vitae (Sobre a brevidade da vida), 1.1.
Passagem consultada (latim): "non exiguum temporis habemus, sed multum perdidimus. satis longa uita et in maximarum rerum consummationem: large data est, si tota bene conlocaretur." Tradução livre: não temos pouco tempo, mas perdemos muito dele; a vida é longa o bastante, se bem empregada.
Link: https://sententiaeantiquae.com/2014/01/25/seneca-de-brevitate-vitae-1-1/
Natureza do texto: interpretação autoral; não há citação literal nos slides nem na legenda.""")

add(date="2026-10-13", slot="B", kind="single", philosopher="Kierkegaard", theme="decidir sem certeza",
    slides=[("A vida só se entende olhando para trás, mas só se vive olhando para a frente. Decidir sem certeza é normal.", "Uma reflexão inspirada em Kierkegaard")],
    scenes=["b_tue"],
    caption="""Muitas vezes esperamos ter certeza para dar o próximo passo. Só que a certeza costuma chegar depois, quando olhamos para trás e o caminho faz sentido.

Kierkegaard anotou em seu diário, em 1843, que a vida só pode ser compreendida olhando para trás, mas precisa ser vivida olhando para a frente. A frase da imagem é uma reflexão autoral inspirada nessa anotação.

Dá para decidir com cuidado e ainda assim sem garantias.

Que passo pequeno você vem adiando por falta de certeza?

Salve para reler quando a dúvida pesar.

Frase autoral inspirada em Kierkegaard, Diários, IV A 164 (1843); não é citação literal.

@doni7m""",
    hashtags=tags30(["#Kierkegaard", "#Existencialismo", "#Decisoes", "#Incerteza", "#Escolhas", "#VivendoOAgora", "#Caminhos",
                     "#FilosofiaExistencial", "#PrimeiroPasso", "#Duvida"], 15),
    ref="""Filósofo: Søren Kierkegaard (1813-1855).
Obra: Diários (Journalen), anotação IV A 164, 1843.
Passagem consultada (tradução inglesa): "Life can only be understood backwards; but it must be lived forwards."
Link: https://wist.info/kierkegaard-soren/35849/
Natureza do texto: frase autoral inspirada na anotação; a frase da imagem não é citação literal. A passagem acima foi consultada apenas como fonte.""")

# ========================= QUARTA 14/10 =========================
add(date="2026-10-14", slot="A", kind="carousel", philosopher="Simone Weil", theme="atenção e presença",
    slides=[
        ("Prestar atenção em alguém pode ser o presente mais raro.", None),
        ("A pessoa fala, e você responde no automático, com a cabeça no que vem depois. Ela percebe, mesmo sem dizer nada.", None),
        ("Ouvir de verdade cansa, porque exige ficar. Sem corrigir, sem ensaiar a resposta, sem olhar o relógio.", None),
        ("Simone Weil via a atenção como a forma mais rara e mais pura de generosidade.", "Uma reflexão inspirada em Simone Weil"),
        ("Em uma conversa hoje, deixe o celular longe, olhe para a pessoa e faça uma pergunta a mais. Depois, apenas escute.", None),
        ("A atenção também vale para você: notar o cansaço, a fome, a vontade de parar. Cuidar começa por perceber.", None),
        ("Que conversa merece a sua atenção inteira hoje?", "Compartilhe com alguém que sabe ouvir."),
    ],
    scenes=["wed_a1", "wed_a2", "wed_a3", "wed_a4", "wed_a5", "wed_a6", "wed_a7"],
    caption="""Existe uma diferença silenciosa entre estar na conversa e estar presente nela.

Simone Weil escreveu a um amigo, em 1942, que a atenção é a forma mais rara e mais pura de generosidade. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Prestar atenção não exige tempo sobrando. Exige, por alguns minutos, deixar uma coisa só ocupar o centro.

Isso vale para quem está ao seu lado e também para você, quando o corpo avisa que precisa parar.

Quem merece o seu ouvir inteiro hoje?

Salve para lembrar de escutar sem pressa e compartilhe com quem sabe ouvir.

Reflexão autoral inspirada em Simone Weil, carta a Joë Bousquet (1942).

@doni7m""",
    hashtags=tags30(["#SimoneWeil", "#Atencao", "#Escuta", "#EscutaAtiva", "#Presenca", "#Generosidade", "#Conversas",
                     "#RelacoesHumanas", "#FilosofiaFrancesa", "#OuvirComAtencao", "#Mindfulness", "#Gentileza"], 20),
    ref="""Filósofa: Simone Weil (1909-1943).
Fonte: carta a Joë Bousquet, 1942, em que escreve: "L'attention est la forme la plus rare et la plus pure de la générosité."
Link consultado: https://kfitz.info/la-plus-rare-et-la-plus-pure/
Natureza do texto: interpretação autoral da ideia; os slides e a legenda não trazem a frase entre aspas.""")

add(date="2026-10-14", slot="B", kind="single", philosopher="Aristóteles", theme="aprender fazendo",
    slides=[("Aprender a viver é como aprender um ofício: aos poucos, errando, repetindo, até o gesto ficar seu.", "Uma reflexão inspirada em Aristóteles")],
    scenes=["b_wed"],
    caption="""Ninguém aprende bordado só olhando, nem a conversar só lendo sobre conversas. O gesto vem com as mãos, com erros e com repetição.

Aristóteles, na Ética a Nicômaco, dizia que o que precisamos aprender antes de fazer, aprendemos fazendo. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Começar torto também conta como começar.

O que você está aprendendo aos poucos, sem pressa de acertar?

Salve para lembrar de ser paciente com o seu ritmo.

Frase autoral inspirada em Aristóteles, Ética a Nicômaco, II, 1; não é citação literal.

@doni7m""",
    hashtags=tags30(["#Aristoteles", "#EticaANicomaco", "#Habitos", "#AprenderFazendo", "#Paciencia", "#Bordado", "#ArtesanatoMadeirense",
                     "#PequenosPassos", "#Pratica", "#RespeiteSeuRitmo"], 25),
    ref="""Filósofo: Aristóteles (384-322 a.C.).
Obra: Ética a Nicômaco, Livro II, cap. 1 (1103a-b).
Passagem consultada (tradução inglesa de W. D. Ross): "For the things we have to learn before we can do them, we learn by doing them, e.g. men become builders by building and lyre players by playing the lyre."
Link: https://classics.mit.edu/Aristotle/nicomachaen.2.ii.html
Natureza do texto: frase autoral inspirada na passagem; não é citação literal.""")

# ========================= QUINTA 15/10 =========================
add(date="2026-10-15", slot="A", kind="carousel", philosopher="Hannah Arendt", theme="recomeços",
    slides=[
        ("Recomeçar não é voltar ao zero. É lembrar que ainda dá para começar.", None),
        ("Um plano que não deu certo, uma fase que acabou, uma versão sua que já não cabe. Parece que tudo terminou.", None),
        ("Mas o que terminou deixou aprendizado, cicatriz e vocabulário novo. Nenhum recomeço parte de uma folha realmente em branco.", None),
        ("Hannah Arendt via no nascimento a raiz da nossa capacidade de agir e começar algo novo: cada pessoa chega como um início.", "Uma reflexão inspirada em Hannah Arendt"),
        ("Comece menor do que gostaria: uma gaveta, uma mensagem, dez minutos de caminhada. O começo não precisa ser grande para ser verdadeiro.", None),
        ("Recomeçar não depende só de vontade. Há fases em que faltam energia, dinheiro ou apoio. Pedir ajuda também é um começo.", None),
        ("O que em você ainda está começando?", "Salve para voltar quando precisar."),
    ],
    scenes=["thu_a1", "thu_a2", "thu_a3", "thu_a4", "thu_a5", "thu_a6", "thu_a7"],
    caption="""Quando algo termina, a primeira sensação costuma ser de fim. Só mais tarde aparece a outra: a de que ainda existe espaço para começar.

Hannah Arendt, em A condição humana, via no fato do nascimento a raiz da capacidade humana de agir e de iniciar o novo. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Recomeçar raramente é um grande gesto. Quase sempre é uma gaveta, uma mensagem, uma caminhada curta.

E há fases em que isso não depende só de vontade. Pedir ajuda também faz parte do começo.

O que em você ainda está começando?

Salve para voltar quando precisar e compartilhe com quem está num recomeço.

Reflexão autoral inspirada em Hannah Arendt, A condição humana (1958).

@doni7m""",
    hashtags=tags30(["#HannahArendt", "#Recomecos", "#Recomecar", "#NovoComeco", "#Natalidade", "#Mudancas", "#NovasFases",
                     "#PedirAjuda", "#FilosofiaPolitica", "#Renovacao", "#SeguirEmFrente", "#Esperanca"], 0),
    ref="""Filósofa: Hannah Arendt (1906-1975).
Obra: A condição humana (The Human Condition, 1958), capítulo sobre a ação.
Passagem consultada: "The miracle that saves the world, the realm of human affairs, from its normal, 'natural' ruin is ultimately the fact of natality, in which the faculty of action is ontologically rooted."
Link: https://thefrailestthing.com/2017/01/02/the-miracle-that-saves-the-world/
Natureza do texto: interpretação autoral do conceito de natalidade; não há citação literal nos slides nem na legenda.""")

add(date="2026-10-15", slot="B", kind="single", philosopher="Marco Aurélio", theme="dias sem vontade",
    slides=[("Há manhãs em que levantar custa. Nesses dias, talvez baste o tamanho de um passo, e não o de um plano inteiro.", "Uma reflexão inspirada em Marco Aurélio")],
    scenes=["b_thu"],
    caption="""Tem manhã que começa devagar, e tudo bem.

Marco Aurélio, nas Meditações, escreveu para si mesmo sobre levantar sem vontade: lembrava que acordava para o trabalho de ser humano. A frase da imagem é uma reflexão autoral inspirada nessa anotação.

Num dia assim, talvez o primeiro passo seja só abrir a janela ou tomar algo quente. O resto pode vir aos poucos.

Se esse cansaço durar muito ou pesar demais, conversar com alguém de confiança ou com um profissional também é uma forma de cuidado.

Qual é o menor passo possível para a sua manhã?

Salve para os dias mais lentos.

Frase autoral inspirada em Marco Aurélio, Meditações, V, 1; não é citação literal.

@doni7m""",
    hashtags=tags30(["#MarcoAurelio", "#Estoicismo", "#DiasDificeis", "#Manha", "#PequenosPassos", "#Cansaco", "#CuidadoEmocional",
                     "#PausaNecessaria", "#ComecarDevagar", "#ManhasLentas"], 4),
    ref="""Filósofo: Marco Aurélio (121-180 d.C.).
Obra: Meditações, Livro V, 1.
Passagem consultada (tradução inglesa de George Long): "In the morning when thou risest unwillingly, let this thought be present: I am rising to the work of a human being."
Link: https://classics.mit.edu/Antoninus/meditations.5.five.html
Natureza do texto: frase autoral inspirada na passagem; não é citação literal.""")

# ========================= SEXTA 16/10 =========================
add(date="2026-10-16", slot="A", kind="carousel", philosopher="Aristóteles", theme="coragem",
    slides=[
        ("Coragem não nasce pronta. Aprende-se aos poucos.", None),
        ("Falar o que pensa, pedir desculpas, dizer não, mudar de rumo. Muita gente acha que os corajosos já nasceram assim.", None),
        ("Mas o medo costuma estar presente até em quem age. A diferença é que alguém, um dia, deu um primeiro passo pequeno.", None),
        ("Aristóteles observava que nos tornamos corajosos praticando atos de coragem, como nos tornamos construtores construindo.", "Uma reflexão inspirada em Aristóteles"),
        ("Escolha uma coragem pequena para esta semana: uma conversa adiada, uma pergunta, um não educado. Treine em escala doméstica.", None),
        ("Coragem não é ignorar o medo nem se expor a tudo. Também pede cuidado, limites e boas companhias para o primeiro passo.", None),
        ("Qual é a sua coragem pequena para esta semana?", "Salve ou envie a quem está treinando a própria."),
    ],
    scenes=["fri_a1", "fri_a2", "fri_a3", "fri_a4", "fri_a5", "fri_a6", "fri_a7"],
    caption="""Quase toda coragem começa pequena e meio desajeitada: uma pergunta feita em voz baixa, um não dito com educação, uma conversa que parecia impossível.

Aristóteles, na Ética a Nicômaco, observava que nos tornamos justos praticando atos justos e corajosos praticando atos de coragem. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Isso não significa se expor sem cuidado. Coragem também pede limites, ritmo e boas companhias para o primeiro passo.

Qual é a sua coragem pequena para esta semana?

Salve para lembrar dela e envie a quem está treinando a própria.

Reflexão autoral inspirada em Aristóteles, Ética a Nicômaco, II, 1.

@doni7m""",
    hashtags=tags30(["#Aristoteles", "#Coragem", "#Bravura", "#VencerOMedo", "#PrimeiroPasso", "#Habitos", "#Virtude",
                     "#EticaAristotelica", "#PequenasCoragens", "#SairDaZonaDeConforto", "#Autoconfianca", "#Medo"], 10),
    ref="""Filósofo: Aristóteles (384-322 a.C.).
Obra: Ética a Nicômaco, Livro II, cap. 1 (1103a-b).
Passagem consultada (tradução inglesa de W. D. Ross): "...so too we become just by doing just acts, temperate by doing temperate acts, brave by doing brave acts."
Link: https://classics.mit.edu/Aristotle/nicomachaen.2.ii.html
Natureza do texto: interpretação autoral; não há citação literal nos slides nem na legenda.""")

add(date="2026-10-16", slot="B", kind="single", philosopher="Sêneca", theme="pequenos prazeres e gratidão",
    slides=[("Um dia comum já guarda muita coisa: uma xícara quente, uma luz boa, alguém que responde. Perceber também é bem usar o tempo.", "Uma reflexão inspirada em Sêneca")],
    scenes=["b_fri"],
    caption="""Às vezes procuramos longe o que já está na mesa: o café ainda quente, a luz da manhã, alguém que respondeu a mensagem.

Sêneca defendia que a vida é longa o bastante quando bem empregada. A frase da imagem é uma reflexão autoral inspirada nessa ideia: notar o que há também é uma forma de usar bem o tempo.

Isso não apaga o que falta. Só ajuda a ver o que já está aqui.

O que, no seu dia de hoje, já merece ser notado?

Salve para lembrar de olhar com calma.

Frase autoral inspirada em Sêneca, De Brevitate Vitae, 1.1; não é citação literal.

@doni7m""",
    hashtags=tags30(["#Seneca", "#Estoicismo", "#Gratidao", "#PequenosPrazeres", "#CafeDaManha", "#DiaComum", "#NotarOQueTem",
                     "#Contentamento", "#VidaSimples", "#Luz"], 15),
    ref="""Filósofo: Lúcio Aneu Sêneca (c. 4 a.C.-65 d.C.).
Obra: De Brevitate Vitae (Sobre a brevidade da vida), 1.1.
Passagem consultada (latim): "satis longa uita et in maximarum rerum consummationem: large data est, si tota bene conlocaretur." Tradução livre: a vida é longa o bastante, se bem empregada.
Link: https://sententiaeantiquae.com/2014/01/25/seneca-de-brevitate-vitae-1-1/
Natureza do texto: frase autoral inspirada na passagem; não é citação literal.""")

# ========================= SÁBADO 17/10 =========================
add(date="2026-10-17", slot="A", kind="carousel", philosopher="Espinosa", theme="tristeza, saudade e alegria",
    slides=[
        ("Nem toda tristeza precisa ser vencida. Algumas precisam ser compreendidas.", None),
        ("Para quem vive longe do que ama, certas noites pesam mais: a saudade de casa, o silêncio, o cheiro de cozinha que não vem.", None),
        ("A gente tenta se apressar para passar por isso. Mas o peso costuma dizer algo sobre o que importa para você.", None),
        ("Para Espinosa, a alegria aumenta nossa força de agir e a tristeza a diminui. Entender o que nos afeta já é um primeiro passo.", "Uma reflexão inspirada em Espinosa"),
        ("Observe o que, no seu dia, aumenta sua força: uma chamada, um passeio, uma comida de casa, uma música. Dê espaço a isso.", None),
        ("Se o peso não alivia ou parece grande demais, procurar companhia, uma conversa ou ajuda profissional também é uma forma de cuidado.", None),
        ("Quem está longe de você e merece uma mensagem hoje?", "Compartilhe com quem vive longe de casa."),
    ],
    scenes=["sat_a1", "sat_a2", "sat_a3", "sat_a4", "sat_a5", "sat_a6", "sat_a7"],
    caption="""Para quem vive longe de casa, algumas noites pesam mais. A saudade chega sem avisar: um cheiro, uma música, uma rua que lembra outra.

Espinosa, na Ética, descreve a alegria como a passagem a uma perfeição maior, ou seja, a um aumento da nossa força de agir, e a tristeza como o caminho inverso. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Entender o que nos enfraquece e o que nos fortalece não faz a saudade sumir. Ajuda a cuidar melhor de si.

E se o peso não alivia, procurar companhia, uma conversa ou ajuda profissional também é cuidado.

Quem está longe de você e merece uma mensagem hoje?

Salve para os dias de saudade e compartilhe com quem vive longe de casa.

Reflexão autoral inspirada em Espinosa, Ética, parte III (proposição 11, escólio).

@doni7m""",
    hashtags=tags30(["#Espinosa", "#Spinoza", "#Saudade", "#SaudadeDeCasa", "#Alegria", "#Tristeza", "#Emocoes",
                     "#VidaLongeDeCasa", "#Imigrantes", "#CompanhiaEAcolhimento", "#Etica", "#Afetos"], 20),
    ref="""Filósofo: Baruch de Espinosa (1632-1677).
Obra: Ética, parte III, proposição 11, escólio (definição de alegria como passagem a uma perfeição maior).
Fonte consultada: Stanford Encyclopedia of Philosophy, verbete Spinoza, que cita "By Joy ... I shall understand that passion by which the Mind passes to a greater perfection" (Ética III, p11s) e descreve a tristeza como passagem a uma perfeição menor.
Link: https://plato.stanford.edu/entries/spinoza/
Natureza do texto: interpretação autoral; não há citação literal nos slides nem na legenda.""")

add(date="2026-10-17", slot="B", kind="single", philosopher="Epicuro", theme="amizade e companhia",
    slides=[("Na hora difícil, ter para quem ligar importa mais do que ter muito. Cultive essa pessoa antes de precisar.", "Uma reflexão inspirada em Epicuro")],
    scenes=["b_sat"],
    caption="""Dois lados de uma baía, duas encostas com luzes acesas. Entre elas, o mar. Dá para atravessar, desde que alguém saia com uma lanterna.

Epicuro colocava a amizade entre as coisas mais valiosas para uma vida feliz. A frase da imagem é uma reflexão autoral inspirada nessa ideia.

Cultivar essa pessoa não pede muito: lembrar do aniversário, perguntar como foi o exame, ligar sem motivo.

Para quem você ligaria numa hora difícil? E quem pode ter você como esse alguém?

Salve para lembrar de ligar e envie a quem veio à sua cabeça.

Frase autoral inspirada em Epicuro, Máximas Principais, XXVII; não é citação literal.

@doni7m""",
    hashtags=tags30(["#Epicuro", "#Epicurismo", "#Amizade", "#Companhia", "#TerComQuemContar", "#Apoio", "#Amigos",
                     "#Lacos", "#FilosofiaAntiga", "#LigarParaAlguem"], 25),
    ref="""Filósofo: Epicuro (341-270 a.C.).
Obra: Máximas Principais (Kyriai Doxai), XXVII, preservada em Diógenes Laércio, Vidas dos Filósofos Ilustres, X.
Passagem consultada (tradução inglesa de R. D. Hicks): "Of all the means which are procured by wisdom to ensure happiness throughout the whole of life, by far the most important is the acquisition of friends."
Link: https://classics.mit.edu/Epicurus/princdoc.html
Natureza do texto: frase autoral inspirada na máxima; não é citação literal.""")

# ========================= DOMINGO 18/10 =========================
add(date="2026-10-18", slot="A", kind="carousel", philosopher="Epicteto", theme="limites e desapego",
    slides=[
        ("Uma lista simples para dias pesados: o que é seu e o que não é.", None),
        ("Você relê a conversa, ensaia a resposta, tenta controlar a opinião dos outros, o trânsito, o resultado de amanhã.", None),
        ("Gastamos energia onde as mãos não alcançam, e sobra pouco para o que está ao nosso alcance.", None),
        ("Epicteto começava seu manual separando o que depende de nós, como escolhas e ações, do que não depende.", "Uma reflexão inspirada em Epicteto"),
        ("Faça duas colunas num papel: o que posso fazer hoje e o que não depende de mim. Comece pela primeira.", None),
        ("Isso não é calar diante do que é injusto nem aceitar tudo. É escolher onde pôr a sua força.", None),
        ("Soltar o que não é seu abre espaço para o que é.", "Salve para a próxima semana pesada."),
    ],
    scenes=["sun_a1", "sun_a2", "sun_a3", "sun_a4", "sun_a5", "sun_a6", "sun_a7"],
    caption="""Domingo à noite é um bom momento para separar o que é seu do que não é.

Epicteto abre o Manual dizendo que algumas coisas dependem de nós, como nossas opiniões e ações, e outras não. Este carrossel é uma reflexão inspirada nessa distinção, e não uma citação literal.

Não é resignação nem indiferença. É escolher onde colocar a força, para que ela chegue inteira ao que pode ser feito.

Duas colunas num papel já ajudam: o que posso fazer esta semana e o que não depende de mim.

O que você pode soltar hoje, ao menos até amanhã?

Salve para a próxima semana pesada e compartilhe com quem vive controlando tudo.

Reflexão autoral inspirada em Epicteto, Encheiridion (Manual), 1.

@doni7m""",
    hashtags=tags30(["#Epicteto", "#Estoicismo", "#Estoico", "#Controle", "#Desapego", "#Limites", "#SoltarOQueNaoEMeu",
                     "#FilosofiaEstoica", "#DomingoANoite", "#Ansiedade", "#SemanaQueComeca", "#Foco"], 0),
    ref="""Filósofo: Epicteto (c. 50-135 d.C.).
Obra: Encheiridion (Manual), §1.
Passagem consultada (tradução inglesa de Elizabeth Carter): "Some things are in our control and others not. Things in our control are opinion, pursuit, desire, aversion, and, in a word, whatever are our own actions."
Link: https://classics.mit.edu/Epictetus/epicench.html
Natureza do texto: interpretação autoral; não há citação literal nos slides nem na legenda.""")

add(date="2026-10-18", slot="B", kind="single", philosopher="Simone Weil", theme="escuta",
    slides=[("Escutar de verdade é um jeito silencioso de dizer: você importa. Hoje, ouça alguém sem pressa.", "Uma reflexão inspirada em Simone Weil")],
    scenes=["b_sun"],
    caption="""Uma concha guarda o som do mar só para quem se aproxima devagar.

Simone Weil via a atenção como a forma mais rara e mais pura de generosidade. A frase da imagem é uma reflexão autoral inspirada nessa ideia: escutar, de verdade, é um modo de dizer a alguém que ele importa.

Não precisa de conselho nem de solução. Às vezes só pede tempo e silêncio do nosso lado.

Quem você poderia escutar sem pressa nesta semana?

Salve para começar a semana com mais escuta.

Frase autoral inspirada em Simone Weil, carta a Joë Bousquet (1942); não é citação literal.

@doni7m""",
    hashtags=tags30(["#SimoneWeil", "#Escuta", "#EscutaAtiva", "#Atencao", "#Presenca", "#OuvirComAtencao", "#Silencio",
                     "#Concha", "#ComecoDeSemana", "#RelacoesHumanas"], 0),
    ref="""Filósofa: Simone Weil (1909-1943).
Fonte: carta a Joë Bousquet, 1942, em que escreve: "L'attention est la forme la plus rare et la plus pure de la générosité."
Link consultado: https://kfitz.info/la-plus-rare-et-la-plus-pure/
Natureza do texto: frase autoral inspirada na ideia; não é citação literal.""")
