# -*- coding: utf-8 -*-
"""Conteúdo 06-11/10/2026 (12 posts), filósofos ocidentais variados."""
from content_w42 import BASE_TAGS, norm, tags30

POSTS = []


def add(**kw):
    POSTS.append(kw)


def sc(prefix, n=7):
    return [f"{prefix}{i}" for i in range(1, n + 1)]


# ---------------- TERÇA 06/10 ----------------
add(date="2026-10-06", slot="A", kind="carousel", philosopher="Platão", theme="ver com calma o que dói",
    slides=[
        ("Olhar para a verdade pode doer no começo, como sair de um quarto escuro direto para a luz.", None),
        ("Platão imaginou pessoas presas numa caverna, acostumadas a ver só sombras na parede e a chamá-las de realidade.", None),
        ("Quando alguém é solto e olha para a luz, os olhos doem. O primeiro impulso é voltar para o que já conhecia.", None),
        ("Ver com clareza é um processo, e processos pedem tempo.", "Uma reflexão inspirada em Platão"),
        ("Talvez você esteja nesse ponto agora, com os olhos ainda se acostumando a algo que antes não via. Isso não é fraqueza.", None),
        ("Vá devagar. Olhe um pouco, descanse, olhe de novo. E conte com quem caminha ao seu lado.", None),
        ("O que você já consegue enxergar hoje, e que antes não via?", "Responda nos comentários ou salve para voltar depois."),
    ],
    scenes=sc("tue_a"),
    caption="""Às vezes a verdade chega como uma luz forte demais: incomoda antes de ajudar.

Na alegoria da caverna, Platão descreve prisioneiros que só conhecem sombras. Quando um deles é libertado e é obrigado a olhar para a luz, sente dor e quer voltar. Este carrossel é uma reflexão inspirada nessa imagem, e não uma citação literal.

Se você está atravessando um momento em que enxergar a própria situação dói, tudo bem ir devagar. Olhar um pouco, descansar e olhar de novo também é caminho. E procurar a companhia de alguém de confiança, ou ajuda profissional quando pesar demais, é uma forma de cuidado.

O que você já consegue enxergar hoje, e que antes não via?

Salve para voltar a este texto quando precisar.

Reflexão autoral inspirada em Platão, A República, Livro VII (alegoria da caverna).

@doni7m""",
    hashtags=tags30(["#Platao", "#AlegoriaDaCaverna", "#FilosofiaAntiga", "#FilosofiaGrega", "#Verdade", "#Clareza", "#Luz",
                     "#Crescimento", "#Paciencia", "#Mudanca", "#Consciencia", "#PensamentoCritico"], 0),
    ref="""Filósofo: Platão (c. 428-348 a.C.).
Obra: A República, Livro VII (alegoria da caverna).
Passagens consultadas (tradução inglesa de Benjamin Jowett): "Behold! human beings living in a underground den, which has a mouth open towards the light"; "when any of them is liberated and compelled suddenly to stand up and turn his neck round and walk and look towards the light, he will suffer sharp pains; the glare will distress him".
Link: https://classics.mit.edu/Plato/republic.8.vii.html
Natureza do texto do post: reflexão autoral, sem citação literal.
""")

add(date="2026-10-06", slot="B", kind="single", philosopher="Heráclito", theme="mudança e aceitação",
    slides=[("O rio de hoje não é o de ontem, e você também não. Dá para ser gentil com quem você está sendo agora.", None)],
    scenes=["tue_b"],
    caption="""Tudo muda, inclusive a gente. O dia difícil de hoje também passa, e o que você sente agora não é o que vai sentir para sempre.

Segundo Platão, no diálogo Crátilo, Sócrates atribui a Heráclito a ideia de que tudo se move e de que não se entra duas vezes na mesma água. Esta imagem é uma reflexão inspirada nisso, e não uma citação literal.

Que gentileza você pode ter hoje com a pessoa que você está sendo agora?

@doni7m""",
    hashtags=tags30(["#Heraclito", "#FilosofiaPreSocratica", "#Impermanencia", "#Mudanca", "#Aceitacao", "#Rio", "#TudoPassa",
                     "#Tempo", "#Recomeco", "#Natureza", "#Levada", "#VidaEmMovimento"], 6),
    ref="""Filósofo: Heráclito de Éfeso (c. 535-475 a.C.), conhecido por intermédio de Platão.
Obra: Crátilo, de Platão, c. 402a.
Passagem consultada (tradução de Jowett): "Heracleitus is supposed to say that all things are in motion and nothing at rest; he compares them to the stream of a river, and says that you cannot go into the same water twice."
Link: https://classics.mit.edu/Plato/cratylus.html
Natureza do texto do post: reflexão autoral, sem citação literal.
""")

# ---------------- QUARTA 07/10 ----------------
add(date="2026-10-07", slot="A", kind="carousel", philosopher="Nietzsche", theme="uma vida que você aceitaria repetir",
    slides=[
        ("E se cada dia que você vive pudesse voltar? Você o viveria do mesmo jeito?", None),
        ("Nietzsche propôs esse pensamento: imaginar a vida voltando inteira, em cada detalhe, e perguntar se você a aceitaria como ela é.", None),
        ("Não é um teste de perfeição. É um convite para perceber o que, na sua rotina, você já ama e o que gostaria de mudar.", None),
        ("Uma vida é boa quando dá para dizer sim a ela.", "Uma reflexão inspirada em Nietzsche"),
        ("Dizer sim não significa gostar de tudo. Significa olhar para o que aconteceu, dor incluída, sem fingir que foi diferente.", None),
        ("Comece pequeno. Escolha um momento do seu dia que você repetiria com prazer e dê a ele um pouco mais de atenção.", None),
        ("Qual é o momento do seu dia que você repetiria de bom grado?", "Conte nos comentários."),
    ],
    scenes=sc("wed_a"),
    caption="""E se este dia voltasse inteiro, de novo e de novo? Você o aceitaria como ele foi?

Nietzsche apresenta essa pergunta em A Gaia Ciência (§341): a vida seria boa se, ao imaginá-la retornando em cada detalhe, conseguíssemos afirmá-la como ela é. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Não se trata de cobrar perfeição de si. É só perceber o que na sua rotina vale ser repetido e dar a isso mais atenção. Se algo do passado pesa demais, conversar com alguém de confiança ou com um profissional também é cuidado.

Qual é o momento do seu dia que você repetiria de bom grado?

Conte nos comentários e salve para lembrar de dizer sim ao que é bom.

Reflexão autoral inspirada em Nietzsche, A Gaia Ciência, §341 (o pensamento do eterno retorno).

@doni7m""",
    hashtags=tags30(["#Nietzsche", "#EternoRetorno", "#AmorFati", "#FilosofiaModerna", "#FilosofiaAlema", "#Gratidao", "#VidaPlena",
                     "#MomentosSimples", "#Rotina", "#Escolhas", "#Sentido", "#DizerSim"], 3),
    ref="""Filósofo: Friedrich Nietzsche (1844-1900).
Obra: A Gaia Ciência (Die fröhliche Wissenschaft), aforismo 341 (o "maior peso").
Passagem consultada (Stanford Encyclopedia of Philosophy, verbete Nietzsche): "our life is good only if, upon imagining its return in every detail, we can affirm it as it is" (GS 341).
Link: https://plato.stanford.edu/entries/nietzsche/
Natureza do texto do post: reflexão autoral, sem citação literal.
""")

add(date="2026-10-07", slot="B", kind="single", philosopher="Aristóteles", theme="o bem que buscamos",
    slides=[("Tudo o que fazemos mira algum bem. Pergunte, com carinho: o que eu quero de verdade com isto?", None)],
    scenes=["wed_b"],
    caption="""Entre tantas tarefas, às vezes a gente esquece o rumo. Uma pergunta simples ajuda a reencontrá-lo: o que eu quero de verdade com isto?

Aristóteles abre a Ética a Nicômaco dizendo que toda arte, investigação, ação e escolha parece visar algum bem. Esta imagem é uma reflexão inspirada nessa abertura, e não uma citação literal.

Qual é o bem que você está buscando esta semana?

@doni7m""",
    hashtags=tags30(["#Aristoteles", "#EticaANicomaco", "#FilosofiaGrega", "#Proposito", "#Rumo", "#Escolhas", "#Planejamento",
                     "#BemViver", "#Barco", "#Horizonte", "#Intencao", "#Foco"], 9),
    ref="""Filósofo: Aristóteles (384-322 a.C.).
Obra: Ética a Nicômaco, Livro I, capítulo 1.
Passagem consultada (tradução inglesa de W. D. Ross): "Every art and every inquiry, and similarly every action and pursuit, is thought to aim at some good; and for this reason the good has rightly been declared to be that at which all things aim."
Link: https://classics.mit.edu/Aristotle/nicomachaen.1.i.html
Natureza do texto do post: reflexão autoral, sem citação literal.
""")

# ---------------- QUINTA 08/10 ----------------
add(date="2026-10-08", slot="A", kind="carousel", philosopher="Sócrates", theme="examinar a vida com gentileza",
    slides=[
        ("Conhecer a si mesmo não é se julgar. É se perguntar com curiosidade.", None),
        ("Segundo Platão, Sócrates defendeu que uma vida sem exame não vale a pena ser vivida.", None),
        ("Mas examinar não é se cobrar. É parar e perguntar: o que eu sinto, o que eu quero, o que está pesando?", None),
        ("Perguntas feitas com gentileza abrem mais portas do que acusações.", "Uma reflexão inspirada em Sócrates"),
        ("Se a resposta vier em forma de cansaço, dúvida ou tristeza, ela também merece ser ouvida sem pressa.", None),
        ("Escrever três linhas num caderno, caminhar sem fone, conversar com alguém de confiança: examinar a vida cabe em gestos pequenos.", None),
        ("Que pergunta você anda evitando se fazer?", "Responda só para você, ou compartilhe."),
    ],
    scenes=sc("thu_a"),
    caption="""Conhecer a si mesmo não precisa ser um tribunal. Pode ser só uma conversa tranquila com você.

Na Apologia de Sócrates, escrita por Platão, Sócrates afirma que a vida sem exame não vale a pena ser vivida. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal, e propõe examinar a vida com curiosidade e gentileza, nunca com dureza.

Se as respostas que aparecerem forem pesadas, não precisa carregá-las sozinho. Procurar companhia ou ajuda profissional é uma forma de cuidado.

Que pergunta você anda evitando se fazer?

Salve para voltar a ela com calma.

Reflexão autoral inspirada em Platão, Apologia de Sócrates, 38a.

@doni7m""",
    hashtags=tags30(["#Socrates", "#ConhecaTeAATiMesmo", "#ApologiaDeSocrates", "#FilosofiaAntiga", "#Autoconhecimento", "#Perguntas",
                     "#Curiosidade", "#SaudeEmocional", "#Diario", "#Escrita", "#Introspeccao", "#Caminhada"], 12),
    ref="""Filósofo: Sócrates (470-399 a.C.), conhecido por intermédio de Platão.
Obra: Apologia de Sócrates, de Platão, 38a.
Passagem consultada (tradução de Jowett): "...and that the life which is unexamined is not worth living".
Link: https://classics.mit.edu/Plato/apology.html
Natureza do texto do post: reflexão autoral, sem citação literal.
""")

add(date="2026-10-08", slot="B", kind="single", philosopher="Thoreau", theme="simplificar",
    slides=[("Simplificar não é ter menos. É abrir espaço para o que realmente importa.", None)],
    scenes=["thu_b"],
    caption="""Às vezes o que cansa não é a falta de coisas, e sim o excesso delas: tarefas, compromissos, objetos, notificações.

Henry David Thoreau, em Walden, defende simplificar a vida e dispensar as supostas necessidades que nos prendem. Esta imagem é uma reflexão inspirada nesse espírito, e não uma citação literal.

O que você poderia soltar hoje para sobrar um pouco mais de calma?

@doni7m""",
    hashtags=tags30(["#Thoreau", "#Walden", "#Simplicidade", "#VidaSimples", "#Minimalismo", "#FilosofiaAmericana", "#MenosEMais",
                     "#CasaPequena", "#Natureza", "#Desacelerar", "#Essencial", "#SlowLife"], 15),
    ref="""Filósofo: Henry David Thoreau (1817-1862).
Obra: Walden, ou a vida nos bosques (1854).
Fonte consultada: Stanford Encyclopedia of Philosophy, verbete Thoreau, que descreve como Thoreau "exhorts us to unclutter and simplify our lives, by eliminating the supposed necessities that can entrap us". Não houve acesso ao texto integral de Walden nesta consulta, por isso o post não traz citação literal.
Link: https://plato.stanford.edu/entries/thoreau/
Natureza do texto do post: reflexão autoral, sem citação literal.
""")

# ---------------- SEXTA 09/10 ----------------
add(date="2026-10-09", slot="A", kind="carousel", philosopher="Schopenhauer", theme="compaixão",
    slides=[
        ("Quando a gente sente a dor de outra pessoa como se fosse um pouco nossa, algo muda.", None),
        ("Schopenhauer defendia que a compaixão é a base da moral: reconhecer, no outro, uma vida tão frágil quanto a nossa.", None),
        ("Não é pena, e não é resolver o problema alheio. É estar disposto a sentir junto, com atenção.", None),
        ("A compaixão nasce quando percebemos que o outro também sente.", "Uma reflexão inspirada em Schopenhauer"),
        ("E vale para você também. Tratar a própria dor com a atenção que daria a um amigo já é um jeito de cuidar.", None),
        ("Um gesto basta: escutar sem interromper, ficar por perto, perguntar como a pessoa está de verdade.", None),
        ("Quem precisa hoje de um pouco da sua atenção?", "Mande uma mensagem."),
    ],
    scenes=sc("fri_a"),
    caption="""Existe um jeito simples de aliviar o peso do mundo: estar presente para quem está ao nosso lado.

Para Schopenhauer, em O Mundo como Vontade e Representação (§§ 63 e 64), a compaixão está na base da moral, pois reconhecemos no outro uma vida como a nossa. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Se hoje você é quem precisa de acolhimento, buscar companhia ou ajuda é uma forma de cuidado, tanto quanto oferecê-la.

Quem precisa hoje de um pouco da sua atenção?

Mande uma mensagem e salve este post para lembrar.

Reflexão autoral inspirada em Schopenhauer, O Mundo como Vontade e Representação, §§ 63-64.

@doni7m""",
    hashtags=tags30(["#Schopenhauer", "#Compaixao", "#Empatia", "#FilosofiaAlema", "#FilosofiaModerna", "#Solidariedade", "#Escuta",
                     "#Cuidado", "#Amizade", "#Presenca", "#Humanidade", "#Bondade"], 18),
    ref="""Filósofo: Arthur Schopenhauer (1788-1860).
Obra: O Mundo como Vontade e Representação, §§ 63-64 (compaixão como fundamento da moral).
Fonte consultada: Stanford Encyclopedia of Philosophy, verbete Schopenhauer: a compaixão como reconhecimento, no outro, da mesma essência; "to feel directly the life of another person" (WWR §§ 63-64, na paráfrase do verbete).
Link: https://plato.stanford.edu/entries/schopenhauer/
Natureza do texto do post: reflexão autoral, sem citação literal.
""")

add(date="2026-10-09", slot="B", kind="single", philosopher="Camus", theme="o passo de hoje",
    slides=[("A luta em direção ao alto já enche um coração. Hoje, só o próximo passo.", None)],
    scenes=["fri_b"],
    caption="""Nem todo dia pede uma grande vitória. Alguns pedem só o próximo passo, feito com o que a gente tem.

Albert Camus termina O Mito de Sísifo dizendo que a luta em direção ao alto basta para preencher um coração. Esta imagem é uma reflexão inspirada nesse trecho, e não uma citação literal.

Qual é o próximo passo possível para você hoje, mesmo que pequeno?

@doni7m""",
    hashtags=tags30(["#Camus", "#MitoDeSisifo", "#Absurdo", "#FilosofiaFrancesa", "#Existencialismo", "#Perseveranca", "#PassoAPasso",
                     "#Esforco", "#Subida", "#Coragem", "#Resiliencia", "#UmDiaDeCada"], 21),
    ref="""Filósofo: Albert Camus (1913-1960).
Obra: O Mito de Sísifo (1942), parágrafo final.
Fonte consultada: Stanford Encyclopedia of Philosophy, verbete Camus, que reproduz "The struggle itself toward the heights is enough to fill a man's heart" e "One must imagine Sisyphus happy" (MS, 123).
Link: https://plato.stanford.edu/entries/camus/
Natureza do texto do post: reflexão autoral, sem citação literal.
""")

# ---------------- SÁBADO 10/10 ----------------
add(date="2026-10-10", slot="A", kind="carousel", philosopher="Hume", theme="o que sentimos nos move",
    slides=[
        ("Nem sempre é a razão que nos move. Muitas vezes é o que sentimos.", None),
        ("Hume defendia que a razão sozinha não nos leva a agir: são os desejos e as emoções que dão direção.", None),
        ("Isso pode ser um alívio. Sentir não é um defeito de raciocínio. É parte do que nos coloca em movimento.", None),
        ("Ouvir o que sentimos ajuda a decidir melhor.", "Uma reflexão inspirada em Hume"),
        ("Antes de uma decisão importante, pergunte à razão e também ao coração. Os dois têm algo a dizer.", None),
        ("Se sentir te deixa confuso, dê nome. Dizer estou ansioso ou estou com saudade já tira um pouco da névoa.", None),
        ("O que você tem sentido ultimamente, e o que isso quer te dizer?", "Se quiser, conte nos comentários."),
    ],
    scenes=sc("sat_a"),
    caption="""Decidir não é só pensar. O que sentimos também faz parte da resposta.

David Hume sustentava, no Tratado da Natureza Humana (Livro II, Parte III), que a razão sozinha nunca é motivo para agir: as paixões dão a direção. Este carrossel é uma reflexão inspirada nessa ideia, e não uma citação literal.

Ouvir as emoções ajuda, e dar nome a elas ajuda mais ainda. Quando estiverem pesadas demais, conversar com alguém de confiança ou procurar ajuda profissional é cuidado.

O que você tem sentido ultimamente, e o que isso quer te dizer?

Salve para refletir com calma.

Reflexão autoral inspirada em Hume, Tratado da Natureza Humana, Livro II, Parte III, seção 3.

@doni7m""",
    hashtags=tags30(["#Hume", "#DavidHume", "#Emocoes", "#FilosofiaEscocesa", "#Iluminismo", "#InteligenciaEmocional", "#Decisoes",
                     "#Sentir", "#Razao", "#Coracao", "#SaudeEmocional", "#NomearEmocoes"], 24),
    ref="""Filósofo: David Hume (1711-1776).
Obra: Tratado da Natureza Humana, Livro II, Parte III, seção 3 (T 2.3.3).
Fonte consultada: Stanford Encyclopedia of Philosophy, verbete Hume's Moral Philosophy: "reason alone can never be a motive to any action of the will" (T 413); a razão como "escrava das paixões" na paráfrase do verbete.
Link: https://plato.stanford.edu/entries/hume-moral/
Natureza do texto do post: reflexão autoral, sem citação literal.
""")

add(date="2026-10-10", slot="B", kind="single", philosopher="Wittgenstein", theme="silêncio",
    slides=[("Nem tudo precisa ser dito. Há silêncios que alcançam o que as palavras não conseguem.", None)],
    scenes=["sat_b"],
    caption="""Existem momentos em que o mais cuidadoso a dizer é nada, e só ficar. O silêncio também comunica.

Wittgenstein encerra o Tractatus Logico-Philosophicus com a proposição 7, sobre aquilo de que não se pode falar. Esta imagem é uma reflexão livremente inspirada nesse final, e não uma citação literal nem uma interpretação do livro.

Onde você poderia, hoje, só ficar em silêncio ao lado de alguém?

@doni7m""",
    hashtags=tags30(["#Wittgenstein", "#Tractatus", "#Silencio", "#FilosofiaAustriaca", "#FilosofiaDaLinguagem", "#Palavras", "#Escuta",
                     "#Noite", "#Lua", "#Quietude", "#Pausa", "#SilencioQueAcolhe"], 27),
    ref="""Filósofo: Ludwig Wittgenstein (1889-1951).
Obra: Tractatus Logico-Philosophicus (1921), proposição 7.
Fonte consultada: Stanford Encyclopedia of Philosophy, verbete Wittgenstein: "Whereof one cannot speak, thereof one must be silent" (TLP 7, tradução de Ogden); Pears/McGuinness: "What we cannot speak about we must pass over in silence".
Link: https://plato.stanford.edu/entries/wittgenstein/
Natureza do texto do post: reflexão autoral livremente inspirada, sem citação literal.
""")

# ---------------- DOMINGO 11/10 ----------------
add(date="2026-10-11", slot="A", kind="carousel", philosopher="Rousseau", theme="menos vitrine, mais cuidado",
    slides=[
        ("Você se compara com os outros mais do que gostaria?", None),
        ("Rousseau distinguia dois amores: o amor de si, que cuida da própria vida, e o amor-próprio, que mede o valor pelo olhar alheio.", None),
        ("O segundo cresce na vitrine: quem está melhor, quem tem mais, quem aparece mais. E cansa.", None),
        ("Voltar ao cuidado simples consigo mesmo alivia a necessidade de aprovação.", "Uma reflexão inspirada em Rousseau"),
        ("Isso não é virar as costas ao mundo. É lembrar que seu valor não depende da comparação do dia.", None),
        ("Experimente um dia com menos vitrine: caminhe sem fotografar, converse sem contar, descanse sem provar nada.", None),
        ("O que seria cuidar de você hoje, sem plateia?", "Conte nos comentários."),
    ],
    scenes=sc("sun_a"),
    caption="""Domingo é um bom dia para soltar a vitrine e voltar ao básico.

Rousseau distingue o amour de soi, o amor de si ligado ao cuidado da própria vida, do amour propre, o amor-próprio, que depende da comparação com os outros. Esta ideia aparece no verbete da Stanford Encyclopedia sobre o autor. O carrossel é uma reflexão inspirada nela, e não uma citação literal.

Se a comparação anda pesando e você se sente sozinho, procurar companhia ou ajuda é cuidado, não fraqueza.

O que seria cuidar de você hoje, sem plateia?

Salve para o próximo dia em que a comparação apertar.

Reflexão autoral inspirada em Rousseau, conforme a distinção entre amour de soi e amour propre.

@doni7m""",
    hashtags=tags30(["#Rousseau", "#JeanJacquesRousseau", "#AmorProprio", "#AmorDeSi", "#FilosofiaFrancesa", "#Iluminismo", "#Comparacao",
                     "#RedesSociais", "#Autoestima", "#Autenticidade", "#DesconectarParaConectar", "#Domingo"], 0),
    ref="""Filósofo: Jean-Jacques Rousseau (1712-1778).
Conceitos: amour de soi e amour propre (Discurso sobre a origem e os fundamentos da desigualdade, 1755).
Fonte consultada: Stanford Encyclopedia of Philosophy, verbete Rousseau: "Human beings ... have such a drive, which he terms amour de soi (self love)"; amour propre como "love of self, often rendered as pride or vanity", "concerned with comparative success or failure as a social being".
Link: https://plato.stanford.edu/entries/rousseau/
Natureza do texto do post: reflexão autoral, sem citação literal.
""")

add(date="2026-10-11", slot="B", kind="single", philosopher="Kant", theme="três perguntas",
    slides=[("O que posso saber? O que devo fazer? O que posso esperar? Três perguntas para um domingo calmo.", None)],
    scenes=["sun_b"],
    caption="""Um domingo tranquilo também serve para perguntar baixinho: o que eu posso saber, o que eu devo fazer, o que eu posso esperar?

Immanuel Kant resume o interesse da razão nessas três perguntas, na Crítica da Razão Pura. Esta imagem é uma reflexão inspirada nelas, e não uma citação literal.

Qual das três está mais viva em você hoje?

@doni7m""",
    hashtags=tags30(["#Kant", "#ImmanuelKant", "#CriticaDaRazaoPura", "#FilosofiaAlema", "#Iluminismo", "#Perguntas", "#Esperanca",
                     "#Dever", "#Conhecimento", "#DomingoTranquilo", "#Escadaria", "#FilosofiaDoDomingo"], 3),
    ref="""Filósofo: Immanuel Kant (1724-1804).
Obra: Crítica da Razão Pura (1781/1787), Doutrina do Método, "O Cânone da Razão Pura" (as três perguntas: "O que posso saber? O que devo fazer? O que me é permitido esperar?").
Fonte consultada: Wikipedia, verbete Immanuel Kant (a presença das três perguntas na Crítica da Razão Pura); a localização exata (A805/B833) é a referência usual da obra, não confirmada por esta consulta.
Link: https://en.wikipedia.org/wiki/Immanuel_Kant
Natureza do texto do post: reflexão autoral, sem citação literal.
""")
