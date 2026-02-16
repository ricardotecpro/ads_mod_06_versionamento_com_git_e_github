# Aula 08 – Pull Requests e Code Review

## 🎯 Objetivos de Aprendizagem
- Entender o fluxo de Pull Request (PR).
- Aprender como sugerir mudanças em projetos.
- Realizar um Code Review básico.
- Finalizar (Merge) um PR pela interface do GitHub.

## 📚 Conteúdo

### 1. O que é um Pull Request (PR)?
Se você trabalha em branches isoladas (como aprendemos na Aula 04), como você avisa sua equipe que terminou e que suas mudanças estão prontas para entrar na `main`?
Você cria um **Pull Request**.
Traduzindo: "Por favor, **puxe** (pull) minhas alterações".

### 2. O Ciclo de Vida do PR
1. **Push**: Você envia sua branch para o GitHub.
2. **Open PR**: No site, você clica em "Compare & pull request".
3. **Review**: Seus colegas leem seu código, comentam e sugerem melhorias.
4. **Approve**: Se tudo estiver ok, um colega aprova.
5. **Merge**: O código é fundido à branch principal.

### 3. Code Review (Revisão de Código)
É a prática de ler o código do outro antes de aceitar.
- **Não é crítica pessoal**: É sobre a qualidade do código.
- **Benefícios**:
  - Encontra bugs antes de ir para produção.
  - O time todo aprende novas formas de resolver problemas.
  - Mantém o padrão de qualidade.

### 4. Merge via GitHub
Diferente do `git merge` no terminal (que é local), o merge do PR acontece no servidor do GitHub. Depois, todos do time fazem `git pull` para baixar a novidade.

## 📽 Roteiro de Slides
- O Coração da Colaboração: Pull Requests.
- Fluxo: Branch -> Push -> PR -> Review -> Merge.
- A Interface do PR no GitHub:
  - Aba "Conversation": Discussão geral.
  - Aba "Files changed": Onde o review acontece linha a linha.
- Code Review: Como ser educado e eficiente.
- Tipos de Merge no GitHub:
  - Create a merge commit (Padrão).
  - Squash and merge (Junta tudo em um só).
  - Rebase and merge (Avançado).

## 📝 Quiz
1. Qual o primeiro passo para criar um Pull Request?
2. Para que serve a aba "Files changed" em um PR?
3. O que é Code Review?
4. Quem deve fazer o merge de um PR idealmente?
5. Após o merge no GitHub, o que os outros desenvolvedores devem fazer?

## Gabarito
1: B ("Push da branch")
2: A
3: C
4: D (Outra pessoa, após aprovar)
5: B (`git pull`)

## 🛠 Exercícios
1. **Prepare**: Crie uma branch `feature-pr` no seu repo de teste.
2. **Mude**: Adicione um arquivo `pr.txt`.
3. **Envie**: `git push -u origin feature-pr`.
4. **GitHub**: Vá ao repo no navegador. Você verá um botão amarelo "Compare & pull request". Clique.
5. **PR**: Escreva um título e descrição. Clique em "Create pull request".
6. **Simule Review**: Vá em "Files changed", clique no `+` ao lado de uma linha e adicione um comentário para você mesmo.
7. **Merge**: Volte para "Conversation", clique em "Merge pull request" e depois "Confirm merge".

## 🚀 Projeto da Aula
No `portfolio-dev`:
1. Crie uma branch chamada `melhoria-readme`.
2. Edite o arquivo `sobre.txt` (ou crie um `README.md` se quiser adiantar) adicionando mais skills.
3. Envie para o GitHub: `git push -u origin melhoria-readme`.
4. Abra o PR no GitHub.
5. Como você não tem um time, você mesmo vai revisar e "Mergear".
6. Veja como a branch `melhoria-readme` foi deletada (opcional) e a `main` agora tem suas mudanças.
7. **Importante**: No seu terminal local, volte para a `main` e digite `git pull` para baixar essas mudanças que agora estão na nuvem!
