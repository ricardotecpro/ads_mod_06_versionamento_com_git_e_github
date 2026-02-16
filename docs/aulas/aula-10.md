# Aula 10 – Issues e projetos no GitHub

## 🎯 Objetivos de Aprendizagem
- Aprender a registrar e organizar tarefas com **Issues**.
- Utilizar **Labels**, **Assignees** e **Milestones** para classificar trabalho.
- Gerenciar o fluxo de trabalho visualmente com **GitHub Projects** (Kanban).
- Conectar Issues com Pull Requests.

## 📚 Conteúdo

### 1. Issues: O Centro de Comando
Issues não são apenas para "problemas". Elas representam **qualquer trabalho a ser feito**.
- **Bug**: "Botão de login não funciona."
- **Feature**: "Adicionar suporte a pagamentos via Pix."
- **Task**: "Atualizar documentação."

### 2. Anatomia de uma Issue
- **Title**: Resumo claro.
- **Description**: Detalhes, passos para reproduzir, imagens.
- **Assignees**: Quem é o responsável? (Pode ser você).
- **Labels**: Etiquetas coloridas (bug, enhancement, documentation, good first issue).
- **Milestones**: Marcos de entrega (ex: Versão 1.0, Lançamento Beta).

### 3. GitHub Projects (O Kanban)
Issues em lista são difíceis de visualizar.
Projects transformam issues em cartões em um quadro (Board).
- **Todo**: A fazer.
- **In Progress**: Fazendo.
- **Done**: Feito.
Isso dá visibilidade instantânea do status do projeto.

### 4. Fechamento Automático
Se você escrever `Closes #123` na descrição de um Pull Request, o GitHub fechará a Issue #123 automaticamente quando o PR for mergeado. Mágica pura!

## 📽 Roteiro de Slides
- Gerenciamento de Projetos: Como não se perder.
- Issues: A unidade atômica de trabalho.
- Etiquetas (Labels): Organização visual.
- GitHub Projects: O Trello embutido no GitHub.
- Automação: "Closes #issue-number" no PR.
- Boas práticas de descrição de Issues.

## 📝 Quiz
1. Qual a função do campo "Assignee" em uma Issue?
2. Para que servem as "Labels"?
3. O que acontece se eu usar a palavra-chave "Closes #10" num Pull Request?
4. O GitHub Projects permite visualizar as tarefas em qual formato popular?
5. Issues servem apenas para reportar bugs (erros)?

## Gabarito
1: B ("Definir o responsável pela tarefa")
2: A ("Categorizar e filtrar issues")
3: C ("A Issue #10 é fechada automaticamente após o merge")
4: A ("Kanban / Quadro")
5: B ("Não, servem para features e discussões também")

## 🛠 Exercícios
1. **Criar Issue**: Vá no `portfolio-dev`, aba Issues, "New Issue". Título: "Adicionar seção de Contato". Descrição: "Precisamos de um email visível no rodapé".
2. **Categorizar**: Adicione a Label "enhancement" e se coloque como Assignee.
3. **Criar Projeto**: Aba Projects > New Project. Escolha "Board".
4. **Adicionar Item**: Adicione sua Issue ao projeto.
5. **Mover**: Arraste o cartão da coluna "Todo" para "In Progress".

## 🚀 Projeto da Aula
Hoje vamos organizar o futuro do `portfolio-dev`.
1. Crie 3 Issues reais para melhorias futuras:
   - "Melhorar CSS da página inicial".
   - "Adicionar foto de perfil real".
   - "Traduzir para Inglês".
2. Crie um **Project** chamado "Roadmap 2026".
3. Adicione as 3 issues ao quadro.
4. Experimente criar uma Issue direto de dentro do projeto (convertendo um rascunho em issue).
5. Deixe tudo na coluna "Todo", pois ainda não começamos a trabalhar nelas.
