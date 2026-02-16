# Exercícios da Aula 04

## 🛠 Exercícios

1. **Manipulação de Branches**:
   - Abra seu terminal no repositório `exercicio-03` (ou crie um novo).
   - Verifique em qual branch você está com `git branch` (a atual tem um asterisco *).
   - Crie uma branch chamada `time-b` (`git branch time-b`).
   - Mude para ela (`git switch time-b`).

2. **Divergência de Histórico**:
   - Na branch `time-b`, crie um arquivo `jogador.txt`.
   - Faça o commit: `git add .` e `git commit -m "Novo jogador"`.
   - Mude de volta para a branch principal (`main` ou `master`).
   - Verifique que `jogador.txt` não existe aqui.
   - Crie outro arquivo `juiz.txt` na branch principal e commite.

3. **Merge Simples**:
   - Agora você quer trazer o jogador para a branch principal.
   - Certifique-se de estar na branch principal.
   - Execute: `git merge time-b`.
   - Use `git log` para ver como os históricos se uniram.

## Dica Importante
- O comando `git switch -c nome-da-branch` cria E muda para a branch ao mesmo tempo. É um atalho muito útil!
