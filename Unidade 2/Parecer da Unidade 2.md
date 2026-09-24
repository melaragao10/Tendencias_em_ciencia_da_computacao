# Parecer Individual — Unidade II
## Programação Assistida por Inteligência Artificial

**Disciplina:** Programação Assistida por Inteligência Artificial (Tendências em Ciência da Computação)
**Professora:** Kadidja Valéria Reginaldo de Oliveira
**Acadêmica:** Melissa Aragão Leite
**Atividade:** Missão Prática — Parecer da Unidade 2 (Atividade Avaliativa A2)
---

## 1. Introdução

A Unidade II do curso teve como eixo central a avaliação crítica da Inteligência Artificial (IA) enquanto parceira de código — e não apenas como uma ferramenta de automação básica. Ao longo das aulas, discutimos como assistentes como **GitHub Copilot**, **Replit** e **Ghostwriter** vêm sendo incorporados ao dia a dia de desenvolvedores, quais práticas tornam essa colaboração produtiva e, sobretudo, onde estão os limites éticos e técnicos que não podem ser ignorados. Este parecer tem como objetivo sistematizar minha reflexão sobre o conteúdo estudado, relacionando as práticas apresentadas (sugestões de código, refatoração, automação) com o *workflow* sustentável de IA discutido em aula e com as questões éticas e de segurança que envolvem o uso dessas ferramentas.

Dados consolidados por instituições como McKinsey, PwC, MIT, Stanford, Harvard, FGV e IBGE, apresentados no Guia de Boas Práticas na Colaboração Humano-IA da disciplina, confirmam o impacto dessas ferramentas no mercado: profissionais que utilizam IA relatam remuneração superior, maior velocidade de entrega, crescimento de carreira acelerado e maior atratividade para recrutadores. Esse cenário reforça a tese central da unidade — a IA já não é o futuro da engenharia de software, mas o padrão atual de produtividade e qualidade de vida profissional.

## 2. Práticas Estudadas: Sugestões, Refatoração e Automação

O material da unidade organiza o uso prático da IA em três frentes principais, todas exploradas por ferramentas como Copilot, Replit e Ghostwriter:

- **Sugestões de código**: geração de implementações padrão e código *boilerplate*, guiada por comentários que descrevem a intenção do desenvolvedor.
- **Refatoração e depuração**: uso da IA para reestruturar trechos existentes, identificar problemas e propor melhorias de legibilidade e performance.
- **Automação de scripts práticos**: geração de rotinas repetitivas que, tradicionalmente, consumiriam tempo desproporcional ao valor que agregam.

O que me pareceu mais relevante nessa discussão não é a capacidade técnica da IA de gerar código — que já é amplamente conhecida —, mas o modelo de **diálogo estruturado** apresentado (MURTA, 2023), que descreve um ciclo de três etapas: (1) *Intenção*, em que o humano escreve comentários detalhados descrevendo o objetivo da função; (2) *Proposta*, em que a IA gera a implementação inicial com base nesse contexto; e (3) *Refinamento*, em que o humano valida, ajusta a lógica e aprimora a integração. Esse ciclo evidencia que a IA não substitui o raciocínio do desenvolvedor — ela responde a ele. A qualidade do código gerado é, em grande medida, proporcional à qualidade da intenção comunicada.

## 3. O Workflow Sustentável com IA

Um dos pontos mais úteis da unidade foi a proposta de um fluxo de trabalho em cinco etapas — planejamento, implementação, revisão, teste e manutenção — que distribui responsabilidades entre humano e IA de forma coerente com a complexidade de cada tarefa:

1. **Planejamento**: definição do problema pelo humano, que separa a arquitetura de alto nível do código *boilerplate* delegável à IA.
2. **Implementação**: desenvolvimento guiado por intenção e comentários, seguindo o diálogo estruturado citado acima.
3. **Revisão**: aplicação de um checklist crítico de segurança e precisão — nunca aceitar código gerado sem verificar se ele faz exatamente o que foi pedido, se trata *edge cases*, se é eficiente e se segue os padrões do projeto.
4. **Teste**: geração e validação de testes unitários, incluindo casos felizes e casos de falha. Aqui, a IA é usada propositalmente para "quebrar" o próprio código, já que testes gerados por IA tendem a cobrir cenários de falha baseados em bugs comuns que o desenvolvedor pode não ter considerado (LEE; GOLDBERG; KOHANE, 2024).
5. **Manutenção**: talvez a aplicação mais subestimada do curso — usar a IA como *tradutora* de código legado, mudando sua função de "geradora" para "analista de compreensão", capaz de explicar o código linha por linha, mapear dependências e riscos, e gerar testes de regressão antes de qualquer refatoração.

Essa lógica se conecta diretamente com a **Matriz de Protagonismo no Código** apresentada em aula: decisões de arquitetura, *trade-offs*, lógica de negócio central e revisão de segurança e ética permanecem sob liderança humana; já código *boilerplate*, sugestões de sintaxe, geração de testes de cobertura e documentação de funções são tarefas de alta escala e padronização, nas quais a IA agrega mais valor. Na minha visão, essa divisão é o ponto de equilíbrio mais importante discutido na unidade: ela evita dois erros simétricos — usar a IA apenas como corretor ortográfico de sintaxe (subutilização) ou terceirizar decisões estruturais para uma ferramenta sem julgamento crítico (dependência excessiva).

## 4. Ética e Segurança: o Lado Oculto da Colaboração

A unidade deixa claro que assistentes de IA não possuem consciência de segurança — a responsabilidade é sempre humana (BARCAUI, 2025). Três riscos centrais foram destacados:

- **Vulnerabilidades**: como os modelos são treinados em dados abertos da internet, há risco real de injeção de SQL, XSS e uso de bibliotecas desatualizadas, exigindo o uso de ferramentas SAST/DAST e sanitização de entradas.
- **Propriedade intelectual**: risco de violação de licenças (por exemplo, código sob licença GPL sendo incorporado a produtos fechados), o que reforça a necessidade de políticas de auditoria (MELLO, 2024).
- **Viés e discriminação**: replicação de preconceitos históricos presentes nos dados de treinamento, exigindo revisão crítica das operações lógicas em busca de justiça e equidade.

Um trecho que considero central para este parecer é a citação de Lee, Goldberg e Kohane (2024): *"Ferramentas de IA são assistentes, não agentes autônomos. Legalmente, o desenvolvedor que aceita e implementa código gerado por IA assume total responsabilidade por esse código."* Isso significa, na prática, que não existe a possibilidade de "culpar a ferramenta" caso uma vulnerabilidade gerada pela IA resulte em vazamento de dados — a responsabilidade pelo *commit* é sempre do desenvolvedor e da organização. Esse princípio também dialoga com a discussão sobre transparência em sistemas críticos (CÓRDOVA, 2025): em domínios de alto risco, como aprovação de crédito, diagnóstico médico ou triagem de RH, a explicabilidade não é um luxo, mas uma exigência — o desenvolvedor precisa ser capaz de explicar como uma conclusão foi alcançada, o que torna o uso de código gerado por IA especialmente criterioso nesses contextos, possivelmente restrito a componentes não críticos.

## 5. Os Cinco Princípios Fundamentais

O guia da unidade sintetiza boas práticas em cinco princípios que considero aplicáveis a qualquer contexto de desenvolvimento assistido por IA: **transparência** (se a IA gerar algo que você não compreende totalmente, pause e aprenda, em vez de simplesmente aceitar); **verificação** (nunca aceitar código gerado sem validar o comportamento prático); **progressão** (usar a IA com confiança em domínios já dominados e com extrema cautela ao aprender conceitos novos); **documentação** (justificar, nos comentários, o porquê de determinada abordagem ter sido escolhida); e **revisão por pares** (tratar o código gerado por IA com o mesmo rigor — ou maior — que o código humano da equipe).

Esses princípios respondem diretamente a um risco discutido no estudo de caso sobre a adoção do Copilot em equipes de desenvolvimento: o risco de **dependência cognitiva**, popularmente descrito como "esquecer como programar". Ao lado dos benefícios evidentes — ganho de velocidade, apoio educacional para desenvolvedores juniores e refatoração inteligente — o material aponta contrapartidas reais: problemas de licenciamento e introdução de código inseguro. Esse contraste alimenta o debate proposto em aula: até que ponto podemos (e devemos) confiar na IA como uma verdadeira parceira de código?

## 6. Considerações Finais (Parecer Pessoal)

Na minha avaliação, a resposta a essa pergunta não é binária. A síntese da unidade resume bem minha posição: **intuição humana + velocidade da IA = desenvolvedor aumentado**. A IA não substitui o desenvolvedor; ela desloca o valor do trabalho de "digitar sintaxe" para "arquitetar soluções lógicas e seguras". Isso significa que a maestria nessa colaboração não está em conhecer a ferramenta, mas em saber integrá-la sem comprometer a qualidade — algo que exige, paradoxalmente, mais criticidade técnica do desenvolvedor, e não menos.

Do ponto de vista prático, os pontos que mais vou levar para minhas próprias entregas (incluindo o TCC e os projetos da disciplina) são: (i) tratar a fase de testes como oportunidade de usar a IA contra o próprio código, buscando falhas que eu não pensaria em cobrir; (ii) nunca modificar código legado sem antes pedir à IA uma análise estrutural de dependências e riscos; e (iii) documentar explicitamente por que aceitei — ou rejeitei — uma sugestão da IA, prática que fortalece tanto a revisão por pares quanto minha própria compreensão do código.

Concluo que dominar essas práticas não é apenas uma vantagem competitiva, mas, como aponta o próprio guia da disciplina, uma condição de sobrevivência na carreira e de escalabilidade de produtividade em um mercado que já naturalizou a colaboração humano-IA como padrão de trabalho.

---

## Referências

BARCAUI, A. **Ética e segurança na colaboração humano-IA em ambientes críticos**. 2025.

CÓRDOVA, R. **Transparência e explicabilidade em sistemas de IA de alto risco**. 2025.

LEE, P.; GOLDBERG, C.; KOHANE, I. **Responsabilidade legal e geração de código por assistentes de Inteligência Artificial**. 2024.

MELLO, F. **Propriedade intelectual e auditoria de código gerado por Inteligência Artificial**. 2024.

MURTA, L. **O diálogo estruturado: desenvolvimento guiado por comentários na colaboração humano-IA**. 2023.

REGINALDO DE OLIVEIRA, K. V. **Guia de Boas Práticas na Colaboração Humano-IA**. Material de apoio da disciplina Programação Assistida por Inteligência Artificial, UDF Centro Universitário, 17 set. 2026.

*Nota: as referências acima reproduzem as citações (autor e ano) apresentadas no material de apoio da disciplina (slides da Unidade II), que constitui a fonte primária utilizada neste parecer, complementada por dados de mercado consolidados por McKinsey, PwC, MIT, Stanford, Harvard, FGV e IBGE, também citados no mesmo material.*

---

## Declaração de Uso de IA

Em atendimento ao requisito de transparência desta atividade, declaro que:

- **Fonte de pesquisa utilizada**: o material de apoio da disciplina *"Guia de Boas Práticas na Colaboração Humano-IA"* (Profa. Kadidja Valéria Reginaldo de Oliveira, 17 set. 2026), fornecido em aula.
- **Ferramenta de IA que apoiou o texto**: Claude (Anthropic), utilizada para organizar e redigir a estrutura textual deste parecer a partir da análise crítica do material da disciplina e das reflexões pessoais da autora.
- Todo o conteúdo foi revisado e validado pela autora antes da entrega, conforme os próprios princípios de verificação e revisão discutidos nesta unidade.
