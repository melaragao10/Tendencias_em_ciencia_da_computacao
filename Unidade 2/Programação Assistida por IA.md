# Aula 06: Leitura Orientada, Debate e Estudo de Caso
## Boas Práticas na Colaboração Humano-IA (Vibe Coding)

**Disciplina:** Tendências em Ciência da Computação
**Professora:** Kadidja Valéria Reginaldo de Oliveira
**Acadêmica:** Melissa Aragão Leite
**Texto-base:** SARKAR, Advait; DROSOS, Ian. *Vibe coding: programming through conversation with artificial intelligence*. In: Proceedings of the 36th Annual Conference of the Psychology of Programming Interest Group (PPIG 2025), set. 2025.

---

## Etapa 1. Leitura Individual: Trechos e Ideias Registradas

Durante a leitura, destaquei quatro trechos/ideias que considero mais relevantes para entender como a IA participa do processo de desenvolvimento, cobrindo prompting, revisão, testes/depuração e confiança:

**1. Sobre formulação de prompts (granularidade e estratégia).** O artigo mostra que não existe um padrão único de prompt eficaz: os desenvolvedores observados alternam entre instruções de altíssimo nível ("make it 10x better") e instruções extremamente detalhadas, técnicas e restritivas (ex.: "don't integrate Stripe yet. Just make a design with dummy data"), muitas vezes na mesma sessão (seção 3.4.3). O caso do desenvolvedor YT22, que reduz deliberadamente o escopo dos prompts para uma "fase" por vez a fim de reduzir alucinações do modelo, me chamou atenção porque mostra que a habilidade de *prompting* não é apenas comunicar uma intenção, mas gerenciar estrategicamente o quanto de contexto e liberdade se entrega à IA de cada vez.

**2. Sobre confiança e verificação.** A passagem mais marcante do texto, para mim, é a definição de confiança na seção 3.8: *"Trust in vibe coding appears to be granular, dynamic, contingent on review, and evolves through interaction with the system"*. O exemplo do participante YT21 ilustra bem isso: ele afirma conseguir chegar a "80-90% do caminho" com a IA, mas também diz que revisa as mudanças porque isso o ajuda "a permanecer no controle até certo ponto" ("I like to review the changes because it helps me remain in control to some extent"). Achei relevante porque desmonta a ideia de que "vibe coding" significa aceitar tudo sem questionar: a confiança descrita no estudo é condicional e se reconstrói a cada interação, não é dada de uma vez.

**3. Sobre depuração (debugging).** O artigo identifica que, mesmo em fluxos fortemente mediados por IA, a depuração continua sendo majoritariamente um processo híbrido: os programadores usam ferramentas tradicionais (console do navegador, inspeção de rede, terminal) para formular hipóteses sobre a causa de um erro, e só então pedem à IA que implemente a correção já diagnosticada (seção 3.5.1). Ou seja, a IA costuma executar o conserto, mas quem diagnostica o problema continua sendo o humano, o que relativiza a ideia de que "a IA resolve os bugs sozinha".

**4. Sobre o papel da expertise.** A conclusão da seção 3.7.1 resume um ponto central do estudo: a expertise do programador não desaparece com o uso de IA, ela é redirecionada: "from writing code directly to evaluating, guiding, and refining AI-generated solutions". O programador passa a atuar mais como diretor, revisor e editor do que como autor linha a linha, mas seu conhecimento técnico continua essencial durante todo o processo.

---

## Etapa 2. Discussão: Questões Norteadoras

### 1. Até que ponto podemos confiar no código produzido pela IA?

O artigo defende que a confiança no código gerado por IA deve ser **granular e contingente à revisão**, nunca uma aceitação em bloco (seção 3.8.1). Mesmo os participantes mais "confiantes" no estudo, como o do vídeo YT22, fazem questão de afirmar que não acreditam em "seguir cegamente a IA" ("I don't believe in blindly following the AI") e tratam a IA explicitamente como ferramenta, não como autoridade. As verificações recorrentes nos vídeos analisados incluem: varredura rápida (mas atenta) dos *diffs* de código gerados, comparação com a documentação oficial das bibliotecas usadas, execução e teste da aplicação em navegador, e rejeição de sugestões que utilizam APIs inexistentes ou abordagens pouco sustentáveis (seção 3.8.1, caso YT21).

Os riscos de aceitar código sem revisão, testes ou compreensão aparecem de forma explícita no estudo de caso descrito na própria orientação da aula: dependências não verificadas, vulnerabilidades de segurança, problemas de manutenibilidade e impactos não previstos em outras partes do sistema. O artigo reforça isso ao mostrar que os modelos "alucinam" e falham em seguir instruções do sistema com frequência suficiente para exigir checagem constante (seção 3.5.1); por exemplo, um modelo que gerou documentação referenciando uma versão de framework diferente da que estava realmente em uso no projeto (caso YT22).

Minha posição é que a confiança no código de IA deve ser proporcional à criticidade do sistema e à familiaridade do desenvolvedor com o domínio: em protótipos ou componentes de baixo risco, uma checagem rápida pode ser suficiente; em lógica de negócio central ou sistemas críticos, a revisão precisa ser equivalente (ou superior) à de um código escrito por outro humano da equipe.

### 2. A IA reduz a necessidade de conhecimento em programação ou transforma o tipo de conhecimento necessário?

O artigo é direto ao refutar a primeira hipótese: *"Our observations challenge the notion that vibe coding eliminates the need for programming expertise. Instead, we observe a redistribution of expertise deployment"* (seção 5, Conclusão). A expertise técnica tradicional continua sendo usada para avaliar rapidamente a qualidade do código gerado, localizar falhas e decidir quando abandonar a IA em favor de edição manual, mas a ela se somam **dois novos domínios de conhecimento** identificados na seção 3.7.2: expertise em IA (entender limitações dos modelos, janelas de contexto, estratégias de prompting) e expertise de gestão de produto (traduzir requisitos em funcionalidades).

O conceito que melhor sintetiza essa transformação é o de *"task stewardship"* (Lee et al., 2025, citado na seção 4.1): a expertise deixa de estar centrada em escrever código linha a linha e passa a estar centrada em orquestrar o modelo e as ferramentas dentro de um ambiente de desenvolvimento complexo. Um exemplo concreto está na seção 3.7.1: o desenvolvedor de YT21 não escreve a correção de um bug de banco de dados diretamente: ele reconhece o erro pela mensagem, formula uma hipótese técnica sobre a causa e só então instrui a IA a aplicar a correção específica.

Também é interessante o risco apontado na seção 3.7.2 sobre "competência ambiente" (*ambient competence*): a sensação de ser capaz de realizar tarefas que não se dominaria sozinho, simplesmente por ter acesso a uma IA capaz de executá-las. O texto sugere que isso pode deslocar o "locus de agência" do desenvolvedor para sua capacidade de orientar o modelo, o que reforça, na minha leitura, que o conhecimento não diminui, apenas muda de forma, e que ignorar essa transformação é o que gera os riscos de dependência excessiva.

### 3. Quando é melhor utilizar a IA e quando é melhor assumir o controle manualmente?

O artigo descreve esse processo como parte do ciclo de *"iterative goal satisfaction"* (seção 3.3.1): formular objetivo, promptar, revisar, testar, identificar problemas e decidir entre refinar o prompt ou migrar para edição manual, repetindo até que o subobjetivo seja atingido. A partir dos critérios observados na seção 3.7.3, proponho os seguintes parâmetros para essa decisão:

- **Usar a IA quando:** a tarefa é repetitiva ou de baixa complexidade cognitiva (código *boilerplate*, geração de testes, documentação); o custo de escrever um prompt é menor que o custo de implementar manualmente; ou o desenvolvedor está explorando uma solução em um domínio que ainda não domina totalmente e quer ver alternativas.
- **Assumir o controle manual quando:** a alteração é pequena o suficiente para que promptar seja mais lento do que editar diretamente (como relatado por YT21 ao optar por uma edição manual de uma linha); o problema exige depuração fina com ferramentas específicas (console, terminal, breakpoints); a tarefa envolve lógica de negócio central, decisões de arquitetura ou trade-offs que exigem julgamento contextual que a IA não possui; ou quando o "momentum de contexto" (seção 3.2.2) da sessão gerou um caminho de implementação que já não atende mais ao objetivo real, exigindo um recomeço deliberado.

Na prática, os vídeos analisados mostram que a decisão raramente é binária: mesmo os desenvolvedores mais favoráveis à IA continuam alternando entre os dois modos ao longo de uma mesma sessão, o que confirma que o critério mais importante não é "IA ou manual", mas a capacidade do desenvolvedor de reconhecer, momento a momento, qual dos dois modos é mais eficiente e mais seguro para aquela tarefa específica.

---

## Etapa 3. Estudo de Caso para o Debate

**Situação:** uma equipe precisa desenvolver rapidamente uma funcionalidade; um integrante pede à IA a implementação completa; o código funciona e passa em um teste inicial, mas não houve revisão detalhada, nem verificação de dependências, segurança, manutenibilidade ou impactos em outras partes do sistema.

**Ações que a equipe deveria realizar antes de incorporar o código ao projeto**, relacionando-as diretamente às ideias do artigo:

1. **Revisão estrutural do código gerado**, indo além do "teste inicial que passou". O artigo mostra que mesmo desenvolvedores experientes fazem uma varredura rápida, mas atenta, dos *diffs* (observando padrões conhecidos, nomes de funções e chamadas de API, seção 3.5.1) antes de aceitar qualquer mudança significativa. Um único teste bem-sucedido não substitui essa etapa.
2. **Verificação de dependências e dos impactos em outras partes do sistema**, algo explicitamente citado como frequentemente negligenciado. A seção 3.7.1 mostra desenvolvedores checando manualmente se a IA usou a API correta ou referenciando nomes de parâmetros entre arquivos diferentes, uma prática que exige entendimento do sistema como um todo, algo que a IA, isolada, não possui.
3. **Geração e execução de testes adicionais (unitários e de regressão)**, cobrindo cenários de falha e não apenas o "caminho feliz" do teste inicial, coerente com o princípio de tratar o código da IA com o mesmo rigor do código humano da equipe.
4. **Formulação de hipóteses de erro e depuração ativa**, em vez de aceitar o funcionamento aparente como prova de correção. O artigo evidencia que o processo de depuração eficaz combina inspeção de código, uso de ferramentas de desenvolvedor (console, terminal) e formulação de hipóteses, não apenas reexecutar o prompt até o erro desaparecer (seção 3.5.1).
5. **Documentação da decisão**, registrando por que aquela implementação foi aceita e quais verificações foram feitas, o que fortalece tanto a rastreabilidade quanto a revisão por pares.

**Responsabilidades que permanecem humanas:** a decisão final de incorporar (ou não) o código ao projeto; a avaliação de segurança, licenciamento e conformidade; o entendimento de como a nova funcionalidade se encaixa na arquitetura existente; e, de forma mais ampla, a responsabilidade, inclusive legal e profissional, por qualquer falha decorrente do código aceito. O artigo é claro ao afirmar que a expertise do desenvolvedor não é substituída pela IA, apenas redirecionada para funções de avaliação, orientação e revisão (seção 3.7.1), e é exatamente essa função que falhou no cenário descrito, já que a equipe pulou diretamente da geração para a incorporação, sem exercer o papel de revisor que o próprio conceito de "vibe coding responsável" pressupõe.

---

## Etapa 4. Síntese e Entregável

### Três boas práticas para a colaboração humano-IA na programação

1. **Tratar a confiança como algo construído, não concedido**: cada sugestão da IA deve ser verificada por revisão de código, testes e, quando possível, execução real; a confiança se consolida pela repetição de resultados corretos, não pela conveniência de aceitar rápido.
2. **Manter o diagnóstico de problemas sob responsabilidade humana**, delegando à IA principalmente a implementação da correção já compreendida, evitando o uso da IA como "caixa-preta" também na depuração.
3. **Adequar o nível de delegação à criticidade da tarefa**: usar a IA com liberdade em código repetitivo, testes e documentação, e reduzir essa liberdade progressivamente conforme a tarefa envolve lógica de negócio, segurança ou decisões arquiteturais que exigem julgamento contextual.

### Síntese (5 a 8 linhas)

> "Programar com IA de maneira responsável não significa apenas saber pedir código; significa também **saber quando não aceitar o que foi recebido**. A leitura de Sarkar e Drosos (2025) mostra que a confiança no código gerado por IA é granular e se reconstrói a cada interação, nunca é assumida de forma automática. Isso exige do desenvolvedor uma postura ativa de revisão, teste e questionamento, e não a passividade sugerida por expressões como "aceitar tudo e seguir em frente". A expertise técnica não desaparece com a IA: ela se redistribui para funções de diagnóstico, avaliação e orientação, tornando o desenvolvedor mais responsável pelo resultado final, e não menos. Programar com IA de forma responsável significa, portanto, manter o julgamento humano como a última instância de decisão sobre o que entra, ou não, no sistema."

---

## Referências

SARKAR, Advait; DROSOS, Ian. **Vibe coding: programming through conversation with artificial intelligence**. In: Proceedings of the 36th Annual Conference of the Psychology of Programming Interest Group (PPIG 2025), set. 2025.

REGINALDO DE OLIVEIRA, Kadidja Valéria. **Orientações para a Aula 06: Programação Assistida por Inteligência Artificial**. Material de apoio da disciplina Programação Assistida por Inteligência Artificial, UDF Centro Universitário, 2026.

---

## Declaração de Uso de IA

Em atendimento ao requisito de transparência da atividade, declaro que:

- **Fonte de pesquisa utilizada**: o artigo *"Vibe coding: programming through conversation with artificial intelligence"* (Sarkar; Drosos, 2025), texto-base indicado na orientação da Aula 06, e o próprio documento de orientações da aula fornecido pela professora.
- **Ferramenta de IA que apoiou o texto**: Claude (Anthropic), utilizada para organizar e redigir a estrutura textual desta atividade a partir da leitura do artigo e das reflexões pessoais da autora sobre as questões norteadoras e o estudo de caso propostos.
- Todo o conteúdo foi revisado e validado pela autora antes da entrega, em coerência com os próprios princípios de verificação e revisão crítica discutidos no texto-base.
