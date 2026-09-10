# Jogo da Forca — Atividade Prática: Programação Assistida por Inteligência Artificial

**Disciplina:** Programação Assistida por Inteligência Artificial
**Professora:** Kadidja Valéria Reginaldo de Oliveira
**Instituição:** UDF Centro Universitário
**Aluna:** Melissa Aragão Leite
**Projeto escolhido:** Nível Intermediário — Jogo da Forca

---

## 1. Objetivo

Esta atividade prática tem como objetivo utilizar a Inteligência Artificial como
apoio contínuo à programação, indo além da geração de código básico para
explorar **refatoração inteligente**. O desafio proposto (nível intermediário)
foi implementar um **Jogo da Forca**, gerenciando o estado do jogo, listas e
laços de repetição, e então usar a IA para refatorar a lógica de exibição das
letras e das tentativas — seguindo o ciclo de colaboração Humano-IA apresentado
em aula: **Contextualizar & Sugerir (IA) → Avaliar Criticamente (Humano) →
Refatorar & Ajustar (Humano + IA) → Decidir & Integrar (Humano)**.

## 2. Declaração de uso de IA

Esta atividade foi desenvolvida com apoio da IA **Claude (Anthropic)**, utilizada
como parceira de programação em par (*pair programming*) durante todo o ciclo:
geração de sugestões de refatoração, revisão crítica de código, criação dos
testes automatizados e redação deste relatório. Todo o código foi executado e
validado (testes automatizados + simulação de partida) antes da entrega, e as
decisões de arquitetura e a responsabilidade final pelo código são da autora,
conforme o princípio discutido em aula: *"a IA escreve, mas é o seu nome no
commit"*.

## 3. Ferramentas utilizadas

| Ferramenta | Papel na atividade |
|---|---|
| Claude (Anthropic) | Par de programação: sugestões de refatoração, revisão de código, geração de testes |
| Python 3 (stdlib) | Linguagem de implementação — sem dependências externas |
| `unittest` | Testes automatizados da lógica do jogo |
| Git / GitHub | Versionamento e entrega do projeto |

## 4. Estrutura do repositório

```
jogo-da-forca/
├── README.md                # este relatório
├── antes/
│   └── forca_v1.py           # versão inicial, escrita manualmente
├── depois/
│   ├── palavras.py           # banco de palavras por categoria
│   ├── desenho.py            # arte ASCII da forca por estágio de erro
│   ├── forca.py              # lógica pura do jogo (estado, regras, vitória/derrota)
│   └── main.py               # loop do jogo e entrada/saída (I/O)
└── tests/
    └── test_forca.py         # testes automatizados da lógica pura
```

## 5. Como executar

Nenhuma dependência externa é necessária (apenas Python 3.10+, pelo uso de
`str | None` e do operador `|` em `set`).

```bash
# Jogar a versão final (refatorada)
cd depois
python3 main.py

# Rodar os testes automatizados
python3 -m unittest discover -s tests -v

# Ver a versão inicial (antes da refatoração), para comparação
python3 antes/forca_v1.py
```

## 6. O ciclo de colaboração aplicado ao projeto

### 6.1 Construir a base (Humano)

A primeira versão (`antes/forca_v1.py`) foi escrita sem apoio de IA, com um
único objetivo: **fazer o jogo funcionar**. O resultado é funcional, mas com
os problemas típicos de uma primeira versão "no impulso":

- tudo em um único arquivo, sem funções — a lógica do jogo, a exibição e o
  laço principal estão misturados;
- quatro variáveis soltas (`palavra`, `letras_certas`, `letras_erradas`,
  `tentativas`) representando o "estado" do jogo, sem nenhuma estrutura que
  as agrupe;
- **nenhuma validação de entrada** — digitar `""`, `"ab"` ou um número quebra
  a lógica de comparação (`chute in palavra`), pois qualquer string é aceita
  como "chute";
- **não impede repetir uma letra já tentada**, o que deixava o jogador gastar
  uma tentativa à toa em uma letra errada repetida;
- uso de `letras_certas.append(...)` com checagem manual de duplicidade —
  uma lista fazendo o papel de um `set`, mais lento e mais verboso;
- lógica de vitória feita com um `for` + *flag* booleana (`ganhou = True`)
  a cada iteração do laço principal, recalculando tudo do zero;
- nenhum teste automatizado — a única forma de saber se o jogo funcionava era
  jogar manualmente.

### 6.2 Contextualizar & Sugerir (IA) / Avaliar Criticamente (Humano)

Com a base pronta, o código foi entregue à IA para avaliação crítica e
sugestão de refatoração, seguindo o roteiro de prompts estruturados
apresentado em aula (contexto → refatoração → debugging), em vez de pedidos
vagos como "melhore esse código".

#### Prompts utilizados

**Contexto (papel + tarefa):**
> "Atue como um dev Python Sênior. Este é um jogo da forca funcional, mas
> escrito como uma primeira versão rápida, tudo em um arquivo. Avalie os
> problemas de design antes de sugerir qualquer mudança: separação de
> responsabilidades, validação de entrada, estrutura de dados usada para o
> estado do jogo."

**Refatoração (foco específico, não genérico):**
> "Refatore a lógica de estado do jogo (`palavra`, letras certas/erradas,
> tentativas) separando a verificação de letras em uma função específica.
> Evite mutação de estado desnecessária e comente as alterações. Não misture
> lógica do jogo com `print`/`input` — separe em módulos."

**Refatoração (estrutura de dados):**
> "As letras já tentadas estão em duas listas com checagem manual de
> duplicidade. Isso pode ser modelado com um `set`? Justifique a mudança em
> termos de legibilidade e desempenho, como no exemplo de `soma = sum(numeros)`
> visto em aula."

**Debugging (caso de borda encontrado ao testar manualmente):**
> "Ao digitar uma letra que já foi tentada antes, a versão original apenas
> desconta uma tentativa de novo se for errada, sem avisar o jogador. Como
> tratar esse caso sem penalizar quem repetiu a letra por engano?"

**Cobertura de testes:**
> "Gere testes automatizados com `unittest` para as funções puras do jogo
> (normalização de entrada, registro de tentativa, palavra revelada,
> condições de vitória/derrota), incluindo casos de borda: entrada vazia,
> entrada com mais de uma letra, letra repetida."

A avaliação crítica humana sobre as sugestões recebidas identificou pontos
que a IA **não poderia decidir sozinha** (ver seção 8) — por exemplo, quantas
categorias de palavras faria sentido ter no banco de palavras deste projeto
específico, e se o jogo deveria permitir jogar novamente sem reiniciar o
programa (decisão de escopo, não de sintaxe).

### 6.3 Refatorar & Ajustar (Humano + IA) → Decidir & Integrar (Humano)

O código final (pasta `depois/`) incorpora as sugestões avaliadas e aceitas,
organizadas em quatro módulos:

- **`palavras.py`** — banco de palavras organizado por categoria
  (`tecnologia`, `faculdade`, `cotidiano`), com `escolher_palavra()` retornando
  um `Desafio` (palavra + categoria), em vez de uma lista solta misturada ao
  laço principal;
- **`desenho.py`** — arte ASCII da forca extraída para uma lista de estágios
  (`ESTAGIOS_DA_FORCA`), com `desenhar_forca(numero_de_erros)` protegida
  contra índices fora da faixa;
- **`forca.py`** — a lógica **pura** do jogo: `EstadoDoJogo` (uma
  `dataclass` que agrupa palavra, letras tentadas e limite de erros no lugar
  das quatro variáveis soltas da v1), e funções sem efeitos colaterais
  (`normalizar_letra`, `registrar_tentativa`, `palavra_revelada`, `venceu`,
  `perdeu`, `jogo_terminado`) — o que as torna testáveis sem precisar simular
  teclado ou tela;
- **`main.py`** — cuida só de entrada/saída (ler letra, imprimir tela, laço de
  "jogar novamente?"), delegando toda a regra do jogo aos módulos acima.

### 6.4 Bug real encontrado em teste manual: palavra "guarda-chuva"

Mesmo com 14 testes automatizados passando, um teste manual jogando a
partida no terminal revelou uma falha que os testes não cobriam: ao sortear
a palavra **"guarda-chuva"**, o jogo travava pedindo letra indefinidamente,
mesmo com todas as letras (g, u, a, r, d, c, h, v) já corretas.

**Causa raiz:** a palavra tem um hífen. `normalizar_letra` rejeita
corretamente qualquer entrada que não seja uma letra do alfabeto — então o
hífen nunca poderia ser "adivinhado" como palpite, e a condição de vitória
(`venceu`) exigia que *todos* os caracteres da palavra, hífen incluído,
estivessem em `letras_tentadas`. Resultado: uma palavra estruturalmente
impossível de vencer.

**Prompt de debugging usado:**
> "O jogo trava pedindo letra pra sempre quando a palavra sorteada é
> 'guarda-chuva', mesmo com todas as letras certas já digitadas. A entrada
> é validada com `letra.isalpha()`, então o hífen nunca é aceito como
> palpite. Como resolver sem remover palavras compostas do banco?"

**Correção aplicada:** caracteres que não são letras (hífen, espaço,
apóstrofo etc.) passaram a ser tratados como já revelados por padrão, tanto
em `palavra_revelada` quanto em `venceu` — eles aparecem na tela desde o
início e não entram na contagem de "letras que faltam adivinhar". Foram
adicionados dois testes de regressão (`TestPalavraComHifen`) para garantir
que esse caso específico não volte a quebrar.

Esse episódio é, na prática, a etapa **"Avaliar Criticamente (Humano)"** do
ciclo de colaboração funcionando como deveria: os testes automatizados
cobriram a lógica pensada de antemão, mas foi o teste manual — jogando de
verdade — que expôs uma decisão de design (que tipos de caractere "contam"
como letra a ser adivinhada) que ninguém, nem a IA nem a versão inicial dos
testes, tinha considerado.

## 7. Comparação Antes → Depois

| Aspecto | Antes (`forca_v1.py`) | Depois (`depois/`) |
|---|---|---|
| Organização | 1 arquivo, sem funções | 4 módulos com responsabilidades separadas |
| Estado do jogo | 4 variáveis soltas | `EstadoDoJogo` (dataclass única) |
| Letras tentadas | 2 listas + checagem manual de duplicidade | 1 `set` (nativo, sem duplicidade por definição) |
| Validação de entrada | Nenhuma | `normalizar_letra` valida e rejeita entradas inválidas |
| Letra repetida | Penaliza o jogador silenciosamente | Detecta e pede outra letra, sem gastar tentativa |
| Verificação de vitória | `for` + flag booleana recalculada a cada rodada | `all(...)` sobre a palavra, função pura reutilizável |
| Testabilidade | Nenhum teste (exigia jogar manualmente) | 16 testes automatizados (`unittest`), cobrindo casos de borda |
| Banco de palavras | Lista única, fixa | Dicionário por categoria, extensível |
| Feedback visual | Apenas texto (`_ p _ h ...`) | Texto + desenho ASCII da forca por estágio de erro |

## 8. Os limites da automação — reflexão

Como discutido em aula, a IA acelerou a *sintaxe* e *lembrou* boas práticas
(uso de `set`, `dataclass`, separação em módulos, testes de borda), mas não
tomou decisões de **negócio/escopo** do projeto — essas continuaram sendo
responsabilidade humana:

- **Quais categorias de palavras fazem sentido** para este jogo (a IA sugeriu
  a estrutura de dicionário; a escolha de `tecnologia`, `faculdade` e
  `cotidiano`, e das palavras dentro de cada uma, foi uma decisão de conteúdo);
- **Quantos erros permitir** antes de perder (`max_erros = 6`, alinhado ao
  número de estágios do desenho ASCII escolhido);
- **Se o jogo deveria oferecer replay** dentro da mesma execução (decisão de
  experiência do usuário, não uma sugestão espontânea da IA);
- A **validação final** de que os testes realmente cobrem os casos que
  importam para esta atividade específica, e não apenas os casos óbvios.

Por isso, a versão entregue não é "o que a IA gerou", mas o resultado de um
ciclo iterativo em que cada sugestão foi avaliada, ajustada ou rejeitada antes
de ser integrada — reforçando a ideia central da aula: **a IA amplia a
capacidade produtiva do desenvolvedor, mas quem decide, valida e assina o
código é o humano.**

## 9. Conclusão

A atividade permitiu experimentar na prática o ciclo de colaboração
Humano-IA aplicado a um problema pequeno, porém completo (gerenciamento de
estado, laços, estruturas de dados e testes). A comparação entre as versões
"antes" e "depois" evidencia ganhos concretos de legibilidade, robustez a
entradas inválidas e testabilidade — sem que isso significasse abrir mão do
controle humano sobre as decisões de design e escopo do projeto.

## 10. Referências

OLIVEIRA, Kadidja Valéria Reginaldo de. **Programação Assistida por
Inteligência Artificial: o novo paradigma da colaboração Humano-Máquina**.
Material de aula — Atividade prática. UDF Centro Universitário, 2026.

PYTHON SOFTWARE FOUNDATION. **The Python Standard Library**. Disponível em:
https://docs.python.org/3/library/. Acesso em: 10 set. 2026.

ANTHROPIC. **Claude**. Disponível em: https://claude.ai/. Acesso em: 10 set.
2026.
