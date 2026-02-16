# Aula 12 – README profissional e Markdown

## 🎯 Objetivos de Aprendizagem
- Entender a importância de um bom `README.md`.
- Aprender a sintaxe básica e intermediária do **Markdown**.
- Criar documentação atraente para seus projetos.
- Usar Badges e Emojis para enriquecer visualmente.

## 📚 Conteúdo

### 1. O Cartão de Visitas
Quando alguém abre seu repositório, a primeira coisa que vê é o `README.md`.
Se ele estiver vazio ou ruim, supõe-se que o projeto é ruim.
Um bom README responde:
- O que é isso?
- Para que serve?
- Como instalo/uso?

### 2. Markdown: A Linguagem da Web
O `.md` significa Markdown. É uma linguagem de marcação leve que o GitHub converte em HTML bonito.
Principais códigos:
- `# Título 1` (H1)
- `## Título 2` (H2)
- `**Negrito**`
- `[Texto do Link](URL)`
- `![Texto da Imagem](URL-da-Imagem)`
- `- Item de lista`

### 3. Estrutura Ideal de um README
1. **Título e Badges**: Nome do projeto e status (build passing, license, version).
2. **Descrição**: Resumo de 2 linhas.
3. **Features**: O que o projeto faz.
4. **Instalação**: Passos para rodar.
5. **Tecnologias**: Ícones ou lista das langs usadas.
6. **Autor/Licença**.

## 📽 Roteiro de Slides
- "Ninguém lê código, todos leem documentação".
- O poder do Markdown: Simples e poderoso.
- Sintaxe Rápida:
  - Títulos (# -> ####)
  - Listas (- ou 1.)
  - Código (```)
- Badges: O que são aquelas "medalhas" coloridas? (Shields.io).
- GIFs e Imagens: Uma imagem vale mais que 1000 linhas de código.

## 📝 Quiz
1. Qual caractere é usado para criar títulos em Markdown?
2. Como se escreve um texto em negrito?
3. Qual a diferença entre link e imagem na sintaxe?
4. Para criar um bloco de código de várias linhas, o que usamos?
5. Qual serviço popular gera badges (escudos) para READMEs?

## Gabarito
1: B ("#")
2: A ("**Texto**")
3: C ("A imagem tem um ! na frente")
4: D ("Três crases ```")
5: B ("Shields.io")

## 🛠 Exercícios
1. **Markdown Playground**: Vá em [dillinger.io](https://dillinger.io) ou use o próprio editor do GitHub (Preview) para testar.
2. **Criando um README**:
   - Título: `# Meu Portfólio`.
   - Subtítulo: `## Sobre mim`.
   - Lista: `- HTML`, `- CSS`, `- Git`.
   - Link: `[Meu LinkedIn](url)`.
   - Código:
     ```python
     print("Hello World")
     ```

## 🚀 Projeto da Aula
Vamos profissionalizar o `portfolio-dev` AGORA.
1. Crie uma branch `docs-readme`.
2. Delete o `sobre.txt` (sim, delete).
3. Crie o arquivo `README.md` (Maiúsculas importam!).
4. Cole o seguinte template e preencha com seus dados:

```markdown
# 🚀 Portfólio de [Seu Nome]

Bem-vindo ao meu portfólio oficial! Aqui você encontra meus projetos e estudos.

## 🛠 Tecnologias
- Git & GitHub
- [Linguagem favorita]
- [Outra skill]

## 📫 Contato
- Email: [seu@email.com]
- LinkedIn: [link]
```

5. Commite (`feat: adiciona readme profissional`), Push, PR e Merge.
6. Vá na página inicial do repo e veja a mágica acontecer!
