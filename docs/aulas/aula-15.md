# Aula 15 – Erros comuns e como resolver

## 🎯 Objetivos de Aprendizagem
- Identificar e corrigir os erros mais frequentes do dia a dia.
- Entender o que é um estado de **Detached HEAD**.
- Resolver commits feitos na branch errada (`git reset`).
- Recuperar arquivos deletados acidentalmente.

## 📚 Conteúdo

### 1. Detached HEAD (Cabeça Desconectada)
Acontece quando você faz `git checkouk <HASH-DO-COMMIT>` em vez de nome de branch.
Você viaja no tempo para ver aquele commit, mas não está "segurando" em nenhuma branch. Se commitar aqui, o commit ficará perdido no limbo quando você voltar para a `main`.
**Solução**: `git switch main` (para voltar) ou `git switch -c nova-branch` (para salvar o estado atual em uma nova branch).

### 2. Push Rejected (Non-fast-forward)
Erro: `! [rejected] main -> main (fetch first)`
Causa: Alguém (ou você mesmo em outro PC) enviou commits para o servidor que você não tem.
**Solução**: `git pull origin main` (Baixe primeiro, resolva conflitos se houver, depois envie).

### 3. Commitei na Branch Errada!
Você estava na `main`, mas deveria estar na `feature-x`. E agora?
**Solução (Reset Suave)**:
1. `git reset --soft HEAD~1`: Desfaz o último commit, mas MANTÉM os arquivos modificados na sua área de stage (verde).
2. `git switch -c feature-x`: Cria/Muda para a branch certa levando as mudanças junto.
3. `git commit -m "mensagem"`: Commita de novo no lugar certo.

## 📽 Roteiro de Slides
- O Pânico do Iniciante.
- "Socorro, perdi meu código!" (Spoiler: É difícil perder coisas no Git).
- Detached HEAD: Você está no limbo. Como sair?
- Reset: Soft vs Hard.
  - Soft: "Oops, volte um passo mas guarde meu trabalho."
  - Hard: "Delete tudo e volte para o passado (Perigoso!)."
- O Reflog: A caixa preta do avião (Recuperando o irrecoverável).

## 📝 Quiz
1. O que significa estar em "Detached HEAD"?
2. Qual comando desfaz o último commit mas mantém seus arquivos modificados prontos para commitar de novo?
3. Se o `git push` for rejeitado por "non-fast-forward", o que você deve fazer?
4. O comando `git reset --hard` é seguro para usar indiscriminadamente?
5. Qual comando mostra um histórico de TUDO o que você fez no terminal (inclusive resets e checkouts)?

## Gabarito
1: C ("Você não está em nenhuma branch, apenas visitando um commit específico")
2: A ("git reset --soft HEAD~1")
3: B ("Dar git pull primeiro")
4: D ("Não, ele apaga as mudanças não commitadas permanentemente")
5: C ("git reflog")

## 🛠 Exercícios
1. **Provocando Detached HEAD**:
   - Dê `git log --oneline`. Copie o hash de um commit antigo.
   - Dê `git checkout <HASH>`.
   - Veja o Git avisar: "You are in 'detached HEAD' state".
   - Crie um arquivo `fantasma.txt`. Commite.
   - Volte para a main: `git switch main`.
   - Veja que o `fantasma.txt` sumiu e o commit "se perdeu". (Ele pode ser recuperado com Reflog, mas isso é papo de sênior).

2. **Salvando commit errado**:
   - Faça uma mudança na `main` que deveria ser numa branch.
   - Commite.
   - Use `git reset --soft HEAD~1`.
   - Veja que o arquivo voltou para o Staging (verde).
   - Crie a branch certa e commite lá. Ufa!

## 🚀 Projeto da Aula
No seu `portfolio-dev`:
1. Simule um erro. Delete o `index.html` sem querer.
2. Dê `git status`. Ele diz `deleted: index.html`.
3. Para recuperar: `git restore index.html` (ou `git checkout index.html`).
4. Ufa, o arquivo voltou intacto. O Git é seu anjo da guarda.
