# Exercícios da Aula 09

## 🛠 Exercícios

1. **Investigação de Branches**:
   - Execute `git branch -a`.
   - O `-a` mostra branches locais e remotas (`remotes/origin/...`).
   - Veja se você tem branches antigas "mentindo" no seu computador que já foram mergeadas e deletadas no GitHub.
   - Use `git fetch --prune` para limpar a lista de branches remotas que não existem mais.

2. **Limpeza Local**:
   - Se você já mergeou a branch `feature-pr` (da aula passada), delete-a do seu computador para manter a ordem.
   - Comando: `git branch -d feature-pr`.
   - Se o Git reclamar que não foi mergeada (e você sabe que foi, ou não importa), use `-D` (maiúsculo) para forçar.

3. **Fluxo Rápido**:
   - Tente fazer o ciclo todo (Criar branch, mudar arquivo, commitar, push) em menos de 2 minutos.
   - O GitHub Flow depende de agilidade. Com a prática, esses comandos viram memória muscular.

## Dica
Mantenha seu repositório limpo. Branches velhas só causam confusão. Mergeou? Deletou.
